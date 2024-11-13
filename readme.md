# Localized States in Point Defects (LSPD)
----
## Kohn-Sham states
Plot the Kohn-Sham states with [eigenplot.py](https://github.com/JosephPVera/Localized-States/blob/main/eigenplot.py).
![Alt text](https://github.com/JosephPVera/Localized-States/blob/main/tests/kohn-sham-states.png)

## Localized states
Get information within the gap with [localized.py](https://github.com/JosephPVera/Localized-States/blob/main/localized.py) (it can be extended by modifying VBM and CBM). Check the example [localized_Va_N1_2.dat](https://github.com/JosephPVera/Localized-States/blob/main/tests/localized_Va_N1_2.dat) file.
   ```bash
   Defect: Va_N1_2

   VBM = 7.2945 eV
   CBM = 11.7449 eV


   ###########################################################
              vasprun.xml file (EIGENVAL information)                            
   ###########################################################
   ###########################################################
                              SPIN UP                     
   ###########################################################
   ###########################################################
                             kpoint 1                   
   ###########################################################
   Band       Energy         Occ        Occupancy
   429        7.943600       0.506200   Partially Occupied
   430        11.375200      0.000000   Unoccupied
   431        11.447100      0.000000   Unoccupied
   432        11.447100      0.000000   Unoccupied
   ```

## Visualize the localized states
Plot the below figures with [locplot.py](https://github.com/JosephPVera/Localized-States/blob/main/locplot.py). The **locplot.py** script takes the sum of the 5 heaviest values (most contribution) ​​in each band per k-point (Energy versus sum), it also can be change for check the total contribution (tot) for each band per k-point (tot vs energies). Check the PROCAR file.
1. Spin up
![Alt text](https://github.com/JosephPVera/Localized-States/blob/main/tests/Spin_up-kpoint_1.png)
2. Spind down
![Alt text](https://github.com/JosephPVera/Localized-States/blob/main/tests/Spin_down-kpoint_1.png)

## Neighbors of the defect
Use the [defects.py](https://github.com/JosephPVera/Localized-States/blob/main/defects.py) script to checks if the localized states belong to ions that are close to or neighboring the defect. Check the example [neighbor_atoms.dat](https://github.com/JosephPVera/Localized-States/blob/main/tests/neighbor_atoms.dat) file.
