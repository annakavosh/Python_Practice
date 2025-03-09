import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""
Poisson Distribution assumptions and use cases:
- Models the count of events occuring in a fixed interval of time or space.
- Events occur independently and at a constant mean rate (λ).
- No simultaneous event, events occur one at a time.

Example use case:
. Number of emails received per day
. Network traffic ( Packet arrivals)

"""

lambda_ = 5 # Lambda is the mean rate, or expeted number of occurances
data = np.random.poisson(lambda_, 1000)

plt.figure(figsize=(8,5))
plt.hist(data, bins= np.arange(min(data), max(data)+1)- 0.5, density=True, 
         alpha= 0.7, color="blue", edgecolor="black")

x = np.arange(0, max(data)+ 1)
pmf_values = stats.poisson.pmf(x, lambda_)
plt.scatter(x, pmf_values, color="red", zorder=3, label="Theoretical PMF")
plt.plot(x, pmf_values, linestyle = "dashed", color="red", alpha = 0.7)
plt.axvline(lambda_, color="green", linestyle="--", linewidth=3, label=f"Mean (λ={lambda_})")

plt.xlabel("Value")
plt.ylabel("Probability")
plt.title(r"Poisson Distribution: $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad \lambda = " + str(lambda_) + r"$")
plt.grid(axis="y", linestyle="--", alpha= 0.7)
plt.legend()
plt.show()

latex_pmf = r"P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \dots"
print("Poisson PMF:")
print(latex_pmf)