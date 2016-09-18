'''
Sentence Length Evaluator v1.0
By Henry Xue
Python 3.5.2
'''

miniC = 3
maxiW = 15
delimiter = ".,!;'?"
fileReport = "asd.txt"
savesleReport = "y"
filesleReport = "sdf.txt"

debug = False

def printd(message):
    if debug == True:
        print("DEBUG: " + message)

def inputHelp():
    printd("HELP")
    pInputsBHelp = True

    while pInputsBHelp: ## TO BE FINISHED
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
            print("About SLE")
            print("Read the SRS")
        elif pInputsHelp == "2":
            print("Installing SLE")
            print("No installation needed")
        elif pInputsHelp == "3":
            print("Launching SLE")
            print("Type 'python SLE.py' in command line interface")
        elif pInputsHelp == "4":
            print("Changing SLE parameters")
            print("When prompt to change parameters, you can change parameters.")
        elif pInputsHelp == "4.1":
            print("Changing minimum characters in word")
            print("When prompt to change parameters, select (1).")
        elif pInputsHelp == "4.2":
            print("Changing maximum words in sentence")
            print("When prompt to change parameters, select (2).")
        elif pInputsHelp == "4.3":
            print("Changing punctuation marking end of sentence")
            print("When prompt to change parameters, select (3).")
        elif pInputsHelp == "5":
            print("Analyzing a report")
            print("When prompt for report, type report with extension (*.txt).")
        elif pInputsHelp == "6":
            print("Tracking historical results")
            print("Historical results are tracked in a file of choice according to...")
            print("file | average")
        elif pInputsHelp == "7":
            printd("Exit help")
            pInputsBHelp = False
        else:
            print("ERROR: Invalid Input!!")

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
                    if miniC.lower() == "help":
                        continue
                    miniC = int(miniC)
                    break
                except:
                    print("ERROR: Invalid Input!!")
        elif pInputs == "2":
            while True:
                print("\nA good sentence should have how many words, maximum?")
                try:
                    maxiW = validateInput(input("-> ").lower())
                    if maxiW.lower() == "help":
                        continue
                    maxiW = int(maxiW)
                    break
                except:
                    print("ERROR: Invalid Input!!")
        elif pInputs == "3":
            while True:
                print("\nWhat punctuation should mark the end of sentence? Please list all.")
                try:
                    delimiter = validateInput(input("-> ").lower())
                    if delimiter == "help":
                        continue
                    break
                except:
                    print("ERROR: Invalid Input!!")
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
            print("ERROR: Invalid Input!!")

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
            if rInputsFile[-4:].lower() != ".txt":
                print("ERROR: Invalid Extension!!")
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
            if rInputsFile[-4:].lower() != ".txt":
                print("ERROR: Invalid Extension!!")
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

    for i in listReportS:
        for j in i.split():
            if len(j) >= miniC: # Check Char Length
                listReportW.append(j)

    blankLines(listReportW)
    
    print("\nIn " + fileReport + ",")

    reportMean = len(listReportW)/len(listReportS)
    print("The average sentence length is " + str(reportMean) + ".")

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
    
    print("These sentences are too long:")
    if len(listLongS) == 0:
        print("None")
    else:
        for i in listLongS:
            print(i.strip())

    fileOpen = open(filesleReport, "r")
    for i in fileOpen:
        listHistorical.append(i.replace("\n", "").split(" | ")[1])
        historicalMean += float(i.replace("\n", "").split(" | ")[1])
    fileOpen.close()
    historicalMean = (historicalMean+reportMean)/(len(listHistorical)+1)
    
    print("Your historical average sentence length is " + str(historicalMean) + ".")
    print("Previous results:")
    previousResults()

    if savesleReport == "y":
        fileOpen = open(filesleReport, "a")
        fileOpen.write(fileReport + " | " + str(reportMean) + "\n")
        fileOpen.close()
        printd("SAVED")
        
    anotherReport()

def previousResults():
    fileOpen = open(filesleReport, "r")
    for i in fileOpen:
        tmpTxt = i.replace("\n", "").split(" | ")
        print("In " + tmpTxt[0] + ", the average sentence length is ", end="")
        print(tmpTxt[1] + "w/s.")
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
                print("ERROR: Invalid Extension!!")
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
