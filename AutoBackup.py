import os
import shutil

ext_music = ['.mp3', '.flac', '.aac', '.wav', '.wma', '.ape', '.alac', '.m4a', '.m4b', '.m4p', '.ogg', '.aiff', '.aif']
ext_artwork = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
ext_extras = ['.m3u', '.m3u8', '.wpl', '.pls', '.asx', '.smi', '.sami', '.xspf', '.txt', '.cue', '.log']
ext_both = ext_music + ext_artwork


def backup(destination_location, path, file):
    target_path = destination_location + os.path.sep + path[(len(destination_location)+1):]
    target_file = os.path.join(target_path, file)

    print(destination_location)
    print(path[(len(destination_location)+1):])
    print(target_path)

    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except OSError:
            print('Unable to create the appropriate folder for', file)
            return 3

    if not os.path.isfile(target_file):
        print(file, 'not found, copying..')
        try:
            shutil.copy2(os.path.join(path, file), target_path)
            print('Copy finished.')
            return 1  # Returned when the file was not found, and the copy was successful.
        except shutil.Error:
            print('Copy failed.')
            return 2  # Returned when the file was not found, but the copy failed.

    return 0  # Returned when the file already exists in destination_location.


def create_log(destination_location, source_location):
    from datetime import datetime

    if not os.path.exists(destination_location):
        try:
            os.makedirs(destination_location) 
        except OSError:
            print('\tUnable to create a log file to:', destination_location, 'a log file will be saved to:',
                  source_location, 'instead.')
            with open(os.path.join(source_location, 'AutoBackup.log'), 'a') as log:
                log.write('\tDate and time: ' + str(datetime.now())[:19] + '\n\n')
            return 1

    print('\tA log file will be saved to:', destination_location)

    with open(os.path.join(destination_location, 'AutoBackup.log'), 'a') as log:
        log.write('\tDate and time: ' + str(datetime.now())[:19] + '\n\n')

    return 0


def update_log(location, file, backup_result):
    with open(os.path.join(location, 'AutoBackup.log'), 'a', encoding='UTF-8') as log:
        if backup_result == 1:
            log.write(file + ' was copied successfully.\n')
        elif backup_result == 2:
            log.write('Unable to copy ' + file + ' because an error occurred.\n')
        elif backup_result == 3:
            log.write('Unable to create the appropriate folder for ' + file + '\n')


def main(source_location, destination_location, operation, extras, two_way_backup, enable_log):
    if enable_log == 'y':
        create_log_result = create_log(destination_location, source_location)
        log_location = [destination_location, source_location]

    arrays = [ext_music, ext_artwork, ext_both]

    for path, _, files in os.walk(source_location):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = str.lower(ext)
            print(ext)
            if ext in arrays[int(operation)-1] or ext in ext_extras and extras == 'y':
                if ext not in ext_artwork or name[:8] != 'AlbumArt' and name != 'Thumbnail' and name != 'Folder':
                    backup_result = backup(destination_location, path, file)

                    if backup_result != 0 and enable_log == 'y':
                        update_log(log_location[create_log_result], file, backup_result)

    if two_way_backup == 'y':
        main(destination_location, source_location, operation, extras, 'n', enable_log)


while True:
    print('Back up: \n\tMusic - 1\n\tArtwork - 2\n\tBoth - 3\nExit - 0')
    print('Back up extras? (play-lists, logs, texts) y/n')
    print('Two-way backup? y/n')
    print('Save a log file? y/n')

    selection = input('Enter your selection in a single line: ')

    if selection[0] in ['1', '2', '3']:
        source = input('Enter Source Location: ')
        destination = input('Enter Destination Location: ')

        main(source, destination, selection[0], str.lower(selection[1]), str.lower(selection[2]),
             str.lower(selection[3]))

        print('\tOperation finished.')
    elif selection[0] == '0':
        break
    else:
        print('Please enter a value between 0-3.')
