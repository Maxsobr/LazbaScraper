# from matplotlib import pyplot as plt
#
# def boxgraph(chel):
#
#     name = list(chel.dictResults.keys())
#     price = list(chel.dictResults.values())
#
#     # Figure Size
#     fig, ax = plt.subplots(figsize=(16, 9))
#
#     # Horizontal Bar Plot
#     ax.barh(name, price)
#
#     # Remove axes splines
#     for s in ['top', 'bottom', 'left', 'right']:
#         ax.spines[s].set_visible(False)
#
#     # Remove x, y Ticks
#     ax.xaxis.set_ticks_position('none')
#     ax.yaxis.set_ticks_position('none')
#
#     # Add padding between axes and labels
#     ax.xaxis.set_tick_params(pad=5)
#     ax.yaxis.set_tick_params(pad=10)
#
#     # Add x, y gridlines
#     ax.grid(b=True, color='grey',
#             linestyle='-.', linewidth=0.5,
#             alpha=0.2)
#
#     # Show top values
#     ax.invert_yaxis()
#
#     # Add annotation to bars
#     for i in ax.patches:
#         plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
#                  str(round((i.get_width()), 2)),
#                  fontsize=10, fontweight='bold',
#                  color='grey')
#
#     title = f"Результаты {chel.name}"
#     # Add Plot Title
#     ax.set_title(title,
#                  loc='center', )
#
#
#     # Show Plot
#     plt.show()
import os

from matplotlib import pyplot as plt

def boxgraph(chel):

    name = list(chel.dictResults.keys())
    price = list(chel.dictResults.values())

    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))

    # Horizontal Bar Plot
    ax.barh(name, price,
            color=['#EA7370', '#89E389', '#B18485', '#EEE37A', '#637683',
                   '#00B7FE'])

    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    # Increase font size and make it bold
    plt.yticks(fontsize=20, weight='bold',minor=False, horizontalalignment='right', y=5)

    # Set x-axis ticks
    plt.xticks([0, 5, 10, 15, 20, 25, 30], fontsize=20, weight='bold')

    # Add x, y gridlines
    # ax.grid(color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

    # Show top values
    ax.invert_yaxis()

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=20, fontweight='bold',
                 color='grey')

    title = f"Результаты {chel.name}"
    # Add Plot Title
    ax.set_title(title, loc='center',fontsize=20, fontweight='bold')

    # Add frame around the plot axis
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    # Set spine width
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)

    filename = f"{chel.name}.png"

    # Assuming you want to save in a directory structure like "dir1/dir2"
    directory = "resultsPng"

    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Full path to the file
    filepath = os.path.join(directory, filename)

    # Save the plot as a separate PNG file
    plt.savefig(filepath, dpi=300, bbox_inches='tight')


    return filepath
