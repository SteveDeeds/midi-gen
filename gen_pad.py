from midiutil.MidiFile import MIDIFile
import random
import numpy as np

def pad_arp(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7,9,11,14]
    random.shuffle(allowed_intervals)
    for _ in range(random.randint(3, 5)):
        intervals.append(allowed_intervals.pop())   
    for bar, chord in enumerate(chords):
        for i, interval in enumerate(intervals):
            time = bar*4+i/2
            duration = 4-i/2
            pitch = scale[chord+interval]+24
            mf.addNote(track, track, pitch, time, duration, volume)
            #print(F"pitch ={pitch} time={time}, duration={duration}")

def pad_hold(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7,9,11,14]
    random.shuffle(allowed_intervals)
    for _ in range(random.randint(3, 5)):
        intervals.append(allowed_intervals.pop())   
    for bar, chord in enumerate(chords):
        for interval in intervals:
            mf.addNote(track, track, scale[chord+interval]+24, bar*4, 4, volume)

def pad_change(scale, mf:MIDIFile, chords, volume, track):

    for bar, chord in enumerate(chords):
        intervals =[]
        allowed_intervals = [0,2,4,7,9,11,14]
        random.shuffle(allowed_intervals)
        for _ in range(random.randint(3, 5)):
            intervals.append(allowed_intervals.pop())   
        if random.random() < 0.2:
            intervals.append(random.choice([6,8,10]))        
        for interval in intervals:
            mf.addNote(track, track, scale[chord+interval]+24, bar*4, 4, volume)

