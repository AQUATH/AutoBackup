import os
import shutil
import sys


ext_music = ['.mp3', '.flac', '.aac', '.wav', '.wma', '.ape', '.alac', '.m4a', '.m4b', '.m4p', '.ogg', '.aiff', '.aif']
ext_artwork = ['.jpg', '.png', '.bmp', '.gif', '.jpeg']
ext_extras = ['.m3u', '.m3u8', '.wpl', '.pls', '.asx', '.smi', '.sami', '.xspf', '.txt', '.cue', '.log']
ext_both = ext_music + ext_artwork
lists = [ext_music, ext_artwork, ext_both]


def file_copy(destination_location, path, file, source):
    # manual path joining is used because os.path.join returns the second argument when two absolute paths are joined
    # e.g. /foo and /bar are joined as /bar instead of /foo/bar
    # whereas this method creates /foo//bar which is then normalized by abspath to /foo/bar
    target_path = os.path.abspath(destination_location + os.path.sep + path[len(source):])
    target_file = os.path.join(target_path, file)

    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except OSError:
            print("Unable to create the appropriate folder for", file)
            return 3

    if not os.path.isfile(target_file):
        try:
            shutil.copy2(os.path.join(path, file), target_path)
            return 1  # Returned when the file was not found and the copy was successful.
        except shutil.Error:
            print('Copy failed.')
            return 2  # Returned when the file was not found, but the copy failed.

    return 0  # Returned when the file already exists in destination_location.


def create_log(log_file, source_location, destination_location, operation, extras, sync):
    if not os.path.exists("Logs"):
        try:
            os.makedirs("Logs")
        except OSError:
            print("ERROR: Unable to create log-folder.")
            return

    try:
        with open(os.path.join("Logs", log_file), 'w+', encoding='UTF-8') as log:
            log.write("Source Location: " + source_location + "\n")
            log.write("Destination Location: " + destination_location + "\n")
            if operation == 0:
                log.write("Chosen Operation: Music only.\n")
            elif operation == 1:
                log.write("Chosen Operation: Artwork only.\n")
            elif operation == 2:
                log.write("Chosen Operation: Music and artwork.\n")
            else:
                log.write("Chosen Operation: Unknown operation, probably an error has occurred.\n")
            log.write("Extra files: " + str(extras) + "\n")
            log.write("Folder-Sync: " + str(sync) + "\n\n")
    except OSError:
        print("ERROR: Unable to create log-folder or logfile.")
    return


def update_log(file, backup_result, log_file):
    with open(os.path.join("Logs", log_file), 'a', encoding='UTF-8') as log:
        if backup_result == 1:
            log.write(file + ' was copied successfully.\n')
        elif backup_result == 2:
            log.write('Unable to copy ' + file + ' because an error occurred.\n')
        elif backup_result == 3:
            log.write('Unable to create the appropriate folder for ' + file + '\n')


def main(source_location, destination_location, operation, extras, sync, log):
    if log:
        from datetime import datetime

        current_date = str(datetime.now())[:19]
        log_file = "AutoBackup_" + current_date[:10] + '_' + current_date[11:] + ".log"
        create_log(log_file, source_location, destination_location, operation, extras, sync)

    for path, _, files in os.walk(source_location):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = str.lower(ext)

            if ext in lists[int(operation)] or extras and ext in ext_extras:
                if ext not in ext_artwork or name[:8] != 'AlbumArt' and name != 'Thumbnail' and name != 'Folder':
                    backup_result = file_copy(destination_location, path, file, source_location)

                    if log and backup_result > 0:
                        update_log(file, backup_result, log_file)

    if sync:
        main(destination_location, source_location, operation, extras, False, log)


def argument_validity(list_of_arguments):
    extras_flag = False
    sync_flag = False
    log_flag = False

    if len(list_of_arguments) < 4:
        print("Usage: python3", list_of_arguments[0], "<source> <destination> <music | artwork> [options]")
        sys.exit()

    source = os.path.abspath(list_of_arguments[1])

    if not os.path.exists(source):
        print(list_of_arguments[1], "does not exist.")
        sys.exit()

    destination = os.path.abspath(list_of_arguments[2])

    if list_of_arguments[3] == "-m" or list_of_arguments[3] == "--music":
        selection = 0
    elif list_of_arguments[3] == "-a" or list_of_arguments[3] == "--artwork":
        selection = 1
    elif list_of_arguments[3] == "-ma" or list_of_arguments[3] == "-c" or list_of_arguments[3] == "--complete":
        selection = 2
    else:
        print("Unrecognized option", list_of_arguments[3])
        sys.exit()

    for i in range(4, len(list_of_arguments)):
        if list_of_arguments[i] == "-e" or list_of_arguments[i] == "--extras":
            extras_flag = True
        elif list_of_arguments[i] == "-s" or list_of_arguments[i] == "--sync":
            sync_flag = True
        elif list_of_arguments[i] == "-l" or list_of_arguments[i] == "--log":
            log_flag = True
        else:
            print("Unrecognized option", list_of_arguments[i])
            sys.exit()

    return source, destination, selection, extras_flag, sync_flag, log_flag


if __name__ == "__main__":
    source, destination, selection, extras_flag, sync_flag, log_flag = argument_validity(sys.argv)
    main(source, destination, selection, extras_flag, sync_flag, log_flag)
