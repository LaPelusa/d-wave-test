import numpy as np
import dimod

# Especificar los coeficientes del problema que queremos resolver es muy sencillo
# Empezaremos con un caso muy simple

J = {(1,1):1,(1,2):-2,(1,3): 6,(1,4):3,(2,1):-2,(2,2):-2,(2,3):-12,(2,4):-6,(3,1): 6,(3,2):-12,(3,3):6,(3,4):18,(4,1):3,(4,2):-6,(4,3):18,(4,4):3}

h = {}
model = dimod.BinaryQuadraticModel(h, J, 0.0, dimod.SPIN)

print("El modelo que vamos a resolver es")
print(model)
print()

# Podemos resolver el modelo de forma exacta


from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print("La solucion exacta es")
print(solution)
print()


# O con *simulated annealing* (un método heurístico de optimización para ordenadores clásicos)


sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("La solucion con simulated annealing es")
print(response)
print()


# Y, por supuesto, con el ordenador cuántico de D-Wave 

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("La solucion con el quantum annealer de D-Wave llamado",sampler_name,"es")
print(response)
print()

print()
print()
print()


# Finalmente, lo resolvemos nuevamente con el *quantum annealer* seleccionando explícitamente el ordenador a utilizar

sampler = EmbeddingComposite(DWaveSampler(solver='Advantage_system1.1'))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("La solucion con el quantum annealer de D-Wave llamado",sampler_name,"es")
print(response)
print()

# Lo mismo, pero con el otro *annealer*

sampler = EmbeddingComposite(DWaveSampler(solver='DW_2000Q_6'))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads=5000)
print("La solucion con el quantum annealer de D-Wave llamado",sampler_name,"es")
print(response)
print()
