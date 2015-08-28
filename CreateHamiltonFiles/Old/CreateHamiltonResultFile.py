#! /usr/bin/python
# coding: utf-8

import csv

path_result = 'GeneratadCSVFiles/'
    
###################################################
#Main
print "##########################################################"

noOfFiles = 80
noOfSamples = 3

plateTemplate = "Plate140122X_"
sampleTemplate = "aq_140122X_"

header = ["RecordId", "TRackBC", "TLabwareId", "TPositionId", "TPositionBC", "TStatusSummary", "TSumStateDescription", "TVolume", "SLabwareId", "SPositionId", "SPositionBC", "ScanDateTime", "ActionDateTime", "UserName", "RobotID", "InputValidated", "OutPutValidated", "Run type"]
rowTemplate = ["1", "Plate140122_0201", "Plate140122_0201", "A01", "88880102ZB_14010H_01", "0", "Correct pipetting", "150.000000000000", "SMP_CAR_24_16x100_BDTube_eBlood_0001", "1", "88880102ZB", "2012-01-08 09:16", "2012-01-08 09:16", "pkulmiln13003", "SN6658", "1", "1", "Pressure based"]
platePos = ["A01", "B01", "C01"]

for curFileIndex in range(noOfFiles):
    fileRows = []
    fileRows.append(header)
    curPlate = plateTemplate + str(curFileIndex)

    filename_out = path_result + "Result" + str(1200 + curFileIndex) + "_01_01_01_01_01.csv"
    with open(filename_out, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header)
        for curSample in range(noOfSamples):
        
        
            rowTemplate[0] = str(curSample + 1)
            rowTemplate[1] = curPlate
            rowTemplate[2] = curPlate
            rowTemplate[3] = platePos[curSample]
            rowTemplate[4] = sampleTemplate + str(curFileIndex) + "_" + str(curSample)
            rowTemplate[9] = str(curSample + 1)
            #fileRows.append(rowTemplate)
            spamwriter.writerow(rowTemplate)
            #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])        
        
        
        
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
    
    

    


