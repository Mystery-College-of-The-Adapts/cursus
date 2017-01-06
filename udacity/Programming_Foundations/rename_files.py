import os, glob, re


def rename_files():
    # get files from a folder
    file_list = os.listdir(r"C:\Users\qubit\Desktop\Robotics Coursera course\new")
    print(file_list)

    os.chdir(r"C:\Users\qubit\Desktop\Robotics Coursera course\new")
    saved_path = os.getcwd()
    print(saved_path)

    # for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+ file_name)
        print("New Name -"+ file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()