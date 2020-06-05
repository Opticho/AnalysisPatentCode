RoughCoding for USPTO patent search
===================================
Library Conjugation

## 0. Introduction   
    I just wan't to get the patent summary(title texts and pdf summary files) from the USPTO patent site.   
    this is the code that I conjugate with the libraries from Python, crowling the html source and send http messages to get information.

## 1. Requirements  
---------------
    - Python == 3.6.5   
    - requests == 2.18.4   
    - beautifulsoup4 == 4.6.0   
    - pypdf2 == 1.26.0

## 2. Arguments   
------------
    - "-i" : Give some command (search, compare, merge, download)   
    - "-q" : Input some Query (just AND and OR operator can available)   
    - "-fp" : change txt save path   
    - "-pp" : change pdf save path   
    
    *Default: -q = 'TTL/(Ultrasonic OR Ultrasound OR Megasound OR Megasonic OR acoustic) AND TTL/(cover OR cap OR case OR covering OR mantle OR hood OR sheet OR shutter OR vinyl OR cowl OR lid OR mulch OR seal)',    
              -fp = os.path.join(path, "patent_search"),    
              -pp = pdf_path = os.path.join(path, "patent_pdf"),    
              note that file directory will be created if there NOT exists directory

## 3. Simple Example   
-----------------
    Python uspto_search.py -i search
    
    Python uspto_search.py -i search -q "TTL/(something OR something ..) OR .."
    (note that it just uses TTL and OR and AND operator, others will occurs error)
    
    Python uspto_search.py -i compare
    (note that it will compare the "now day" text file with the "yester day" text file.   
    And renew pdf files when the new patent appears)
    
    Python uspto_search.py -i download
    (it will download pdf summary file, using default query)

