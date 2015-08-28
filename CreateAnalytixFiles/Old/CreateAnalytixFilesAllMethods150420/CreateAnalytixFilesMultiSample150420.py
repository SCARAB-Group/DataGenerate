#! /usr/bin/python
# coding: utf-8

import random
import time

path_result = 'Generated_XMLfiles_150420/'

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


origRid = "M150420_01_"

methodList =[
['BBKZEB', 'X150420ZB'], 
['BBKZEP', 'X150420ZP'], 
['BBKZC', 'X150420ZC'], 
['BBKZLHG', 'X150420ZL'], 
['BBKZNH', 'X150420ZN'], 
['BBKZS', 'X150420ZS'], 
['BBKZSG', 'X150420ZG'], 
['BBKZU', 'X150420ZU'], 
['BBKZS10', 'X150420ZT'], 
['BBKZE10', 'X150420ZA'], 
['BBKYEB', 'X150420YB'], 
['BBKYEP', 'X150420YP'], 
['BBKYC', 'X150420YC'], 
['BBKYLHG', 'X150420YL'], 
['BBKYNH', 'X150420YN'], 
['BBKYS', 'X150420YS'], 
['BBKYSG', 'X150420YG'], 
['BBKYU', 'X150420YU'], 
['BBKYS10', 'X150420YT'], 
['BBKYE10', 'X150420YA'], 
['BBKVEB', 'X150420VB'], 
['BBKVEP', 'X150420VP'], 
['BBKVC', 'X150420VC'], 
['BBKVLHG', 'X150420VL'], 
['BBKVNH', 'X150420VN'], 
['BBKVS', 'X150420VS'], 
['BBKVSG', 'X150420VG'], 
['BBKVU', 'X150420VU'], 
['BBKVS10', 'X150420VT'], 
['BBKVE10', 'X150420VA'], 
['BBKWEB', 'X150420WB'], 
['BBKWEP', 'X150420WP'], 
['BBKWC', 'X150420WC'], 
['BBKWLHG', 'X150420WL'], 
['BBKWNH', 'X150420WN'], 
['BBKWS', 'X150420WS'], 
['BBKWSG', 'X150420WG'], 
['BBKWU', 'X150420WU'], 
['BBKWS10', 'X150420WT'], 
['BBKWE10', 'X150420WA'], 
['BBKZEB2', 'X150420Z0'], 
['BBKZEP2', 'X150420Z1'], 
['BBKZC2', 'X150420Z2'], 
['BBKZLHG2', 'X150420Z3'], 
['BBKZNH2', 'X150420Z4'], 
['BBKZS2', 'X150420Z5'], 
['BBKZSG2', 'X150420Z6'], 
['BBKZU2', 'X150420Z7'], 
['BBKZS102', 'X150420Z8'], 
['BBKZE102', 'X150420Z9'], 
['BBKYEB2', 'X150420Y0'], 
['BBKYEP2', 'X150420Y1'], 
['BBKYC2', 'X150420Y2'], 
['BBKYLHG2', 'X150420Y3'], 
['BBKYNH2', 'X150420Y4'], 
['BBKYS2', 'X150420Y5'], 
['BBKYSG2', 'X150420Y6'], 
['BBKYU2', 'X150420Y7'], 
['BBKYS102', 'X150420Y8'], 
['BBKYE102', 'X150420Y9'], 
['BBKVEB2', 'X150420V0'], 
['BBKVEP2', 'X150420V1'], 
['BBKVC2', 'X150420V2'], 
['BBKVLHG2', 'X150420V3'], 
['BBKVNH2', 'X150420V4'], 
['BBKVS2', 'X150420V5'], 
['BBKVSG2', 'X150420V6'], 
['BBKVU2', 'X150420V7'], 
['BBKVS102', 'X150420V8'], 
['BBKVE102', 'X150420V9'], 
['BBKWEB2', 'X150420W0'], 
['BBKWEP2', 'X150420W1'], 
['BBKWC2', 'X150420W2'], 
['BBKWLHG2', 'X150420W3'], 
['BBKWNH2', 'X150420W4'], 
['BBKWS2', 'X150420W5'], 
['BBKWSG2', 'X150420W6'], 
['BBKWU2', 'X150420W7'], 
['BBKWS102', 'X150420W8'], 
['BBKWE102', 'X150420W9'], 
['BBKZEB3', 'X150420ZE'], 
['BBKZEP3', 'X150420ZK'], 
['BBKZC3', 'X150420ZF'], 
['BBKZLHG3', 'X150420ZI'], 
['BBKZNH3', 'X150420ZJ'], 
['BBKZS3', 'X150420ZM'], 
['BBKZSG3', 'X150420ZH'], 
['BBKYEB3', 'X150420YE'], 
['BBKYEP3', 'X150420YK'], 
['BBKYC3', 'X150420YF'], 
['BBKYNH3', 'X150420YJ'], 
['BBKYS3', 'X150420YM'], 
['BBKYSG3', 'X150420YH'], 
['BBKVEB3', 'X150420VE'], 
['BBKVEP3', 'X150420VK'], 
['BBKVC3', 'X150420VF'], 
['BBKVLHG3', 'X150420VI'], 
['BBKVNH3', 'X150420VJ'], 
['BBKVS3', 'X150420VM'], 
['BBKVSG3', 'X150420VH'], 
['BBKWEB3', 'X150420WE'], 
['BBKWEP3', 'X150420WK'], 
['BBKWC3', 'X150420WF'], 
['BBKWLHG3', 'X150420WI'], 
['BBKWNH3', 'X150420WJ'], 
['BBKWS3', 'X150420WM'], 
['BBKWSG3', 'X150420WH'], 
['BBKZLHG4', 'X150420ZD'], 
['BBKZSG4', 'X150420ZO'], 
['BBKYLHG4', 'X150420YD'], 
['BBKYSG4', 'X150420YO'], 
['BBKVLHG4', 'X150420VD'], 
['BBKVSG4', 'X150420VO'], 
['BBKWLHG4', 'X150420WD'], 
['BBKWSG4', 'X150420WO']
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


    
    filename_out = path_result + "MethodTests150420_" + str(i) + "_" + str(curSample[1]) + "_" + str(curSample[0]) + ".xml"
    f = open(filename_out, 'w')
    f.write(xmlText)
    f.close()
    
    

    


