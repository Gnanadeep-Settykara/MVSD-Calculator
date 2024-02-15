import numpy as np

def calculate(list):

    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

    a = np.array(list).reshape(3,3)
    result = dict()
    result['mean'] = [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean()]
    result['variance'] = [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var()]
    result['standard deviation'] = [a.std(axis=0).tolist(),a.std(axis=1).tolist(), a.std()]
    result['max'] = [a.max(axis=0).tolist(), a.max(axis=1).tolist(),a.max()]
    result['min'] = [a.min(axis=0).tolist(), a.min(axis=1).tolist(),a.min()]
    result['sum'] = [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(),a.sum()]

    return result

   