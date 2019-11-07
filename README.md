# AutoBackup

A simple backup script aimed for music libraries. It is able to back-up audio files, artwork and other files
used in music libraries, such as playlists, cue files, logs, etc.

## Getting Started

### Prerequisites

Python 3.2+

### Using AutoBackup

Run AutoBackup as follows:
```
$ python3 autobackup.py <source> <destination> <music | artwork> [options]
```
where these are mandatory arguments:
```
source          location containing the files to be backed up
destination     location where the files will be stored

music | artwork:
m or music      backup audio files only
a or artwork    backup artwork (image) files only
c or complete   backup both audio and artwork
```
while these are optional:
```
options:
-h or --help    show help message and exit
-e or --extras  backup files that may be present in a music library, besides audio and artwork
-s or --sync    synchronize source and destination folders
-l or --log     save a log file in the same directory as autobackup.py
-v or --version show program's version number and exit
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
