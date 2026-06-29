import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        m = np.max(z)
        num = np.exp(z-m)
        denom = np.sum(num)
        return np.round(num/denom,4)