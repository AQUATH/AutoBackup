import os, shutil
def music():
    print('Music Backup')
    fold0 = input('Enter Source Location: ')
    fold1 = input('Enter Destination Location: ')
    extm = ['.mp3', '.flac', '.aac', '.wav', '.ape', '.alac', '.m4a', '.ogg', '.aiff']
    name1 = '.'
    for (path, dirs, files) in os.walk(fold0):
        subp = path[(len(fold0)+1):]
        for file in files:
            name, ext = os.path.splitext(file)
            if not ext in extm:
                continue
            name = name + ext
            file = path + '/' + file
            path_ = fold1 + '/' + subp
            if not os.path.exists(path_):
                    os.makedirs(path_)
            for (path1, dirs1, files1) in os.walk(path_):
                for file1 in files1:
                    name1 = os.path.basename(file1)
                    if name == name1:
                        break
                if name == name1:
                    break
            if name != name1:
                print(name + ' not found, copying..') 
                shutil.copy(file, path_)
                print('Copy finished.')
    print('Music Backup finished')
def game_save():
    print('Saves Backup')
    fold2 = input('Enter Source Location: ')
    fold3 = input('Enter Destination Location: ')
    name3 = '.'
    for (path2, dirs2, files2) in os.walk(fold2):
        for file2 in files2:
            name2 = os.path.basename(file2)
            file2 = path2 + '/' + file2
            filedate = os.stat(file2)
            time = filedate.st_mtime
            for (path3, dirs3, files3) in os.walk(fold3):
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
                    print('Updating save..')   
                    shutil.copy(file2, fold3)
                    print('Update finished.')
                elif time < time1:
                    print('No update needed.')
            else:
                print('Save not found, copying..')   
                shutil.copy(file2, fold3)
                print('Copy finished.')
    print('Saves Backup finished')
print('Music Backup - 1\nSaves Backup - 2\nBack Up Both - 3\nExit - 0')
while True:
    op_s = input('Select Operation: ')
    if op_s == '1':
        music()
    elif op_s == '2':
        game_save()
    elif op_s == '3':
        music()
        game_save()
    elif op_s == '0':
        break
exit
