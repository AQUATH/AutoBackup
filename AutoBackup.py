import os
import shutil

extMusic = ['.mp3', '.flac', '.aac', '.wav', '.wma', '.ape', '.alac', '.m4a', '.m4b', '.m4p', '.ogg', '.aiff', '.aif']
extArtwork = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
extExtras = ['.m3u', '.m3u8', '.wpl', '.pls', '.asx', '.smi', '.sami', '.xspf', '.txt', '.cue', '.log']

def backup(sourceLocation, destinationLocation, path, file, name, ext):
    pathCheck = destinationLocation + '/' + path[(len(sourceLocation)+1):] 
    fileCheck = pathCheck + '/' + file
    file = path + '/' + file
    if not os.path.exists(pathCheck):
        try:
            os.makedirs(pathCheck)
        except:
            print('Unable to create the appropriate folder for ' + name + ext)
            return 3
    if not os.path.isfile(fileCheck):
        print(name + ext + ' not found, copying..')
        try:
            shutil.copy2(file, pathCheck)
            print('Copy finished.')
            return 1 #Returned when the file was not found, and the copy was successful.
        except:
            print('Copy failed.')
            return 2 #Returned when the file was not found, but the copy failed.
    return 0 #Returned when the file already exists in destinationLocation.

def createLog(destinationLocation, sourceLocation):
    from datetime import datetime
    if not os.path.exists(destinationLocation):
        try:
            os.makedirs(destinationLocation) 
        except:
            print('\tUnable to create a log file to: ' + destinationLocation + ' a log file will be saved to: ' + sourceLocation + ' instead.')
            with open(sourceLocation + '\AutoBackup.log', 'a') as log:
                log.write('\n\tDate and time: ' + str(datetime.now())[:19] + '\n\n')
            return 1
    print('\tA log file will be saved to: ' + destinationLocation)
    with open(destinationLocation + '\AutoBackup.log', 'a') as log:
        log.write('\n\tDate and time: ' + str(datetime.now())[:19] + '\n\n')
    return 0

def updateLog(location, name, ext, backupResult):
    with open(location + '\AutoBackup.log', 'a', encoding = 'UTF-8') as log:
        if(backupResult == 1):
            log.write(name + ext + " was copied successfully.\n")
        elif(backupResult == 2):
            log.write("Unable to copy " + name + ext + " because an error occured.")
        elif(backupResult == 3):
            log.write('Unable to create the appropriate folder for ' + name + ext)

def main(sourceLocation, destinationLocation, operation, extras, twoWayBackup, createLogCheck):
    if createLogCheck == 'y':
        createLogResult = createLog(destinationLocation, sourceLocation)
        logLocation = {0: destinationLocation, 1: sourceLocation}
    for (path, dirs, files) in os.walk(sourceLocation):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if (operation == '1' or operation == '3') and ext in extMusic or extras == 'y' and ext in extExtras:
                backupResult = backup(sourceLocation, destinationLocation, path, file, name, ext)
                if backupResult != 0 and createLogCheck == 'y':
                    updateLog(logLocation[createLogResult], name, ext, backupResult)
            if (operation == '2' or operation == '3') and ext in extArtwork and name[:8] != 'AlbumArt' and name != 'Thumbnail' and name != 'Folder':
                backupResult = backup(sourceLocation, destinationLocation, path, file, name, ext)
                if backupResult != 0 and createLogCheck == 'y':
                    updateLog(logLocation[createLogResult], name, ext, backupResult)
    if twoWayBackup == 'y':
        main(destinationLocation, sourceLocation, operation, extras, 'n', createLogCheck)

while True:
    print('Back up: \n\tMusic - 1\n\tArtwork - 2\n\tBoth - 3\nExit - 0')
    print('Back up extras? (Playlists, logs, texts) y/n')
    print('Two-way backup? y/n')
    print('Save a log file? y/n')
    selection = input('Enter your selection in a single line: ')
    if selection[0] == '1' or selection[0] == '2' or selection[0] == '3':
        sourceLocation = input('Enter Source Location: ')
        destinationLocation = input('Enter Destination Location: ')
        main(sourceLocation, destinationLocation, selection[0], str.lower(selection[1]), str.lower(selection[2]), str.lower(selection[3]))
        print('\tOperation finished')
    elif selection[0] == '0':
        break
    else:
        print('Please enter a value between 0-3.')

# To implement
#
# ---------
# Changelog
# Try/catch for copy/dir creation
# Added ability to create a log file on the destination location
# Renamed every variable
# name += ext unnecessary, intergrated to print
# Added exit option to menu
# Put ext arrays/lists outside function definition
# Backup function to avoid continue
# Input all options in a single line ([op][twoWayBackup]) - operation combo
# Backup extras
