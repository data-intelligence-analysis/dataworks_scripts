#Import Punctuation
#from string import punctuation

# Detect delimiter in file
# from detect_delimiter import detect
#    Copyright 2018   Tim McNamara

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import re
import os
import csv
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

###Future function add ons

#def console_ouput
#def remove_special_characters()
#def find_duplicates()
#def convert()
#def sys_exit() - when application closes

#Console Output
print ('OPERATING SYSTEM OF CHOICE')
print ('--------------------------')
print ("1. Windows\n")
print ("2. Mac OS X")
print ('---------------------------')
user = input('Enter the number for your OS (Operating System): ')
print('\n')
print ('CONVERT CSV FILE')
print ('--------------------------------------------------------')
convert = input('Convert header to preferred delimiter? (y/n): ')
print ('--------------------------------------------------------')
print('\n')
print ('SELECT DELIMITER')
print ('--------------------------------------------------------')
print ("1. PIPE\n")
print ("2. comma\n")
print ("3. TAB\n")  
print('----------------------------------------------------------')
file_delimiter = input ('Select the delimter to convert to, or choice of conversion  (Leave blank for false): ')
print('\n')

with open('config.txt', 'r', encoding='utf-8') as input:
    if user == str(1):
        read = input.readlines()
        let = read[0].strip()
        spec = let[let.index('C'):]
        #directory = read.strip()
        #label = print(directory)
        for file in os.listdir(spec):#("C:\\Users\\DO069840\\OneDrive - Cerner Corporation\\Desktop\\Correct_HeaderRows")
            if file.endswith(".txt") and not file.startswith(("config","README","LICENSE-2.0")):
                with open("header.txt","rt", encoding='utf-8') as infile, open("header_repaired.txt", "wt", encoding='utf-8') as outfile:
                    #Read Input File
                    reader = csv.reader(infile)
                    #reader = infile.read()
                    writer = csv.writer(outfile)
                    #If delimiter is Pipe
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')
                    #If delimiter is Comma
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')

                    ######Still in the works#####
                    #If delimiter is TAB 
                    conversionTAB = set('["/.!@#$%^&*[]|()-+={}:<>?'',`~]')

                    #Execute Loop
                    for row in reader:
                        #Replace special characters
                        #symbols = '[_"/.!@#$%^&*()[]-+={}:<>?/\'`~]'
                        #symbols +=
                        #new_string = re.sub(str(symbols), '', row)
                        #symbols=str(set(punctuation))
                        #Delimiter
                        delimiter = detect(str(row))

                        #Condition for Delimiter
                        if delimiter == '|':
                            #Replace special characters
                            new_row = ["".join('' if i in conversionComma else i for i in entry) for entry in row]
                            writer.writerow(new_row)
                                
                        elif delimiter == ',':
                            #Replace special characters
                            new_row2 = ["".join('' if i in conversionPipe else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(new_row2)
                        else:
                            print ("Unrecognized delimiter")
                                     
                        ######Still in the works#####
                        """elif delimiter == '\t':
                            #Replace special characters
                            print ("checkmark")
                            #new_row3 = ["".join('' if i in conversionTAB else i for i in entry) for entry in row]
                            #Write new header row in output file
                            #writer.writerow(new_row3)"""
                        
                    
                    print ("SUCCESS")
                    print ("----------------------------------------------------")
                    print ("\nSuccessfully removed special characters")
                    print ("\nOpen header_repaired.txt to view the header fields")
                    print ("-----------------------------------------------------")
                    print ("\n")
                    break
                            
                outfile.close()
                    
            elif file.endswith(".csv") and not file.startswith(("config","README","license-2.0")):
                with open("header.csv", "rt", encoding='utf-8') as infile, open("header_repaired.csv", "wt", encoding='utf-8') as outfile:

                    #Read Input File
                    reader = csv.reader(infile)

                    #Write to Output File
                    writer = csv.writer(outfile)

                    ####Special Characters
                    #If delmiter is Comma
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')
                    #If delimiter is Pipe
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')

                    ######Still in the works#####
                    #If delimiter is TAB
                    conversionTAB = set('["/.!@#$%^&*[]()|-+={}:<>?/\',`~]')
                    ###############################
                    
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
                        else:
                            print ("Unrecognized delimiter")

                        ######Still in the works#####
                        """elif delimiter == '\t':
                            #Replace special characters
                            new_row3 = ["".join('' if i in conversionTAB else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(new_row3)"""
                        
                            
                    print ("SUCCESS")
                    print ("----------------------------------------------------")
                    print ("\nSuccessfully removed special characters")
                    print ("\nOpen header_repaired.txt to view the header fields")
                    print ("-----------------------------------------------------")
                    print ("\n")
                    break
    
                    outfile.close()
            #finally:
            #    infile.close()
            #    outfile.close()             
    elif user==str(2):
        read = input.readlines()
        let = read[1].strip()
        spec2 = let[let.index('/'):]
        #index = read[read.index('C'):]
        #directory = read.strip()
        #label = print(directory)
        for file in os.listdir(spec2):#("C:\\Users\\DO069840\\OneDrive - Cerner Corporation\\Desktop\\Correct_HeaderRows")
            if file.endswith(".txt") and not file.startswith(("config","README","LICENSE-2.0")):
                with open("header.txt","rt", encoding='utf-8') as infile, open("header_repaired.txt", "wt", encoding='utf-8') as outfile:
                    #Read Input File
                    reader = csv.reader(infile)
                    #reader = infile.read()
                    writer = csv.writer(outfile)
                    #If delimiter is Pipe
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')
                    #If delimiter is Comma
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')

                    ######Still in the works#####
                    #If delimiter is TAB
                    conversionTAB = set('["/.!@#$%^&*[]()-+={}:<>?/\',`|~]')

                    #Execute Loop
                    for row in reader:
                        #Replace special characters
                        #symbols = '[_"/.!@#$%^&*()[]-+={}:<>?/\'`~]'
                        #symbols +=
                        #new_string = re.sub(str(symbols), '', row)
                        #symbols=str(set(punctuation))
                        #Delimiter
                        delimiter = detect(str(row))

                        #Condition for Delimiter
                        if delimiter == '|':
                            #Replace special characters
                            new_row = ["".join('' if i in conversionComma else i for i in entry) for entry in row]
                            writer.writerow(new_row)
                            
                        elif delimiter == ',':
                            #Replace special characters
                            new_row2 = ["".join('' if i in conversionPipe else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(new_row2)
                        else:
                            print ("Unrecognized delimiter")
                        ######Still in the works#####    
                        """elif delimiter == '\t':
                            #Replace special characters
                            new_row3 = ["".join('' if i in conversionTAB else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(new_row3)"""
                        
   
                    print ("SUCCESS")
                    print ("----------------------------------------------------")
                    print ("\nSuccessfully removed special characters")
                    print ("\nOpen header_repaired.txt to view the header fields")
                    print ("-----------------------------------------------------")
                    print ("\n")
                    break
                
                outfile.close()
                
            elif file.endswith(".csv") and not file.startswith(("config","README","license-2.0")):
                with open("header.csv", "rt", encoding='utf-8') as infile, open("header_repaired.csv", "wt", encoding='utf-8') as outfile:

                    #Read Input File
                    reader = csv.reader(infile)

                    #Write to Output File
                    writer = csv.writer(outfile)

                    ####Special Characters
                    #If delmiter is Comma
                    conversionPipe = set('["/.!@#$%^&*[]()-+={}:<>?/\'|`~]')
                    #If delimiter is Pipe
                    conversionComma = set('["/.!@#$%^&*[]()-+={}:<>?/\',`~]')

                    ######Still in the works#####
                    #If delimiter is TAB
                    conversionTAB = set('["/.!@#$%^&*[]()-+={}:<>?/\',`|~]')

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
                        else:
                            print ("Unrecognized delimiter")
                            
                        ######Still in the works#####
                        """elif delimiter == '\t':
                            #Replace special characters
                            new_row3 = ["".join('' if i in conversionTAB else i for i in entry) for entry in row]
                            #Write new header row in output file
                            writer.writerow(new_row3)"""
                        
                            
                    print ("SUCCESS")
                    print ("----------------------------------------------------")
                    print ("\nSuccessfully removed special characters")
                    print ("\nOpen header_repaired.txt to view the header fields")
                    print ("-----------------------------------------------------")
                    print ("\n")
                    break
                                   
            #finally:
            #    infile.close()
            #    outfile.close()
                outfile.close()
    else:
        print("Wrong input for Operating Sytem")

## Finding Duplicates
with open('header_repaired.txt','rt', encoding='utf-8') as infile, open('duplicate.txt','w', encoding='utf-8') as outfile:
    #readerComma = csv.reader(infile, delimiter=(","))
    #readerPipe = csv.reader(infile, delimiter=("|"))
    reader = csv.reader(infile)
    #Additional Notes
    '''for string in reader:
        delimiter = detect(str(string))
        if delimiter ==",":
            duplicates_list =[]
            print("string")
            for read in string:
                duplicates_list.extend(read)
            duplicates =[i for i in duplicates_list]
            seen = set()
            count = 0
            for m in duplicates:
                if m in seen:
                    outfile.write(str(m.split(",")))
                    count+=1
                    continue
                seen.add(m)
            print("Duplicates found: ",count)'''
    '''duplicates_list = []
    lines = [line for line in readerComma]
    for read in lines:
        duplicates_list.extend(read)
    duplicates = [i for i in duplicates_list]
    seen = set()
    count = 0

    for m in duplicates:
        if m in seen:
            outfile.write(str(m.split(",")))
            count+=1
            #print(m)
            continue
        seen.add(m)
    print("Duplicates found: ",count)

    duplicates_list2 = []
    lines = [line for line in readerPipe]
    for read in lines:
        duplicates_list2.extend(read)
    duplicates2 = [i for i in duplicates_list2]
    seen = set()
    count = 0
    for m in duplicates2:
        if m in seen:
            outfile.write(str(m.split(",")))
            count+=1
            #print(m)
            continue
        seen.add(m)
    print("Duplicates found: ",count)'''

    for read in reader:
        delimited = detect(str(read))
        #print (delimited)
        #print (delimited)
        if delimited ==",":
            #duplicates_list =[]
            #print("stringComma")
            #for reader2 in read:
                #duplicates_list.extend(reader2)
            duplicates =[i for i in read]
            seen = set()
            count = 0
            for m in duplicates:
                if m in seen:
                    outfile.write(str(m.split(",")))
                    count+=1
                    continue
                seen.add(m)
            print ("CHECK FOR DUPLICATES")
            print ("-------------------------")
            print ("Duplicates found: ", count)
            print ("-------------------------")
            print("\n")
            if count > 0:
                print("\nOpen duplicate.txt to view duplicate data fields")
                print ("-------------------------------------------------")
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
            #print(spl)
            #print(string)
            count2 = 0
            for m in spl:
                if m in seen:
                    outfile.write(str(m))
                    count2+=1
                seen.add(m)
            print ("Check For Duplicates")
            print ("-------------------------")
            print ("Duplicates found: ", count2)
            print ("-------------------------")
            print("\n")
            if count2 > 0:
                print("\nOpen duplicate.txt to view duplicate data fields")
                print ("-------------------------------------------------")
            break
    
    #if give == str(exit):
    outfile.close()

####WORK ON ERROR HANDLING AND EXCEPTIONS
#Convert file to delimiter of choice 
if convert == "y" or convert == "Y":
    print ("CONVERSION")
    print ("-----------------------------")
    print ("Start Converting file...\n")
    #op = open('header_repaired.txt')
    sniffer = csv.Sniffer()
    buffer = 32#bytes
    ##class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
    with open('header_repaired.txt', 'rt', encoding='utf-8-sig') as input_file, open('header_converted.txt','w',newline='',encoding='utf-8-sig') as output_file:
        if (file_delimiter == str(1) and convert == "y") or (file_delimiter == str(1) and convert == "Y"):
            #sniffs comma delimited files by default
            delim = sniffer.sniff(input_file.read(buffer))
            input_file.seek(0)
            
            #delim.delimiter - selects or sniffs comma delimiter by default
            string = str(delim.delimiter)
            
            read = csv.DictReader(input_file, delimiter = string)
            keyValue = read.fieldnames
            writer = csv.DictWriter(output_file, keyValue, delimiter='|', quoting=csv.QUOTE_NONE)
            writer.writeheader()
            data = {key: value for key, value in input_file if key in read}
            writer.writerows(data)
            print ("Conversion complete")
            print ("--------------------------")
        elif (file_delimiter == str(2) and convert == "y") or (file_delimiter == str(2) and convert == "Y"):
            #Returns input file as string
            read = input_file.readline()
            delim = sniffer.sniff(read.split('\n')[0][:512], delimiters=['|','\t',':',';'])
            string = str(delim.delimiter)
            input_file.seek(0)
            DictRead = csv.DictReader(input_file, delimiter=string)
            keyValue = DictRead.fieldnames 
            writer = csv.DictWriter(output_file, keyValue, delimiter=',',quoting=csv.QUOTE_NONE)
            writer.writeheader()
            writer.writerows(DictRead)
            print ("Conversion complete")
            print ("--------------------------")
        elif (file_delimiter == str(3) and convert == "y") or (file_delimiter == str(3) and convert == "Y"):
            #reads one line per iteration in the input_file as a string
            read = input_file.readline()

            #reads input_file and puts values (multiple lines) in list 
            #read2 = input_file.readlines()
            
            detect_delimiter = sniffer.sniff(read.split('\n')[0][:512], delimiters=['|',',',':',';'])
            string = str(detect_delimiter.delimiter)
            
            #separates elements in single line string into a list 
            spliter = read.split(string)

            #turns list to a dictionary adding key value pair
            alphaDict = dict.fromkeys(spliter, 0)


            input_file.seek(0)
            field_names = alphaDict.keys()
            #DictRead = csv.DictReader(input_file, delimiter=string)
            #keyValue = DictRead.fieldnames
            writer = csv.DictWriter(output_file, fieldnames=field_names, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar= ' ') 
            writer.writeheader()
            
            #Creates a dictionary and writes key, value pairs
            #data = {key: value for key, value in alphaDict.items() if key in field_names}
            try:
                writer.writerow(field_names)
            except AttributeError:
                pass
            
            print ("Conversion complete")
            print ("--------------------------")
        else:
            print ("Wrong input\n")
            print ("Conversion not completed")
            print ("--------------------------")
                                                                                                                                                    
elif convert == "n" or convert == "n":
    print ("No header to convert")
    print ("-----------------------")
    try:
        open('header_converted.txt', 'w').close()
    except Exception as l:
        print(l)
else:
    print ("Wrong input for preferred delimiter")
    print ("--------------------------------------")

   
#System Exit - Erase all contents
close = "Application is closed"
print ('\n')
print ("EXIT")
print ('----------------------')
print (close)
print ('----------------------')
if close:
   try:
       open('header.txt', 'w').close()
       sys.exit()
   except Exception as e:
       print(e)


