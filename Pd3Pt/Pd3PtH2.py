from ase.spacegroup import crystal
from ase.visualize import view
from ase.build import surface
from ase.io import write
from ase.build import fcc111, add_adsorbate

#build the Pt crystal structure
lc=4.02 #angstrom
adsorbate_distance = 0.5
alloy_name = 'Pt'
slab = fcc111('Pd', size=(3,3,2), vacuum=10.0,a=lc)
add_adsorbate(slab,'H',adsorbate_distance,'fcc',(1,1))
add_adsorbate(slab,'H',adsorbate_distance+.55,'fcc',(1,1))
print(slab.get_tags())
slab[2].symbol = alloy_name
slab[6].symbol = alloy_name
slab[8].symbol = alloy_name
slab[0].symbol = alloy_name
slab[10].symbol = alloy_name
slab[16].symbol = alloy_name
slab.a = lc
#save .traj file
write('Pd_Alloys/Pd3Pt/Pd3PtH2.traj',slab)
write('POSCAR',slab) #in case the .traj file cannot be read
view(slab)
