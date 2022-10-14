"""
This module deals with loading midi files into the desired format for analysis
"""
# Import Libraries
import mido

# Define Classes
class MidoMidiFile():
    """Wrapper for midi file object
    """
    # Constructor
    def __init__(self, path_to_file):
        self.midi_file = mido.MidiFile(path_to_file)
        self.midi_data = self._extract_midi_data()
      
    # Public Methods  
    def get_track_names(self):
        """Extracts track names contained in the midi file object

        Returns:
            List<string>: names of all the tracks in the midi file
        """
        tracks = []
        for i, track in enumerate(self.midi_file.tracks):
            tracks.append(track.name)
        
        return tracks
    
    def print_all_messages(self):
        for i, track in enumerate(self.midi_file.tracks):
            for msg in track:
                if msg.type == "note_on":
                    print(msg)
    
    def get_midi_notes(self):
        return [data.note for data in self.midi_data]
    
    # Private Methods
    def _extract_midi_data(self):
        midi_data = []
        for i, track in enumerate(self.midi_file.tracks):
            for msg in track:
                if msg.type == "note_on":
                    midi_data.append(MIDINoteData(msg))
        
        return midi_data
        
      
class MIDINoteData:
    """
    Struct for holding important midi note info
    """    
    def __init__(self, mido_msg):
        self.note = mido_msg.note
        self.velocity = mido_msg.velocity
        self.length = mido_msg.time
    
    def print_values(self):
        """Prints the properties of MIDI note
        """
        print('Note: {} Velocity: {} Length: {}'.format(self.note, self.velocity, self.length))
        

    """
    Takes mido message object and return desired value
    Args:
        midiMsg (_type_): _description_
    """    
    print("Place holder")