import cirq
import cirq_google as cg

# Set up the Engine
engine = cg.Engine(project_id='quantum-google-qgp')

# Define the circuit (as before)
q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
    cirq.H(q0),
    cirq.X(q0),  # Replace CNOT with X gate
    cirq.measure(q0, q1, key='result')
)

# Run on the quantum processor
job = engine.run_sweep(
    program=circuit,
    params={},
    repetitions=1000,
    processor_id='processor_name'
)

# Get results
results = job.results()
for result in results:
    print(result.measurements['result'])
