class FitnessLogic:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout, duration_str):
        if not workout or not duration_str:
            return {"status": "error", "message": "Please enter both workout and duration."}

        try:
            duration = int(duration_str)
            self.workouts.append({"workout": workout, "duration": duration})
            return {"status": "success", "message": f"'{workout}' added successfully!"}
        except ValueError:
            return {"status": "error", "message": "Duration must be a number."}

    def get_workouts_summary(self):
        if not self.workouts:
            return "No workouts logged yet."

        workout_list = "Logged Workouts:\n"
        for i, entry in enumerate(self.workouts):
            workout_list += f"{i+1}. {entry['workout']} - {entry['duration']} minutes\n"
        return workout_list