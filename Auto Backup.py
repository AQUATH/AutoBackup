import os, shutil
#Music
def music(folder, folder1):
    name1 = '.'
    for (path, dirs, files) in os.walk(folder):
        subp = path[(len(folder)+1):]
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == '.jpg' or ext == '.png' or ext == '.ini' or ext == '.db':
                continue
            name = name + ext
            file = path + '/' + file
            for (path1, dirs1, files1) in os.walk(folder1):
                subp1 = path1[(len(folder1)+1):]
                for file1 in files1:
                    name1 = os.path.basename(file1)
                    file1 = path1 + '/' + file1
                    if name == name1:
                        break
                if name == name1:
                    break
            if name != name1 or (name == name1 and subp != subp1):
                print(name + ' Not found')
                path_ = folder1 + '/' + subp
                if not os.path.exists(path_):
                    print('Directory not found, creating..')
                    os.makedirs(path_)
                    print('Directory created.')
                print('Copying..')   
                shutil.copy(file, path_)
                print('Copy finished.')
    print('Music Backup Finished')
#Saves                
def game_save(folder2, folder3):
    name3 = '.'
    for (path2, dirs2, files2) in os.walk(folder2):
        for file2 in files2:
            name2 = os.path.basename(file2)
            file2 = path2 + '/' + file2
            filedate = os.stat(file2)
            time = filedate.st_mtime
            for (path3, dirs3, files3) in os.walk(folder3):
                for file3 in files3:
                    name3 = os.path.basename(file3)
                    file3 = path3 + '/' + file3
                    file1date = os.stat(file3)
                    time1 = file1date.st_mtime     
                    if name2 == name3:
                        break
                if name2 == name3:
                    break
            if name2 == name3:
                if time > time1:
                    print('Updating Save..')   
                    shutil.copy(file2, folder3)
                    print('Update finished.')
                elif time < time1:
                    print('Dest newer than source')
            else:
                print(name2 + ' NOT FOUND')
                print('Copying..')   
                shutil.copy(file2, folder3)
                print('Copy finished.')
    print('Saves Backup Finished')
print('Music Backup - 1\nSaves Backup - 2\nBack Up Both - 3\nExit - 0')
op_s = int(input('Select Operation - '))
if op_s == 1:
    so = input('Enter Source Location: ')
    de = input('Enter Destination Location: ')
    music(so, de)
elif op_s == 2:
    so1 = input('Enter Source Location: ')
    de1 = input('Enter Destination Location: ')
    game_save(so1, de1)
elif op_s == 3:
    print('Music')
    so = input('Enter Source Location: ')
    de = input('Enter Destination Location: ')
    music(so, de)
    print('Saves')
    so1 = input('Enter Source Location: ')
    de1 = input('Enter Destination Location: ')
    game_save(so1, de1)
elif op_s == 0:
    exit
