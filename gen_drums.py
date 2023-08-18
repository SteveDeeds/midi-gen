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

    tom_notes = [41,43,45,47,48,50]

              #1    e    +    a    2    e    +    a    3    e    +    a    4    e    +    a
    kick_p =  [1,   0.2, 0.4, 0,   0.8, 0,   0,   0,   0.5, 0,   0,   0,   0.5, 0,   0,   0.2]
    snare_p = [0,   0,   0,   0,   0.5, 0,   0,   0.2, 1,   0.2, 0.5, 0,   0.8, 0, 0.3,   0]
    chh_p =   [0.8, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4]
    tom_p =   [0,   0,   0,   0,   0,   0,   0,   0,   0.3, 0.1, 0,   0,   0.6, 0.1, 0.9, 0.1]

    kick = np.zeros((16))
    snare = np.zeros((16))
    chh = np.zeros((16))
    crash = np.zeros((16))
    tom = np.zeros((16))

    for sixteenth in range(16):
        if random.random() < kick_p[sixteenth]:
            kick[sixteenth] = 1
        if random.random() < snare_p[sixteenth]:
            snare[sixteenth] = 1
        if random.random() < chh_p[sixteenth]:
            chh[sixteenth] = 1
        if random.random() < tom_p[sixteenth]:
            tom[sixteenth] = 1
    
    if(random.random()<0.9):
        crash[0] = 1
        if(random.random()<0.5):
            crash[4] = 1
            if(random.random()<0.5):
                crash[8] = 1
    
    # change some of the closed high hats to open high hats
    # print(tom)
    ohh = []
    for i, sixteenth in enumerate(chh):
        if random.random() < 0.2:
            ohh.append(sixteenth)
            chh[i] = 0
        else:
            ohh.append(0)

    for bar, chord in enumerate(chords):
        for sixteenth in range(16):
            if kick[sixteenth] > 0:
                mf.addNote(track, track, 36, bar*4+sixteenth/4, .5, volume) # 36 = electronic kick (also C1)
            if snare[sixteenth] > 0:
                mf.addNote(track, track, 38, bar*4+sixteenth/4, .5, volume) # 38 = snare
            if chh[sixteenth] > 0:
                mf.addNote(track, track, 42, bar*4+sixteenth/4, .5, volume) # 42 = CHH
            if ohh[sixteenth] > 0:
                mf.addNote(track, track, 46, bar*4+sixteenth/4, .5, volume) # 46 = OHH
            if crash[sixteenth] > 0 and bar==0:
                mf.addNote(track, track, 49, bar*4+sixteenth/4, .5, volume) # 49 = crash
            if tom[sixteenth] > 0 and (bar==3 or bar==7):
                mf.addNote(track, track, random.choice(tom_notes), bar*4+sixteenth/4, .5, volume) 

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