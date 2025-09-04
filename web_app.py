from flask import Flask, render_template, request, redirect, url_for, flash
from .fitness_logic import FitnessLogic

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

logic = FitnessLogic()

@app.route('/')
def index():
    """Renders the main page of the web app."""
    workouts = logic.get_workouts_summary()
    return render_template('index.html', workouts=workouts)

@app.route('/add_workout_web', methods=['POST'])
def add_workout_web():
    """Handles adding a workout from a web form."""
    workout_name = request.form.get('workout_name')
    duration = request.form.get('duration')

    result = logic.add_workout(workout_name, duration)

    flash(result["message"], result["status"])
    return redirect(url_for('index'))