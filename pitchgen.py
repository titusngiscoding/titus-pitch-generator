import wave, struct, math

SAMPLE_RATE = 44100.0
CHANNELS = 1 #mono
SAMPLE_WIDTH = 2 #16-bit
VOLUME = 20000.0 #max 32767.0

class PitchGenerator:
    def __init__(self,duration=5.0,standard=440.0):
        self.duration=duration
        self.standard=standard

    def pitchToFrequency(self,note="A4"):
        return 864.0

    def generateWAV(self,note="A4"):
        self.frequency=self.pitchToFrequency(note)
        wavef = wave.open(note + ".wav", "w")
        wavef.setnchannels(CHANNELS)
        wavef.setsampwidth(SAMPLE_WIDTH) 
        wavef.setframerate(SAMPLE_RATE)
        for i in range(int(self.duration * SAMPLE_RATE)):
            value = int(VOLUME*math.sin(self.frequency*math.pi*float(i)/float(SAMPLE_RATE)))
            data = struct.pack('<h', value)
            wavef.writeframesraw(data)
        #wavef.writeframes('')
        wavef.close()
