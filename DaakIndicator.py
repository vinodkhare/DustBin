import appindicator
import gtk

class DustBinIndicator(appindicator.Indicator):
	def initWidgets(self):
		self.set_status(appindicator.STATUS_ACTIVE)
		menu = gtk.Menu()

		self.quitMenuItem = gtk.MenuItem('Quit')
		self.quitMenuItem.show()
		self.quitMenuItem.connect("activate", gtk.main_quit)
		
		self.prefsMenuItem = gtk.MenuItem('Preferences')
		self.prefsMenuItem.show()
		# prefsMenuItem.connect("activate", prefsWindow.toggleVisible)
		
		self.checkMenuItem = gtk.MenuItem('Check Now')
		self.checkMenuItem.show()
		
		#~ self.timeMenuItem = gtk.MenuItem('Time')
		#~ self.timeMenuItem.show()
		
		menu.append(self.checkMenuItem)
		#~ menu.append(self.timeMenuItem)
		menu.append(self.prefsMenuItem)
		menu.append(self.quitMenuItem)

		self.set_menu(menu)
		self.set_label('1')
