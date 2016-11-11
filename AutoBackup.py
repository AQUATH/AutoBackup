import os, shutil
def music(sloc, dloc, op, sel):
    extm = ['.mp3', '.flac', '.aac', '.wav', '.ape', '.alac', '.m4a', '.ogg', '.aiff', '.aif']
    exta = ['.jpg', '.png', '.bmp', '.gif', '.jpeg', '.JPG', '.JPEG']
    for (path, dirs, files) in os.walk(sloc):
        for file in files:
            name, ext = os.path.splitext(file)
            if op == '1' and ext not in extm:
                continue
            elif op == '2' and (ext not in exta or name[:13] == 'AlbumArtSmall' or name == 'Thumbnail' or name == 'Folder'):
                continue
            elif op == '3' and (ext not in (extm and exta) or (ext in exta and (name[:13] == 'AlbumArtSmall' or name == 'Thumbnail' or name == 'Folder'))):
                continue
            name += ext
            path_ = dloc + '/' + path[(len(sloc)+1):] 
            check = path_ + '/' + file
            file = path + '/' + file
            if not os.path.exists(path_):
                os.makedirs(path_)
            if not os.path.isfile(check):
                print(name + ' not found, copying..') 
                shutil.copy(file, path_)
                print('Copy finished.')
    if sel == 'y' or 'Y':
        sel = 'n'
        music(dloc, sloc, op, sel)
while True:
    op = input('Back up: Music - 1, Artwork - 2, Both - 3: ')
    sel =  input('Two-way backup? y/n: ')
    sloc = input('Enter Source Location: ')
    dloc = input('Enter Destination Location: ')
    music(sloc, dloc, op, sel)
    print('Operation finished')
