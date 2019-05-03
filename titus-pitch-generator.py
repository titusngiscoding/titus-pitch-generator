import os, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer
from pitch_generator import PitchGenerator

MUSIC_NOTES=["C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","A#","Bb","B"]

def playNote(filename):
    mixer.init()
    player = mixer.Sound(filename)
    length = player.get_length()
    print("Playing {} ...".format(filename))
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
    print("Notes available: {}".format(MUSIC_NOTES))
    again=True
    while again:
        print()
        note = input("Please enter note: ")
        standard=440
        print("Asserting A4 = 440 hz")
        filename="cache/{}4({}).wav".format(note,standard)
        if not os.path.exists(filename):
            pg = PitchGenerator(standard=standard)
            pg.generateWAV(note,filename)
        playNote(filename)
        again=getIsTryAgain()
    input("Press Enter to exit ...")
    
if __name__ == "__main__":
    main()
