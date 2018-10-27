import re
import os
import csv

dir_string = "/data/pubchem/ddl/inchikey/"
directory = os.fsencode(dir_string)

file_prefix = "pc_inchikey2compound_"
regex_str  = 'inchikey:([A-Z-]*).*compound:CID([0-9]*)'

p = re.compile(regex_str)

cid_needing_inchikey = {}
# Get all Wikidata URI with CID that needs a InChiKey
# And put everything in a Hash
with open('/home/vemonet/sandbox/wikimedia/extract_pubchem/wikidataId-pubchem-without-inchikey.csv', newline='') as csvfile:
     iterate_csv = csv.reader(csvfile, delimiter=',', quotechar='|')
     # Iterate over every CID that needs a InChiKey
     for row in iterate_csv:
         cid_needing_inchikey[row[1]] = row[0]
         # Value is the Wikidata ID


# Iterate over every line in each file and check if this line needs to be extracted to add the InChiKey
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.startswith(file_prefix) and filename.endswith(".ttl"):
        print(filename)

        for i, line in enumerate(open(dir_string + filename)):
            # Extract InChiKey and CID from each line
            for match in re.finditer(p, line):

                if match.group(2) in cid_needing_inchikey:
                    # Getting Wikidata ID from cid_needing_inchikey
                    print(cid_needing_inchikey[match.group(2)] + ",P235," + match.group(1) + ",S248,Q278487,S813,+2018-10-27T00:00:00Z/11")

        continue
    else:
        continue



#/home/vemonet/sandbox/wikimedia/extract_pubchem/wikidataId-pubchem.csv
# Here we have a nice hash with stereocount for CID

# How do you add the stereocount?
#                           statedIn pubchem
#"Q22124656,P235,3,S248,Q278487,S813,+2018-10-27T00:00:00Z/11"
