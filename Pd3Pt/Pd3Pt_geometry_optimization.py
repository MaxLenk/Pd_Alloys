from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton

#f = open('WCl_adsorption/W_geometry_optimization_500_441/energy.txt', 'w')
#f.write('starting')  # python will convert \n to os.linesep

Pd3Pt_slab_path = 'Pd_Alloys/Pd3Pt/Pd3Pt.traj'
output_directory = 'Pd_Alloys/Pd3Pt/Pd3Pt_geometry_optimization_600_661/'

Pd3Pt_slab=read(Pd3Pt_slab_path)
Pd3Pt_slab.calc=espresso(pw=600,
                       dw=4500,
                       kpts=(6,6,1),
                       xc='PBE',
                       outdir= output_directory + 'E_Pd3Pt_slab',#espresso outdirectory saved
                                            #here                                    
                       convergence={'energy':1e-6,
                                    'mixing':0.05,
                                    'mixing_mode':'local-TF',
                                    'maxsteps':1000,
                                    'diag':'cg'})

relax_Pd3Pt_slab=QuasiNewton(Pd3Pt_slab,
                           logfile=output_directory + 'opt.log',
                           trajectory=output_directory + 'opt.traj',
                           restart=output_directory + 'opt.pckl') #ase output
relax_Pd3Pt_slab.run(fmax=0.05)

E_Pd3Pt_slab=Pd3Pt_slab.get_potential_energy()
#f.write(E_W_slab)
#f.write('\n END')
#f.close()  # you can omit in most cases as the destructor will call it
print(E_Pd3Pt_slab)
