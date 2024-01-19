from datetime import datetime
import customtkinter as ctk


class CoffeeTimer(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.parent = parent
        self.timer_label = None
        self.timer_running = False

        # Start button
        self.start_button = ctk.CTkButton(parent, text="Start Timer", command=self.start_timer, fg_color='transparent',
                                          hover_color='#4158D0', border_color='#4158D0', border_width=2)
        self.start_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Timer label
        self.timer_label = ctk.CTkLabel(parent, text="Timer: 0:00", font=('Helvetica', 30))
        self.timer_label.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def toggle_timer(self):
        if self.timer_running:
            self.stop_timer()
            self.start_button.configure(text="Start Timer")
        else:
            self.start_timer()
            self.start_button.configure(text="Stop Timer")

    def update_timer(self):
        start_time = datetime.now()
        while self.timer_running:
            elapsed_time = datetime.now() - start_time
            timer_str = f"Timer: {elapsed_time.seconds // 60}:{elapsed_time.seconds % 60:02}"
            self.timer_label.configure(text=timer_str)
            self.parent.update_idletasks()
            self.parent.after(100)
