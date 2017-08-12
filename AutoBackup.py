import os
import shutil

extm = ['.mp3', '.flac', '.aac', '.wav', '.ape', '.alac', '.m4a', '.ogg', '.aiff', '.aif']
exta = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
exte = ['.m3u', '.m3u8', '.txt', '.cue', '.log']

def backup(sourceLocation, destinationLocation, path, file, name, ext):
    pathCheck = destinationLocation + '/' + path[(len(sourceLocation)+1):] 
    fileCheck = pathCheck + '/' + file
    file = path + '/' + file
    if not os.path.exists(pathCheck):
        os.makedirs(pathCheck)
    if not os.path.isfile(fileCheck):
        print(name + ext + ' not found, copying..') 
        shutil.copy2(file, pathCheck)
        print('Copy finished.')

def func(sourceLocation, destinationLocation, operation, extras, twoWayBackup):
    for (path, dirs, files) in os.walk(sourceLocation):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if operation == '1' or operation == '3' and ext in extm or extras == 'y' and ext in exte:
                backup(sourceLocation, destinationLocation, path, file, name, ext)
            if operation == '2' or operation == '3' and ext in exta and name[:8] != 'AlbumArt' and name != ('Thumbnail' and 'Folder'):
                backup(sourceLocation, destinationLocation, path, file, name, ext)
    if twoWayBackup == ('y' or 'Y'):
        twoWayBackup = 'n'
        func(destinationLocation, sourceLocation, operation, extras, twoWayBackup)

while True:
    print('Back up: \n\tMusic - 1\n\tArtwork - 2\n\tBoth - 3\nExit - 0')
    print('Back up extras? (Playlists, logs, texts) y/n')
    print('Two-way backup? y/n')
    selection = input('Enter your selection in a single line: ')
    if selection[0] == '1' or selection[0] == '2' or selection[0] == '3':
        sourceLocation = input('Enter Source Location: ')
        destinationLocation = input('Enter Destination Location: ')
        func(sourceLocation, destinationLocation, selection[0], str.lower(selection[1]), str.lower(selection[2]))
    elif selection[0] == '0':
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
# Input all options in a single line ([op][twoWayBackup]) - operation combo
# Backup extras
