
import numpy as np
import matplotlib.pyplot as plt


n_groups = 3

means_calc = (27.79285035, 22.90918903, 19.17495022)
std_calc = (0.309311347386, 0.430659401092, 0.132665172245)

means_total = (36.548, 46.126, 30.326)
std_total = (0.680950805859, 2.68960703449, 0.450217725106)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_calc, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_calc,
                 error_kw=error_config,
                 label='Calculation time')

rects2 = plt.bar(index + bar_width, means_total, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=std_total,
                 error_kw=error_config,
                 label='Total Wait time')

plt.xlabel('Server')
plt.ylabel('Time (s)')
plt.title('Server Comparison by Time of Calculation and Total Wait Time (NSLS-II FMX beamline, sampling factor = 0.7)')
plt.xticks(index + bar_width, ('alpha', 'nsls2', 'cpu-001'))
plt.xlim(-0.3, 3)
plt.legend(loc=4)
plt.grid()

plt.tight_layout()
plt.show()

