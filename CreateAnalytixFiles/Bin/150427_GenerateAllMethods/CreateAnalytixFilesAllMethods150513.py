#! /usr/bin/python
# coding: utf-8

import random
import time
import os


path_result_orig = '../../Result/Generated_XMLfiles_150604_A01_'
fileNamePrefix_orig = "MethodTests150604_01_"
origRid_orig = "A01_"
sampleTemplate_orig = "A01_"
  
sampleDrawtime = "20150604081001"
nrOfFolders = 15

xmltext_1 = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE SafirMessage SYSTEM \"8REQW.dtd\">\n<SafirMessage>\n<Envelope>\n<Message ID=\"R5V919AC\" Type=\"REQ\" Origin=\"EDI\" Version=\"008\"/>\n<FromSystem ID=\"KUL:30:S1037\"/>\n<ToSystem ID=\"S9416\"/>\n<Sent DateTime=\"20130612015615\"/>\n</Envelope>\n<Requisition Status=\"N\" GUID=\"05D461B9-8335-4FAE-9C49-7FBBA315CAAC\" ReqType=\"TubeCode\" RequisitionID=\""
xmltext_2 ="\" ExternalRequisitionID=\"324234333\" CareType=\"S\">\n<ReqComment Type=\"RP\" Text=\"Remitent Bibbisvar test1 fakt test2\"/>\n<ReqInformation Code=\"UBBK1\" Value=\"1\"/>\n<Patient PatientID=\"19121212-1212\" Surname=\"ERIK1\" FirstName=\"ERIKSSON1\" Sex=\"M\" BirthDate=\"19180306\" GivenNameQualifier=\"\" Address=\"TOLVAR STIGEN\" PostalCode=\"123 45\" PostalAddress=\"STOCKHOLM\" Country=\"SV\" District=\"0180\" Telephone=\"\" SocialInsuranceOffice=\"\" Comment=\"\" Secrecy=\"N\"/>\n<Biobank Concent=\"01\"/>\n<ReqUnit AddressCode=\"req_110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Bibbi Olofsson\" ContactId=\"\" TelephoneNumber=\"\"/>\n<PayUnit AddressCode=\"pay_110026831\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 2\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<CopyUnit1 AddressCode=\"Copy_110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n"

#xmltext_3 = "<Sample DrawTime=\"20150421020101\" FormatQualifier=\"203\" LaboratoryID=\""
xmltext_3 = "<Sample DrawTime=\"" + sampleDrawtime + "\" FormatQualifier=\"203\" LaboratoryID=\""

xmltext_4 = "\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"ColUnit_KUL\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\""


xmltext_5 = "\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n"

xmltext_6 = "\n</Requisition>\n</SafirMessage>"


def read_file(filename):
    text_file = open(filename, "r")
    indata = text_file.readlines()
    text_file.close()
    return indata

def create_labelList(start,stop,step):
    return range(start,stop,step) 
    
###################################################
#Main
print "##########################################################"

#labelList = read_file(Infile)

