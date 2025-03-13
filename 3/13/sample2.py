import numpy as np

A = np.array([[-13, 2, 4],[2, -11, 6],[4, 6,- 15]])
B = np.array([5,-10,5])

print(np.linalg.solve(A,B))