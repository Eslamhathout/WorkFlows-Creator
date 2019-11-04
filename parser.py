import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from sequenceCreator import sequenceCreator
import re
import numpy as np


dfs = pd.read_excel('sample_WDI.xlsx', sheet_name='All', skiprows={0,1,2,3}, index_col=4)


# # Forcing naming convention on inputs, outputs, and action names
# def inputNamingConvention(inputVariables):
#     for inputvariable in inputVariables:
#         #Using startswith not contain!!
#         try:
#             if inputvariable.lower().startswith('in'):
#                 print(inputvariable)
#         except:
#             pass



#Getting Columns Data
applicationsList = dfs['Applications']
actionsList = dfs['Actions']
actionTypeList = dfs['Action Type']
invokedSequencesList = dfs['Invoked Sequences']
inputsArgumentsList = dfs['Inputs Arguments']
outputsArgumentsList = dfs['Outputs Arguments']
startScreenList = dfs['Start Screen']
endScreenList = dfs['End Screen']
actionDescription = dfs['Description']

#fill nan in application name
applicationsList = pd.Series(applicationsList).fillna(method='ffill')

#forcing inputs names
# inputsArgumentsList = inputNamingConvention(inputsArgumentsList)
# inputNamingConvention(inputsArgumentsList)

#Adding Naming Convention for Applications
# applicationsList = NamingConverntion('app_', applicationsList)

creatorCLS = sequenceCreator()


for i in range(0,len(actionsList)):
    # To skip nan actions
    if type(actionsList[i]) == type(4.0):
        pass
    else:
        print(actionsList[i])
        print(applicationsList[i])
        print("")
        #Inputs prep
        try:
            inputsList = [re.findall(r'(.*)?\)', i) for i in inputsArgumentsList[i].split(',') ]
        except AttributeError: #In case of no inputs "nan"
            inputsList = ""


        #Outputs prep
        try:
            outputsList = [re.findall(r'(.*)?\)', i) for i in outputsArgumentsList[i].split(',') ]
        except AttributeError: #In case of no inputs "nan"
            outputsList = ""
        
        #Annotation Prep
        try:
            reformatedInputsList = "Inputs: "+str([inputVariable[0].split('(')[0] for inputVariable in inputsList])
        except:
            reformatedInputsList = ""
        try:
            reofrmatedOutputsList = "Outputs: "+str([outputVariable[0].split('(')[0] for outputVariable in outputsList])
        except:
            reofrmatedOutputsList = ""
        annotationString = "Usage: " + str(actionDescription[i]) + "&#xA;" + reformatedInputsList + "&#xA;" + reofrmatedOutputsList + "&#xA;Start Scree: " + str(startScreenList[i]) + "&#xA;End Screen: " + str(endScreenList[i])

        # print(annotationString)
        # print (inputsList)
        print (applicationsList[i])

        creatorCLS.sequenceCreator(actionsList[i], inputsList, outputsList, annotationString, applicationsList[i])
