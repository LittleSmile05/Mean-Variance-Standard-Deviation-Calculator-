import numpy as np

def get_results(op, matrix):
    if op == "sum":
        axis1 = matrix.sum(axis=0).tolist()
        axis2 = matrix.sum(axis=1).tolist()
        flattened = matrix.sum()
    elif op == "min":
        axis1 = matrix.min(axis=0).tolist()
        axis2 = matrix.min(axis=1).tolist()
        flattened = matrix.min()
    elif op == "max":
        axis1 = matrix.max(axis=0).tolist()
        axis2 = matrix.max(axis=1).tolist()
        flattened = matrix.max()
    elif op == "std":
        axis1 = matrix.std(axis=0).tolist()
        axis2 = matrix.std(axis=1).tolist()
        flattened = matrix.std()
    elif op == "var":
        axis1 = matrix.var(axis=0).tolist()
        axis2 = matrix.var(axis=1).tolist()
        flattened = matrix.var()
    elif op == "mean":
        axis1 = matrix.mean(axis=0).tolist()
        axis2 = matrix.mean(axis=1).tolist()
        flattened = matrix.mean()
    return [axis1, axis2, flattened]

def calculate(mylist):
    if len(mylist) != 9:
        raise ValueError("List must contain nine numbers.")
  
    else:
        matrix = np.array(mylist).reshape(3, 3)
        calculations = {
                        'mean': get_results('mean', matrix),
                        'variance': get_results('var', matrix),
                        'standard deviation': get_results('std', matrix),
                        'max': get_results('max', matrix),
                        'min': get_results('min', matrix),
                        'sum': get_results('sum', matrix),
                        }

    return calculations