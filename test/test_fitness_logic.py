import pytest
from ..fitness_logic import FitnessLogic # The '..' is important for the package structure

def test_add_workout_success():
    """Test successful addition of a workout."""
    logic = FitnessLogic()
    result = logic.add_workout("Running", "30")
    assert result["status"] == "success"
    assert len(logic.workouts) == 1
    assert logic.workouts[0] == {'workout': 'Running', 'duration': 30}

def test_add_workout_missing_fields():
    """Test adding a workout with missing fields."""
    logic = FitnessLogic()
    result = logic.add_workout("", "30")
    assert result["status"] == "error"
    assert "Please enter both" in result["message"]
    assert len(logic.workouts) == 0

def test_add_workout_invalid_duration():
    """Test adding a workout with a non-numeric duration."""
    logic = FitnessLogic()
    result = logic.add_workout("Cycling", "thirty")
    assert result["status"] == "error"
    assert "Duration must be a number" in result["message"]
    assert len(logic.workouts) == 0

def test_get_workouts_summary_empty():
    """Test the summary message when no workouts are logged."""
    logic = FitnessLogic()
    summary = logic.get_workouts_summary()
    assert summary == "No workouts logged yet."

def test_get_workouts_summary_with_entries():
    """Test the summary message with multiple workout entries."""
    logic = FitnessLogic()
    logic.add_workout("Running", "30")
    logic.add_workout("Lifting", "45")
    summary = logic.get_workouts_summary()
    expected_message = "Logged Workouts:\n1. Running - 30 minutes\n2. Lifting - 45 minutes\n"
    assert summary == expected_message