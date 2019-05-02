import wave, struct, math, time, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer

SAMPLE_RATE = 44100.0
CHANNELS = 1 #mono
SAMPLE_WIDTH = 2 #2=16bit
VOLUME = 30000 #max = 2**(8*SAMPLE_WIDTH-1)-1 (for 16bit, thats 32767)
NOTES=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
EQUIVILANTS={"Db":"C#", "Eb":"D#", "Gb":"F#", "Ab":"G#", "Bb":"A#"}

class PitchGenerator:
    def __init__(self,duration=5,standard=440):
        self.duration=duration
        self.standard=standard
        print("Asserting A4 = 440 hz")

    def flatToSharp(self,note="A"):
        if note in EQUIVILANTS:
            return EQUIVILANTS[note]
        else:
            return note

    def pitchToFrequency(self,note="A"):
        note=self.flatToSharp(note)
        steps=NOTES.index(note)-NOTES.index("A")
        return self.standard*(2**(1/12))**(steps)

    def playNote(self,filename):
        print("Playing note ...")
        mixer.init()
        mixer.music.load(filename)
        mixer.music.play()
        time.sleep(5)

    def generateWAV(self,note="A"):
        frequency=self.pitchToFrequency(note)
        print("Generating {} seconds of {}4 = {} hz ...".format(self.duration,note,frequency))
        filename="cache/{}4({}).wav".format(note,self.standard)
        wavef = wave.open(filename, "w")
        wavef.setnchannels(CHANNELS)
        wavef.setsampwidth(SAMPLE_WIDTH) 
        wavef.setframerate(SAMPLE_RATE)
        for i in range(int(self.duration * SAMPLE_RATE)):
            value = int(VOLUME*math.sin(frequency*SAMPLE_WIDTH*math.pi*float(i)/float(SAMPLE_RATE)))
            data = struct.pack('<h', value)
            wavef.writeframesraw(data)
        wavef.close()
        print("Saved note to {}".format(filename))
        return filename
