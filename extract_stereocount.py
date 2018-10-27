import re
import os
import csv

dir_string = "/data/pubchem/"
directory = os.fsencode(dir_string)

file_prefix = "pc_descr_DefinedAtomStereoCount_value_"
regex_str  = 'CID([0-9]*)_.*"([0-9]*)"'

p = re.compile(regex_str)

cid_to_stereocount = {}

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.startswith(file_prefix) and filename.endswith(".ttl"): # TODO: change to ttl
        print(filename)

        for i, line in enumerate(open(dir_string + filename)):
            for match in re.finditer(p, line):
                #print('CID: %s | Stereo: %s' % (match.group(1), match.group(2)))
                cid_to_stereocount[match.group(1)] = match.group(2)

        continue
    else:
        continue

print(cid_to_stereocount)

# Get Wikidata URI related to the CID
with open('/home/vemonet/sandbox/wikimedia/extract_pubchem/wikidataId-pubchem.csv', newline='') as csvfile:
     iterate_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in iterate_csv:
         print()
         print(row[0]) # URI
         print(row[1]) # CID
         print(', OOOAAAA '.join(row))

#/home/vemonet/sandbox/wikimedia/extract_pubchem/wikidataId-pubchem.csv
# Here we have a nice hash with stereocount for CID

# How do you add the stereocount?
#                           statedIn pubchem
"Q22124656,P235,Q6581097,S248,Q278487,S813,+2018-10-27T00:00:00Z/11"
