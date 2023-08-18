from midiutil.MidiFile import MIDIFile
import random
import numpy as np

def bass_root_eights(scale, mf:MIDIFile, chords, volume, track):
    for bar, chord in enumerate(chords):
        for beat in np.arange(0,4,0.5):
            mf.addNote(track, track, scale[chord]+12, bar*4+beat, 0.5, volume)

def bass_third_eights(scale, mf:MIDIFile, chords, volume, track):
    for bar, chord in enumerate(chords):
        for beat in np.arange(0,4,0.5):
            mf.addNote(track, track, scale[chord+2]+12, bar*4+beat, 0.5, volume)

def bass_one_and_four(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [0,2,4,7]
    for _ in range(2):
        intervals.append(random.choice(allowed_intervals))
    for bar, chord in enumerate(chords):
        mf.addNote(track, track, scale[chord+intervals[0]]+12, bar*4, 0.5, volume)
        mf.addNote(track, track, scale[chord+intervals[0]]+12, bar*4+0.5, 2.5, volume*3//4)
        mf.addNote(track, track, scale[chord+intervals[1]]+12, bar*4+3, 0.5, volume)

def bass_random(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    allowed_intervals = [-1,-1,-1,-1,0,2,4,7]
    for _ in range(8):
        intervals.append(random.choice(allowed_intervals))
    for bar, chord in enumerate(chords):
        for eighth in range(8):
            if intervals[eighth] >= 0:
                mf.addNote(track, track, scale[chord+intervals[eighth]]+12, bar*4+eighth/2, 0.5, volume)

def bass_wild(scale, mf:MIDIFile, chords, volume, track):
    allowed_intervals = [-1,-1,-1,-1,0,2,4,7]
    for bar, chord in enumerate(chords):
        for eighth in range(8):
            interval = random.choice(allowed_intervals)
            mf.addNote(track, track, scale[chord+interval]+12, bar*4+eighth/2, 0.5, volume)

def bass_subdivided(scale, mf:MIDIFile, chords, volume, track):
    intervals =[]
    subdivisions = []
    allowed_intervals = [0,2,4,7]
    for _ in range(4):
        intervals.append(random.choice(allowed_intervals))
        subdivisions.append(random.randint(0,2))
    for bar, chord in enumerate(chords):
        for quarter in range(4):
            match (subdivisions[quarter]):
                case 0:
                    _
                case 1:
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter, 1, volume)
                case 2:
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter, 0.5, volume)
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter+0.5, 0.5, volume)
                case 3:
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter, 0.125, volume)
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter+0.125, 0.125, volume)
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter+0.125*2, 0.125, volume)
                    mf.addNote(track, track, scale[chord+intervals[quarter]]+12, bar*4+quarter+0.125*3, 0.125, volume)