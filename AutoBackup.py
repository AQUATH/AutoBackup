import os
import shutil
import sys
import argparse


ext_music = [".mp3", ".flac", ".aac", ".wav", ".wma", ".ape", ".alac", ".m4a", ".m4b", ".m4p", ".ogg", ".aiff", ".aif"]
ext_artwork = [".jpg", ".png", ".bmp", ".gif", ".jpeg"]
ext_extras = [".m3u", ".m3u8", ".wpl", ".pls", ".asx", ".smi", ".sami", ".xspf", ".txt", ".cue", ".log"]
ext_both = ext_music + ext_artwork
lists = [ext_music, ext_artwork, ext_both]


def file_copy(destination_location, path, file, source_location):
    # manual path joining is used because os.path.join returns the second argument when two absolute paths are joined
    # e.g. /foo and /bar are joined as /bar instead of /foo/bar
    # whereas this method creates /foo//bar which is then normalized by normpath to /foo/bar
    target_path = os.path.normpath(destination_location + os.path.sep + path[len(source_location):])
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
            print("Copy failed.")
            return 2  # Returned when the file was not found, but the copy failed.

    return 0  # Returned when the file already exists in destination_location.


def create_log(log_file, source_location, destination_location, operation, extras, sync):
    operation_list = ["Music only.", "Artwork only.", "Music and Artwork."]

    if not os.path.exists("Logs"):
        try:
            os.makedirs("Logs")
        except OSError:
            print("ERROR: Unable to create log folder.")
            return

    try:
        with open(os.path.join("Logs", log_file), "w+", encoding="UTF-8") as log:
            log.write("Source Location: " + source_location + "\n")
            log.write("Destination Location: " + destination_location + "\n")
            log.write("Chosen Operation: " + operation_list[operation] + "\n")
            log.write("Extra files: " + str(extras) + "\n")
            log.write("Folder-Sync: " + str(sync) + "\n\n")
    except OSError:
        print("ERROR: Unable to create log-folder or logfile.")
    return


def update_log(file, backup_result, log_file):
    with open(os.path.join("Logs", log_file), 'a', encoding="UTF-8") as log:
        if backup_result == 1:
            log.write(file + "\n")
        elif backup_result == 2:
            log.write("Unable to copy " + file + " because an error occurred.\n")
        elif backup_result == 3:
            log.write("Unable to create the appropriate folder for " + file + "\n")


def scan_and_backup(source_location, destination_location, operation, extras, sync, log):
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
                if ext not in ext_artwork or name[:8] != "AlbumArt" and name != "Thumbnail" and name != "Folder":
                    backup_result = file_copy(destination_location, path, file, source_location)

                    if log and backup_result > 0:
                        update_log(file, backup_result, log_file)

    if sync:
        scan_and_backup(destination_location, source_location, operation, extras, False, log)


def argument_validity():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("source", help="location containing the files to be backed up")
    parser.add_argument("destination", help="location where the files will be stored")
    parser.add_argument("action", metavar="action", choices=["m", "music", "a", "artwork", "c", "complete"],
                        help="m or music: audio files only, a or artwork: image files only, c or complete: both audio"
                             " and image files")
    parser.add_argument("-e", "--extras", action="store_true", dest="extras_flag", help="back-up extra files")
    parser.add_argument("-s", "--sync", action="store_true", dest="sync_flag",
                        help="synchronize source and destination folder")
    parser.add_argument("-l", "--log", action="store_true", dest="log_flag", help="save a log file")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.3.0")

    args = parser.parse_args()

    source = os.path.abspath(args.source)

    if not os.path.exists(source):
        print(source, "does not exist.")
        sys.exit()

    destination = os.path.abspath(args.destination)

    if args.action == "m" or args.action == "music":
        selection = 0
    elif args.action == "a" or args.action == "artwork":
        selection = 1
    else:
        selection = 2

    return source, destination, selection, args.extras_flag, args.sync_flag, args.log_flag


if __name__ == "__main__":
    source, destination, selection, extras_flag, sync_flag, log_flag = argument_validity()
    scan_and_backup(source, destination, selection, extras_flag, sync_flag, log_flag)
