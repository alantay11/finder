import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()
missingTotal = 0

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
    resultTextFile = open("missing.txt","a")

    for f in files:
        if f[indexSize + 1] == "5": # for skipping manually downloaded replacements with XX.5 naming scheme
            continue
        try:    
            currentIndex = f[:indexSize]
            if counter != int(currentIndex):
                missingTotal += 1
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
        resultLine = str(counter) + " is missing"
        print(resultLine)
        missingTotal += 1
        if save:
            resultTextFile.write(resultLine + "\n")
        counter += 1
    
    resultLine = "Total missing: " + str(missingTotal)
    print(resultLine)
    resultTextFile.write(resultLine + "\n")
    
    properTotal = int(totalNo) - startIndex + 1
    actualTotal = int(totalNo) - startIndex - missingTotal + 1
    resultLine = "You have " + str(actualTotal) + "/" + str(properTotal) + " videos"
    print(resultLine)    
    
    resultTextFile.write(resultLine)
    resultTextFile.close()
else:
    for f in files:
        if f[indexSize + 1] == "5": # for skipping manually downloaded replacements with XX.5 naming scheme
            continue
        try:    
            currentIndex = f[:indexSize]
            if counter != int(currentIndex):
                missingTotal += 1
                resultLine = str(counter) + " is missing"
                print(resultLine)        
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
        resultLine = str(counter) + " is missing"
        print(resultLine)
        missingTotal += 1
        counter += 1
    
    print("Total missing: " + str(missingTotal))
    
    properTotal = int(totalNo) - startIndex + 1
    actualTotal = int(totalNo) - startIndex - missingTotal + 1
    print("You have " + str(actualTotal) + "/" + str(properTotal) + " videos")   