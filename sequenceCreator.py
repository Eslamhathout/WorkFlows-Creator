import os
class sequenceCreator:
    def getXML(self):
        xSequence = open("xSequence.xaml","r")
        sequenceTemplate = xSequence.readlines()
        return sequenceTemplate

    def sequenceCreator(self, name, inputs, outputs, annotation):
        sequenceTemplate = sequenceCreator.getXML(self)
        inputsRange=[]
        for i in range(0, len(sequenceTemplate)):
            if 'AnnotationText' in sequenceTemplate[i]:
                # xmlTag.replace('AnnotationText="Usage: You can use this sequence as a test.&#xD;&#xA;Inputs: xInput&#xD;&#xA;outputs: xOutput"', annotation)
                pass
            elif 'Members>' in sequenceTemplate[i]:
                inputsRange.append(i)
        del sequenceTemplate[inputsRange[0]+1:inputsRange[-1]]
        for inputVariable in inputs:
            sequenceTemplate.insert(inputsRange[0]+1, '<x:Property Name="{}" Type="InArgument(x:String)" />\n'.format(inputVariable[0].strip()))
        # sequenceTemplate.append('')
        # print(sequenceTemplate[0:5])
        # print(len(sequenceTemplate))
        # print("actionsList: {}".format(name))
        # print("inputsArgumentsList: {}".format(inputs))
        # print("outputsArgumentsList: {}".format(outputs))
        print (sequenceTemplate[inputsRange[0]:inputsRange[0]+5])


if __name__ == "__main__":
    pass