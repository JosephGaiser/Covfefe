import customtkinter as ctk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from timer import CoffeeTimer

package = __package__ or 'app'

# Sample pour-over recipes data (you can replace this with your actual data)
recipes_data = {
    'Chemex': {'Time (s)': [0, 30, 60, 90, 120], 'Water (g)': [0, 60, 180, 300, 420]},
    'V60': {'Time (s)': [0, 15, 45, 75, 105], 'Water (g)': [0, 50, 150, 250, 350]},
}


class CoffeeApp:
    def __init__(self, root: ctk.CTk):
        self.root = root
        self.root.title("Coffee Pour-Over App")
        self.root.geometry("800x800")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.canvas = None
        self.target_weight_label = None

        # Recipe selection
        self.recipe_label = ctk.CTkLabel(root, text="Select Recipe:", font=('Helvetica', 12))
        self.recipe_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.recipe_var = ctk.StringVar()
        self.recipe_combobox = ctk.CTkComboBox(root, variable=self.recipe_var, values=list(recipes_data.keys()))
        self.recipe_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        # Plot button
        self.plot_button = ctk.CTkButton(root, text="Plot Recipe", command=self.plot_recipe)
        self.plot_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # Timer
        self.timer_frame = ctk.CTkFrame(root)
        self.timer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.timer = CoffeeTimer(self.timer_frame)
        self.timer.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def plot_recipe(self):
        selected_recipe = self.recipe_var.get()

        if selected_recipe in recipes_data:
            recipe_data = recipes_data[selected_recipe]

            # Create a DataFrame from recipe data
            df = pd.DataFrame(recipe_data)

            # Use a style that matches the app's theme
            plt.style.use('dark_background')  # You can change the style to match your preference

            # Plot the data with custom styling
            fig, ax = plt.subplots()
            ax.plot(df['Time (s)'], df['Water (g)'], marker='o', color='cyan', linestyle='-', linewidth=2)

            # Customize the appearance
            ax.set_xlabel('Time (s)', fontweight='bold', fontsize=12, color='white')
            ax.set_ylabel('Water (g)', fontweight='bold', fontsize=12, color='white')
            ax.set_title(f'{selected_recipe} Pour-Over Recipe', fontweight='bold', fontsize=14, color='white')

            # If canvas exists, hide it
            if hasattr(self, 'canvas') and self.canvas is not None:
                self.canvas.get_tk_widget().grid_forget()

            # Display the new plot in the tkinter window
            self.canvas = FigureCanvasTkAgg(fig, master=self.root)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("./themes/NeonBanana.json")
    main = ctk.CTk()
    app = CoffeeApp(main)
    main.mainloop()
