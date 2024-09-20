import numpy as np
A = np.zeros((100,100))
for i in range(0,100):
    for j in range(0,6):
        jump = i+j+1
        if (jump < 100):
            A[i,jump] = 1/6
# We manually fill the entries where jump goes beyond 99.
A[99,99] = 1
A[98,99] = 1
A[97,99] = 5/6
A[96,99] = 4/6
A[95,99] = 3/6
A[94,99] = 2/6
# Fill in other statements depending on what you want to compute.
v0 = np.zeros(100)
v0[0] = 1
print(np.argmax(np.dot(v0, np.linalg.matrix_power(A, 20))))
print(np.amax(np.dot(v0, np.linalg.matrix_power(A, 30))))