import wave, struct, math

SAMPLE_RATE = 44100.0
CHANNELS = 1 #mono
SAMPLE_WIDTH = 2 #2=16bit
VOLUME = (2**(8*SAMPLE_WIDTH-1)-1)//2 #max = 2**(8*SAMPLE_WIDTH-1)-1
NOTES=["E","F","F#","G","G#","A","A#","B","C","C#","D","D#"]
EQUIVILANTS={"Db":"C#", "Eb":"D#", "Gb":"F#", "Ab":"G#", "Bb":"A#"}

class PitchGenerator:
    def __init__(self,duration=5.0,standard=440.0):
        self.duration=duration
        self.standard=standard

    def flatToSharp(self,note="A"):
        if note in EQUIVILANTS:
            return EQUIVILANTS[note]
        else:
            return note

    def pitchToFrequency(self,note="A"):
        note=self.flatToSharp(note)
        steps=NOTES.index(note)-NOTES.index("A")
        return self.standard*(2**(1/12))**(steps)

    def generateWAV(self,note="A"):
        self.frequency=self.pitchToFrequency(note)
        wavef = wave.open(note + ".wav", "w")
        wavef.setnchannels(CHANNELS)
        wavef.setsampwidth(SAMPLE_WIDTH) 
        wavef.setframerate(SAMPLE_RATE)
        for i in range(int(self.duration * SAMPLE_RATE)):
            value = int(VOLUME*math.sin(self.frequency*SAMPLE_WIDTH*math.pi*float(i)/float(SAMPLE_RATE)))
            data = struct.pack('<h', value)
            wavef.writeframesraw(data)
        wavef.close()