methodList =[
['BBKZEB', 'ZB'], 
['BBKZEP', 'ZP'], 
['BBKZC', 'ZC'], 
['BBKZLHG', 'ZL'], 
['BBKZNH', 'ZN'], 
['BBKZS', 'ZS'], 
['BBKZSG', 'ZG'], 
['BBKZU', 'ZU'], 
['BBKZS10', 'ZT'], 
['BBKZE10', 'ZA'], 
['BBKYEB', 'YB'], 
['BBKYEP', 'YP'], 
['BBKYC', 'YC'], 
['BBKYLHG', 'YL'], 
['BBKYNH', 'YN'], 
['BBKYS', 'YS'], 
['BBKYSG', 'YG'], 
['BBKYU', 'YU'], 
['BBKYS10', 'YT'], 
['BBKYE10', 'YA'], 
['BBKVEB', 'VB'], 
['BBKVEP', 'VP'], 
['BBKVC', 'VC'], 
['BBKVLHG', 'VL'], 
['BBKVNH', 'VN'], 
['BBKVS', 'VS'], 
['BBKVSG', 'VG'], 
['BBKVU', 'VU'], 
['BBKVS10', 'VT'], 
['BBKVE10', 'VA'], 
['BBKWEB', 'WB'], 
['BBKWEP', 'WP'], 
['BBKWC', 'WC'], 
['BBKWLHG', 'WL'], 
['BBKWNH', 'WN'], 
['BBKWS', 'WS'], 
['BBKWSG', 'WG'], 
['BBKWU', 'WU'], 
['BBKWS10', 'WT'], 
['BBKWE10', 'WA'], 
['BBKZEB2', 'Z0'], 
['BBKZEP2', 'Z1'], 
['BBKZC2', 'Z2'], 
['BBKZLHG2', 'Z3'], 
['BBKZNH2', 'Z4'], 
['BBKZS2', 'Z5'], 
['BBKZSG2', 'Z6'], 
['BBKZU2', 'Z7'], 
['BBKZS102', 'Z8'], 
['BBKZE102', 'Z9'], 
['BBKYEB2', 'Y0'], 
['BBKYEP2', 'Y1'], 
['BBKYC2', 'Y2'], 
['BBKYLHG2', 'Y3'], 
['BBKYNH2', 'Y4'], 
['BBKYS2', 'Y5'], 
['BBKYSG2', 'Y6'], 
['BBKYU2', 'Y7'], 
['BBKYS102', 'Y8'], 
['BBKYE102', 'Y9'], 
['BBKVEB2', 'V0'], 
['BBKVEP2', 'V1'], 
['BBKVC2', 'V2'], 
['BBKVLHG2', 'V3'], 
['BBKVNH2', 'V4'], 
['BBKVS2', 'V5'], 
['BBKVSG2', 'V6'], 
['BBKVU2', 'V7'], 
['BBKVS102', 'V8'], 
['BBKVE102', 'V9'], 
['BBKWEB2', 'W0'], 
['BBKWEP2', 'W1'], 
['BBKWC2', 'W2'], 
['BBKWLHG2', 'W3'], 
['BBKWNH2', 'W4'], 
['BBKWS2', 'W5'], 
['BBKWSG2', 'W6'], 
['BBKWU2', 'W7'], 
['BBKWS102', 'W8'], 
['BBKWE102', 'W9'], 
['BBKZEB3', 'ZE'], 
['BBKZEP3', 'ZK'], 
['BBKZC3', 'ZF'], 
['BBKZLHG3', 'ZI'], 
['BBKZNH3', 'ZJ'], 
['BBKZS3', 'ZM'], 
['BBKZSG3', 'ZH'], 
['BBKYEB3', 'YE'], 
['BBKYEP3', 'YK'], 
['BBKYC3', 'YF'], 
['BBKYLHG3', 'YI'], 
['BBKYNH3', 'YJ'], 
['BBKYS3', 'YM'], 
['BBKYSG3', 'YH'], 
['BBKVEB3', 'VE'], 
['BBKVEP3', 'VK'], 
['BBKVC3', 'VF'], 
['BBKVLHG3', 'VI'], 
['BBKVNH3', 'VJ'], 
['BBKVS3', 'VM'], 
['BBKVSG3', 'VH'], 
['BBKWEB3', 'WE'], 
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
['BBK1', 'ZB'], 
['BBK1', 'ZP'],
['BBK2', 'ZB'], 
['BBK2', 'ZP']
]



##
##
##
##
##ridList = create_labelList(88880001,88880013,1)
##sampExt01 = ['Z','Y','V','W'] 
###sampExt02 = ['P','C','L','N','S','G','U','T','A']
##
##sampExt02 = [
##['EB', 'B'],
##['EP', 'P'] ,
##['C',  'C'],
##['LHG','L'],
##['NH', 'N'] ,
##['S', 'S'] ,
##['SG', 'G'] ,
##['U', 'U'] ,
##['S10', 'T'], 
##['E10', 'A'] ]
##
##


#path_result_orig = '../../Result/Generated_XMLfiles_150513_'
#fileNamePrefix_orig = "MethodTests150513_"
#origRid_orig = "S0513_"
#sampleTemplate_orig = "S0513_"



for curFolderIndex in range(nrOfFolders):
    path_result = path_result_orig + str(curFolderIndex) + "/"
    fileNamePrefix = fileNamePrefix_orig + str(curFolderIndex) + "_"
    origRid = origRid_orig + str(curFolderIndex) + "_"
    sampleTemplate = sampleTemplate_orig + str(curFolderIndex) + "_"

    if not os.path.exists(path_result):
        os.makedirs(path_result)

    
    
    #curDate = (time.strftime("%Y%m%d"))
    i = 0
    for curSample in methodList:
        curRid = origRid + curSample[0] 
        print str("Current sample: " + curSample[0] + "  " + sampleTemplate + curSample[1])
        i = i + 1
        xmlText = xmltext_1 + str(curRid) + xmltext_2
        #xmlText = xmlText + xmltext_3 + sampleTemplate + curSample[1] + xmltext_4 + curSample[0] + xmltext_5 + xmltext_6    
        xmlText = xmlText + xmltext_3 + sampleTemplate + curSample[0] + curSample[1] + xmltext_4 + curSample[0] + xmltext_5 + xmltext_6    


        
        filename_out = path_result + fileNamePrefix + str(i) + "_" + sampleTemplate + str(curSample[1]) + "_" + str(curSample[0]) + ".xml"
        f = open(filename_out, 'w')
        f.write(xmlText)
        f.close()
        
    

    


