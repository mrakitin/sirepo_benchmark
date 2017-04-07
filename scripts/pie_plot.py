"""
Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
labels = 'Calculation Time', 'Non-Calculation (Data Transfer) Time'
all_sizes = {
    'cpu-001': (19.17495022, 11.15104978),
    'alpha': (27.79285035, 8.755149649),
    'nsls-ii': (22.90918903, 23.21681097),
}
colors = ['yellowgreen', 'gold']

for k in sorted(all_sizes.keys()):
    plt.pie(all_sizes[k], labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('cpu-001 server, NSLS-II FMX beamline, sampling factor = 0.7')
    plt.show()
