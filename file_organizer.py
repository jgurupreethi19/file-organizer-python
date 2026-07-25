import os
import shutil
def move_file(file_path,file,folder,value):
    if os.path.exists(folder):
        shutil.move(os.path.join(file_path,file),os.path.join(folder,file))
    else:
        os.mkdir(folder)
        shutil.move(os.path.join(file_path,file),os.path.join(folder,file))
    count[value]+=1
    
                
print("Enter the folder path: ")
count={"Images":0,"Documents":0,"Videos":0,"Audio":0,"Java":0,"Python":0,"Archives":0,"Others":0}
file_path=input()
if os.path.exists(file_path)==False:
    print("Folder not found")
else:
    files=os.listdir(file_path)
    d={".jpg":"Images",".jpeg":"Images",".png":"Images",".pdf":"Documents",".docx":"Documents",
       ".pptx":"Documents",".mp4":"Videos",".mp3":"audio",".py":"Python",".java":"Java",".zip":"Archives",
       ".rar":"Archives"}
    for file in files:
        if os.path.isfile(os.path.join(file_path,file)):
            root,ext=os.path.splitext(file)
            key=ext.lower()
            
            if key in d:
                value=d[key]
                #print(value)
                folder=os.path.join(file_path,value)
                move_file(file_path,file,folder,value)
            else:
                folder=os.path.join(file_path,"Others")
                if os.path.exists(folder):
                         shutil.move(os.path.join(file_path,file),os.path.join(folder,file))
                else:
                        os.mkdir(folder)
                        shutil.move(os.path.join(file_path,file),os.path.join(folder,file))

print("================ SUMMARY ================")                   
for key in count:
    print(key,"       : ",count[key])

                
                
                    
