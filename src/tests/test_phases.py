import pytest
from src.game.phases import BasicPhase


def test_basic_phase_start(capsys):
    phase = BasicPhase()
    phase.start_phase()
    captured = capsys.readouterr()
    assert "Starting basic phase..." in captured.out


def test_basic_phase_execution(capsys):
    phase = BasicPhase()
    phase.execute_phase()
    captured = capsys.readouterr()
    assert "Executing basic phase..." in captured.out


def test_basic_phase_end(capsys):
    phase = BasicPhase()
    phase.end_phase()
    captured = capsys.readouterr()
    assert "Ending basic phase..." in captured.out
