#! /usr/bin/python
# coding: utf-8

path_result = ''

#
#labelList = ['01116383',
#'01116375',
#'01116367',
#'01116359',
#'01116342',
#'01116334',
#'01116326',
#'01116318',
#'01116300',
#'01116292',
#'01116284',
#'01116276',
#'01116268',
#'01116250',
#'01116243',
#'01116235',
#'01116227',
#'01116219',
#'01116201',
#'01116193']


    
labelList = ['01116185',
'01116177',
'01116169',
'01116151',
'01116144',
'01116136',
'01116128',
'01116110',
'01116102',
'01116094',
'01116086',
'01116078',
'01116060',
'01117753',
'01117746',
'01117738',
'01117720',
'01117712',
'01117704',
'01117696',
'01117688',
'01117670',
'01117662',
'01117654',
'01117647',
'01117639',
'01117621',
'01117613',
'01117605',
'01117597',
'01117589',
'01117571',
'01117563',
'01117555',
'01117548',
'01117530',
'01117522',
'01117514',
'01117506',
'01117498',
'01117480',
'01117472',
'01117464',
'01117456',
'01117449',
'01117431',
'01117423',
'01117415',
'01117407',
'01117399',
'01117381',
'01117373',
'01117365',
'01117357',
'01117340',
'01117332',
'01117324',
'01117316',
'01117308',
'01117290',
'01117282',
'01117274',
'01117266',
'01117258',
'01117241',
'01117233',
'01117225',
'01117217',
'01117209',
'01117191',
'01117183',
'01117175',
'01117167',
'01117159',
'01117142',
'01117134',
'01117126',
'01117118',
'01117100',
'01117092',
'01117084',
'01117076',
'01117068',
'01117050',
'01117043',
'01117035',
'01117027',
'01117019',
'01117001',
'01116995',
'01116987',
'01116979',
'01116961',
'01116953',
'01116946',
'01116938',
'01116920',
'01116912',
'01116904',
'01116896',
'01116888',
'01116870',
'01116862',
'01116854',
'01116847',
'01116839',
'01116821',
'01116813',
'01116805',
'01116797',
'01116789',
'01116771',
'01116763',
'01116755',
'01116748',
'01116730',
'01116722',
'01116714',
'01116706',
'01116698',
'01116680',
'01116672',
'01116664',
'01116656',
'01116649',
'01116631',
'01116623',
'01116615',
'01116607',
'01116599',
'01116581',
'01116573',
'01116565',
'01116557',
'01116540',
'01116532',
'01116524',
'01116516',
'01116508',
'01116490',
'01116482',
'01116474',
'01116466',
'01116458',
'01116441',
'01116433',
'01116425',
'01116417',
'01116409']


#
#labelList = [
#'1116185',
#'1116177',
#'1116169',
#'1116151',
#'1116144',
#'1116136',
#'1116128',
#'1116110',
#'1116102',
#'1116094',
#'1116086',
#'1116078',
#'1116060',
#'1117753',
#'1117746',
#'1117738',
#'1117720',
#'1117712',
#'1117704',
#'1117696',
#'1117688',
#'1117670',
#'1117662',
#'1117654',
#'1117647',
#'1117639',
#'1117621',
#'1117613',
#'1117605',
#'1117597',
#'1117589',
#'1117571',
#'1117563',
#'1117555',
#'1117548',
#'1117530',
#'1117522',
#'1117514',
#'1117506',
#'1117498',
#'1117480',
#'1117472',
#'1117464',
#'1117456',
#'1117449',
#'1117431',
#'1117423',
#'1117415',
#'1117407',
#'1117399',
#'1117381',
#'1117373',
#'1117365',
#'1117357',
#'1117340',
#'1117332',
#'1117324',
#'1117316',
#'1117308',
#'1117290',
#'1117282',
#'1117274',
#'1117266',
#'1117258',
#'1117241',
#'1117233',
#'1117225',
#'1117217',
#'1117209',
#'1117191',
#'1117183',
#'1117175',
#'1117167',
#'1117159',
#'1117142',
#'1117134',
#'1117126',
#'1117118',
#'1117100',
#'1117092',
#'1117084',
#'1117076',
#'1117068',
#'1117050',
#'1117043',
#'1117035',
#'1117027',
#'1117019',
#'1117001',
#'1116995',
#'1116987',
#'1116979',
#'1116961',
#'1116953',
#'1116946',
#'1116938',
#'1116920',
#'1116912',
#'1116904',
#'1116896',
#'1116888',
#'1116870',
#'1116862',
#'1116854',
#'1116847',
#'1116839',
#'1116821',
#'1116813',
#'1116805',
#'1116797',
#'1116789',
#'1116771',
#'1116763',
#'1116755',
#'1116748',
#'1116730',
#'1116722',
#'1116714',
#'1116706',
#'1116698',
#'1116680',
#'1116672',
#'1116664',
#'1116656',
#'1116649',
#'1116631',
#'1116623',
#'1116615',
#'1116607',
#'1116599',
#'1116581',
#'1116573',
#'1116565',
#'1116557',
#'1116540',
#'1116532',
#'1116524',
#'1116516',
#'1116508',
#'1116490',
#'1116482',
#'1116474',
#'1116466',
#'1116458',
#'1116441',
#'1116433',
#'1116425',
#'1116417',
#'1116409']
#




