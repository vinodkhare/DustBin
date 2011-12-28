import gtk
import gobject

from DaakIndicator import *
from DaakPrefsWindow import *
from pygmail import *
from keyring import *

class DustBinApplication:
	def __init__(self):
		self.indicator = DaakIndicator("daak", "/home/vinod/Code/Daak/daak-new.png", appindicator.CATEGORY_APPLICATION_STATUS)
		self.indicator.initWidgets()
	
		self.gmailClient = pygmail()
		self.gmailClient.login('vinod.khare', 'Ncc1737d')
		nUnread = self.gmailClient.get_unread_count()
		self.indicator.set_label(str(nUnread))
	
		self.prefsWindow = DaakPrefsWindow()
		self.prefsWindow.initWidgets()
    
		# Make connections
		#~ self.indicator.prefsMenuItem.connect('activate', self.prefsWindow.toggleVisible)
		self.indicator.prefsMenuItem.connect('activate', self.prefsWindow.presentWindow)
		self.indicator.checkMenuItem.connect('activate', self.checkNow)
		#~ self.indicator.timeMenuItem.connect('activate', self.timeNow)
		
		#add the timer
		gobject.timeout_add(5000, self.checkNow)
	
	def checkNow(self, widget = None):
		#~ print "checkNow()"
		nUnread = self.gmailClient.get_unread_count()
		self.indicator.set_label(str(nUnread))
		return True
		
	#~ def timeNow(self, widget):
		#~ gobject.timeout_add(5000, self.checkNow)
	
	def main(self):
		daakKeyring = Keyring('daak', 'gmail.com', 'imap')
		print daakKeyring.has_credentials()
	
		gtk.main()
