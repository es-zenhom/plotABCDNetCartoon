import matplotlib.pyplot as plt
import numpy as np

def create_detailed_region_plot(regions, x_boundaries, y_boundaries, x_label, y_label, condition_text):
    fig, ax = plt.subplots(figsize=(12, 10))
    colors = {'A': '#BAFFC9', 'B': '#BAE1FF', 'C': '#FFB3BA', 'D': '#FFE4B5'}

    for label, x_range, y_range, subregions in regions:
        x_min, x_max = x_range
        y_min, y_max = y_range
        color = colors[label]

        if subregions:
            for sublabel, sub_x_range, sub_y_range in subregions:
                sub_x_min, sub_x_max = sub_x_range
                sub_y_min, sub_y_max = sub_y_range
                ax.add_patch(plt.Rectangle((sub_x_min, sub_y_min), sub_x_max - sub_x_min, sub_y_max - sub_y_min,
                                           fill=True, facecolor=color))
                ax.text((sub_x_min + sub_x_max) / 2, (sub_y_min + sub_y_max) / 2, sublabel,
                        ha='center', va='center', fontsize=30, fontweight='bold')
        else:
            ax.add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                       fill=True, facecolor=color))
            ax.text((x_min + x_max) / 2, (y_min + y_max) / 2, label,
                    ha='center', va='center', fontsize=50, fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 10)
    ax.set_xlabel(x_label, fontsize=32, x=1, ha='right')
    ax.set_ylabel(y_label, fontsize=32, y=1.02, ha='right', va='top', rotation=0)

    for x in x_boundaries:
        ax.axvline(x=x, color='black', linestyle='-', linewidth=1)
    for y in y_boundaries:
        if y == 8.0:
            ax.plot([0, 0.86], [y, y], color='black', linestyle='-', linewidth=1)
        else:
            ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

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

    ax.set_xticks([0] + x_boundaries)
    ax.set_xticklabels(['0'] + [f'{x:.2f}' for x in x_boundaries], fontsize=24)
    ax.set_yticks(y_boundaries)
    ax.set_yticklabels([f'{y:.1f}' for y in y_boundaries], fontsize=24)

    plt.text(0.5, 1.05, condition_text, transform=ax.transAxes, ha='center', va='bottom', fontsize=32, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/home/eslam/AN_plots/abcd_subregions_cartoon.pdf', format='pdf', bbox_inches='tight', dpi=300)
    plt.show()

# Detailed regions
regions = [
    ('A', (0.86, 1), (6.1, 10), None),
    ('B', (0.86, 1), (0, 6.1), [('B1', (0.86, 1), (3, 6.1)), ('B2', (0.86, 1), (0, 3))]),
    ('C', (0, 0.86), (6.1, 10), [('C1', (0.49, 0.86), (8, 10)), ('C3', (0, 0.49), (8, 10)),
                                 ('C2', (0.49, 0.86), (6.1, 8)), ('C4', (0, 0.49), (6.1, 8))]),
    ('D', (0, 0.86), (0, 6.1), [('D1', (0.49, 0.86), (3, 6.1)), ('D3', (0, 0.49), (3, 6.1)),
                                ('D2', (0.49, 0.86), (0, 3)), ('D4', (0, 0.49), (0, 3))])
]

create_detailed_region_plot(regions, x_boundaries=[0.49, 0.86], y_boundaries=[3.0, 6.1, 8.0],
                            x_label='ABCDNet Score', y_label='$|\Delta\eta_{jj}|$',
                            condition_text='')
