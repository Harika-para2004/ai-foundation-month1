import math
from typing import List, Tuple

class Distribution:
    """Base class for probability distributions"""
    
    def __init__(self, data: List[float]):
        self.data = data
        self.mean = sum(data) / len(data) if data else 0
    
    def variance(self) -> float:
        """Calculate variance"""
        if not self.data:
            return 0
        return sum((x - self.mean) ** 2 for x in self.data) / len(self.data)
    
    def std_dev(self) -> float:
        """Calculate standard deviation"""
        return math.sqrt(self.variance())
    
    def summary(self) -> dict:
        """Return summary statistics"""
        return {
            'count': len(self.data),
            'mean': self.mean,
            'variance': self.variance(),
            'std_dev': self.std_dev(),
            'min': min(self.data) if self.data else None,
            'max': max(self.data) if self.data else None
        }


class NormalDistribution(Distribution):
    """Normal/Gaussian distribution"""
    
    def pdf(self, x: float) -> float:
        """Probability density function"""
        variance = self.variance()
        if variance == 0:
            return 0
        exponent = -((x - self.mean) ** 2) / (2 * variance)
        return (1 / math.sqrt(2 * math.pi * variance)) * math.exp(exponent)


if __name__ == "__main__":
    data = [1.2, 2.3, 2.1, 3.5, 2.8]
    dist = NormalDistribution(data)
    print(dist.summary())

