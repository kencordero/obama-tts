# Cordero 8.12 Text-to-Speech v0.2

#updating 13.04 v 0.3.0
import sys
import csnd
import pyxine
from random import sample, shuffle

class CsdFile(object):
    def __init__(self):
        pass
    def create(self, file_name):
        self.file = open(file_name, "w")
        self.file.write('<CsoundSynthesizer>\n\n')
        add_options()
        add_instruments()
        add_score()
        self.file.write('</CsoundSynthesizer>')
        self.file.close()
    def add_options(self):
        self.file.write('<CsOptions>\n')
        self.file.write('  -o speech.wav\n')
        self.file.write('</CsOptions>\n\n')
        pass
    def add_instruments(self):
        self.instrument_count = 0
        self.file.write('<CsInstruments>\n')
        add_instrument('My Mother Preferred A Gentler Portrait.wav')
        add_instrument('I Pulled Into The Airport Parking Lot.wav')
        add_instrument('Auma Drove.wav')
        add_instrument('speech on racism.wav')
        self.file.write('</CsInstruments>\n\n')
    def add_score(self):
        self.file.write('<CsScore>\n')
        self.file.write(';in  time     len      off\n')
        current_time = 0.0
        #TODO choose method
        self.file.write('</CsScore>\n\n')
    def add_instrument(self, file_name):
        self.instrument_count += 1
        self.file.write('instr {0}\n  iskptim = p4\n  a1, a2 soundin "{1}", iskptim\n  a1 = a1 + a2\n  out a1\nendin\n\n'.format(self.instrument_count, file_name))

class TextToSpeechEngine:
    def tts():
        text = []
        for arg in sys.argv:
            if arg != "tts.py" and arg[0] != '>':
                text.append(arg)
        srcFile = open("dictionary.txt", "r")
        all_data = []
        for line in srcFile:
            line = line.strip()
            data = line.split(" ")
            all_data.append(data)
        tts = dict()
        for word in all_data:
            tts[word[0]] = [word[1], word[2], word[3]]
        #TODO create and write csd file                        

    def create_sound_file(csd_data_file):
        #run csound        
        cs = csnd.Csound()
        res = cs.Compile(csd_data_file)
        cs.Perform()
    
    def play_sound_file():        
        xine = pyxine.Xine()
        stream = xine.stream_new()
        stream.open("obama.wav")
        stream.play()
        input("Press enter to exit...")
        
    def create_data_file():
        #TODO
        pass
    
    def standard():
        for word in text:
            if tts.has_key(word):
                vals = tts[word]
                dstFile.write("i%d %f %f %f\n" % (int(vals[0]), currentTime, float(vals[2]), float(vals[1])))
                currentTime += float(vals[2])           
    
    def antakshari_shuffle():
        count = 0
        s = tts.keys()
        shuffle(s)
        for word in s:
            if (count == 0 or word[0] == last_letter):
                vals = tts[word]
                dstFile.write("i%d %f %f %f\n" % (int(vals[0]), currentTime, float(vals[2]), float(vals[1])))
                currentTime += float(vals[2])
                last_letter = word[len(word)-1]
                count += 1   

    def sample():
        s = sample(tts.keys(), 100)
        for i in s:
            vals = tts[i]
            dstFile.write("i%d %f %f %f\n" % (int(vals[0]), currentTime, float(vals[2]), float(vals[1])))
            currentTime += float(vals[2])
