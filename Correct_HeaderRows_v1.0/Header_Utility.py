#Import replace library
import re
#Import os library
import os
#Import csv library
import csv
#Import String
import string
#Import System
import sys

from collections import Counter
import string
import copy
from typing import Optional, List

SILLY_DELIMITERS = frozenset(string.ascii_letters + string.digits + '.')

def same(sequence):
    elements = iter(sequence)
    try:
        first = next(elements)
    except StopIteration:
        return True
    for el in elements:
        if el != first:
            return False
    return True

def detect(text:str, default:Optional[str]=None, whitelist:Optional[List[str]]=None,
blacklist:Optional[List[str]]=SILLY_DELIMITERS) -> Optional[str]:
    r"""
    Detects the delimiter used in text formats such as CSV and its
    many counsins.

    >>> detect(r"looks|like|the vertical bar\nis|the|delimiter\n")
    '|'

    `detect_delimiter.detect()` looks at the text provided to try to
    find an uncommon delimiter, such as `' for whatever reason.

    >>> detect('looks\x10like\x10something stupid\nis\x10the\x10delimiter')
    '\x10'

    When `detect()` doesn't know, it returns `None`:

    >>> text = "not really any delimiters in here.\nthis is just text.\n"
    >>> detect(text)

    It's possible to provide a default, which will be used in that case:

    >>> detect(text, default=',')
    ','

    By default, it will prevent avoid checking alpha-numeric characters
    and the period/full stop character ("."). This can be adjusted via
    the `blacklist` parameter.

    If you believe that you know the delimiter, it's possible to provide
    a list of possible delimiters to check for via the `whitelist` parameter.
    If you don't provide a value, `[',', ';', ':', '|', '\t']` will be checked.
    """
    if whitelist:
        candidates = whitelist
    else:
        candidates = list(',;:|\t')

    sniffed_candidates = Counter()
    likely_candidates = []

    lines = []
    # todo: support streaming
    text_ = copy.copy(text)
    while len(lines) < 5:
        for line in text_.splitlines():
            lines.append(line)

    for c in candidates:
        fields_for_candidate = []

        for line in lines:
            for char in line:
                if char not in blacklist:
                    sniffed_candidates[char] += 1
            fields = line.split(c)
            n_fields = len(fields)

            # if the delimiter isn't present in the
            # first line, it won't be present in the others
            if n_fields == 1:
                break
            fields_for_candidate.append(n_fields)

        if not fields_for_candidate:
            continue

        if same(fields_for_candidate):
            likely_candidates.append(c)


    # no delimiter found
    if not likely_candidates:
        if whitelist is None and sniffed_candidates:
            new_whitelist = [char for (char, _count) in sniffed_candidates.most_common()]
            return detect(text, whitelist=new_whitelist) or default
        return default

    if default in likely_candidates:
        return default

    return likely_candidates[0]

#Select the type of operating system you are running the script o
print ("1. Windows\n")
print ("2. Mac OS X")
print ('------------')
user = input('Enter the number for your OS (Operating System): ')


