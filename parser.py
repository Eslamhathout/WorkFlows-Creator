import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from sequenceCreator import sequenceCreator
import re


dfs = pd.read_excel('WDI.xlsx', sheet_name='All', skiprows={0,1,2,3}, index_col=4)


#Getting Columns Data
actionsList = dfs['Actions']
actionTypeList = dfs['Action Type']
invokedSequencesList = dfs['Invoked Sequences']
inputsArgumentsList = dfs['Inputs Arguments']
outputsArgumentsList = dfs['Outputs Arguments']
startScreenList = dfs['Start Screen']
endScreenList = dfs['End Screen']

#Get instance of the class
creatorCLS = sequenceCreator()
# x = creatorCLS.getXML()
# print(x)

for i in range(10,11):
    inputsList = [re.findall(r'.* ', i) for i in inputsArgumentsList[i].split(',') ]
    print (inputsList)
    creatorCLS.sequenceCreator(actionsList[i], inputsList, [outputsArgumentsList[i]], "Usage : use" )