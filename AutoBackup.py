import os
import shutil
extm = ['.mp3', '.flac', '.aac', '.wav', '.ape', '.alac', '.m4a', '.ogg', '.aiff', '.aif']
exta = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
exte = ['.m3u', '.m3u8', '.txt', '.cue', '.log']
def backup(sloc, dloc, path, file, name, ext):
    pch = dloc + '/' + path[(len(sloc)+1):] 
    fch = pch + '/' + file
    file = path + '/' + file
    if not os.path.exists(pch):
        os.makedirs(pch)
    if not os.path.isfile(fch):
        print(name + ext + ' not found, copying..') 
        shutil.copy2(file, pch)
        print('Copy finished.')
def func(sloc, dloc, sel, extras, twb):
    for (path, dirs, files) in os.walk(sloc):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if sel == '1' or sel == '3' and ext in extm or extras == 'y' and ext in exte:
                backup(sloc, dloc, path, file, name, ext)
            if sel == '2' or sel == '3' and ext in exta and name[:8] != 'AlbumArt' and name != ('Thumbnail' and 'Folder'):
                backup(sloc, dloc, path, file, name, ext)
    if twb == ('y' or 'Y'):
        twb = 'n'
        func(dloc, sloc, sel, extras, twb)
while True:
    print('Back up: \n\tMusic - 1\n\tArtwork - 2\n\tBoth - 3\nExit - 0')
    print('Back up extras? (Playlists, logs, texts) y/n')
    print('Two-way backup? y/n')
    op = input('Enter your selection in a single line: ')
    if op[0] == '1' or op[0] == '2' or op[0] == '3':
        sloc = input('Enter Source Location: ')
        dloc = input('Enter Destination Location: ')
        func(sloc, dloc, op[0], str.lower(op[1]), str.lower(op[2]))
    elif op[0] == '0':
        break
    else:
        print('Please enter a value between 0-3.')
    print('Operation finished')
# To implement
# Log
# Try/catch for copy/dir creation
# ---------
# Changelog
# name += ext unnecessary, intergrated to print
# Added exit option to menu
# Put ext arrays/lists outside function definition
# Backup function to avoid continue
# Input all options in a single line ([op][twb]) - operation combo
# Backup extras
