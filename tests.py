# tests.py
import time
import pytest
from unittest.mock import patch
from control_main import control_light  # Replace 'your_module_name' with the actual name of your module

# Test the control_light function when turning the light on and off
def test_control_light_turn_on_off():
    # Mock the print function to capture the printed messages
    with patch('builtins.print') as mock_print:
        # Mock the is_pressed function to simulate pressing 'ctrl' three times
        with patch('keyboard.is_pressed') as mock_is_pressed:
            mock_is_pressed.side_effect = [False, True, False, True, False, True, False]
            
            # Call the function being tested
            control_light()
    
    # Define the expected calls to the print function
    calls = [call('Press Ctrl to control the light. Press \'q\' to quit.'),
             call('Light ON'), call('Light ON'), call('Light ON'),
             call('Exiting...')]

    # Assert that the print function was called with the expected messages
    mock_print.assert_has_calls(calls, any_order=True)

# Test the control_light function when exiting the program
def test_control_light_exit():
    # Mock the print function to capture the printed messages
    with patch('builtins.print') as mock_print:
        # Mock the is_pressed function to simulate pressing 'q' once
        with patch('keyboard.is_pressed') as mock_is_pressed:
            mock_is_pressed.side_effect = [False, False, False, True]
            
            # Call the function being tested
            control_light()
    
    # Define the expected calls to the print function
    calls = [call('Press Ctrl to control the light. Press \'q\' to quit.'),
             call('Exiting...')]

    # Assert that the print function was called with the expected messages
    mock_print.assert_has_calls(calls, any_order=True)
