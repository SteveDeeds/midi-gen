from midiutil.MidiFile import MIDIFile
import random
import numpy as np
import gen_drums
import gen_bass
import gen_pad
import gen_rhythm
import gen_chords

scale = [24,26,28,29,31,33,35, # octave 0
         36,38,40,41,43,45,47, # octave 1
         48,50,52,53,55,57,59, # octave 2
         60,62,64,65,67,69,71, # octave 3
         72,74,76,77,79,81,83, # octave 4
         84,86,88,89,91,93,95, # octave 5
         96,98,100,101,103,105,107, # octave 6
         108,110,112,113,115,117,119,120]  # octave 7


functions = [gen_chords.A_A_prime, gen_chords.rock_and_turn]
random_function = random.choice(functions)

chords = random_function()

to_chords = ["C", "Dm", "Em", "F", "G", "Am", "Bdim"]

for chord in chords:
    print (F"{to_chords[chord]} ", end='')

for i in range(8):
# create your MIDI object
    mf = MIDIFile(numTracks=16)    
    volume = 100
    ## bass ####################
    track = 1
    volume = 100
    mf.addTempo(track, 0, 120)
    mf.addProgramChange(track, track, time=0, program=34) # 34 = Fingered Bass
    mf.addTrackName(track, 0, "bass")
    functions = [gen_bass.bass_third_eights, gen_bass.bass_root_eights, gen_bass.bass_one_and_four, gen_bass.bass_random, gen_bass.bass_subdivided]
    random_function = random.choice(functions)
    random_function(scale, mf, chords, volume, track)

    ### pad ####################
    track = 2
    volume = 80
    mf.addProgramChange(track, track, time=0, program=17) # 17 = organ
    mf.addTrackName(track, 0, "pad")
    functions = [gen_pad.pad_arp, gen_pad.pad_hold]
    random_function = random.choice(functions)
    random_function(scale, mf, chords, volume, track)

    ## rhythm ####################
    track = 3
    volume = 60
    mf.addProgramChange(track, track, time=0, program=30) # 30 = Overdrive Guitar
    mf.addTrackName(track, 0, "rhythm")
    functions = [gen_rhythm.rhythm_drop_one_eigths, gen_rhythm.rhythm_quarter_notes]
    random_function = random.choice(functions)
    random_function(scale, mf, chords, volume, track)

    ### drums ####################
    track = 9 # track 9 works as drums.  Most other tracks do not work as drums.
    volume = 100
    mf.addProgramChange(track, track, time=0, program=128)
    mf.addTrackName(track, 0, "drums")
    functions = [gen_drums.drums_two_step, gen_drums.drums_probabilistic, gen_drums.drum_subdivided]
    random_function = random.choice(functions)
    random_function(scale, mf, chords, volume, track)

    # write it to disk
    with open(F"output{i}.mid", 'wb') as outf:
        mf.writeFile(outf)



