import appindicator
import gtk

class DBIndicator(appindicator.Indicator):
    def __init__(self):
	appindicator.Indicator.__init__()
	self.set_status(self.set_status(appindicator.STATUS_ACTIVE))
	self.menu = gtk.Menu()
