import gtk
import gobject
import os, glob, time, shutil

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
