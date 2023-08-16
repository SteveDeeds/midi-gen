from midiutil.MidiFile import MIDIFile
import random
import numpy as np

def rhythm_drop_one_eigths(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7,9,11,14]
    for _ in range(random.randint(3, 5)):
        intervals.append(random.choice(allowed_intervals))

    pattern = np.ones(8) 
    pattern[random.randint(0,7)]=0
    for bar, chord in enumerate(chords):
        for eighth in range(8):
            if pattern[eighth] > 0:        
                for i, interval in enumerate(intervals):
                    mf.addNote(track, track, scale[chord+interval]+24, bar*4+eighth/2, 0.5, volume)

def rhythm_quarter_notes(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7,9,11,14]
    for _ in range(random.randint(3, 5)):
        intervals.append(random.choice(allowed_intervals))

    for bar, chord in enumerate(chords):
        for quarter in range(8):     
            for i, interval in enumerate(intervals):
                mf.addNote(track, track, scale[chord+interval]+24, bar*4+quarter, 1, volume)