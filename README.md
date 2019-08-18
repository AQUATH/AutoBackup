# AutoBackup

A simple backup script suited to music libraries. It is able to backup audio files, artwork and misc. files, such as playlists used in music libraries.

## Getting Started

### Prerequisites

To use AutoBackup you only need Python 3. No installation needed.

### Using AutoBackup

Call AutoBackup as follows:
```
$ python3 AutoBackup.py <source> <destination> <music | artwork> [options]
```
where these are mandatory arguments:
```
source: source folder
destination: destination folder
<music | artwork>:
-m or --music to backup audio files
-a or --artwork to backup artwork (image) files
-ma or -c or --complete to backup both
```
while these are optional:
```
options:
-e or --extras to backup files that may be present in a music library, besides audio and artwork
-s or --sync to synchronize source and destination folders. By using this option both folders will contain the same files when AutoBackup finishes its execution.
-l or --log to save a log file in the same directory as AutoBackup.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
