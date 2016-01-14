#! /usr/bin/python
# coding: utf-8

import csv
import os


    
###################################################
#Main
print "##########################################################"

nrOfFolders = 4
origLabelID_orig = "U01_"
#path_result_orig = '../../Result/GeneratadCSVFiles150930_L01_'
path_result_orig = '../../Result/'

fileNamePrefix_orig = "Result_XX_09_30_01_01_"
plateTemplate_orig = "_L01_0930_"

sampleTemplate = "q"
batchID = "15093001"

#robotID = "SN6268"
#robotID = "SN6658"
#robotID = "SN7483"

robotIDArray = ["SN6268","SN6658","SN7483","SN6268","SN6658","SN7483","SN6268","SN6658","SN7483","SN6268","SN6658","SN7483","SN6268","SN6658","SN7483","SN6268","SN6658","SN7483"]
#robotIDArray = ["SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268","SN6268"]


noOfFiles = 1
#noOfSamples = 3

nrOfPlateRows = 12
nrOfPlateCols = 8

nrOfTotSamples = 384
#nrOfMotherSamples = 105

#nrOfMotherSamplesList = [0,0,0,105,105,105,10,10,10,0,0,0,0,0,0,0,0]
nrOfMotherSamplesList = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]


header = ["RecordId", "TRackBC", "TLabwareId", "TPositionId", "TPositionBC", "TStatusSummary", "TSumStateDescription", "TVolume", "SLabwareId", "SPositionId", "SPositionBC", "ScanDateTime", "ActionDateTime", "UserName", "RobotID", "InputValidated", "OutPutValidated", "Run type", "BatchID"]
rowTemplate = ["1", "Plate140122_0201", "Plate140122_0201", "A01", "88880102ZB_14010H_01", "0", "Correct pipetting", "150.000000000000", "SMP_CAR_24_16x100_BDTube_eBlood_0001", "1", "X150317ZP", "2015-04-21 08:01", "2015-04-21 08:16", "pkulmiln13003", "SN7483", "1", "1", "Pressure based", "15042101"]
platePos = ["A01", "B01", "C01"]

plateRowChar = ["A", "B", "C", "D", "E", "F", "G", "H"]
plateColChar = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"] 

methodList =[
#['BBKZEB', 'ZB'], 
['BBKZEP', 'ZP'], 
['BBKZC', 'ZC'], 
['BBKZLHG', 'ZL'], 
['BBKZNH', 'ZN'], 
['BBKZS', 'ZS'], 
['BBKZSG', 'ZG'], 
['BBKZU', 'ZU'], 
['BBKZS10', 'ZT'], 
['BBKZE10', 'ZA'], 
#['BBKYEB', 'YB'], 
['BBKYEP', 'YP'], 
['BBKYC', 'YC'], 
['BBKYLHG', 'YL'], 
['BBKYNH', 'YN'], 
['BBKYS', 'YS'], 
['BBKYSG', 'YG'], 
['BBKYU', 'YU'], 
['BBKYS10', 'YT'], 
['BBKYE10', 'YA'], 
#['BBKVEB', 'VB'], 
['BBKVEP', 'VP'], 
['BBKVC', 'VC'], 
['BBKVLHG', 'VL'], 
['BBKVNH', 'VN'], 
['BBKVS', 'VS'], 
['BBKVSG', 'VG'], 
['BBKVU', 'VU'], 
['BBKVS10', 'VT'], 
['BBKVE10', 'VA'], 
#['BBKWEB', 'WB'], 
['BBKWEP', 'WP'], 
['BBKWC', 'WC'], 
['BBKWLHG', 'WL'], 
['BBKWNH', 'WN'], 
['BBKWS', 'WS'], 
['BBKWSG', 'WG'], 
['BBKWU', 'WU'], 
['BBKWS10', 'WT'], 
['BBKWE10', 'WA'], 
#['BBKZEB2', 'Z0'], 
['BBKZEP2', 'Z1'], 
['BBKZC2', 'Z2'], 
['BBKZLHG2', 'Z3'], 
['BBKZNH2', 'Z4'], 
['BBKZS2', 'Z5'], 
['BBKZSG2', 'Z6'], 
['BBKZU2', 'Z7'], 
['BBKZS102', 'Z8'], 
['BBKZE102', 'Z9'], 
#['BBKYEB2', 'Y0'], 
['BBKYEP2', 'Y1'], 
['BBKYC2', 'Y2'], 
['BBKYLHG2', 'Y3'], 
['BBKYNH2', 'Y4'], 
['BBKYS2', 'Y5'], 
['BBKYSG2', 'Y6'], 
['BBKYU2', 'Y7'], 
['BBKYS102', 'Y8'], 
['BBKYE102', 'Y9'], 
#['BBKVEB2', 'V0'], 
['BBKVEP2', 'V1'], 
['BBKVC2', 'V2'], 
['BBKVLHG2', 'V3'], 
['BBKVNH2', 'V4'], 
['BBKVS2', 'V5'], 
['BBKVSG2', 'V6'], 
['BBKVU2', 'V7'], 
['BBKVS102', 'V8'], 
['BBKVE102', 'V9'], 
#['BBKWEB2', 'W0'], 
['BBKWEP2', 'W1'], 
['BBKWC2', 'W2'], 
['BBKWLHG2', 'W3'], 
['BBKWNH2', 'W4'], 
['BBKWS2', 'W5'], 
['BBKWSG2', 'W6'], 
['BBKWU2', 'W7'], 
['BBKWS102', 'W8'], 
['BBKWE102', 'W9'], 
#['BBKZEB3', 'ZE'], 
['BBKZEP3', 'ZK'], 
['BBKZC3', 'ZF'], 
['BBKZLHG3', 'ZI'], 
['BBKZNH3', 'ZJ'], 
['BBKZS3', 'ZM'], 
['BBKZSG3', 'ZH'], 
#['BBKYEB3', 'YE'], 
['BBKYEP3', 'YK'], 
['BBKYC3', 'YF'], 
['BBKYLHG3', 'YI'], 
['BBKYNH3', 'YJ'], 
['BBKYS3', 'YM'], 
['BBKYSG3', 'YH'], 
#['BBKVEB3', 'VE'], 
['BBKVEP3', 'VK'], 
['BBKVC3', 'VF'], 
['BBKVLHG3', 'VI'], 
['BBKVNH3', 'VJ'], 
['BBKVS3', 'VM'], 
['BBKVSG3', 'VH'], 
#['BBKWEB3', 'WE'], 
['BBKWEP3', 'WK'], 
['BBKWC3', 'WF'], 
['BBKWLHG3', 'WI'], 
['BBKWNH3', 'WJ'], 
['BBKWS3', 'WM'], 
['BBKWSG3', 'WH'], 
['BBKZLHG4', 'ZD'], 
['BBKZSG4', 'ZO'], 
['BBKYLHG4', 'YD'], 
['BBKYSG4', 'YO'], 
['BBKVLHG4', 'VD'], 
['BBKVSG4', 'VO'], 
['BBKWLHG4', 'WD'], 
['BBKWSG4', 'WO'],
#['BBK1', 'ZB'], 
['BBK1', 'ZP'],
#['BBK2', 'ZB'], 
['BBK2', 'ZP']
]



