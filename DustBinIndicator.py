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
		
		self.TrashSizeMenuItem = gtk.MenuItem('Size: ')
		self.TrashSizeMenuItem.set_state(gtk.STATE_INSENSITIVE)
		self.TrashSizeMenuItem.show()
		
		#~ self.timeMenuItem = gtk.MenuItem('Time')
		#~ self.timeMenuItem.show()
		
		menu.append(self.TrashSizeMenuItem)
		menu.append(self.checkMenuItem)
		#~ menu.append(self.timeMenuItem)
		menu.append(self.prefsMenuItem)
		menu.append(self.quitMenuItem)

		self.set_menu(menu)
		
	def AddRestored(self, PathName):
		pass
		
	def SetSize(self, TrashSize):
		self.TrashSizeMenuItem.set_label('Size: %0.1f GB' % (TrashSize / 1000))
		
