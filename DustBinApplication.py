import gtk
import gobject
import os, glob, time, shutil
import pyinotify

from DustBin import *
from DustBinIndicator import *

TRASH_DIR = '/media/Store/.Trash-1000'
TRASH_INFO_DIR = '/media/Store/.Trash-1000/info'
TRASH_FILE_DIR = '/media/Store/.Trash-1000/files'
MAX_SIZE = 20000;

mask = pyinotify.IN_MOVED_TO | pyinotify.IN_MOVED_FROM # watched events

# event handler class
class EventHandler(pyinotify.ProcessEvent):
	def __init__(self, Bin, Indicator):
		pyinotify.ProcessEvent.__init__(self)
		self.Bin = Bin
		self.Indicator = Indicator
	
	def process_IN_MOVED_FROM(self, event):
		self.Indicator.SetSize(self.Bin.Size())
		self.Indicator.AddRestored(event.pathname)
	
	def process_IN_MOVED_TO(self, event):
		self.Indicator.SetSize(self.Bin.Size())
		self.Indicator.AddTrashed(event.pathname)
		
		if self.Bin.Size() > MAX_SIZE:
			self.Bin.Compact()

class DustBinApplication:
	def __init__(self):
		# create the dust bin
		self.Bin = DustBin()
		
		self.indicator = DustBinIndicator("dustbin", "/home/vinod/Code/DustBin/trash-dark.png", appindicator.CATEGORY_APPLICATION_STATUS)
		self.indicator.initWidgets()
		self.indicator.SetSize(self.Bin.Size())
		
		# create the folder change notifier
		wm = pyinotify.WatchManager()
		wdd = wm.add_watch(TRASH_FILE_DIR, mask, rec=True)
		handler = EventHandler(self.Bin, self.indicator)
		self.Notifier = pyinotify.Notifier(wm, handler, timeout=10)
		
		# Add the timer
		gobject.timeout_add(100, self.CheckTrash)
		
	def CheckTrash(self, widget=None):
		assert self.Notifier._timeout is not None, 'Notifier must be constructed with a short timeout'

		self.Notifier.process_events()
		while self.Notifier.check_events():  #loop in case more events appear while we are processing
			self.Notifier.read_events()
			self.Notifier.process_events()
			
		return True

	def main(self):
		gtk.main()
