import os
class sequenceCreator:
    def getXML(self):
        xSequence = open("xSequence.xaml","r")
        sequenceTemplate = xSequence.readlines()
        return sequenceTemplate

    def NamingConverntion(self, initializer, NamesList):
        try:
            NamesList = NamesList.replace(initializer,'')
        except:
            pass
        if ' ' in NamesList:
            namingList = NamesList.split(' ')
            applicationName = [app.capitalize() for app in namingList]
            refinedName = initializer
            for appName in applicationName:
                refinedName += appName
            NamesList = refinedName
        else:
            NamesList = initializer + NamesList
        return NamesList

    def sequenceCreator(self, name, inputs, outputs, annotation, application):
        typeMapping = {
            'Integer':'Int32',
            'String':'String',
            'Boolean':'Boolean',
            'text':'String',
        }
        sequenceTemplate = sequenceCreator.getXML(self)

        ArgsRange=[]
        for i in range(0, len(sequenceTemplate)):
            if 'AnnotationText' in sequenceTemplate[i]:
                sequenceTemplate[i] = '<Sequence sap2010:Annotation.AnnotationText="{}" DisplayName="{}" sap:VirtualizedContainerService.HintSize="480,715" sap2010:WorkflowViewState.IdRef="Sequence_1">'.format(annotation, name)
  
            elif 'Members>' in sequenceTemplate[i]:
                ArgsRange.append(i)
        del sequenceTemplate[ArgsRange[0]+1:ArgsRange[-1]]

        #Add inputs in case of not none
        if type(inputs) == type(['']):
            for inputVariable in inputs:
                inputName, inputType = inputVariable[0].split('(')
                inputName = sequenceCreator.NamingConverntion(self, 'in_', inputName.strip())
                sequenceTemplate.insert(ArgsRange[0]+1, '<x:Property Name="{}" Type="InArgument(x:{})" />\n'.format(inputName.strip(), typeMapping[inputType.strip()]))
        

        #Add outputs in case of not none
        if type(outputs) == type(['']):
            for outputVariable in outputs:
                outputName, outputType = outputVariable[0].split('(')
                outputName = sequenceCreator.NamingConverntion(self, 'out_', outputName.strip())
                sequenceTemplate.insert(ArgsRange[0]+1, '<x:Property Name="{}" Type="OutArgument(x:{})" />\n'.format(outputName.strip(), typeMapping[outputType.strip()]))


        #Handling Files Creation
        #Applications Naming Convention
        applicationName = sequenceCreator.NamingConverntion(self, 'app_', application)
        #Creating Folders
        try:
            os.mkdir('./Workflows/'+applicationName)
        except:
            pass
        #Create and wirte to file
        actionName = sequenceCreator.NamingConverntion(self, '', name)
        f= open("./Workflows/{}/{}.xaml".format(applicationName, actionName),"w+")
        for i in range(len(sequenceTemplate)):
            f.write(sequenceTemplate[i])
        f.close()



if __name__ == "__main__":
    pass