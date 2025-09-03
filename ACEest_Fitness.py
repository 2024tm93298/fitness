import tkinter as tk
from tkinter import messagebox
from .fitness_logic import FitnessLogic # The '.' is important for a proper package structure

class FitnessTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("ACEestFitness and Gym")
        self.logic = FitnessLogic() # Use an instance of the logic class

        # Labels and Entries for adding workouts
        self.workout_label = tk.Label(master, text="Workout:")
        self.workout_label.grid(row=0, column=0, padx=5, pady=5)
        self.workout_entry = tk.Entry(master)
        self.workout_entry.grid(row=0, column=1, padx=5, pady=5)

        self.duration_label = tk.Label(master, text="Duration (minutes):")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(master)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(master, text="Add Workout", command=self.add_workout)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Workouts", command=self.view_workouts)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_workout(self):
        workout = self.workout_entry.get()
        duration_str = self.duration_entry.get()

        result = self.logic.add_workout(workout, duration_str)

        if result["status"] == "success":
            messagebox.showinfo("Success", result["message"])
            self.workout_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", result["message"])

    def view_workouts(self):
        summary = self.logic.get_workouts_summary()
        messagebox.showinfo("Workouts", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()