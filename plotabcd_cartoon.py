import matplotlib.pyplot as plt
import numpy as np

def create_region_plot(regions, x_boundary, y_boundary, x_label, y_label, condition_text):
    fig, ax = plt.subplots(figsize=(12, 10))

    colors = ['#FFB3BA', '#BAFFC9', '#FFE4B5', '#BAE1FF']

    for i, (label, x_range, y_range) in enumerate(regions):
        x_min, x_max = x_range
        y_min, y_max = y_range
        ax.add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                   fill=True, facecolor=colors[i % len(colors)]))
        ax.text((x_min + x_max) / 2, (y_min + y_max) / 2, label,
                ha='center', va='center', fontsize=50, fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 12.2)
    ax.set_xlabel(x_label, fontsize=32, x=1, ha='right')
    ax.set_ylabel(y_label, fontsize=32, y=1.02, ha='right', va='top', rotation=0)
    ax.axvline(x=x_boundary, color='black', linestyle='-', linewidth=3)
    ax.axhline(y=y_boundary, color='black', linestyle='-', linewidth=3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.spines['left'].set_linewidth(3)
    ax.spines['bottom'].set_linewidth(3)

    ax.spines['left'].set_capstyle('butt')
    ax.spines['bottom'].set_capstyle('butt')
    ax.plot((1), (0), ls="", marker=">", ms=15, color="k",
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=15, color="k",
            transform=ax.get_xaxis_transform(), clip_on=False)

    ax.set_xticks([0, x_boundary])
    ax.set_xticklabels(['0', f'{x_boundary}'], fontsize=24)
    ax.set_yticks([6.1])
    ax.set_yticklabels(['6.1'], fontsize=24)

    plt.text(0.5, 1.05, condition_text, transform=ax.transAxes, ha='center', va='bottom', fontsize=32, fontweight='bold')

    plt.tight_layout()
    plt.savefig('/home/eslam/AN_plots/abcd_cartoon.pdf', format='pdf', bbox_inches='tight', dpi=300)
    plt.show()

# Example usage
regions = [
    ('C', (0, 0.86), (6.1, 12.2)),
    ('A', (0.86, 1), (6.1, 12.2)),
    ('D', (0, 0.86), (0, 6.1)),
    ('B', (0.86, 1), (0, 6.1))
]
create_region_plot(regions, x_boundary=0.86, y_boundary=6.1,
                   x_label='ABCDNet score', y_label='$|\Delta\eta_{jj}|$',
                   condition_text='')
