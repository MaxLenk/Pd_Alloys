from ase.spacegroup import crystal
from ase.visualize import view
from ase.build import surface
from ase.io import write
from ase.build import fcc111, add_adsorbate

#build the Pt crystal structure
lc=4.07 #angstrom
adsorbate_distance = 1.5
alloy_name = 'Ag'
slab = fcc111('Pd', size=(3,3,2), vacuum=10.0)
print(slab.get_tags())
slab[2].symbol = alloy_name
slab[6].symbol = alloy_name
slab[8].symbol = alloy_name
slab[0].symbol = alloy_name
slab[10].symbol = alloy_name
slab[16].symbol = alloy_name
slab.a = lc
#save .traj file
write('Pd_Alloys/Pd3Ag/Pd3Ag.traj',slab)
write('POSCAR',slab) #in case the .traj file cannot be read
view(slab)
