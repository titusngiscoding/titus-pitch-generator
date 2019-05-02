from pitchgen import PitchGenerator

def main():
    note=input("Enter note: ")
    pg=PitchGenerator()
    pg.generateWAV(note)
    input("Press Enter to exit ...")
    
if __name__ == "__main__":
    main()
