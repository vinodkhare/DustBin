# Notifier example from tutorial
#
# See: http://github.com/seb-m/pyinotify/wiki/Tutorial
#
import pyinotify
import os, glob, time

TRASH_DIR = '/media/Store/.Trash-1000'
TRASH_INFO_DIR = '/media/Store/.Trash-1000/info'
TRASH_FILE_DIR = '/media/Store/.Trash-1000/files'
MAX_SIZE = 2000;

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_MOVED_TO  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MOVED_TO(self, event):
        print "Creating: ", event.pathname
        
        trashCanSize = getTrashCanSize()
        print "Trash can size: %0.1f M" % trashCanSize
        
        if trashCanSize > MAX_SIZE:
            print "Size of trash can exceeded maximum allowed limit. Compacting."
            compactTrash()
        
    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname


def getTrashCanSize():
    folder_size = 0
    
    for (path, dirs, files) in os.walk(TRASH_DIR):
        for file in files:
            filename = os.path.join(path, file)
            folder_size += os.path.getsize(filename)
    
    folder_size /= (1024*1024.0)
    return folder_size
    

def compactTrash():
    infoList = lstime(TRASH_INFO_DIR)
    
    i = 0;
    while getTrashCanSize() > MAX_SIZE:
        folder, fileName = os.path.split(infoList[i][1]);
        fileName = fileName.rsplit('.', 1)
        
        filePath = os.path.join(TRASH_FILE_DIR,fileName[0])
        infoFilePath = os.path.join(TRASH_INFO_DIR, fileName[0])
        infoFilePath = infoFilePath + '.trashinfo'
        
        i += 1
        
        print "Deleting: ", filePath
        print "Deleting: ", infoFilePath
        
        if os.path.isdir(filePath):
            if isDirEmpty(filePath):
                os.rmdir(filePath)
                os.remove(infoFilePath)
        else:
            os.remove(filePath)
            os.remove(infoFilePath)
            
        print 'Trashcan size: ', getTrashCanSize()
            

def lstime(root):
    date_file_list = []
    for folder in glob.glob(root):
        # select the type of file, for instance *.jpg or all files *.*
        for file in glob.glob(folder + '/*.*'):
            # retrieves the stats for the current file as a tuple
            # (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
            # the tuple element mtime at index 8 is the last-modified-date
            stats = os.stat(file)
            # create tuple (year yyyy, month(1-12), day(1-31), hour(0-23), minute(0-59), second(0-59),
            # weekday(0-6, 0 is monday), Julian day(1-366), daylight flag(-1,0 or 1)) from seconds since epoch
            # note:  this tuple can be sorted properly by date and time
            lastmod_date = time.localtime(stats[8])
            #print image_file, lastmod_date   # test
            # create list of tuples ready for sorting by date
            date_file_tuple = lastmod_date, file
            date_file_list.append(date_file_tuple)
        
    #print date_file_list  # test

    date_file_list.sort()
    return date_file_list
    
    # date_file_list.reverse()  # newest mod date now first
"""    
    for file in date_file_list:
        # extract just the filename
        folder, file_name = os.path.split(file[1])
        # convert date tuple to MM/DD/YYYY HH:MM:SS format
        file_date = time.strftime("%m/%d/%y %H:%M:%S", file[0])
        print "%-40s %s" % (file_name, file_date)
"""        
    
    
    
def isDirEmpty(folder):
    if os.listdir(folder) == []:
        return True
    else:
        return False

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(TRASH_FILE_DIR, mask, rec=True)

notifier.loop()
