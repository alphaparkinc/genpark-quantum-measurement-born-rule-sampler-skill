import random, math
from typing import List, Dict, Any

class QuantumMeasurementSampler:
    @staticmethod
    def sample_measurement(state: List[complex], shots: int = 1000) -> Dict[str, Any]:
        probs = [abs(c) ** 2 for c in state]
        num_qubits = int(math.log2(len(state)))
        cum_probs = []
        c = 0.0
        for p in probs:
            c += p
            cum_probs.append(c)
        counts = {}
        for _ in range(shots):
            r = random.random()
            idx = 0
            for i, cp in enumerate(cum_probs):
                if r <= cp:
                    idx = i
                    break
            bitstr = format(idx, f'0{num_qubits}b')
            counts[bitstr] = counts.get(bitstr, 0) + 1
        return {"shots": shots, "counts": counts}

    def benchmark_measurement(self) -> Dict[str, Any]:
        inv = 1.0 / math.sqrt(2.0)
        bell = [complex(inv, 0.0), complex(0.0, 0.0), complex(0.0, 0.0), complex(inv, 0.0)]
        return self.sample_measurement(bell, shots=500)
