#this programme will rename all the files in prank folder (the numbers in the file name will be renamed)

import os
def rename_files():
    #find all the file names from the folder
    file_names = os.listdir(r"C:\Personal\GitHub\Python-course-assigments\02 Programming Foundations with Python - Udacity\prank")
    #get the files from a folder
    print(file_names)

rename_files()