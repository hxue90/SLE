'''
Sentence Length Evaluator v1.0
By Henry Xue
Python 3.5.2
'''
import os


miniC = 3
maxiW = 15
delimiter = ".,!;'?"
fileReport = ""
savesleReport = "y"
filesleReport = ""

debug = False

def printd(message):
    if debug == True:
        print("DEBUG: " + message)

def inputHelp():
    printd("HELP")
    pInputsBHelp = True

    while pInputsBHelp:
        print("\nPlease input the number for the help topic you're seeking:")
        print("1 - About SLE")
        print("2 - Installing SLE")
        print("3 - Launching SLE")
        print("4 - Changing SLE parameters")
        print("4.1 - Changing minimum characters in word")
        print("4.2 - Changing maximum words in sentence")
        print("4.3 - Changing punctuation marking end of sentence")
        print("5 - Analyzing a report")
        print("6 - Tracking historical results")
        print("7 - Exit help")
        pInputsHelp = input("-> ").lower()
        if pInputsHelp == "1":
            print("\nAbout SLE\nSLE aka Sentence Length Evaluator is an application used to", end=" ")
            print("help analyze, reported and track average sentence length for plain text reports.", end=" ")
            print("It help users avoid using over-long-run-on sentences.")
        elif pInputsHelp == "2":
            print("\nInstalling SLE")
            print("No installation of SLE is required.")
        elif pInputsHelp == "3":
            print("\nLaunching SLE")
            print("On command line interface, change directory to SLE directory.", end=" ")
            print("Type 'python SLE.py' *Python 3.5.2 is required*")
        elif pInputsHelp == "4":
            print("\nChanging SLE parameters")
            print("Users will be prompt to change SLE parameters such as 'minimum characters in a word',", end=" ")
            print("'maximum words in sentence', 'punctuation marking end of sentence'. Select valid options when prompt.")
        elif pInputsHelp == "4.1":
            print("\nChanging minimum characters in word")
            print("When prompt to change SLE parameters, select (1).")
        elif pInputsHelp == "4.2":
            print("\nChanging maximum words in sentence")
            print("When prompt to change SLE parameters, select (2).")
        elif pInputsHelp == "4.3":
            print("\nChanging punctuation marking end of sentence")
            print("When prompt to change SLE parameters, select (3).")
        elif pInputsHelp == "5":
            print("\nAnalyzing a report")
            print("When prompt for user report, type user report with extension (*.txt).")
        elif pInputsHelp == "6":
            print("\nTracking historical results")
            print("Historical results are tracked in a SLE report file of choice.", end=" ")
            print("Historical results include file name and average sentence length.")
        elif pInputsHelp == "7":
            printd("Exit help")
            pInputsBHelp = False
        else:
            print("ERROR: Invalid input for help topic.")

def validateInput(vInput):
    printd("VALIDATE INPUT")
    if vInput == "help":
        inputHelp()
        return vInput
    else:
        return vInput
        
def parametersInput():
    printd("PARAMETERS INPUT")
    global miniC, maxiW, delimiter
    pInputsB = True
    
    while pInputsB:
        print("\nPlease input the number for any parameter you want to change or continue:")
        print("(1) Minimum characters in word")
        print("(2) Maximum words in sentence")
        print("(3) Punctuation marking end of sentence")
        print('(4) None; I will keep all defaults - 3,15,".,!;' + "'?" + '"')
        print("(5) Continue - " + str(miniC) + "," + str(maxiW) + ',"' + delimiter + '"')
        pInputs = input("-> ").lower()
        if pInputs == "1":
            while True:
                print("\nThe smallest word I should count contains how many letters?")
                try:
                    miniC = validateInput(input("-> ").lower())
                    if miniC == "help":
                        continue
                    miniC = int(miniC)
                    break
                except:
                    print("ERROR: Invalid input for minimum number of characters in a word.")
        elif pInputs == "2":
            while True:
                print("\nA good sentence should have how many words, maximum?")
                try:
                    maxiW = validateInput(input("-> ").lower())
                    if maxiW == "help":
                        continue
                    maxiW = int(maxiW)
                    break
                except:
                    print("ERROR: Invalid input for maximum words in a sentence.")
        elif pInputs == "3":
            while True:
                print("\nWhat punctuation should mark the end of sentence? Please list all.")
                try:
                    delimiter = validateInput(input("-> ").lower())
                    if delimiter == "help":
                        continue
                    break
                except:
                    print("ERROR: Invalid input for punctuation.")
        elif pInputs == "4":
            printd("None")
            pInputsB = False
            requestReport()
        elif pInputs == "5":
            printd("Continue")
            pInputsB = False
            requestReport()
        elif pInputs == "help":
            inputHelp()
        else:
            print("ERROR: Invalid input for parameters.")

