import os
import shutil

extMusic = ['.mp3', '.flac', '.aac', '.wav', '.ape', '.alac', '.m4a', '.ogg', '.aiff', '.aif']
extArtwork = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
extExtras = ['.m3u', '.m3u8', '.txt', '.cue', '.log']

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
            if operation == '1' or operation == '3' and ext in extMusic or extras == 'y' and ext in extExtras:
                backup(sourceLocation, destinationLocation, path, file, name, ext)
            if operation == '2' or operation == '3' and ext in extArtwork and name[:8] != 'AlbumArt' and name != 'Thumbnail' and name != 'Folder':
                backup(sourceLocation, destinationLocation, path, file, name, ext)
    if twoWayBackup == 'y' or twoWayBackup == 'Y':
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
