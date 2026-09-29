from goals import calculate_progress


def test_progress_calculation():
    assert calculate_progress(9, 12) == 75.0


def test_goal_achieved():
    assert calculate_progress(12, 12) == 100.0


def test_half_goal():
    assert calculate_progress(5, 10) == 50.0