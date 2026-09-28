from client import QuantumMeasurementSampler

def run_example():
    print("=== GenPark Quantum Born Rule Measurement Example ===")
    sampler = QuantumMeasurementSampler()
    print("Shots:", sampler.benchmark_measurement())

if __name__ == "__main__":
    run_example()
