import os

#read files
def secret_msg():
 names = os.listdir(r"C:\Python27\alphabet")
 print(names)
 the_path = os.getcwd()
 print(the_path)
 os.chdir(r"C:\Python27\alphabet")
     
#rename it
 for file_name in names:
     print("old_name-",file_name)
     print("new_name-",file_name.translate(None , "0123456789"))
     os.rename
     (file_name,file_name.translate(None,"0123456789"))
     os.chdir(the_path)

secret_msg()
