class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        old_val = init
        new_val = old_val
        for i in range(iterations):
            new_val = old_val - learning_rate*2*old_val
            old_val=new_val
        return round(new_val,5)
        ...
