from math import log

import numpy as np

import matplotlib.pyplot as plt

n = np.linspace(1, 50, 150)

log_n = [log(x) for x in n]

plt.plot( log_n, label = "log(n)")
plt.xlabel("n")
plt.ylabel("log(n)")
plt.title("Gráfico de log(n)")
plt.legend()
plt.grid(True)
plt.show()



