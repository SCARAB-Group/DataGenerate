#! /usr/bin/python
# coding: utf-8

import csv


    
###################################################
#Main
print "##########################################################"

path_result = '../../Result/GeneratadCSVFiles150513_50/'
fileNamePrefix = "Result_2015_05_13_01_02_50"
#origLabelID = "S0512_08"
#origLabelID = "H0512_09"
origLabelID = "S0513_50"

#plateTemplate = "SOL_150512_09_"
#plateTemplate = "HUD_150512_09_"
plateTemplate = "AA150513_50_"

sampleTemplate = "aq"
batchID = "14051301"
robotID = "SN6268"
#robotID = "SN6658"
#robotID = "SN7483"

noOfFiles = 1
#noOfSamples = 3

nrOfPlateRows = 12
nrOfPlateCols = 8


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
    filename_out = path_result + fileNamePrefix + str(curFileIndex)  + ".csv"

    with open(filename_out, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header)
        sampleCounter = 1
        aqIndex = 1


        curPlateIndex = 0
        sampleIndex = 0
        while sampleIndex < len(methodList):
            curPlateIndex = curPlateIndex + 1
            curPlate = plateTemplate + str(curPlateIndex)
            for curRowItem in plateRowChar:
                if (sampleIndex == len(methodList)):
                    break
                for curColItem in plateColChar:
                    print "SampleIndex: " + str(sampleIndex)
                    if (sampleIndex == len(methodList)):
                        break
                    curPlatePosition = curRowItem + curColItem
                    curMotherSample = origLabelID + methodList[sampleIndex][0]+ methodList[sampleIndex][1] 
                    curSample = sampleTemplate + curMotherSample + "_" + str(aqIndex)
            
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


                    #fileRows.append(rowTemplate)
                    spamwriter.writerow(rowTemplate)
                    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])        
                    #sampleCounter = sampleCounter + 1
    
        
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
    
    