#Remove Special Characters
with open('config.txt', 'r', encoding='utf-8') as input: #config.txt contains directory (path) to folder
    #read path
    if user == str(1):
        read = input.readlines()
        let = read[0].strip()
        #read entire directory
        spec1 = let[let.index('C'):]

        #Using os library to read and open files in directory
        for file in os.listdir(spec1):#("directory is in config.txt e.g.")
            if file.endswith(".txt") and not file.startswith(("config","README","LICENSE-2.0")):
                with open("header.txt","rt", encoding='utf-8') as infile, open("header_repaired.txt", "wt", encoding='utf-8') as outfile:
                    #Read Input File
                    reader = csv.reader(infile)
                    #Write to output file
                    writer = csv.writer(outfile)
                    #If delimiter is pipe
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')
                    #If delimiter is Comma
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')

                    #Execute Loop
                    for row in reader:

                        delimiter = detect(str(row))

                        #Condition for Delimiter
                        if delimiter == '|':
                            #Replace special characters
                            new_row = ["".join('' if i in conversionComma else i for i in entry) for entry in row]
                            writer.writerow(new_row)

                        elif delimiter == ',':
                            #Replace special characters
                            new_row2 = ["".join('' if i in conversionPipe else i for i in entry) for entry in row]
                            writer.writerow(new_row2)

            elif file.endswith(".csv"):
                with open("speciality.csv", "rt", encoding='utf-8') as infile, open("repaired.csv", "wt", encoding='utf-8') as outfile:

                    #Read Input File
                    reader = csv.reader(infile)

                    #Write to Output File
                    writer = csv.writer(outfile)

                    ####Special Characters
                    #If delmiter is pipe
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')
                    #If delimiter is Comma
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')

                    #Execute Loop
                    for row in reader:
                        delimiter = detect(str(row))
                        if delimiter == '|': ###Unable to "," fix problem if there is one occurrence of the character
                            #Replace special characters
                            newrow = ["".join('' if i in conversionComma else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(newrow)
                        elif delimiter == ',':
                            #Replace special characters
                            newrow2 = ["".join('' if i in conversionPipe else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(newrow2)
        outfile.close()

        print("Successfully removed special characters")
        print("\nOpen header_repaied.txt to view the corrected header fields")

        print("\n")

    elif user == str(2):
        read = input.readlines()
        let = read[1].strip()
        #read entire directory
        spec2 = let[let.index('/'):]

        #Using os library to read and open files in directory
        for file in os.listdir(spec2):#("directory is in config.txt e.g.")
            if file.endswith(".txt") and not file.startswith(("config","README","LICENSE-2.0")):
                with open("header.txt","rt", encoding='utf-8') as infile, open("header_repaired.txt", "wt", encoding='utf-8') as outfile:
                    #Read Input File
                    reader = csv.reader(infile)
                    #Write to output file
                    writer = csv.writer(outfile)
                    #If delimiter is pipe
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')
                    #If delimiter is Comma
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')

                    #Execute Loop
                    for row in reader:

                        delimiter = detect(str(row))

                        #Condition for Delimiter
                        if delimiter == '|':
                            #Replace special characters
                            new_row = ["".join('' if i in conversionComma else i for i in entry) for entry in row]
                            writer.writerow(new_row)

                        elif delimiter == ',':
                            #Replace special characters
                            new_row2 = ["".join('' if i in conversionPipe else i for i in entry) for entry in row]
                            writer.writerow(new_row2)

            elif file.endswith(".csv"):
                with open("speciality.csv", "rt", encoding='utf-8') as infile, open("repaired.csv", "wt", encoding='utf-8') as outfile:

                    #Read Input File
                    reader = csv.reader(infile)

                    #Write to Output File
                    writer = csv.writer(outfile)

                    ####Special Characters
                    #If delmiter is pipe
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')
                    #If delimiter is Comma
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')

                    #Execute Loop
                    for row in reader:
                        delimiter = detect(str(row))
                        if delimiter == '|': ###Unable to "," fix problem if there is one occurrence of the character
                            #Replace special characters
                            newrow = ["".join('' if i in conversionComma else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(newrow)
                        elif delimiter == ',':
                            #Replace special characters
                            newrow2 = ["".join('' if i in conversionPipe else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(newrow2)
        outfile.close()

        print("Successfully removed special characters")
        print("\nOpen header_repaied.txt to view the corrected header fields")

        print("\n")


#Finding Duplicates
with open('header_repaired.txt','rt', encoding='utf-8') as infile, open('duplicates.txt','w', encoding='utf-8') as outfile:
    #readerComma = csv.reader(infile, delimiter=(","))
    #readerPipe = csv.reader(infile, delimiter=("|"))
    reader = csv.reader(infile)

    for read in reader:
        delimited = detect(str(read))
        if delimited ==",":
            duplicates =[i for i in read]
            seen = set()
            count = 0
            for m in duplicates:
                if m in seen:
                    outfile.write(str(m.split(",")))
                    count+=1
                    continue
                seen.add(m)
            print("Duplicates found: ",count)
            print("\n")
            if count > 0:
                print("\nOpen duplicate.txt to view duplicate data fields")
            break
        elif delimited =="|":
            #for reader2 in read:
                #duplicates_list.extend(reader2)
            duplicates2 =[i for i in read]
            seen = set()
            string = duplicates2
            deli = string[-1]
            deli+="|"
            stri =str(deli)
            spl=stri.split('|')
            count2 = 0
            for m in spl:
                if m in seen:
                    outfile.write(str(m))
                    count2+=1
                seen.add(m)
            print("Duplicates found: ",count2)
            print("\n")
            if count > 0:
                print("\nOpen duplicate.txt to view duplicate data fields")
            break
    outfile.close()

#System Exit - Erease all contents
close = "Application is closed"
print(close)
print('-----------------------')
if close:
    try:
        open('header.txt','w').close()
        sys.exit()
    except Exception as e:
        print(e)
