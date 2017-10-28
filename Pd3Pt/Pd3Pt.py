from ase.build import fcc111
from ase.io import read, write
slab = fcc111('Pt3Pt', size=(3,3,2), vacuum=5.0)
write('Pd_Alloys/Pd3Pt/Pd3Pt.traj', slab)
