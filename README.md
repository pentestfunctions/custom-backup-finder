
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

## Contributing :raised_hands:
Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/pentestfunctions/custom-backup-finder.py/issues).

## License :page_facing_up:
This project is [MIT](https://github.com/pentestfunctions/custom-backup-finder.py/blob/main/LICENSE) licensed.
