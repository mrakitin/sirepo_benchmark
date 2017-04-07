"""
Demo of table function to display a table within a plot.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_stacked_bars(data, title=None, fontsize=22, figname='plot.png'):
    columns = ('Alpha', 'NSLS-II (Vagrant)', 'NSLS-II (Docker)')
    rows = ['Total User Time [s]', 'Total Server Time [s]', 'Calculation Time [s]']
    phase = ['Calculation', 'Response Preparation', 'Data Transfer']

    values = np.arange(0, 25, 5)
    value_increment = 1000

    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0.1, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.6
    bar_width = 0.46

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))

    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        l = ' '.join(rows[-row - 1].split(' ')[:3])
        a = plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row], tick_label=l, edgecolor='black')
        if row > 0:
            for i in range(len(a)):
                plt.text(
                    a[i].get_x() + a[i].get_width() + 0.01,
                    y_offset[i] + a[i].get_height(),
                    '{}'.format(l),
                    ha='left', va='center'
                )
        for i, r in enumerate(a):
            plt.text(
                r.get_x() + r.get_width() / 2.,
                y_offset[i] + r.get_height() / 2. - 300,
                '{}'.format(' '.join(phase[row].split(' ')[:2])),
                ha='center', va='bottom'
            )
        y_offset += data[row]
        cell_text.append(['{:1.1f}'.format(x / 1000.0) for x in y_offset])

    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()

    # Add a table at the bottom of the axes
    the_table = plt.table(
        cellText=cell_text,
        rowLabels=rows,
        rowColours=colors,
        colLabels=columns,
        loc='bottom'
    )
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(14)

    # Set font size:
    matplotlib.rcParams.update({'font.size': fontsize})
    plt.tick_params(axis='y', which='major', labelsize=fontsize)

    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.ylabel('Time [s]', {'fontsize': fontsize})
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.xlim([0, 3.2])
    if title:
        plt.title(title)
    plt.grid(color='gray', linestyle='dotted')

    # plt.show()
    fig = plt.gcf()
    fig.set_size_inches(16, 11.25)
    plt.savefig(figname)
    plt.show()


if __name__ == '__main__':
    title = 'NSLS-II FMX beamline simulation time comparison'
    figname = 'stacked_bars_server_preparation.png'
    data = [
        [13650, 11612, 10310],
        [2268, 3406, 1826],
        [3726, 7144, 5290],
    ]
    plot_stacked_bars(data, figname=figname)
