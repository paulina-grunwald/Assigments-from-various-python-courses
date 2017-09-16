#this programme will rename all the files in prank folder (the numbers in the file name will be renamed)

import os
def rename_files():
    #find all the file names from the folder
    #os.listdir() lists all in the directory

    file_list = os.listdir(r"C:\Personal\GitHub\Python-course-assigments\02 Programming Foundations with Python - Udacity\prank")
    #change file names
    saved_path = os.getcwd()
    print("Current working drectory is"+saved_path)
    os.chdir(r"C:\Personal\GitHub\Python-course-assigments\02 Programming Foundations with Python - Udacity\prank")
    print(file_list)

    #for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()