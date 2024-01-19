import pandas as pd
import matplotlib.pyplot as plt
import time


def record_weight():
    # Create an empty DataFrame
    data = pd.DataFrame(columns=['Time', 'Weight'])

    # Simulate tracking weight over time
    for i in range(10):  # You can adjust the number of data points as needed
        time.sleep(1)  # Simulate 1-second intervals
        current_time = int(time.time())  # Get current time in seconds
        weight = simulate_weight()  # Simulate weight measurement (replace with actual measurement)

        # Add data to DataFrame
        data = pd.concat([data, pd.DataFrame([[current_time, weight]], columns=['Time', 'Weight'])], ignore_index=True)
    return data


def simulate_weight():
    # Simulate weight measurement (replace with actual measurement)
    # For this example, let's use a random weight between 0 and 100 grams
    import random
    return random.uniform(0, 100)


def plot_graph(data):
    # Plot the graph using Matplotlib
    plt.plot(data['Time'], data['Weight'])
    plt.title('Weight of Water Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Weight (grams)')
    plt.show()


# Main execution
if __name__ == "__main__":
    # Record weight data
    weight_data = record_weight()

    # Display the recorded data
    print("Recorded Weight Data:")
    print(weight_data)

    # Plot the graph
    plot_graph(weight_data)
