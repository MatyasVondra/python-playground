import matplotlib.pyplot as plt

labels = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

temperatures = {
    "Prague": [12, 14, 15, 14, 13, 12, 11],
    "Tokyo": [18, 20, 19, 21, 22, 20, 18],
    "New York": [7, 8, 12, 10, 11, 9, 8],
    "Sydney": [22, 23, 25, 24, 23, 22, 21],
}

def make_graph(temperatures):
    fig = plt.figure(figsize=(5, 4))

    for key, value in temperatures.items():
        plt.plot(value, label=key)

    plt.set_cmap("tab10")
    plt.ylim(5, 30)
    plt.legend(loc='upper right')
    plt.ylabel("Temperature (°C)")
    plt.xlabel("Figure 1:")  # Asi? :D
    set_labels(fig.axes[0], labels)

    return fig


def set_labels(ax, labels):
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)

plt.show(make_graph(temperatures))