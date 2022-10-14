"""
Tests for midi_handler module
"""
# Import Libraries
from Modules.MIDIHandler.midi_handler import MidoMidiFile as midi_file

# Constants
mid = midi_file("C:/Users/jack_/Desktop/Queen - Bohemian Rhapsody.mid")

# Tests
def test_print_all_messages():
    mid.print_all_messages()