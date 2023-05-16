
def testChart(chel):
    print(chel.name)
    for category, score in chel.dictResults.items():
        print(category, ": ", score)


import matplotlib.pyplot as plt
import numpy as np


def draw_chart(chel):
    print(chel.name)
    for category, score in chel.dictResults.items():
        print(category, ": ", score)

    rows = 6
    categories = list(chel.dictResults.keys())
    values = list(chel.dictResults.values())

    fig, ax = plt.subplots(figsize=(16, 12))

    # Plotting the lines
    for i in range(rows):
        ax.hlines(i + 1, 0, values[i], color='blue', linewidth=2)
        ax.text(-2, i + 1, categories[i], ha='right', va='center', fontsize=12)

    ax.set_xlim(0, max(values) + 5)
    ax.set_ylim(0, rows + 1)
    ax.set_yticks(range(1, rows + 1))
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.grid(axis='y', linestyle='--', linewidth=0.5)

    # Graph label
    ax.text(0.5, rows + 1.3, chel.name, ha='center', va='center', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.savefig('chart.png', dpi=200)
    plt.show()


# Example usage:
class ExampleChel:
    def __init__(self, name, dictResults):
        self.name = name
        self.dictResults = dictResults


# Create a sample instance of Chel
chel = ExampleChel("Example Chel",
                   {"Маскулинность/Феминность": 15, "Поиск стимуляции": 25, "Манипулятивность": 10, "Установка на успех": 28, "Напористость": 18,
                    "Агрессивность": 12})

# Draw the chart
draw_chart(chel)
