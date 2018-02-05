import numpy as np

from plot_lib import plot_bars

if __name__ == '__main__':
    quantities = ['command_line', 'web']
    quantity_labels = ['Command line interface', 'Browser interface']
    xlabel = 'Sampling factor'
    ylabel = 'Time [s]'
    title = 'Server Comparison by Time of Calculation and\nTotal Wait Time (NSLS-II FMX beamline, sampling factor = 0.7)'
    data = {
        0.5: {
            'web': np.array([
                25.62,
                28.04,
                44.76,
                30.76,
                34.03,
                39.54,
            ]),
            'command_line': np.array([
                14.099,
                14.935,
                14.962,
                13.340,
                15.135,
                15.129,
            ]),
        },
        0.7: {
            'web': np.array([
                60.00,
                42.49,
                77.00,
                53.98,
            ]),
            'command_line': np.array([
                23.301,
                22.478,
                26.795,
                21.745,
            ]),
        },
        1.0: {
            'web': np.array([
                114,
                118,
                137,
                112,
                140,
            ]),
            'command_line': np.array([
                41.766,
                38.133,
                39.857,
                38.484,
                39.174,
            ]),
        },
    }

    plot_bars.plot_bars(
        data=data,
        quantities=quantities,
        quantity_labels=quantity_labels,
        xlabel=xlabel,
        ylabel=ylabel,
        figname='bars_time_vs_sampling.png'
    )
