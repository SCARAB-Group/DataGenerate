#! /usr/bin/python
# coding: utf-8

import csv

path_result = '../../Result/GeneratadCSVFiles150427_FullPlates_3/'
fileNamePrefix = "MethodTests150427_04_"    
plateTemplate = "Plate150427_04_"
sampleTemplate = "Z150427_"

    
###################################################
#Main
print "##########################################################"

noOfFiles = 77
#noOfSamples = 3

nrOfPlateRows = 12
nrOfPlateCols = 8


header = ["RecordId", "TRackBC", "TLabwareId", "TPositionId", "TPositionBC", "TStatusSummary", "TSumStateDescription", "TVolume", "SLabwareId", "SPositionId", "SPositionBC", "ScanDateTime", "ActionDateTime", "UserName", "RobotID", "InputValidated", "OutPutValidated", "Run type", "BatchID"]
rowTemplate = ["1", "Plate140122_0201", "Plate140122_0201", "A01", "88880102ZB_14010H_01", "0", "Correct pipetting", "150.000000000000", "SMP_CAR_24_16x100_BDTube_eBlood_0001", "1", "X150422V1", "2015-04-20 08:01", "2015-04-20 08:16", "pkulmiln13003", "SN6268", "1", "1", "Pressure based", "15042699"]
platePos = ["A01", "B01", "C01"]

plateRowChar = ["A", "B", "C", "D", "E", "F", "G", "H"]
plateColChar = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"] 


for curFileIndex in range(noOfFiles):
    fileRows = []
    fileRows.append(header)
    curPlate = plateTemplate + str(curFileIndex)

    #filename_out = path_result + "Result" + str(1200 + curFileIndex) + "_01_01_01_01_01.csv"
    filename_out = path_result + fileNamePrefix + str(curFileIndex)  + ".csv"

    with open(filename_out, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header)
        sampleCounter = 1
        for curRowItem in plateRowChar:
            for curColItem in plateColChar:
                curSample = sampleTemplate + str(curFileIndex) + curRowItem + curColItem
            
                rowTemplate[0] = sampleCounter
                rowTemplate[1] = curPlate
                rowTemplate[2] = curPlate
                rowTemplate[3] = curRowItem + curColItem
                rowTemplate[4] = curSample
                rowTemplate[9] = sampleCounter
                #fileRows.append(rowTemplate)
                spamwriter.writerow(rowTemplate)
                #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])        
                sampleCounter = sampleCounter + 1
        
        
#print header
#print rowTemplate
#
## Create random RID number.
#curRIDnr = int(round(random.random() * 1000000,0))
#
#for item in range(len(labelList)):
#    curLabelID = labelList[item]
#    curRIDnr = curRIDnr + 1
#    filename_out = "Generated_XMLFiles/" + str(curRIDnr) + ".xml"
#    textout = xmltext_1 + str(curRIDnr) + xmltext_2 + curLabelID[0:8] + xmltext_3 + str(curRIDnr) + "Y" + xmltext_4
#    f = open(filename_out, 'w')
#    f.write(textout)
#    f.close()
    
    

    