for curFolderIndex in range(nrOfFolders):
    #path_result = path_result_orig + str(curFolderIndex) + "/"
    path_result = path_result_orig + robotIDArray[curFolderIndex] + "/"

    #fileNamePrefix = fileNamePrefix_orig
    fileNamePrefix = fileNamePrefix_orig.replace("XX", origLabelID_orig) #+ str(curFolderIndex) + "_"
   # print "FilenamePrefix", fileNamePrefix
    
    origLabelID = origLabelID_orig + str(curFolderIndex) + "_"
    plateTemplate = plateTemplate_orig + str(curFolderIndex) + "_"

    robotID = robotIDArray[curFolderIndex]

    if not os.path.exists(path_result):
        os.makedirs(path_result)
        
    # Create plate pos list

    platePositionID = []
    for curRowItem in plateRowChar:
        for curColItem in plateColChar:
            platePositionID.append(curRowItem + curColItem)


    #for item in platePositionID:
    #    print item


    for curFileIndex in range(noOfFiles):
        fileRows = []
        fileRows.append(header)
        curPlate = plateTemplate + str(curFileIndex)

        #filename_out = path_result + "Result" + str(1200 + curFileIndex) + "_01_01_01_01_01.csv"
        #print "pathresult", path_result
        filename_out = path_result +  str(fileNamePrefix) + str(curFileIndex) + str(curFolderIndex)  + ".csv"


        
        #curMotherSampleIndex = nrOfMotherSamplesList[curFileIndex]

        with open(filename_out, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(header)
            sampleCounter = 1
            aqIndex = 0


            curPlateIndex = 0
            sampleIndex = 0
            curMotherSampleIndex = 0
#            while sampleIndex < len(methodList):
            while sampleIndex < nrOfTotSamples:

                curPlateIndex = curPlateIndex + 1
                curPlate = plateTemplate + str(curPlateIndex)

                for curRowItem in plateRowChar:
##                    if (sampleIndex == len(methodList)):
##                        break

                    for curColItem in plateColChar:
                        print "SampleIndex: " + str(sampleIndex)
                        
##                        if (sampleIndex == len(methodList)):
##                            break
                        curPlatePosition = curRowItem + curColItem
                        
                        curMotherSample = origLabelID + methodList[curMotherSampleIndex][0]+ methodList[curMotherSampleIndex][1] 

                        curSample = sampleTemplate + curMotherSample + "_" + str(aqIndex)
                        #curSample = sampleTemplate + curMotherSample + "_" + str(curMotherSampleIndex)
                
                        rowTemplate[0] = sampleIndex + 1
                        rowTemplate[1] = curPlate
                        rowTemplate[2] = curPlate
                        rowTemplate[3] = curPlatePosition
                        rowTemplate[4] = curSample
                        rowTemplate[9] = sampleIndex + 1
                        rowTemplate[10] = curMotherSample
                        rowTemplate[14] = robotID                    
                        rowTemplate[18] = batchID
                        sampleIndex = sampleIndex + 1
                        aqIndex = aqIndex + 1

                        #curMotherSampleIndex = curMotherSampleIndex + 1
                        if aqIndex > nrOfMotherSamplesList[curFolderIndex] - 1:
                            aqIndex = 0
                            if curMotherSampleIndex > 104:
                                curMotherSampleIndex = 0
                            else:
                                curMotherSampleIndex = curMotherSampleIndex + 1
                            

                        #curMotherSampleIndex = curMotherSampleIndex + 1
                        #if curMotherSampleIndex > nrOfMotherSamplesList[curFolderIndex]:
                        #    curMotherSampleIndex = 0
                        #    aqIndex = 0


                        #fileRows.append(rowTemplate)
                        spamwriter.writerow(rowTemplate)
                        #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])        
                        #sampleCounter = sampleCounter + 1
        
        

