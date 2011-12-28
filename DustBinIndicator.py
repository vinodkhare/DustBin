import appindicator
import gtk

RECENT_FILE_COUNT = 5

class DustBinIndicator(appindicator.Indicator):
	def initWidgets(self):
		self.set_status(appindicator.STATUS_ACTIVE)
		self.menu = gtk.Menu()

		self.quitMenuItem = gtk.MenuItem('Quit')
		self.quitMenuItem.show()
		self.quitMenuItem.connect("activate", gtk.main_quit)
		
		self.TrashSizeMenuItem = gtk.MenuItem('Size: ')
		self.TrashSizeMenuItem.set_state(gtk.STATE_INSENSITIVE)
		self.TrashSizeMenuItem.show()
		
		self.RecentMenu = gtk.Menu()
		self.RecentMenu.show()
		item = gtk.MenuItem('')
		item.show()
		self.RecentMenu.append(item)
		
		self.RecentMenuItem = gtk.MenuItem('Recent')
		self.RecentMenuItem.set_submenu(self.RecentMenu)
		self.RecentMenuItem.show()
		
		self.menu.append(self.TrashSizeMenuItem)
		self.menu.append(self.quitMenuItem)
		self.AddSeparator()
		self.menu.append(self.RecentMenuItem)

		self.set_menu(self.menu)
		self.FileList = None
		
	def AddRestored(self, PathName):
		item = gtk.MenuItem('<-\t' + PathName)
		item.show()
		self.RecentMenu.append(item)
		self.TrimRecentMenu()
		
	def AddTrashed(self, PathName):
		item = gtk.MenuItem('->\t' + PathName)
		item.set_state(gtk.STATE_INSENSITIVE)
		item.show()
		self.RecentMenu.append(item)
		self.TrimRecentMenu()
		
	def AddSeparator(self):
		separator = gtk.SeparatorMenuItem()
		separator.show()
		self.menu.append(separator)
		
	def SetSize(self, TrashSize):
		self.TrashSizeMenuItem.set_label('Size: %0.1f GB' % (TrashSize / 1000))
		
	def TrimRecentMenu(self):
		RecentMenuItemList = self.RecentMenu.get_children()
		
		while len(RecentMenuItemList) > RECENT_FILE_COUNT:
			self.RecentMenu.remove(RecentMenuItemList[0])
			RecentMenuItemList = self.RecentMenu.get_children()
		
