import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 7))

# Draw the Arduino
ax.add_patch(patches.Rectangle((1, 8), 2, 1, edgecolor='blue', facecolor='lightblue'))
ax.text(1.5, 8.5, 'Arduino', horizontalalignment='center', verticalalignment='center')

# Draw the L298N Motor Driver
ax.add_patch(patches.Rectangle((4, 4), 4, 3, edgecolor='red', facecolor='pink'))
ax.text(6, 5.5, 'L298N', horizontalalignment='center', verticalalignment='center')
ax.text(4.1, 6.7, 'ENA', verticalalignment='center')
ax.text(4.1, 6.4, 'IN1', verticalalignment='center')
ax.text(4.1, 6.1, 'IN2', verticalalignment='center')
ax.text(4.1, 5.8, '12V', verticalalignment='center')
ax.text(4.1, 5.5, 'GND', verticalalignment='center')
ax.text(4.1, 5.2, 'OUT1', verticalalignment='center')
ax.text(4.1, 4.9, 'OUT2', verticalalignment='center')
ax.text(4.1, 4.6, 'ENB', verticalalignment='center')
ax.text(4.1, 4.3, 'IN3', verticalalignment='center')
ax.text(4.1, 4.0, 'IN4', verticalalignment='center')
ax.text(4.1, 3.7, 'GND', verticalalignment='center')
ax.text(4.1, 3.4, 'OUT3', verticalalignment='center')
ax.text(4.1, 3.1, 'OUT4', verticalalignment='center')

# Draw the LEGO NXT Motors
ax.add_patch(patches.Rectangle((10, 6), 2, 1, edgecolor='green', facecolor='lightgreen'))
ax.text(11, 6.5, 'Motor A', horizontalalignment='center', verticalalignment='center')

# Draw the power supply
ax.add_patch(patches.Rectangle((7, 0), 2, 1, edgecolor='black', facecolor='gray'))
ax.text(8, 0.5, 'Power Supply', horizontalalignment='center', verticalalignment='center')

# Connections from Arduino to L298N
ax.annotate('', xy=(3, 8.5), xytext=(4.5, 6.7), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(3.5, 7.8, 'ENA (D9)', verticalalignment='center')
ax.annotate('', xy=(3, 8.5), xytext=(4.5, 6.4), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(3.5, 7.5, 'IN1 (D2)', verticalalignment='center')
ax.annotate('', xy=(3, 8.5), xytext=(4.5, 6.1), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(3.5, 7.2, 'IN2 (D3)', verticalalignment='center')
ax.annotate('', xy=(3, 8.5), xytext=(4.5, 4.6), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(3.5, 6.9, 'ENB (D10)', verticalalignment='center')
ax.annotate('', xy=(3, 8.5), xytext=(4.5, 4.3), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(3.5, 6.6, 'IN3 (D4)', verticalalignment='center')
ax.annotate('', xy=(3, 8.5), xytext=(4.5, 4.0), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(3.5, 6.3, 'IN4 (D5)', verticalalignment='center')

# Connections from L298N to Motors
ax.annotate('', xy=(8.5, 6.4), xytext=(9.5, 6.5), arrowprops=dict(arrowstyle="->", color='black'))
ax.annotate('', xy=(8.5, 6.1), xytext=(9.5, 6.5), arrowprops=dict(arrowstyle="->", color='black'))

# Connections from Power Supply to L298N
ax.annotate('', xy=(8, 1), xytext=(5.5, 5.8), arrowprops=dict(arrowstyle="->", color='black'))
ax.annotate('', xy=(8, 1), xytext=(5.5, 3.7), arrowprops=dict(arrowstyle="->", color='black'))
ax.annotate('', xy=(8, 1), xytext=(5.5, 5.5), arrowprops=dict(arrowstyle="->", color='black'))

# Labels
ax.text(7, 1.5, '12V', verticalalignment='center')
ax.text(7, 2, 'GND', verticalalignment='center')

# Connections from NXT Motor to Arduino
ax.annotate('', xy=(11.5, 6.5), xytext=(2, 7.5), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(6, 7.5, 'Pin 3 (Red) -> GND', verticalalignment='center')
ax.annotate('', xy=(11.5, 6.5), xytext=(2, 7), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(6, 7, 'Pin 4 (Green) -> 5V', verticalalignment='center')
ax.annotate('', xy=(11.5, 6.5), xytext=(2, 6.5), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(6, 6.5, 'Pin 5 (Yellow) -> D6', verticalalignment='center')
ax.annotate('', xy=(11.5, 6.5), xytext=(2, 6), arrowprops=dict(arrowstyle="->", color='black'))
ax.text(6, 6, 'Pin 6 (Blue) -> D7', verticalalignment='center')

# Set limits and turn off the axes
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

plt.show()
