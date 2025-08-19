import numpy as np
import random
from itertools import product

def random_colour():
 h=random.randint(0,360)
 s=random.randint(60,90)
 l=random.randint(40,70)
 return f"hsl({h}, {s}%, {l}%)"
 
def mapper_visual(counts, statevector,qubits=3):
 visual_data=[]
 random.seed()
 
 for bits in product('01',repeat=qubits):
  bitsize = "".join(bits)
  index = int(bitsize,2)
  amp = statevector.data[index]
  phase = np.angle(amp)
  brightness = (np.cos(phase)+1)/2
  height = counts.get(bitsize,0)
  width = np.random.randint(1,4)
  colour = random_colour()
  visual_data.append({'bitsize':bitsize, 'height':height, 'width':width, 'colour':colour,'brightness':brightness})
 
 return visual_data


