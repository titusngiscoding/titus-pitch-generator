import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from validation import sanitizeInput, caseInsensitiveIn, caseInsensitiveIndex
from pitch_generator import PitchGenerator

MUSIC_NOTES = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
YES_RESPONSES = ["y", "yes"]
NO_RESPONSES = ["n", "no"]
DEFAULT_STANDARD = 440


def generateFilename(note, standard):
    return "{}4({}).wav".format(note, standard)


def getYesNo(input_msg):
    ans = sanitizeInput(YES_RESPONSES + NO_RESPONSES, input_msg)
    return caseInsensitiveIn(ans, YES_RESPONSES)


def playNote(filepath):
    pygame.mixer.init()
    player = pygame.mixer.Sound(filepath)
    length = player.get_length()
    print("Playing {} ...".format(filepath))
    player.play()
    time.sleep(length)


def main():
    print("titus-pitch-generator 1.0")
    standard = DEFAULT_STANDARD
    use_default = getYesNo("Do you wish to use default standard: A4 = 440 hz? (y/n): ")
    if(not use_default):
        standard = int(sanitizeInput([str(x) for x in range(400, 500)], "Please enter standard (e.g. 432): "))
    pg = PitchGenerator(standard=standard)
    print("Notes available: {}".format(MUSIC_NOTES))
    print()
    again = True
    while again:
        note = sanitizeInput(MUSIC_NOTES, "Please enter a note: ")
        note = MUSIC_NOTES[caseInsensitiveIndex(note, MUSIC_NOTES)]
        filepath = pg.generateWAV(note, generateFilename(note, standard))
        playNote(filepath)
        again = getYesNo("One more time? (y/n): ")
        print()
    input("Press Enter to exit ...")


if __name__ == "__main__":
    main()
