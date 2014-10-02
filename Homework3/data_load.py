import os
import shutil
import fnmatch
import pickle
import time
 
def get_traversal_data():
     files_data = []
     for dirpath, dirs, files in os.walk('E:\\h2h'):
          for single_file in files:
               filepath = os.path.abspath(os.path.join(dirpath, single_file))
               File = open(filepath,'r')
               data = File.read().replace('\n', ' ')
               modTime = "Last Modified: "+ time.ctime(os.path.getmtime(filepath))
               fileSize = "Size of file in Bytes: "+str(os.path.getsize(filepath))
               t = (filepath,data,modTime,fileSize)
               files_data.append(t)
     pickle.dump(files_data,open("raw_data.pickle", "wb"))



               

             
