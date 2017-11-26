from ase.io import read, write
from ase.lattice.cubic import DiamondFactory, SimpleCubicFactory
from ase.lattice.tetragonal import SimpleTetragonalFactory
from ase.lattice.triclinic import TriclinicFactory
from ase.lattice.hexagonal import HexagonalFactory
from ase.build import bulk
from ase.visualize import view
from ase import Atoms
from ase.build import surface
# The L1_2 structure is "based on FCC", but is really simple cubic
# with a basis.
#class AuCu3Factory(SimpleCubicFactory):
 #   "A factory for creating AuCu3 (L1_2) lattices."
  #  bravais_basis = [[0, 0, 0], [0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]]
   # lement_basis = (0, 1, 1, 1)

#AuCu3 = L1_2 = AuCu3Factory('Pt','Pd')

#a1 = bulk('Pd3Pt', 'fcc', a=3.6)
#print(a1.get_chemical_symbols())


#lattice_constant_pdpt3 = 3.96
#l = lattice_constant_pdpt3 / 2
#a = Atoms(['Pt','Pd','Pd','Pd'], positions=[(0, 0, 0), (0, l, l), (l, 0, l), (l, l, 0)], cell=[l*2,l*2,l*2,90,90,90])
#a = Atoms('N3', [(0, 0, 0), (1, 0, 0), (0, 0, 1)])
#a_surface = surface(a,(3,3,1),2)
#a_surface.center(vacuum=10, axis=2)

a = 4.02
Pd3Pt = Atoms('Pd3Pt',
              scaled_positions=[(0, 0, 0),
                                (0.5, 0.5, 0),
                                (0.5, 0, 0.5),
                                (0, 0.5, 0.5)],
              cell=[a, a, a],
              pbc=True)
s3 = surface(Pd3Pt, (1, 1, 1), 3)
s3.center(vacuum=10, axis=2)
s3_repeat = s3.repeat((2,2,1))
print(s3_repeat.positions.shape)
write('Pd_Alloys/Pd3Pt/Pd3Pt.traj', s3_repeat)
view(s3_repeat)
