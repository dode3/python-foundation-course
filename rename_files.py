import os


def rename_files():
    #get location of photos file
    file_list = os.listdir(r"C:\Python27\prank")
    print(file_list)
    saved_path=os.getcwd()
    print('the working one is'+saved_path)
    os.chdir(r"C:\Python27\prank")

    #rename it
    for file_name in file_list:
        print("old_name -",file_name)
        print("new_name -",file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
        os.chdir(saved_path)

rename_files()
        
        
        
