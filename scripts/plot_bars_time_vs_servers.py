import numpy as np

from plot_lib import plot_bars

if __name__ == '__main__':
    quantities = ['calc_time', 'wait_time']
    quantity_labels = ['Calculation time', 'Total waiting time']
    xlabel = 'Servers'
    ylabel = 'Time [s]'
    title = ''
    data = {
        'Alpha': {
            'calc_time': np.array([
                26.94924378,
                28.26125908,
                27.33992815,
                27.74088383,
                28.67293692,
            ]),
            'wait_time': np.array([
                35.12,
                36.85,
                35.53,
                36.24,
                39.00,
            ]),
        },
        'NSLS-II (Vagrant)': {
            'calc_time': np.array([
                23.8326509,
                22.98116207,
                23.8729701,
                21.96989799,
                21.88926411,
            ]),
            'wait_time': np.array([
                52.92,
                44.93,
                38.91,
                42.26,
                51.61,
            ]),
        },
        'NSLS-II (Docker)': {
            'calc_time': np.array([
                18.85590315,
                19.169384,
                19.10668492,
                19.6615119,
                19.08126712,
            ]),
            'wait_time': np.array([
                29.34,
                29.54,
                29.98,
                31.61,
                31.16,
            ]),
        },
    }

    plot_bars.plot_bars(
        data=data,
        quantities=quantities,
        quantity_labels=quantity_labels,
        xlabel=xlabel,
        ylabel=ylabel,
        figname='bars_time_vs_servers.png'
    )
