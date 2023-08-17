
import random

# choose random chord roots
def A_A_prime():
    notes =[]
    for i in range(4):
        notes.append(random.randint(0, 5))

    if(random.random()>0.5):
        notes.sort()

    chords = [notes[0], notes[1], notes[2], notes[2], 
          notes[0], notes[1], notes[3], notes[3]]
              
    return chords

def rock_and_turn():
    notes =[]
    for i in range(3):
        notes.append(random.randint(0, 5))

    if(random.random()>0.5):
        notes.sort()

    chords = [notes[0], notes[1], notes[0], notes[1], 
          notes[0], notes[1], notes[2], notes[2]]
              
    return chords