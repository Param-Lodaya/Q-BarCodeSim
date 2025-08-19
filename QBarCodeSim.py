from circuit_generator import circuit_generator
from Mapper_code import mapper_visual
from visualise import visualize_barcode

def project():
  _, counts, statevector = circuit_generator()
  visual_data = mapper_visual(counts, statevector, qubits=3)
  visualize_barcode(visual_data,filename="quantum_barcode_3d.html")



if __name__ == "__main__":
    project()
