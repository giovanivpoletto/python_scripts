#tested with 1.395.440 files in the same directory. Run for almost 24h.
import shutil
import os 
from time import sleep
from os.path import basename
import fnmatch

def check_files(month):
    for file in file_list:
        if fnmatch.fnmatch(file, '*_2020'+month+'*.wav'): #string i was looking for in a huge files list
            shutil.copy2(path+'/'+file,dst+'/'+month) # I used copy2 instead of move, because i was scare to death to loose those files. =)
            print(file)

path = "path_name"
dst = "destination directory"

file_list = os.listdir(path)
months = [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for month in months:
    check_files(month)
    print(month)
    sleep(5)  