def requestReport():
    printd("REQUEST REPORT")
    global fileReport
    rInputs = True

    while rInputs:
        print("\nPlease provide the name of the .txt report (in the SLE folder) you want SLE to analyze.")
        rInputsFile = input("-> ").lower()
        if rInputsFile == "help":
            inputHelp()
        else:
            if rInputsFile[-4:] != ".txt":
                print("ERROR: Invalid file extension.")
                continue
            fileReport = rInputsFile

            try:
                fileOpen = open(fileReport, "r")
                fileOpen.close()
            except FileNotFoundError:
                print("Error: No such file or directory '" + fileReport + "'")
                continue
            except:
                print("Error: Problem importing file '" + fileReport + "'")
                continue

            requestSLEReport()            
            rInputs = False

def requestSLEReport():
    printd("REQUEST SLE REPORT")
    global filesleReport, savesleReport
    rInputs = True

    while rInputs:
        print("\nDo you have an SLE report you'd like these results to be added to?")
        print("If yes, make sure it's in the SLE folder and provide the name. If no, type 'n'.")
        rInputsFile = input("-> ").lower()
        if rInputsFile == "n":
            printd("n")
            savesleReport = "n"
            checkReport()
            rInputs = False
        elif rInputsFile == "help":
            inputHelp()
        else:
            if rInputsFile[-4:] != ".txt":
                print("ERROR: Invalid file extension.")
                continue
            filesleReport = rInputsFile

            try:
                fileOpen = open(filesleReport, "r")
                fileOpen.close()
            except FileNotFoundError:
                print("Error: No such file or directory '" + filesleReport + "'")
                continue
            except:
                print("Error: Problem importing file '" + filesleReport + "'")
                continue

            savesleReport = "y"

            fileOpen = open("SLE.tmp", "w") # Clear out SLE.tmp
            fileOpen.close()
            
            checkReport()
            rInputs = False

def blankLines(lst):
    while True:
        try:
            lst.remove("")
        except ValueError:
            return lst
            break

