#! /usr/bin/python
# coding: utf-8

import random
import time

path_result = 'Generated_XMLfiles_150421_3/'

xmltext_1 = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE SafirMessage SYSTEM \"8REQW.dtd\">\n<SafirMessage>\n<Envelope>\n<Message ID=\"R5V919AC\" Type=\"REQ\" Origin=\"EDI\" Version=\"008\"/>\n<FromSystem ID=\"KUL:30:S1037\"/>\n<ToSystem ID=\"S9416\"/>\n<Sent DateTime=\"20130612015615\"/>\n</Envelope>\n<Requisition Status=\"N\" GUID=\"05D461B9-8335-4FAE-9C49-7FBBA315CAAC\" ReqType=\"TubeCode\" RequisitionID=\""
xmltext_2 ="\" ExternalRequisitionID=\"324234333\" CareType=\"S\">\n<ReqComment Type=\"RP\" Text=\"Remitent Bibbisvar test1 fakt test2\"/>\n<ReqInformation Code=\"UBBK1\" Value=\"1\"/>\n<Patient PatientID=\"19121212-1212\" Surname=\"ERIK1\" FirstName=\"ERIKSSON1\" Sex=\"M\" BirthDate=\"19180306\" GivenNameQualifier=\"\" Address=\"TOLVAR STIGEN\" PostalCode=\"123 45\" PostalAddress=\"STOCKHOLM\" Country=\"SV\" District=\"0180\" Telephone=\"\" SocialInsuranceOffice=\"\" Comment=\"\" Secrecy=\"N\"/>\n<Biobank Concent=\"01\"/>\n<ReqUnit AddressCode=\"req_110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Bibbi Olofsson\" ContactId=\"\" TelephoneNumber=\"\"/>\n<PayUnit AddressCode=\"pay_110026831\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 2\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<CopyUnit1 AddressCode=\"Copy_110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n"

xmltext_3 = "<Sample DrawTime=\"20150421020101\" FormatQualifier=\"203\" LaboratoryID=\""
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


origRid = "M150421_03_"

