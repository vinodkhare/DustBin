#!/usr/bin/python

import gtk
import gobject
import os, glob, time, shutil, shlex, subprocess
from DustBinIndicator import *
from Utils import *

TRASH_DIR = '/media/Store/.Trash-1000'
TRASH_INFO_DIR = '/media/Store/.Trash-1000/info'
TRASH_FILE_DIR = '/media/Store/.Trash-1000/files'
MAX_SIZE = 20000;

class DustBin:
	def Compact(self):
		infoList = lstime(TRASH_INFO_DIR)
		
		i = 0;
		while self.Size() > MAX_SIZE:
			folder, fileName = os.path.split(infoList[i][1]);
			fileName = fileName.rsplit('.', 1)
			
			filePath = os.path.join(TRASH_FILE_DIR,fileName[0])
			infoFilePath = os.path.join(TRASH_INFO_DIR, fileName[0])
			infoFilePath = infoFilePath + '.trashinfo'
			
			i += 1
			
			print "Deleting: ", filePath
			print "Deleting: ", infoFilePath
			
			if os.path.isdir(filePath):
				shutil.rmtree(filePath)
				os.remove(infoFilePath)
			else:
				os.remove(filePath)
				os.remove(infoFilePath)
				
			print 'Trashcan size: ', self.Size()
        
	def Size(self):		
		"""
		folder_size = 0
		
		for (path, dirs, files) in os.walk(TRASH_DIR):
			for file in files:
				filename = os.path.join(path, file)
				folder_size += os.path.getsize(filename)
		"""
		output = subprocess.check_output(['du', '-s', '/media/Store/.Trash-1000'])
		outputSplit = shlex.split(output)
		folderSize = float(outputSplit[0])
		
		folderSize /= 1024
		return folderSize
