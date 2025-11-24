import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 NumPy array
    matrix = np.array(list).reshape(3, 3)

    # Prepare calculations
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),     # mean of columns
            matrix.mean(axis=1).tolist(),     # mean of rows
            matrix.mean()                     # mean of flattened
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum()
        ]
    }

    return calculations
