#! /usr/bin/python
# coding: utf-8

import random

path_result = ''
Infile = 'InData/SampleNumberToXML2.csv'
    

xmltext_1 = "\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE SafirMessage SYSTEM \"8REQW.dtd\">\n<SafirMessage>\n<Envelope>\n<Message ID=\"R5V919AC\" Type=\"REQ\" Origin=\"EDI\" Version=\"008\"/>\n<FromSystem ID=\"KUL:30:S1037\"/>\n<ToSystem ID=\"S9416\"/>\n<Sent DateTime=\"20130612015615\"/>\n</Envelope>\n<Requisition Status=\"N\" GUID=\"05D461B9-8335-4FAE-9C49-7FBBA315CAAC\" ReqType=\"TubeCode\" RequisitionID=\""
xmltext_2 ="\" ExternalRequisitionID=\"324234333\" CareType=\"S\">\n<ReqComment Type=\"RP\" Text=\"Remitent Bibbisvar test1 fakt test2\"/>\n<ReqInformation Code=\"UBBK1\" Value=\"1\"/>\n<Patient PatientID=\"19180306-6172\" Surname=\"ERIK1\" FirstName=\"ERIKSSON1\" Sex=\"M\" BirthDate=\"19180306\" GivenNameQualifier=\"\" Address=\"TOLVAR STIGEN\" PostalCode=\"123 45\" PostalAddress=\"STOCKHOLM\" Country=\"SV\" District=\"0180\" Telephone=\"\" SocialInsuranceOffice=\"\" Comment=\"\" Secrecy=\"N\"/>\n<Biobank Concent=\"01\"/>\n<ReqUnit AddressCode=\"110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Bibbi Olofsson\" ContactId=\"\" TelephoneNumber=\"\"/>\n<PayUnit AddressCode=\"110026831\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 2\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<CopyUnit1 AddressCode=\"110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Sample DrawTime=\"20130612015615\" FormatQualifier=\"203\" LaboratoryID=\""
xmltext_3 = "\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"KUL\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n<Sample DrawTime=\"20130612015615\" FormatQualifier=\"203\" LaboratoryID=\""
xmltext_4 = "\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"KUL\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n</Requisition>\n</SafirMessage>"


def read_file(filename):
    text_file = open(filename, "r")
    indata = text_file.readlines()
    text_file.close()
    return indata


###################################################
#Main
print "##########################################################"

labelList = read_file(Infile)

# Create random RID number.
curRIDnr = int(round(random.random() * 1000000,0))

for item in range(len(labelList)):
    curLabelID = labelList[item]
    curRIDnr = curRIDnr + 1
    filename_out = "Generated_XMLFiles/" + str(curRIDnr) + ".xml"
    textout = xmltext_1 + str(curRIDnr) + xmltext_2 + curLabelID[0:8] + xmltext_3 + str(curRIDnr) + "Y" + xmltext_4
    f = open(filename_out, 'w')
    f.write(textout)
    f.close()
    
    

    


