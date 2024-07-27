
# Custom Backup Finder Script :floppy_disk:

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Issues](https://img.shields.io/github/issues/pentestfunctions/custom-backup-finder.py)
![Forks](https://img.shields.io/github/forks/pentestfunctions/custom-backup-finder.py)
![Stars](https://img.shields.io/github/stars/pentestfunctions/custom-backup-finder.py)

## Overview :mag_right:
`custombackup.py` is a Python script designed to generate permutations of common backup file names and extensions. It's an essential tool for security professionals and developers in identifying potential backup files that may have been left exposed on web servers.

## Features :star2:
- Generates permutations of common archive names and file extensions.
- Includes a variety of file extensions, such as `.zip`, `.tar`, and `.sql`.
- Allows for custom date range input for generating date-based backup names.
- Outputs permutations to a text file for easy use.

## Installation :wrench:
Clone the repository using:
```bash
git clone https://github.com/pentestfunctions/custom-backup-finder.git
```

## Usage :computer:
1. Run the script:
   ```python
   python custombackup.py
   ```
2. Enter the desired domain name when prompted.
3. The script will generate a file `custom_backup_list.txt` with possible backup file names.

## Example 🖥️
```bash
backup_dev.bak
backup_dev.dump
backup_dev.gzip
backup_dev.bz2
backup_dev.gz
hacknex_2024.zip
hacknex_2024.tar
hacknex_2024.tar.gz
hacknex_2024.tgz
hacknex_2024.tar.bz2
hacknex_2024.tar.xz
```


## Custom Logfinder
1. Example custom commands with the input domain hacknex.us

```bash
202407211812_log.txt.log
202407211812_log.txt.txt
202407211812_log.txt.sql
hacknex.us_202407211812.log.log
hacknex.us_202407211812.log.txt
hacknex.us_202407211812.log.sql
www.hacknex.us_202407211812.log.log
www.hacknex.us_202407211812.log.txt
www.hacknex.us_202407211812.log.sql
```

## Other formats

It is worth noting to also look for custom backups with this file name scheme
`dbname_20221015_202410.sql.gz`

wherein the dbname would be the database name if you have found it already.

## Contributing :raised_hands:
Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/pentestfunctions/custom-backup-finder.py/issues).

## License :page_facing_up:
This project is [MIT](https://github.com/pentestfunctions/custom-backup-finder.py/blob/main/LICENSE) licensed.
