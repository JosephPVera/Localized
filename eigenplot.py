#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

from LSPD.reader.reader import VasprunReader
from LSPD.analyzer.main_variables import VariablesExtractor
from LSPD.analyzer.get_results import ResultsExtractor
from LSPD.plotter.eigen_plotter import EigenvaluesPlotter

"Plot the Kohn-Sham states"

# Variables following the valence band maximum (VBM) and conduction band minimum (CBM).
vbm = 7.2945  
cbm = 11.7449

# res is optional to rescale the Kohn-Sham (eigenvalues) plot with respect to VBM, it may also be off.
res = vbm

# Read the file
xml_reader = VasprunReader("vasprun.xml")

# Prepare the vasprun.xml file to parse
vasp_data = VariablesExtractor(xml_reader)

# Find the main variables in vasprun.xml file: spin, kpoints and bands.
vasp_data.find_spin_numbers()
vasp_data.find_kpoint_numbers()
vasp_data.find_band_numbers()

# Prepare the extraction results with the main variables
results_extractor = ResultsExtractor(vasp_data.spin_numbers, vasp_data.kpoint_numbers, vasp_data.band_numbers)

# Extract results (spin, kpoint, band, tot, sum) from PROCAR and energy_occupancy (energy, occupancy) from EIGENVAL in columns.
results_extractor.extract_results()
results_extractor.extract_energy_occupancy()

# Merge the results and energy_occupancy in one list to plot.
total_results = results_extractor.create_total_results()

# Extract k-point coordinates and labels for x-axis as xticks to plot .
vasp_data.extract_kpoint_coordinates()
vasp_data.generate_x_labels()

# Prepare the plotter by declaring its variables
plotter = EigenvaluesPlotter(vbm, cbm, vasp_data.kpoint_numbers, vasp_data.generate_x_labels, res)

# Use the total_results list to plot
plotter.store_final_results(total_results)

# Plot the Kohn-Sham states
plotter.plot_eigenvalues()
