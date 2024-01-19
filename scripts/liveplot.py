import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

# Create an empty DataFrame
data = pd.DataFrame(columns=['Time', 'Weight', 'Delta'])
# Set target completion weight
target_completion_weight = 375
# Set target completion time
target_completion_time = 60 * 4

# Create DataFrame with the provided recipe data
recipe_data = pd.DataFrame({
    'Time': [0, 5, 30, 45, 60, 75, 90, 115, 210],
    'Weight': [0, 75, 75, 175, 175, 275, 275, 375, 375],
    'Coffee': [24, 24, 24, 24, 24, 24, 24, 24, 24]
})

# Plot the Recipe
plt.plot(recipe_data['Time'], recipe_data['Weight'], marker='o', linestyle='-', color='blue', label='Target Recipe')
plt.title('HL-V60 Coffee Recipe')
plt.xlabel('Time (seconds)')
plt.ylabel('Weight (grams)')
plt.legend()

# Set initial x-axis and y-axis limits
plt.xlim(0, target_completion_time)
plt.ylim(0, target_completion_weight)

def record_weight(i):
    # Simulate weight measurement
    current_time = int(time.time())
    weight = simulate_weight()

    # Calculate delta from the target recipe
    delta = weight - recipe_data['Weight'].iloc[-1]

    # Append data to DataFrame
    data.loc[current_time] = [current_time, weight, delta]

    # Plot the graph
    plt.clf()
    plt.plot(data['Time'], data['Weight'], label='Actual Weight', color='green')
    plt.plot(data['Time'], data['Weight'] - data['Delta'], label='Delta (Actual - Target)', color='red', linestyle='--')
    plt.title('Weight of Water Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Weight (grams)')
    plt.legend()


def simulate_weight():
    # Simulate weight measurement by incrementing the weight until it reaches 375 grams
    if 'last_weight' not in simulate_weight.__dict__:
        simulate_weight.last_weight = 0

    simulate_weight.last_weight += random.uniform(1, 3)  # Increment weight by a random value
    return min(simulate_weight.last_weight, target_completion_weight)


# Set up animation
ani = animation.FuncAnimation(plt.gcf(), record_weight, interval=250)

# Show the live graph
plt.show()
