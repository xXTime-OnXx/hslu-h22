# RollDieWithArgument.py
"""Graphing frequencies of die rolls for a given number of rolls given by sys.argv"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import sys

# input how often the die should be rolled by a single command line argument
number_rolls = int(sys.argv[1])

# simulate the die rolls
rolls = [random.randrange(1, 7) for i in range(number_rolls)]
values, frequencies = np.unique(rolls, return_counts=True)

# create a title for the bar plot
title = f'{len(rolls):,} Mal Würfeln eines Würfels'

# overwrite the derault style white with no grid
sns.set_style('whitegrid')

# create and display the bar plot
axes = sns.barplot(x=values, y=frequencies, palette='bright')

# set the title of the plot
axes.set_title(title)

# label the axes
axes.set(xlabel='Augenzahl', ylabel='Häufigkeit')

# scale the y-axis to add room for text above bars
axes.set_ylim(top=max(frequencies) * 1.15)

# create and display the text for each bar
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
    
    
# display the graph in a window if startet from terminal
plt.show()