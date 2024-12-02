# Abstractions for different game phases, allowing flexibility to add new phases in the future

from abc import ABC, abstractmethod


class Phase(ABC):
    """
    Abstract base class for game phases.
    """
    @abstractmethod
    def start_phase(self):
        pass

    @abstractmethod
    def execute_phase(self):
        pass

    @abstractmethod
    def end_phase(self):
        pass


class BasicPhase(Phase):
    """
    A simple implementation of a basic game phase.
    """
    def start_phase(self):
        print("Starting basic phase...")

    def execute_phase(self):
        print("Executing basic phase...")

    def end_phase(self):
        print("Ending basic phase...")
