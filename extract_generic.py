import re
import os

dir_string = "/data/pubchem/"
directory = os.fsencode(dir_string)

list_to_process = [
    {"filePrefix": "pc_descr_DefinedAtomStereoCount_value_", "regex": 'CID([0-9]*)_.*"([0-9]*)"'},
    {"filePrefix": "pc_inchikey2compound_", "regex": 'inchikey:([A-Z-]*).*compound:CID([0-9]*)'}
]

# NOTE: not used

for to_process in list_to_process:

    p = re.compile(to_process.get("regex"))

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith(to_process.get("filePrefix")) and filename.endswith(".ttl"): # TODO: change to ttl
            print(filename)

            for i, line in enumerate(open(dir_string + filename)):
                for match in re.finditer(p, line):
                    print('Value1: %s | Value2: %s' % (match.group(1), match.group(2)))

            continue
        else:
            continue