methodList =[
['BBKZEB', 'Z150421ZB'], 
['BBKZEP', 'Z150421ZP'], 
['BBKZC', 'Z150421ZC'], 
['BBKZLHG', 'Z150421ZL'], 
['BBKZNH', 'Z150421ZN'], 
['BBKZS', 'Z150421ZS'], 
['BBKZSG', 'Z150421ZG'], 
['BBKZU', 'Z150421ZU'], 
['BBKZS10', 'Z150421ZT'], 
['BBKZE10', 'Z150421ZA'], 
['BBKYEB', 'Z150421YB'], 
['BBKYEP', 'Z150421YP'], 
['BBKYC', 'Z150421YC'], 
['BBKYLHG', 'Z150421YL'], 
['BBKYNH', 'Z150421YN'], 
['BBKYS', 'Z150421YS'], 
['BBKYSG', 'Z150421YG'], 
['BBKYU', 'Z150421YU'], 
['BBKYS10', 'Z150421YT'], 
['BBKYE10', 'Z150421YA'], 
['BBKVEB', 'Z150421VB'], 
['BBKVEP', 'Z150421VP'], 
['BBKVC', 'Z150421VC'], 
['BBKVLHG', 'Z150421VL'], 
['BBKVNH', 'Z150421VN'], 
['BBKVS', 'Z150421VS'], 
['BBKVSG', 'Z150421VG'], 
['BBKVU', 'Z150421VU'], 
['BBKVS10', 'Z150421VT'], 
['BBKVE10', 'Z150421VA'], 
['BBKWEB', 'Z150421WB'], 
['BBKWEP', 'Z150421WP'], 
['BBKWC', 'Z150421WC'], 
['BBKWLHG', 'Z150421WL'], 
['BBKWNH', 'Z150421WN'], 
['BBKWS', 'Z150421WS'], 
['BBKWSG', 'Z150421WG'], 
['BBKWU', 'Z150421WU'], 
['BBKWS10', 'Z150421WT'], 
['BBKWE10', 'Z150421WA'], 
['BBKZEB2', 'Z150421Z0'], 
['BBKZEP2', 'Z150421Z1'], 
['BBKZC2', 'Z150421Z2'], 
['BBKZLHG2', 'Z150421Z3'], 
['BBKZNH2', 'Z150421Z4'], 
['BBKZS2', 'Z150421Z5'], 
['BBKZSG2', 'Z150421Z6'], 
['BBKZU2', 'Z150421Z7'], 
['BBKZS102', 'Z150421Z8'], 
['BBKZE102', 'Z150421Z9'], 
['BBKYEB2', 'Z150421Y0'], 
['BBKYEP2', 'Z150421Y1'], 
['BBKYC2', 'Z150421Y2'], 
['BBKYLHG2', 'Z150421Y3'], 
['BBKYNH2', 'Z150421Y4'], 
['BBKYS2', 'Z150421Y5'], 
['BBKYSG2', 'Z150421Y6'], 
['BBKYU2', 'Z150421Y7'], 
['BBKYS102', 'Z150421Y8'], 
['BBKYE102', 'Z150421Y9'], 
['BBKVEB2', 'Z150421V0'], 
['BBKVEP2', 'Z150421V1'], 
['BBKVC2', 'Z150421V2'], 
['BBKVLHG2', 'Z150421V3'], 
['BBKVNH2', 'Z150421V4'], 
['BBKVS2', 'Z150421V5'], 
['BBKVSG2', 'Z150421V6'], 
['BBKVU2', 'Z150421V7'], 
['BBKVS102', 'Z150421V8'], 
['BBKVE102', 'Z150421V9'], 
['BBKWEB2', 'Z150421W0'], 
['BBKWEP2', 'Z150421W1'], 
['BBKWC2', 'Z150421W2'], 
['BBKWLHG2', 'Z150421W3'], 
['BBKWNH2', 'Z150421W4'], 
['BBKWS2', 'Z150421W5'], 
['BBKWSG2', 'Z150421W6'], 
['BBKWU2', 'Z150421W7'], 
['BBKWS102', 'Z150421W8'], 
['BBKWE102', 'Z150421W9'], 
['BBKZEB3', 'Z150421ZE'], 
['BBKZEP3', 'Z150421ZK'], 
['BBKZC3', 'Z150421ZF'], 
['BBKZLHG3', 'Z150421ZI'], 
['BBKZNH3', 'Z150421ZJ'], 
['BBKZS3', 'Z150421ZM'], 
['BBKZSG3', 'Z150421ZH'], 
['BBKYEB3', 'Z150421YE'], 
['BBKYEP3', 'Z150421YK'], 
['BBKYC3', 'Z150421YF'], 
['BBKYNH3', 'Z150421YJ'], 
['BBKYS3', 'Z150421YM'], 
['BBKYSG3', 'Z150421YH'], 
['BBKVEB3', 'Z150421VE'], 
['BBKVEP3', 'Z150421VK'], 
['BBKVC3', 'Z150421VF'], 
['BBKVLHG3', 'Z150421VI'], 
['BBKVNH3', 'Z150421VJ'], 
['BBKVS3', 'Z150421VM'], 
['BBKVSG3', 'Z150421VH'], 
['BBKWEB3', 'Z150421WE'], 
['BBKWEP3', 'Z150421WK'], 
['BBKWC3', 'Z150421WF'], 
['BBKWLHG3', 'Z150421WI'], 
['BBKWNH3', 'Z150421WJ'], 
['BBKWS3', 'Z150421WM'], 
['BBKWSG3', 'Z150421WH'], 
['BBKZLHG4', 'Z150421ZD'], 
['BBKZSG4', 'Z150421ZO'], 
['BBKYLHG4', 'Z150421YD'], 
['BBKYSG4', 'Z150421YO'], 
['BBKVLHG4', 'Z150421VD'], 
['BBKVSG4', 'Z150421VO'], 
['BBKWLHG4', 'Z150421WD'], 
['BBKWSG4', 'Z150421WO']
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


#curDate = (time.strftime("%Y%m%d"))
i = 0
for curSample in methodList:
    curRid = origRid + curSample[0] 
    print str("Current sample: " + curSample[0] + "  " + curSample[1])
    i = i + 1
    xmlText = xmltext_1 + str(curRid) + xmltext_2
    xmlText = xmlText + xmltext_3 + curSample[1] + xmltext_4 + curSample[0] + xmltext_5 + xmltext_6    


    
    filename_out = path_result + "MethodTests150421_3_" + str(i) + "_" + str(curSample[1]) + "_" + str(curSample[0]) + ".xml"
    f = open(filename_out, 'w')
    f.write(xmlText)
    f.close()
    
    

    