#xmltext_1 = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE SafirMessage SYSTEM \"8REQW.dtd\">\n<SafirMessage>\n<Envelope>\n<Message ID=\"R1LC20AI\" Type=\"REQ\" Origin=\"EDI\" Version=\"008\"/>\n<FromSystem ID=\"KUL:30:S1037\"/>\n<ToSystem ID=\"12345\"/>\n<Sent DateTime=\"20130612015615\"/>\n</Envelope>\n<Requisition Status=\"N\" GUID=\"00AC4B05-79CF-4CB8-A129-68E619A4A601\" ReqType=\"TubeCode\" RequisitionID=\""
#xmltext_2 = "\" ExternalRequisitionID=\"27944522\" CareType=\"S\">\n<ReqComment Type=\"RP\" Text=\"Best‰llarens kommentar Blodsmitta\"/>\n<ReqComment Type=\"RL\" Text=\"Provtagarens kommentar\"/>\n<Patient PatientID=\"19500505-0546\" Surname=\"TESTPERSON\" FirstName=\"TESTA\" Sex=\"F\" BirthDate=\"19500505\" GivenNameQualifier=\"\" Address=\"KUVERT UTAN LOGGA!!!!\" PostalCode=\"62150\" PostalAddress=\"VISBY\" Country=\"SV\" District=\"0199\" Telephone=\"\" SocialInsuranceOffice=\"\" Comment=\"\" Secrecy=\"N\"/>\n<Biobank Concent=\"02\"/>\n<ReqUnit AddressCode=\"110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Svante Lewald\" ContactId=\"\" TelephoneNumber=\"\"/>\n<CopyUnit1 AddressCode=\"110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Sample DrawTime=\"201301211218\" FormatQualifier=\"203\" LaboratoryID=\""
#xmltext_3 = "\"\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"MIKS\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"S\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"BIOBANK\" Name1=\" Biobanksprov\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n<Sample DrawTime=\"201301211218\" FormatQualifier=\"203\" LaboratoryID=\"27944522ZB\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"MIKS\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"S\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"BIOBANK\" Name1=\"Biobanksprov\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n</Analysis>\n</Sample>\n</Requisition>\n</SafirMessage>/>\n</Analysis>\n</Sample>\n</Analysis>\n</Sample>\n</Requisition>\n</SafirMessage>"
#xmltext_4 = ""


xmltext_1 = "\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE SafirMessage SYSTEM \"8REQW.dtd\">\n<SafirMessage>\n<Envelope>\n<Message ID=\"R5V919AC\" Type=\"REQ\" Origin=\"EDI\" Version=\"008\"/>\n<FromSystem ID=\"KUL:30:S1037\"/>\n<ToSystem ID=\"S9416\"/>\n<Sent DateTime=\"20130612015615\"/>\n</Envelope>\n<Requisition Status=\"N\" GUID=\"05D461B9-8335-4FAE-9C49-7FBBA315CAAC\" ReqType=\"TubeCode\" RequisitionID=\""
xmltext_2 ="\" ExternalRequisitionID=\"324234333\" CareType=\"S\">\n<ReqComment Type=\"RP\" Text=\"Remitent Bibbisvar test1 fakt test2\"/>\n<ReqInformation Code=\"UBBK1\" Value=\"1\"/>\n<Patient PatientID=\"19180306-6172\" Surname=\"ERIK1\" FirstName=\"ERIKSSON1\" Sex=\"M\" BirthDate=\"19180306\" GivenNameQualifier=\"\" Address=\"TOLVAR STIGEN\" PostalCode=\"123 45\" PostalAddress=\"STOCKHOLM\" Country=\"SV\" District=\"0180\" Telephone=\"\" SocialInsuranceOffice=\"\" Comment=\"\" Secrecy=\"N\"/>\n<Biobank Concent=\"01\"/>\n<ReqUnit AddressCode=\"110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"Bibbi Olofsson\" ContactId=\"\" TelephoneNumber=\"\"/>\n<PayUnit AddressCode=\"110026831\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 2\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<CopyUnit1 AddressCode=\"110026830\" Name1=\"Karolinska Huddinge\" Name2=\"Best‰llarorg IT;Testkod 1\" Address=\"C1 81\" PostalAddress=\"141 86 Stockholm\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Sample DrawTime=\"20130612015615\" FormatQualifier=\"203\" LaboratoryID=\""
xmltext_3 = "\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"KUL\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n<Sample DrawTime=\"20130612015615\" FormatQualifier=\"203\" LaboratoryID=\"78437217ZP\">\n<ColUnit PartyQualifier=\"REQ\" AddressCode=\"KUL\" Name1=\"\" Name2=\"\" Address=\"\" PostalAddress=\"\" ContactPerson=\"\" TelephoneNumber=\"\"/>\n<Analysis PriorityCode=\"R\" TestMethodCode=\"BBK1\">\n<Lab AdressCode=\"SCARABLAB\" Name1=\"Biobanksbes till SCARAB\" Name2=\"\" Address=\"\" PostalAddress=\" \" ContactPerson=\"\" TelephoneNumber=\"\"/>\n</Analysis>\n</Sample>\n</Requisition>\n</SafirMessage>"


###################################################
#Main
print "##########################################################"
#print xmltext_1 + xmltext_2 + xmltext_3

curRIDnr = 711111

for item in range(len(labelList)):
    curLabelID = labelList[item]
    curRIDnr = curRIDnr + 1
    filename_out = "Files/" + str(curRIDnr) + ".xml"
    textout = xmltext_1 + str(curRIDnr) + xmltext_2 + curLabelID + xmltext_3
    f = open(filename_out, 'w')
    f.write(textout)
    f.close()
    
    

    


