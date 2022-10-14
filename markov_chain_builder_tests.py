"""
Tests for building markv chain from midi files
"""
# Import Libraries
from Modules.MarkovChainBuilder.markov_chain_builder import MIDIMarkovChain
from Modules.MIDIHandler.midi_handler import MidoMidiFile

# Constants
mid = MidoMidiFile("C:/Users/jack_/Desktop/Queen - Bohemian Rhapsody.mid")

# Tests
def test_build_markov_chain():
    mrkv_chn = MIDIMarkovChain(mid.get_midi_notes())
    
    for i in range(0, 20):
        print(mrkv_chn.get_next_state())

test_build_markov_chain()