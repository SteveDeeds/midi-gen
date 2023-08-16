from midiutil.MidiFile import MIDIFile
import random
import numpy as np

def pad_arp(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7,9,11,14]
    for _ in range(random.randint(3, 5)):
        intervals.append(random.choice(allowed_intervals))    
    for bar, chord in enumerate(chords):
        for i, interval in enumerate(intervals):
            mf.addNote(track, track, scale[chord+interval]+24, bar*4+i/2, 4-i/2, volume)

def pad_hold(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7,9,11,14]
    for _ in range(random.randint(3, 5)):
        intervals.append(random.choice(allowed_intervals))
    for bar, chord in enumerate(chords):
        for interval in intervals:
            mf.addNote(track, track, scale[chord+interval]+24, bar*4, 4, volume)