# Cordero 8.12 Text-to-Speech v0.2

#updating 13.04 v 0.3.0
import sys

class TextToSpeechEngine:
	def tts:
		pass

	def create_sound_file(csd_data_file):
		#run csound
		import csnd
		cs = csnd.Csound()
		res = cs.Compile(csd_data_file)
		cs.Perform()
	
	def play_sound_file:
		import pyxine
		xine = pyxine.Xine()
		stream = xine.stream_new()
		stream.open("obama.wav")
		stream.play()
		input("Press enter to exit...")
		
	def create_data_file():
		#TODO
		pass
	
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
#create and write csd file
dstFile = open("tts.csd", "w")
dstFile.write("<CsoundSynthesizer>\n\n<CsOptions>\n  -o speech.wav\n</CsOptions>\n\n<CsInstruments>\ninstr 1\n  iskptim = p4\n")
dstFile.write("  a1, a2 soundin \"My Mother Preferred A Gentler Portrait.wav\", iskptim\n  a1 = a1 + a2\n  out a1\nendin\n\ninstr 2\n")
dstFile.write("  iskptim = p4\n  a1, a2 soundin \"I Pulled Into The Airport Parking Lot.wav\", iskptim\n  a1 = a1 + a2\n  out a1\nendin")
dstFile.write("\n\ninstr 3\n  iskptim = p4\n  a1, a2 soundin \"Auma Drove.wav\", iskptim\n  a1 = a1 + a2\n  out a1\nendin\n")
dstFile.write("\ninstr 4\n  iskptim = p4\n  a1 soundin \"speech on racism.wav\", iskptim\n  out a1\nendin\n</CsInstruments>\n")
dstFile.write("\n<CsScore>\n;in  time     len      off\n")
currentTime = 0.0
for word in text:
  if tts.has_key(word):
    vals = tts[word]
    dstFile.write("i%d %f %f %f\n" % (int(vals[0]), currentTime, float(vals[2]), float(vals[1])))
    currentTime += float(vals[2])
dstFile.write("</CsScore>\n\n</CsoundSynthesizer>")
dstFile.close()



