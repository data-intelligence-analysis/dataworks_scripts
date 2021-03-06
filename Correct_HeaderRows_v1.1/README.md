# <u>Header_Utility</u>
A standard script to remove special characters from the data fields and identify duplicate data fields within the header row of the raw data.

**NOTICE**: Please **DO NOT** modify this file or the contents in this repository directly. Use the two methods provided below
to contribute to the program:

## First Method
* |OK| This is good.
* |FIXME| Please fix me.

## Second Method
Go to the support section to contact developer of any inquiries you might have
<u></u>

## <u> Summary</u>
Header_Utility is a python script that removes special characters from and identify duplicate data within the header row retrieved from the client's raw data. It detects the delimiter, either a comma(',') or pipe(|), within the header row of a text or csv file and removes the special characters as well as identify duplicates, which ultimately corrects and cleans the fields in the header row for the data architect during the data ingestion process without any errors pertaining to unnecessary characters and data fields in the header. 

## Table of Contents

1. [Background](#background)

2. [Requirements](#requirements)

3. [Installation](#installation)

4. [Usage](#usage)

5. [Support](#support)

6. [Roadmap](#roadmap)

7. [License](#license)


## Background
To eliminate time spent on manually searching, removing, and identifying special characters and duplicate data fields within the header of the raw data, the script removes those special characters automatically for the data architect and identifies duplicates whiles maintaining the structure and integrity of the header.

## Requirements
 1. Python 3.0 and later releases (Python 3.x.x). 
 2. Command Prompt (cmd).
 3. Text editor (e.g. Notepad++, Notepad).
 4. Must be installed and used on a windows machine (Windows (C:)).
 5. Can be used on Macintosh (Mac OS X) machines as well. Paths and directories in config.txt must be defined with forward slashes (/) as opposed to backward slashes.


## Installation

This script requires Python 3.0 or any other of the Python 3 releases (Python 3.x.x), to execute, and it must be installed on your windows machine. 

The latest release can be downloaded from https://www.python.org/ 

Installation guide for windows can be found on https://phoenixnap.com/kb/how-to-install-python-3-windows
Installation guide for Macintosh can be found on https://docs.python.org/3/using/mac.html


## Usage

Files generated in the Correct_HeaderRows Folder:

1. <b>config.txt</b> -- contains the directory (path) to where the files are located for example : C:\Users\.....\.....\Correct_HeaderRowsv1.1 for windows. You must define your directory where the file is located before the script can read the file.
2. <b>LICENSE-2.0.txt</b> --contains the [Apache License](http://www.apache.org/licenses/LICENSE-2.0)Version 2.0 that governs the use of the detect_delmiter module in the code. 
3. <b>header.txt (header.csv)</b> -- This is the input file containing **ONLY** the header_row of the raw data.
4. <b>header_repaired.txt</b> (header_repaired.csv) -- This is the output file that would be generated that contains the ccorrected version of the header row without any uneccessary special characters. 
5. <b>duplicates.txt</b> -- This is the output file that contains the data field duplicates found in the header_repaired.txt file.
6. <b>header_converted.txt</b> -- This the output file that contains the header converted to the choice of delimiter

<b>Operation</b>: 
The user must have access to the raw data, usually in .csv or .txt format, to retrieve the data field header. Once the header row has been retrieved, it must be copied and pasted on to the input file called header.txt located in the Correct_HeaderRows folder on your windows machine and then save the file (header.txt). Be sure to check if the header row has a delimiter (this program reads the common delimiters comma (",") and pipe ("|")). Thereafter, you must open command prompt and navigate to the Correct_HeaderRows folder as described in the <b>installation usage</b> section below and then run


<b>Installation usage</b>: 

Once Python 3.0 has been installed, navigate to your Correct_HeaderRows folder, containing the RemoveSpecialCharacters.py, by using the 'cd' command. Thereafter, the program can be launched using the 'python3' argument as follows:


<b>Windows</b>
```Command Prompt
cd C:\Users\....\.....\Correct_HeaderRows_v1.1
C:\Users\....\.....\Correct_HeaderRows>python3 Header_Utility.py
```

<b>Mac OS X</b>
```Terminal
~ <User_name>$ cd /Users/...../...../Correct_HeaderRows_v1.1
Correct_HeaderRows_v1.1 <User_name>$ python3 Header_Utility.py
```

## Support
For any help or assistance please address the following contact information 

You can contact developer via email on the following: 
	1. Email: menace3780@gmail.com 
	2. Name: Dennis Osafo


## Roadmap

This script will keep updating based on how many test cases of special characters are found in the header row of the Client's data in the future. As a result, the database of special characters will keep updating to satisfy all conditions in eliminating unnecessary characters from the data fields in the header.

Version 1.1 would include an encoding function that converts all files to UTF8 into the script; the ability for the user to convert file to delimiter (PIPE ("|"), comma (","), TAB ("\t"))


## License

The detect_delimiter module used in this software is Copyright 2018 owned by Tim McNamara and is licensed under the Apache License, Version 2.0 (the "License"). You may obtain a copy of the License at:

[Detect Delimiter] (http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

## Release (Version)
v1.0 - Reoves special characters and identify duplicates for PIPE and comma delimited header (fieldnames) file.

v1.1 - In addition to removing special characters and identifying duplicates, files are converted to  UTF8, and convert header to delimiter of choice either PIPE ('|'), comma (','), or TAB ('\t'). New file added header_converted.txt depending on choice of file.


