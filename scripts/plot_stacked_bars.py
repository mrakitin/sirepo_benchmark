"""
Demo of table function to display a table within a plot.
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_stacked_bars(data, title=None, fontsize=26, figname='plot.png'):
    # Set font size:
    matplotlib.rcParams.update({'font.size': fontsize})

    columns = ('Alpha', 'NSLS-II (Docker)', 'NSLS-II (Vagrant)')
    rows = ['Total User Time [s]', 'Total Server Time [s]', 'Calculation Time [s]']
    phase = ['Calculation', 'Response Preparation', 'Data Transfer']

    values = np.arange(0, 25, 5)
    value_increment = 1000

    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0.1, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.6
    bar_width = 0.25

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        l = ' '.join(rows[-row - 1].split(' ')[:3])
        a = ax.bar(index, data[row], bar_width,
                   bottom=y_offset, color=colors[row], tick_label=l, edgecolor='black',
                   label=phase[row], zorder=100)
        if row > 0:
            for i in range(len(a)):
                ax.text(
                    a[i].get_x() + a[i].get_width() + 0.01,
                    y_offset[i] + a[i].get_height(),
                    '{}'.format(l),
                    ha='left', va='center', fontsize=fontsize,
                )
        # for i, r in enumerate(a):
        #     plt.text(
        #         r.get_x() + r.get_width() / 2.,
        #         y_offset[i] + r.get_height() / 2. - 300,
        #         '{}'.format(' '.join(phase[row].split(' ')[:2])),
        #         ha='center', va='bottom'
        #     )
        y_offset += data[row]
        # cell_text.append(['{:1.1f}'.format(x / 1000.0) for x in y_offset])

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc='upper left')

    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    # cell_text.reverse()

    # Add a table at the bottom of the axes
    # the_table = ax.table(
    #     cellText=[['', '', '']],
    #     rowLabels=[''],
    #     rowColours=colors,
    #     colLabels=columns,
    #     loc='bottom'
    # )
    # the_table.auto_set_font_size(False)
    # the_table.set_fontsize(fontsize)

    # Set font size:
    # matplotlib.rcParams.update({'font.size': fontsize})
    ax.tick_params(axis='y', which='major', labelsize=fontsize)

    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.ylabel('Time [s]', {'fontsize': fontsize})
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    index = np.arange(len(columns))
    bar_width = 0.35
    plt.xticks(index + 1.7 * bar_width, columns)
    plt.xlim([0.3, 3.5])
    plt.ylim([0, 27000])
    if title:
        plt.title(title)
    plt.grid(color='gray', linestyle='dotted')

    # plt.show()
    fig = plt.gcf()
    fig.set_size_inches(18.0, 12.0)
    plt.tight_layout()
    plt.savefig(figname)
    plt.show()


if __name__ == '__main__':
    title = 'NSLS-II FMX beamline simulation time comparison'
    figname = 'stacked_bars_server_preparation.png'
    data = [  # milliseconds
        # alpha, nsls-ii docker, nsls-ii vagrant
        [13650, 10310, 11612],  # duration (SRW calculation)
        [2268, 1826, 3406],  # waiting - duration (response preparation)
        [3726, 5290, 7144],  # total - waiting (data transfer)
    ]
    plot_stacked_bars(data, figname=figname)
