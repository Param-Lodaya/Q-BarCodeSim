import qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import circuit_drawer, plot_histogram,plot_state_city
import matplotlib as plt
import numpy as np

def circuit_generator():
 alpha0 = np.random.uniform(0,np.pi)
 beta0 = np.random.uniform(0,2*np.pi)
 alpha1 = np.random.uniform(0,np.pi)
 beta1 = np.random.uniform(0,2*np.pi)
 alpha2 = np.random.uniform(0,np.pi)
 beta2 = np.random.uniform(0,2*np.pi)
 
 circuit = QuantumCircuit(3,3)
 circuit.ry(alpha0, 0)
 circuit.rz(beta0, 0)
 circuit.ry(alpha1, 1)
 circuit.rz(beta1, 1)
 circuit.ry(alpha2, 2)
 circuit.rz(beta2, 2)
 
 circuit.h(0)
 circuit.h(1)
 circuit.h(2)
 circuit.cz(0,1)
 circuit.cx(0,1)
 circuit.cy(0,1)
 circuit.cz(0,2)
 circuit.cx(0,2)
 circuit.cy(0,2)
 circuit.cz(1,2)
 circuit.cx(1,2)
 circuit.cy(1,2)

 
 circuit.measure(0,0)
 circuit.measure(1,1)
 circuit.measure(2,2)
 circuit.draw(output='mpl').savefig('Quantum_Circuit.png')

 simulator = AerSimulator()
 compiled_cir = transpile(circuit, simulator)
 job = simulator.run(compiled_cir, shots=2500)
 result = job.result()
 counts = result.get_counts(circuit)
 plot_histogram(counts).savefig('Quantum_Measurement.png')
  
 circuit_save = circuit.remove_final_measurements(inplace=False)
 statevector = Statevector.from_instruction(circuit_save)
 
 return circuit, counts, statevector

if __name__ == "__main__":
 circuit_generator()





