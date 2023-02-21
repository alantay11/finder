import os
import codecs

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()
resultTextFile = codecs.open("names.txt", "a", encoding="utf8")
    
for f in files:   
    resultTextFile.write(f + "\n")         

resultTextFile.close()
