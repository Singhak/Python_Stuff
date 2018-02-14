import win32com.client
import pythoncom

class Handler_Class(object):
	def OnNewMailEx(self, receivedItemsIDs):
		senderList = ['', '', '', '']
		for ID in receivedItemsIDs.split(","):
			# https://msdn.microsoft.com/en-us/library/microsoft.office.interop.outlook._mailitem_properties.aspx
			mailItem = outlook.Session.GetItemFromID(ID)
			#senderId = mailItem.SenderEmailAddress
			senderName = mailItem.SenderName
			print ("Subj: " + mailItem.Subject)
			print ("SenderName: " + senderName)
			if(senderName in senderList):
				print('\007')
				print("Important Mail")
			print ("========")


outlook = win32com.client.DispatchWithEvents("Outlook.Application", Handler_Class)

#and then an infinit loop that waits from events.
pythoncom.PumpMessages() 
