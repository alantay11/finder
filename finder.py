import os
import codecs

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()
missingTotal = 0

print("Do you have an exported list? (Y/N)")
exported = input().lower() == "y"

if exported:
    print("Please input file name of the exported list")
    listName = input()
    if os.path.isfile(listName):
        exportedList = codecs.open(listName, "r", encoding="utf8")     
    else:
        print("The file could not be found, please try again")
        exit()

print("How many digits is your index?")
indexSize = int(input())
print("What is your starting index?")
startIndex = int(input())
counter = startIndex
print("What is your ending index?")
totalNo = input()
print("Do you want to save the results? (Y/N)")
save = input().lower() == "y"

if save and os.path.exists("missing.txt"):
    print("File already exists, do you want to overwrite it? (Y/N)")
    delete = input().lower() == "y"    
    if delete:
        os.remove("missing.txt")        
    else:
        print("Check the existing file")
        exit()

print()

if save:
    resultTextFile = codecs.open("missing.txt", "a", encoding="utf8")
    
for f in files:
    if f[indexSize + 1] == "5" or f[indexSize] != ".": # for skipping manually downloaded replacements with XX.5 naming scheme and other files
        continue
    try:    
        currentIndex = f[:indexSize]
        #print("zero counter: "+ str(counter) + " currentIndex: " + currentIndex + " file: " + f)
        if counter != int(currentIndex):
            missingTotal += 1

            if exported:
                for line in exportedList:   
                    if counter > int(totalNo) - startIndex + 1:
                        break
                    line = line.strip()
                    if line == str(counter) or line == "0" + str(counter) or line == "00" + str(counter):
                        #print("firstR counter: " + str(counter) + " line: " + line + " currentIndex: " + currentIndex)
                        resultLine = (str(counter) + ". " + next(exportedList).strip() + " is missing")
                        print(resultLine)
                        if save:
                            resultTextFile.write(resultLine + "\n")
                        break   
                
                counter += 1
    
                while counter < int(currentIndex) + 1:
                    if counter != int(currentIndex):
                        missingTotal += 1
                        for innerLine in exportedList:  
                            if counter > int(totalNo) - startIndex + 1:
                                break
                            innerLine = innerLine.strip()
                            if innerLine == str(counter) or innerLine == "0" + str(counter) or innerLine == "00" + str(counter):
                                #print("secondR counter: " + str(counter) + " line: " + innerLine)
                                innerResultline = innerLine + ". " + next(exportedList).strip() + " is missing"
                                print(innerResultline)
                                if save:
                                    resultTextFile.write(innerResultline + "\n")       
                                break                            
                    counter += 1
            else:
                resultLine = str(counter) + " is missing"
                print(resultLine)        
                if save:
                    resultTextFile.write(resultLine + "\n")
                counter += 1
    
                while counter < int(currentIndex) + 1:
                    if counter != int(currentIndex):
                        missingTotal += 1
                        resultLine = str(counter) + " is missing"
                        print(resultLine)        
                        if save:
                            resultTextFile.write(resultLine + "\n")                        
                    counter += 1
        else:
            counter += 1                
    except:
        pass

counter += 1

for counter in range(counter, int(totalNo) + 1):
    if exported:
        for line in exportedList:  
            if counter > int(totalNo) - startIndex + 1:
                break    
            line = line.strip()
            if line == str(counter) or line == "0" + str(counter) or line == "00" + str(counter):
                #print("thirdR counter: " + str(counter) + " line: " + line)
                resultLine = str(counter) + ". " + next(exportedList).strip() + " is missing"
                print(resultLine)
                if save:
                    resultTextFile.write(resultLine + "\n")
                break
        missingTotal += 1
    else:
        for counter in range(counter, int(totalNo) + 1):
            resultLine = str(counter) + " is missing"
            print(resultLine)
            missingTotal += 1
            if save:
                resultTextFile.write(resultLine + "\n")
            counter += 1
    
    counter += 1

resultLine = "Total missing: " + str(missingTotal)
print(resultLine)
if save:
    resultTextFile.write(resultLine + "\n")

properTotal = int(totalNo) - startIndex + 1
actualTotal = int(totalNo) - startIndex - missingTotal + 1
resultLine = "You have " + str(actualTotal) + "/" + str(properTotal) + " videos"
print(resultLine)    

if save:
    resultTextFile.write(resultLine)
    resultTextFile.close()

if exported:
    exportedList.close()