def checkReport():
    printd("CHECK REPORT")
    global fileReport, filesleReport
    listReportS = []
    listReportW = []
    listReportTMP = []
    listHistorical = []
    listLongS = []
    reportMean = 0
    historicalMean = 0
    
    fileOpen = open(fileReport, "r") # Import Whole Report O(n)
    for i in fileOpen:
        listReportS.append(i.replace("\n", ""))
    fileOpen.close()

    for i in delimiter: # Sentence Detection O(n^3)
        listReportTMP = listReportS
        listReportS = []
        for j in listReportTMP:
            for k in j.split(i):
                listReportS.append(k)

    blankLines(listReportS)

    for i in listReportS: # Check word length O(n^2)
        for j in i.split():
            if len(j) >= miniC:
                listReportW.append(j)

    blankLines(listReportW)
    
    print("\nIn " + fileReport + ",")
    saveTmp("\nIn " + fileReport + ",")

    reportMean = len(listReportW)/len(listReportS)
    print("The average sentence length is " + str(reportMean) + ".")
    saveTmp("The average sentence length is " + str(reportMean) + ".")

    listReportTMP = [] # Remove non-words
    for i in listReportS:
        tmpStr = ""
        for j in i.split():
            if len(j) >= miniC:
                listReportW.append(j)
                tmpStr += " " + j
        listReportTMP.append(tmpStr)
    listReportS = listReportTMP

    for i in listReportS: # Long Sentence Detection
        if len(i.split()) > maxiW:
            listLongS.append(i)
    
    if len(listLongS) == 0:
        print("There are no too long sentences.")
        saveTmp("There are no too long sentences.")
    else:
        print("These sentences are too long:")
        saveTmp("These sentences are too long:")
        counter = 0
        for i in listLongS:
            counter += 1
            print(str(counter) + ": " +i.strip())
            saveTmp(str(counter) + ": " +i.strip())

    if savesleReport == "y":
        if os.stat(filesleReport).st_size == 0:
            print("There are no historical average sentence length.")
            saveTmp("There are no historical average sentence length.")
            return
        
        fileOpen = open(filesleReport, "r")
        counter = 0
        for i in fileOpen:
            counter += 1
            try:
                listHistorical.append(i.replace("\n", "").split(" | ")[1])
                historicalMean += float(i.replace("\n", "").split(" | ")[1])
            except:
                print("ERROR: Line " + str(counter) + " in SLE report is invalid so skipped.")
        fileOpen.close()
        historicalMean = (historicalMean+reportMean)/(len(listHistorical)+1)

        print("Your historical average sentence length is " + str(historicalMean) + ".")
        saveTmp("Your historical average sentence length is " + str(historicalMean) + ".")

        print("Previous results:")
        saveTmp("Previous results:")
        previousResults()

        fileOpen = open(filesleReport, "a")
        fileOpen.write(fileReport + " | " + str(reportMean) + "\n")
        fileOpen.close()
        printd("SAVED")
    else:
        print("There are no historical average sentence length.")
        saveTmp("There are no historical average sentence length.")
        
    anotherReport()

def saveTmp(saveStr):
    fileOpen = open("SLE.tmp", "a")
    fileOpen.write(saveStr + "\n")
    fileOpen.close()

def previousResults():
    fileOpen = open(filesleReport, "r")
    counter = 0
    for i in fileOpen:
        counter += 1
        try:
            tmpTxt = i.replace("\n", "").split(" | ")
            float(tmpTxt[1]) # Check invalid lines
            print("In " + tmpTxt[0] + ", the average sentence length is ", end="")
            saveTmp("In " + tmpTxt[0] + ", the average sentence length is " + tmpTxt[1] + "w/s.")
            print(tmpTxt[1] + "w/s.")
        except:
            print("ERROR: Line " + str(counter) + " in SLE report is invalid so skipped.")
            continue
    fileOpen.close()

def anotherReport():
    printd("ANOTHER REPORT")
    global fileReport
    rInputs = True

    while rInputs:
        print("\nHave another report in the SLE folder to analyze?", end=" ")
        print("If so, please provide the exact name.\nIf no, type 'n'")
        rInputsFile = input("-> ").lower()
        if rInputsFile == "help":
            inputHelp()
        elif rInputsFile == "n":
            print("\nGood bye, writer!")
            exit()
        else:
            if rInputsFile[-4:] != ".txt":
                print("ERROR: Invalid file extension.")
                continue
            fileReport = rInputsFile

            try:
                fileOpen = open(fileReport, "r")
                fileOpen.close()
            except FileNotFoundError:
                print("Error: No such file or directory '" + fileReport + "'")
                continue
            except:
                print("Error: Problem importing file '" + fileReport + "'")
                continue

            checkReport()           
            rInputs = False
        
def main():
    print("Hi, writer!\nWelcome to the Sentence Length Evaluator.")
    print("I am going to analyse the length of sentences in you're report, to help you be more efficient writer.")
    print("Anytime you need help input 'help'")

    try:
        firstTime = open("SLE.ocx", "r")
        if firstTime.readline() != "firstTime=0":
            firstTime.close()
            print("\nI notice this is your first time using Sentence Length Evaluator.")
            print("Let me help you.")
            firstTime = open("SLE.ocx", "w")
            firstTime.write("firstTime=0")
            firstTime.close()
            inputHelp()
    except IOError:
        print("\nI notice this is your first time using Sentence Length Evaluator.")
        print("Let me help you.")
        firstTime = open("SLE.ocx", "w")
        firstTime.write("firstTime=0")
        firstTime.close()
        inputHelp()

    parametersInput()

if __name__ == "__main__":
    main()
