import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
#matplotlib inline

x = np.arange(30, 100, 0.1)
## LINEAR
# Create the membership functions
x_cold_lin = fuzz.trimf(x, [30, 30, 50])
x_mild_lin = fuzz.trimf(x, [30, 50, 70])
x_warm_lin = fuzz.trimf(x, [50, 70, 100])
x_hot_lin = fuzz.trimf(x, [70, 100, 100])

# Plot the results of the linear fuzzy membership
plt.figure()
plt.plot(x, x_cold_lin, 'b', linewidth=1.5, label='Cold')
plt.plot(x, x_mild_lin, 'k', linewidth=1.5, label='Mild')
plt.plot(x, x_warm_lin, 'm', linewidth=1.5, label='Warm')
plt.plot(x, x_hot_lin, 'r', linewidth=1.5, label='Hot')
plt.title('Temperature, Linear Fuzzy')
plt.ylabel('Membership')
plt.xlabel('Temperature (Fahrenheit)')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5),
          ncol=1, fancybox=True, shadow=True)
plt.show()

