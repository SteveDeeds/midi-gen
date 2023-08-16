from midiutil.MidiFile import MIDIFile
import random
import numpy as np

def drums_two_step(scale, mf:MIDIFile, chords, volume, track):
    for bar, chord in enumerate(chords):
        mf.addNote(track, track, 35, bar*4, .5, volume) # 35 = kick
        mf.addNote(track, track, 38, bar*4+2, .5, volume) # 38 = snare
        for beat in np.arange(0,4,1):
            mf.addNote(track, track, 42, bar*4+beat, .5, volume) # 42 = CHH
            mf.addNote(track, track, 42, bar*4+beat+0.5, .5, volume//2) # 42 = CHH

def drums_probabilistic(scale, mf:MIDIFile, chords, volume, track):
            #1    e    +    a    2    e    +    a    3   e     +    a    4    e    +    a
    kick_p =  [1,   0,   0,   0,   0.5, 0,   0,   0,   0.8,   0,   0,   0,   0.5, 0,   0,   0]
    snare_p = [0,   0,   0,   0,   0.8,   0,   0,   0,   0.5, 0,   0,   0,   1,   0,   0,   0]
    chh_p =   [0.8, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4]

    kick = np.zeros((16))
    snare = np.zeros((16))
    chh = np.zeros((16))

    for sixteenth in range(16):
        if random.random() < kick_p[sixteenth]:
            kick[sixteenth] = 1
        if random.random() < snare_p[sixteenth]:
            snare[sixteenth] = 1
        if random.random() < chh_p[sixteenth]:
            chh[sixteenth] = 1

    for bar, chord in enumerate(chords):
        for sixteenth in range(16):
            if kick[sixteenth] > 0:
                mf.addNote(track, track, 35, bar*4+sixteenth/4, .5, volume) # 35 = kick
            if snare[sixteenth] > 0:
                mf.addNote(track, track, 38, bar*4+sixteenth/4, .5, volume) # 38 = snare
            if chh[sixteenth] > 0:
                mf.addNote(track, track, 42, bar*4+sixteenth/4, .5, volume) # 42 = CHH

def drum_subdivided(scale, mf:MIDIFile, chords, volume, track):
    subdivisions = []
    for _ in range(4):
        subdivisions.append(random.randint(0,3))
    for bar, chord in enumerate(chords):
        mf.addNote(track, track, 35, bar*4, .5, volume) # 35 = kick
        mf.addNote(track, track, 38, bar*4+2, .5, volume) # 38 = snare        
        for quarter in range(4):
            match (subdivisions[quarter]):
                case 0:
                    _
                case 1:
                    mf.addNote(track, track, 42, bar*4+quarter, 1, volume) # 42 = CHH
                case 2:
                    mf.addNote(track, track, 42, bar*4+quarter, 0.5, volume)
                    mf.addNote(track, track, 42, bar*4+quarter+0.5, 0.5, volume)
                case 3:
                    mf.addNote(track, track, 42, bar*4+quarter, 0.125, volume)
                    mf.addNote(track, track, 42, bar*4+quarter+0.125, 0.125, volume)
                    mf.addNote(track, track, 42, bar*4+quarter+0.125*2, 0.125, volume)
                    mf.addNote(track, track, 42, bar*4+quarter+0.125*3, 0.125, volume)