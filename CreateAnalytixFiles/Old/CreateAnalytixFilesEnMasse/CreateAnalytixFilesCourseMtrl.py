#! /usr/bin/python
# coding: utf-8

import random
import math
import csv

path_result = ''

xmltext_1 = "\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE SafirMessage SYSTEM \"8REQW.dtd\">\n<SafirMessage>\n<Envelope>\n<Message ID=\"R5V919AC\" Type=\"REQ\" Origin=\"EDI\" Version=\"008\"/>\n<FromSystem ID=\"KUL:30:S1037\"/>\n<ToSystem ID=\"S9416\"/>\n<Sent DateTime=\"20130612015615\"/>\n</Envelope>\n<Requisition Status=\"N\" GUID=\"05D461B9-8335-4FAE-9C49-7FBBA315CAAC\" ReqType=\"TubeCode\" RequisitionID=\""
xmltext_2 ="\" ExternalRequisitionID=\"324234333\" CareType=\"S\">\n<ReqComment Type=\"RP\" Text=\"Textkommentar RP\"/>\n<ReqInformation Code=\"UBBK1\" Value=\"1\"/>\n<Patient PatientID=\"19800701-0161\" Surname=\"DeHex\" FirstName=\"Magica\" Sex=\"F\" BirthDate=\"19800701\" GivenNameQualifier=\"\" Address=\"Granstigen 35\" PostalCode=\"123 45\" PostalAddress=\"STOCKHOLM\" Country=\"SV\" District=\"0180\" Telephone=\"098765\" SocialInsuranceOffice=\"yy\" Comment=\"Provet innehåller visst lite blodsmitta iallafall..\" Secrecy=\"N\"/>\n<Biobank Concent=\"01\"/>\n<ReqUnit AddressCode=\"88776655\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Arne Anka\" ContactId=\"543xx\" TelephoneNumber=\"5432\"/>\n<PayUnit AddressCode=\"9944885\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 2\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Krille Krokodil\" TelephoneNumber=\"54324\"/>\n<CopyUnit1 AddressCode=\"Q5544663344\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Klara Kluck\" TelephoneNumber=\"5432345\"/>\n<Sample DrawTime=\"18990203094510\" FormatQualifier=\"203\" LaboratoryID=\""
xmltext_3 = "\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"Q1234\" Name1=\"ColName1\" Name2=\"ColName2\" Address=\"ColAddress1\" PostalAddress=\"ColPost\" ContactPerson=\"ColContact\" TelephoneNumber=\"123321123\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"x\" Address=\"y\" PostalAddress=\"z \" ContactPerson=\"q\" TelephoneNumber=\"432\"/>\n</Analysis>\n</Sample>\n<Sample DrawTime=\"18990203094510\" FormatQualifier=\"203\" LaboratoryID=\""
xmltext_4 = "\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"Q1234\" Name1=\"ColName1\" Name2=\"ColName2\" Address=\"ColAddress1\" PostalAddress=\"ColPost\" ContactPerson=\"ColContact\" TelephoneNumber=\"123321123\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"x\" Address=\"y\" PostalAddress=\"z \" ContactPerson=\"q\" TelephoneNumber=\"432\"/>\n</Analysis>\n</Sample>\n</Requisition>\n</SafirMessage>"



csvheader = ["RecordId", "TRackBC", "TLabwareId", "TPositionId", "TPositionBC", "TStatusSummary", "TSumStateDescription", "TVolume", "SLabwareId", "SPositionId", "SPositionBC", "ScanDateTime", "ActionDateTime", "UserName", "RobotID", "InputValidated", "OutPutValidated"]
csvlist = []
csvlist.append(csvheader)

#csvheader = "RecordId;TRackBC;TLabwareId;TPositionId;TPositionBC;TStatusSummary;TSumStateDescription;TVolume;SLabwareId;SPositionId;SPositionBC;ScanDateTime;ActionDateTime;UserName;RobotID;InputValidated;OutPutValidated"


def read_file(filename):
    text_file = open(filename, "r")
    indata = text_file.readlines()
    text_file.close()
    return indata

def convIndex(value, maxval):
    outStr = ""
    for a in range(maxval - len(value)):
        outStr = outStr + "0"
    return outStr + value

def findBoxIndex(itemIndex, boxCol, BoxRow):
    boxcapacity = boxCol*BoxRow
    boxindex = int(math.floor(float(itemIndex) / float(boxcapacity)))
    return convIndex(str(boxindex), 4)

def findBoxPos(itemIndex, boxCol, BoxRow):
    boxcapacity = boxCol*BoxRow
    restPos = itemIndex - math.floor(float(itemIndex) / float(boxcapacity)) * boxcapacity
    curCol = int(math.floor(float(restPos) / float(boxCol))) + 1
    curRow = int(restPos - (curCol - 1) * boxCol) + 1
    curBoxPos = chr(64 + int(curCol)) + convIndex(str(curRow), 2)

    return curBoxPos


###################################################
#Main
print "##########################################################"

templateRID = "20130910_"
templateSample = "Kurs_"
nrOfSamples = 21
boxCol = 8
BoxRow = 8
#curBoxName = "Plate_" + templateSample 

#csv_filename_out = "Generated_csvFiles2/Result_2013_09_10_01_01_01.csv"
##csv_filename_out = "Generetad_csvFiles/Result_1870_01_01_01_01_" + curIndex + ".csv"     
#out = csv.writer(open(csv_filename_out,"a"), delimiter=';',quoting=csv.QUOTE_ALL)
#out.writerow(csvheader)
##out.writerow(csvline)


for itemIndex in range(1,nrOfSamples):
    curIndex = convIndex(str(itemIndex),2)
    
    curLabelID1 = templateSample + curIndex + "ZB"
    curLabelID2 = templateSample + curIndex + "ZP"
    curRIDnr = templateRID + curIndex
    
    xml_filename_out = "Generated_XMLFiles2/" + str(curRIDnr) + ".xml"
    textout = xmltext_1 + str(curRIDnr) + xmltext_2 + curLabelID1 + xmltext_3 + curLabelID2 + xmltext_4
    f = open(xml_filename_out, 'w')
    f.write(textout)
    f.close()
    
    curFileIndex = convIndex(str(itemIndex),2)
    csv_filename_out = "Generated_csvFiles2/Result_2013_09_10_01_01_" + str(curFileIndex) + ".csv"
    out = csv.writer(open(csv_filename_out,"a"), delimiter=';',quoting=csv.QUOTE_ALL)
    out.writerow(csvheader) 
    
    motherSampleName = curLabelID1
    curBoxName = templateSample + convIndex(str(itemIndex),2)

    nrOfAliq = 5
    for aliqIndex in range(1,nrOfAliq):
        curBoxPos = "A" + convIndex(str(aliqIndex),2)
        aliquotName = curLabelID1 + "_sub" + convIndex(str(aliqIndex),2)
        csvline = [aliqIndex + 1, curBoxName, curBoxName, curBoxPos, aliquotName, "0", "Correct pipetting", "150", "SMP_CAR_24_13x100_BDTube_eBlood_0001", "X", motherSampleName, "2013-09-05 09:37", "2013-09-05 09:40", "pkulmiln13001", "SN000", "0","0"]
        out.writerow(csvline)    


    #csv_filename_out = "Generetad_csvFiles/Result_1870_01_01_01_01_" + curIndex + ".csv"     
    #out.writerow(csvline)
    #csvlist.append(csvline)
    
    
    
    
    
    
    


