import os, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer
from pitch_generator import PitchGenerator

MUSIC_NOTES=["C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","A#","Bb","B"]

def generateFilename(note,standard):
    return "{}4({}).wav".format(note,standard)

def playNote(filepath):
    mixer.init()
    player = mixer.Sound(filepath)
    length = player.get_length()
    print("Playing {} ...".format(filepath))
    player.play()
    time.sleep(length)

def getIsTryAgain():
    while(True):
        inputDecision = input("One more time? (y/n): ").lower()
        if inputDecision in ["y","yes"]:
            return True
        elif inputDecision in ["n","no"]:
            return False

def main():
    print("titus-pitch-generator 1.0")
    standard=int(input("Please enter standard: "))
    pg=PitchGenerator(standard=standard)
    print("Notes available: {}".format(MUSIC_NOTES))
    print()
    again=True
    while again:
        note = input("Please enter note: ")
        filepath = pg.generateWAV(note,generateFilename(note,standard))
        playNote(filepath)
        again=getIsTryAgain()
        print()
    input("Press Enter to exit ...")
    
if __name__ == "__main__":
    main()
