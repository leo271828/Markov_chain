import numpy as np

A = np.array([  [1, 1/2, 1/3, 1, 0],
                [0, 0, 1/3, 0, 1/3],
                [0, 1/2, 0, 0, 1/3],
                [0, 0, 0, 0, 1/3],
                [0, 0, 1/3, 0, 0 ]])
M = np.array([
            [0, 1/2, 0, 0],
            [1/3, 0, 0, 1/2],
            [1/3, 0, 1, 1/2],
            [1/3, 1/2, 0, 0]])

def Markov_raw_version(A):
    print("Markov old ")
    n = A.shape[0]
    v = np.zeros(n)
    v[0] = 1
    for i in range(50):
        v = A.dot(v)
    print("\nv : ", np.around(v, 2))
    print()

def Markov(A, beta=1):
    print("\nMarkov chain ")
    n = A.shape[0]
    v = np.zeros(n)
    v[0] = 1
    print("P : \n", np.around(A, 3))
    print("\np0 : ", v)
    for i in range(100):
        v = beta * A.dot(v) + (1 - beta)*np.ones(n) / n
    print("\nv' : ", np.around(v, 3))
    print()

# beta = 0.8
Markov(A, 0.8)
