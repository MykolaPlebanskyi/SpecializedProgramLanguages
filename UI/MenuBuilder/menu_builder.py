"""
Menu System Module

This module defines an abstract base class 'Menu' and a 'MenuFacade' class
to manage a collection of menus. The 'Menu' class serves as a blueprint for
individual menu implementations, and the 'MenuFacade' class provides a
user-friendly interface for interacting with multiple menus.

Classes:
    - Menu: Abstract base class for menu implementations.
    - MenuFacade: Facade class for managing a collection of menus.

Usage:
    Create instances of specific menu classes that inherit from 'Menu' to define
    custom menu behaviors. Then, use the 'MenuFacade' class to organize and present
    these menus to users.
"""
import json
from abc import ABC, abstractmethod


class Menu(ABC):
    """
    A base class for creating menus.

    This class provides a template for creating menus in an application.
    Subclasses must implement the `run` method.

    Attributes:
        _config (dict): A dictionary containing the configuration variables for the menu.

    """

    def __init__(self):
        with open('config.json', 'r') as config_file:
            self._config = json.load(config_file)
            self._config = self._config["variables"]

    @abstractmethod
    def run(self):
        """
        Abstract method to be implemented by subclasses.

        This method defines the behavior of the menu when it is executed.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """