import random

def prepare_qubits(num_qubits):
    qubits = []
    for _ in range(num_qubits):
        qubit = random.choice(["0", "1"])
        basis = random.choice(["X", "Z"])  # X-basis or Z-basis
        qubits.append((qubit, basis))
    return qubits

def measure_qubits(qubits):
    measurements = []
    for qubit, basis in qubits:
        if basis == "X":
            measurement = random.choice(["0", "1"])
        else:
            measurement = qubit
        measurements.append(measurement)
    return measurements

def compare_bases(alice_bases, bob_bases):
    matching_indices = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]
    return matching_indices

def filter_matching_qubits(qubits, indices):
    return [qubits[i] for i in indices]

def main():
    num_qubits = 20  # Number of qubits sent by Alice and received by Bob

    # Step 1: Alice prepares qubits
    alice_qubits = prepare_qubits(num_qubits)

    # Step 2: Alice chooses random bases and measures qubits
    alice_bases = [random.choice(["X", "Z"]) for _ in range(num_qubits)]
    alice_measurements = measure_qubits(alice_qubits)

    # Step 3: Alice sends the bases to Bob

    # Step 4: Bob chooses random bases and measures qubits
    bob_bases = [random.choice(["X", "Z"]) for _ in range(num_qubits)]
    bob_measurements = measure_qubits(alice_qubits)  # Bob measures the qubits he received from Alice

    # Step 5: Bob sends the bases he used to Alice

    # Step 6: Alice and Bob compare bases and keep matching measurements
    matching_indices = compare_bases(alice_bases, bob_bases)
    alice_matching_qubits = filter_matching_qubits(alice_measurements, matching_indices)
    bob_matching_qubits = filter_matching_qubits(bob_measurements, matching_indices)

    # Step 7: Establish the final secure key
    secure_key = "".join(alice_matching_qubits)

    # Output the results
    print("Alice's qubits:", [qubit[0] for qubit in alice_qubits])
    print("Alice's bases: ", alice_bases)
    print("Bob's bases:   ", bob_bases)
    print("Matching qubits:", secure_key)

if __name__ == "__main__":
    main()
