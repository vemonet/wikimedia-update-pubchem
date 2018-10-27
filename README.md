# Wikimedia Hackathon

https://phabricator.wikimedia.org/T208036

## Download PubChem

A few commands to download different parts of PubChem FTP can be found in download_pubchem.sh

## Adding inchikey 

* get all items without inchikey

```sql
SELECT ?wikidata ?pubchem WHERE {
  ?wikidata wdt:P662 ?pubchem .
  filter not exists { 
    ?wikidata wdt:P235 ?inchikey
  }
}
```

* Download all inchikey to compound files

```shell
wget -r -A ttl.gz -nH --cut-dirs=2 ftp://ftp.ncbi.nlm.nih.gov/pubchem/RDF/inchikey/pc_inchikey2compound_*wget -r -A ttlwget -r -A ttl.gz -nH --cut-dirs=2 ftp://ftp.ncbi.nlm.nih.gov/pubchem/RDF/inchikey/pc_inchikey2compound_*.gz -nH --cut-dirs=2 ftp://ftp.ncbi.nlm.nih.gov/pubchem/RDF/inchikey/pc_inchikey2compound_*
```



## SPARQL queries

* Get all Chemicals with a PubChem ID but no InChIKey

```sql
SELECT ?wikilabel ?pubchem WHERE {
  ?wikidata wdt:P662 ?pubchem .
  filter not exists { 
    ?wikidata wdt:P235 ?inchikey
  }
  BIND(strafter(str(?wikidata), "www.wikidata.org/entity/") AS ?wikilabel)
}
```



* Exploratory query 

```sql
SELECT ?p ?propLabel ?o WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } 

  #wd:Q153 ?p ?o . # Get Ethanol
  #?s wdt:P662 "702" . # get ethanol by PubChem ID
  #?s wdt:P235 "LFQSCWFLJHTTHZ-UHFFFAOYSA-N" . # Search ethanol by InChiKey
  #?s wdt:P274 "C₂H₆O" . # Search Ethanol by Chemical Formula

  #?s wdt:P662 "134797139" . # Get one of the last PubChem ID
  #?s wdt:P235 "XZHCKCNVYAHADQ-UHFFFAOYSA-N" . # Search by InChiKey
  ?s wdt:P274 "C₂₃H₃₀ClN₅O₃S" . # Search by Chemical Formula
  
  ?s ?p ?o .
  ?prop wikibase:directClaim ?p . #resolve prop Label 
  FILTER ( ?p != schema:description )
  FILTER ( ?p != rdfs:label )
  FILTER ( ?p != skos:altLabel )
}
```

