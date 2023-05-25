import math
import matplotlib.pyplot as plt

P_1 = 100
A_1 = 13.8858
B_1 = 2788.51
C_1 = 220.79

A_2 = 14.0045
B_2 = 3279.47
C_2 = 213.2

y_1 = 0.8
y_2 = 0.2

A = [A_1, A_2]
B = [B_1, B_2]
C = [C_1, C_2]
y = [y_1, y_2]
P = [P_1, P_1]

iteration = 0
max_iterations = 30

T_values = []
Temperature = []
Temperature_new = []
total = 0
keep_looping = True

for i in range(2):
  t = (B[i] / (A[i] - math.log(P[i]))) - C[i]
  total = total + t
  Temperature.append(t)

avg = total / 2
avg1 = total / 2

while (keep_looping):
  p1 = math.exp(A[0] - (B[0] / (avg + C[0])))
  for i in range(2):
    x1 = (y[0] * P_1) / p1
    x2 = 1 - x1
    p2 = y[1] * P_1 / x2
    T_new = (B[1] / (A[1] - math.log(p2))) - C[1]
    Temperature_new.append(T_new)
    avg = 0
    avg = avg + T_new

  if iteration < max_iterations:
    iteration += 1
    T_values.append(T_new)
  else:
    keep_looping = False

plt.plot(range(iteration), T_values, label='Temperature values', color='purple')
plt.title('Temperature value throughout iterations', fontweight='bold')
plt.xlabel('Number of times iterated')
plt.ylabel('Temperature (°K)')
plt.grid(True)
plt.legend()
plt.show()
print("The graph converges to", T_values[-1], "after", iteration, "loops")
print("the difference between the 2 final temperature values:", abs(T_values[-2] - T_values[-1]))