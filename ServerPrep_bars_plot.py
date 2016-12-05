"""
Demo of table function to display a table within a plot.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data = [
    [13650, 11612, 10310],
    [2268, 3406, 1826],
    [3726, 7144, 5290],
]

columns = ('Alpha', 'NSLS-II', 'CPU-001')
rows = ['Total User Time [s]', 'Total Server Time [s]', 'Calculation Time [s]']
phase = ['Calculation', 'Response Preparation', 'Data Transfer']

values = np.arange(0, 25, 5)
value_increment = 1000

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.50

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.array([0.0] * len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    l = ' '.join(rows[-row-1].split(' ')[:3])
    a = plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row], tick_label=l)
    if row > 0:
        for i in range(len(a)):
            plt.text(a[i].get_x()+a[i].get_width()+0.01, y_offset[i]+a[i].get_height(), '{}'.format(l),
                     ha='left', va='center')
    for i, r in enumerate(a):
        plt.text(r.get_x()+r.get_width()/2., y_offset[i]+r.get_height()/2. - 300, '{}'.format(' '.join(phase[row].split(' ')[:2])),
                 ha='center', va='bottom')
    y_offset += data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])

   
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
the_table.auto_set_font_size(False)
the_table.set_fontsize(14)

                      
# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel('Time (s)')
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.xlim([0, 3.2])
plt.title('NSLS-II FMX beamline simulation time comparison')
plt.grid(True)

# plt.show()
matplotlib.rcParams.update({'font.size': 22})
fig = plt.gcf()
fig.set_size_inches(18, 11.25)
plt.savefig('ServerPrep_bars_plot.png')
