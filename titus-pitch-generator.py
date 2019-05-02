from pitchgen import PitchGenerator

MUSIC_NOTES=["C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","A#","Bb","B"]
def main():
    print("titus-pitch-generator 1.0")
    print("Notes available: {}".format(MUSIC_NOTES))
    pg = PitchGenerator()
    note = pg.sanitizeInput("Please enter a Note: ")
    filename = pg.generateWAV(note)
    pg.playNote(filename)
    input("Press Enter to exit ...")
    
if __name__ == "__main__":
    main()
