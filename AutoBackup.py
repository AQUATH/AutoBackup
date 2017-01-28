import os, shutil
def music(sloc, dloc, op, twb):
    extm = ['.mp3', '.flac', '.aac', '.wav', '.ape', '.alac', '.m4a', '.ogg', '.aiff', '.aif']
    exta = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
    for (path, dirs, files) in os.walk(sloc):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if op == '1' and ext not in extm:
                continue
            elif op == '2' and (ext not in exta or name[:8] == 'AlbumArt' or name == 'Thumbnail' or name == 'Folder'):
                continue
            elif op == '3' and ((ext not in extm and ext not in exta) or (ext in exta and (name[:8] == 'AlbumArt' or name == 'Thumbnail' or name == 'Folder'))):
                continue
            name += ext
            pch = dloc + '/' + path[(len(sloc)+1):] 
            fch = pch + '/' + file
            file = path + '/' + file
            if not os.path.exists(pch):
                os.makedirs(pch)
            if not os.path.isfile(fch):
                print(name + ' not found, copying..') 
                shutil.copy(file, pch)
                print('Copy finished.')
    if twb == ('y' or 'Y'):
        twb = 'n'
        music(dloc, sloc, op, twb)
while True:
    op = input('Back up: Music - 1, Artwork - 2, Both - 3: ')
    twb =  input('Two-way backup? y/n: ')
    sloc = input('Enter Source Location: ')
    dloc = input('Enter Destination Location: ')
    music(sloc, dloc, op, twb)
    print('Operation finished')
