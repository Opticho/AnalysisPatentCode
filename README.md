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

    Python uspto_search.py -i search -q "TTL/(something OR something ..) OR .." -fp "text path" -pp "pdf path"

## 4. Results(Default)
-------------
    1 10,639,008 Support and cover structures for an ultrasound probe head 
    2 10,595,823 Internal ultrasound assembly fluid seal 
    3 10,584,606 Turbomachine case comprising an acoustic structure and an abradable element 
    4 10,574,208 Acoustic wave filters with thermally conductive sheet 
    5 10,549,661 Acoustic seal for vehicle seat 
    6 10,543,687 Ultrasonic maintenance cap 
    7 10,499,158 Electro-acoustic transducer with radiating acoustic seal and stacked magnetic circuit assembly 
    8 10,498,310 Protective cover for an acoustic wave device and fabrication method thereof 
    9 10,415,242 Gasket and drop seal associated with acoustic panel capable of impeding flow of sound into cavity of drop seal 
    10 10,413,314 Ultrasonic surgical instrument with activation member pair and slidable cover 
    11 10,398,409 Transducer cover, method for forming the cover, and ultrasonic medical instrument with the cover 
    12 10,398,288 Hood for ultrasonic endoscope and ultrasonic endoscope 
    13 10,293,575 Process for producing ultrasonic seal, and film structures and flexible containers with same 
    14 10,277,989 Opto-acoustic transducer and cover glass 
    15 10,264,374 Ball and socket connection with an acoustic seal and mounting interface for a hearing assistance device 
    16 10,232,804 Acoustic protection cover for encapsulating a motor vehicle component 
    17 10,220,474 Method and apparatus for gas turbine combustor inner cap and high frequency acoustic dampers 
    18 10,219,054 Protective member for acoustic component and waterproof case 
    19 10,200,802 Inverted button cap in acoustic transducer 
    20 10,149,661 Probe cover, ultrasonic probe, and ultrasonic image display apparatus 
    21 10,142,748 Thermoformed acoustic seal 
    22 10,129,623 Electronic device having covering substrate carrying acoustic transducer and related technology 
    23 10,110,981 Vibro acoustic cover using expanded PTFE composite 
    24 9,998,814 Acoustic sensor wind cap and a corresponding acoustic sensor 
    25 9,993,967 Method for joining a sealing seam of a tubular bag packaging by means of an ultrasound applicator and longitudinal seal joining device for use with said method 
    26 9,980,700 Ultrasound apparatus cover 
    27 9,980,065 Ball and socket connection with an acoustic seal and mounting interface for a hearing assistance device 
    28 9,975,292 Retrofit of a form-fill-seal machine heat station with an advanced ultrasonic welding kit 
    29 9,973,169 Surface acoustic wave filter with a cap layer for improved reliability 
    30 9,937,659 Ultrasonic edge sealing of sheet molding compound carrier film 
    31 9,908,485 Acoustic barrier assembly with acoustic seal 
    32 9,874,842 Sheet determination apparatus using ultrasonic wave transmitting unit or reception unit 
    33 9,667,226 Surface acoustic wave device and filter with additional covering films 
    34 9,662,829 Retrofit of a form-fill-seal machine heat station with an advanced ultrasonic welding kit 
    35 9,641,938 Electro-acoustic transducer with radiating acoustic seal and stacked magnetic circuit assembly 
    36 9,605,328 Surface contouring of a weld cap and adjacent base metal using ultrasonic impact treatment 
    37 9,541,431 Ultrasonic flow meter unit with an insulating damping member covering the ultrasonic transducers, a measuring circuit and lead wires 
    38 9,496,695 Electrical outlet box acoustic seal 
    39 9,436,161 Musical watch case with improved acoustic performance 
    40 9,433,271 Protective cover with an acoustic isolation mechanism 
    41 9,362,799 Acoustic covering for a generator set enclosure with pressure sensitive adhesive 
    42 9,309,666 Wall covering for thermal and acoustic comfort 
    43 9,207,217 Access hole cover ultrasonic inspection tooling 
    44 9,200,537 Gas turbine exhaust case with acoustic panels 
    45 9,157,241 Tile for a covering with enhanced acoustic properties 
    46 9,149,259 Patient safety and wellbeing device for covering wires and needles used in mammography or ultrasound guided needle localization 
    47 9,131,921 Cover for an ultrasonic head 
    48 9,120,442 Acoustic and thermal cover assembly 
    49 9,071,918 Ball and socket connection with an acoustic seal and mounting interface for a hearing assistance device 
    50 9,038,773 Acoustic cover assembly 
    51 D724,745 Cap for an ultrasound probe 
    52 8,915,538 Two shot double inverted acoustic hood to cowl seal 
    53 8,841,823 Ultrasonic transducer wear cap 
    54 8,798,279 Adjusting acoustic speaker output based on an estimated degree of seal of an ear about a speaker port 
    55 8,795,183 Handpiece for ultrasonic medical devices including seal for mechanical isolation of ultrasonic driver assembly 
    56 8,734,597 Segmental ultrasonic cleaning apparatus for removing scales and sludge on top of tube sheet in heat exchanger 
    57 8,708,093 Acoustic cover for vehicle fuel injection pump 
    58 8,591,679 Retrofit of a form-fill-seal machine heat station with an advanced ultrasonic welding kit 
    59 8,500,642 Ultrasonic treatment apparatus with a protective cover 
    60 8,403,184 Cap for an aerosol can or a spray can, with an acoustic seal 
    61 D678,500 Disposable and flexible cover for a surface ultrasound probe 
    62 8,381,591 Electrode cap for ultrasonic testing 
    63 8,351,295 Waterproof membrane cover for acoustic arrays in sodar systems 
    64 8,186,229 Ultrasonic flow meter having a port cover assembly 
    65 8,148,879 Sheet-type vibrator and acoustic apparatus 
    66 8,144,897 Adjusting acoustic speaker output based on an estimated degree of seal of an ear about a speaker port 
    67 8,122,866 Acoustic bumpers with engine front cover hidden mounting 
    68 8,080,922 Ultrasonic sensor having a cover including a damping element 
    69 8,066,098 Acoustic septum cap honeycomb 
    70 8,066,097 Acoustic enhancement device for underlayment of a covering 
    71 7,984,788 Laminated acoustic absorption sheet with flame retardant 
    72 D639,466 Ultrasonic pest repeller with LED night light and extra outlet safety cover 
    73 D629,527 Ultrasound therapy cap connection 
    74 D629,526 Therapy cap for ultrasonic therapy head 
    75 7,854,298 Acoustic septum cap honeycomb 
    76 7,797,809 Zero acoustic splice fan case liner 
    77 7,794,213 Integrated acoustic damper with thin sheet insert 
    78 7,779,710 Cable cover for an ultrasonic flow meter 
    79 7,757,809 Acoustic cover part for a vehicle 
    80 7,749,595 Thermoformable acoustic sheet 
    81 7,707,711 Acoustic noise reduction in a computer system having a vented cover 
    82 7,684,726 Image forming apparatus having the outer cover including acoustic insulation and heat conductive layers 
    83 7,654,522 Sheet feeder with ultrasonic double feed detector 
    84 7,510,052 Acoustic septum cap honeycomb 
    85 D585,556 Probe connector cover for an ultrasonic diagnosis apparatus 
    86 7,434,659 Acoustic septum cap honeycomb 
    87 7,404,559 Sheet feeding apparatus with ultrasonic sensor for detecting multiple feed of papers 
    88 7,400,501 Method and apparatus for acoustic noise reduction in a computer system having a vented cover 
    89 D562,456 Ultrasound case 
    90 7,328,771 Zero acoustic splice fan case liner 
    91 7,283,359 Method and apparatus for acoustic noise reduction in a computer system having a vented cover 
    92 7,226,656 Thermoformable acoustic sheet 
    93 7,110,536 Acoustic seal system 
    94 7,086,648 Acoustic seal 
    95 7,045,385 Method for fabricating surface acoustic wave filter packages and package sheet used therein 
    96 6,966,957  Bonding method for a plurality of components, bonding method for container and lid member, and ultrasonic welding apparatus 
    97 6,932,187  Protective acoustic cover assembly 
    98 6,887,204  Connector case, ultrasonic probe and ultrasonic imaging apparatus 
    99 6,821,367  Ultrasonic tool and method for securing a covering to a frame 
    100 6,687,377  Method and apparatus for determining in situ the acoustic seal provided by an in-ear device 
    101 6,654,333  Case body with front panel and acoustic apparatus for vehicle use 
    102 6,622,821  Thin acoustic muffler exhaust pipes, method of sheet metal construction thereof, and exhaust systems which utilize such exhaust pipes for increased ground clearance on race cars 
    103 6,604,630  Carrying case for lightweight ultrasound device 
    104 6,580,198  Surface acoustic wave device having a thin metal oxide film fully covering at least the electrodes and method of fabricating same 
    105 6,564,711  Ultrasonic cleaner and toner agglomerate disperser for liquid ink development (LID) systems using second sound 
    106 6,543,288  Laser-ultrasonic measurement of elastic properties of a thin sheet and of tension applied thereon 
    107 D469,877  Handheld ultrasonic display device with cover 
    108 6,512,834  Acoustic protective cover assembly 
    109 6,499,592  Case for acoustic and/or electrical instruments 
    110 6,493,180  Hard disk drive cover that contains a helmholtz resonator which attenuates acoustic energy 
    111 6,441,703  Multiple frequency acoustic reflector array and monolithic cover for resonators and method 
    112 6,437,412  Surface acoustic wave device having a package including a conductive cap that is coated with sealing material 
    113 6,411,287  Stress seal for acoustic wave touchscreens 
    114 6,407,964  Device for examining sheet-like articles using ultrasound 
    115 6,402,695  Cover for ultrasound probe 
    116 6,324,889  Ultrasound sensor for a fumes extractor hood 
    117 6,267,726  Cover for ultrasound probe 
    118 6,202,702  Acoustic damping pipe cover 
    119 6,186,578  Fixed glazing in contact with a peripheral seal for improved acoustic protection 
    120 6,132,378  Cover for ultrasound probe 
    121 6,059,260  Fume hood exhaust terminal having an ultrasonic motor drive actuator 
    122 5,919,539  Ultrasonic seaming of spunbonded polyolefin sheet material 
    123 5,897,503  Ultrasound transducer probe having case handle grip surfaces 
    124 D406,850  Face panel of automobile acoustic amplifier including transparent cover with twin wattage meters 
    125 5,830,300  Method of ultrasonic welding for a resin case 
    126 5,784,054  Surface acoustic wave touchscreen with housing seal 
    127 5,729,185  Acoustic wave filter package lid attachment apparatus and method utilizing a novolac epoxy based seal 
    128 D387,867  Medical ultrasound transducer case 
    129 5,681,408  Acoustic lamina wall covering 
    130 5,676,159  Ultrasound cover 
    131 5,660,909  Sheet for measuring ultrasonic waves 
    132 5,632,844  Acoustic lamina wall covering 
    133 5,598,050  Acoustic actuator and flextensional cover plate there for 
    134 5,565,635  Automatic playing apparatus with pedal actuators supported by bracket independent of case of acoustic piano 
    135 5,522,878  Solid multipurpose ultrasonic biomedical couplant gel in sheet form and method 
    136 5,444,181  Keyboard instrument selectively entering into an acoustic sound mode and an electronic sound mode through a rotation of a stopper with a cushion sheet against damper wires 
    137 5,372,042  Ultrasonic inspection of seal integrity of bond lines in sealed containers 
    138 5,364,681  Acoustic lamina wall covering 
    139 5,359,895  Process and device for the ultrasonic testing for welds between plastics packaging and cover foils 
    140 5,354,392  Method for connecting a wiring arranged on a sheet with another wiring arranged on another sheet by ultrasonic waves 
    141 5,288,350  Plastic case having improved ultrasonic welds between halves thereof and method for producing same 
    142 5,259,383  Sterile ultrasound cover tube 
    143 5,233,258  Ultrasonic sheet feeder, low-profile ultrasonic motor, and method of driving the same 
    144 5,199,593  Plastic case having improved ultrasonic welds between halves thereof and method for producing same 
    145 5,117,752  Ultrasonic ink seal for use in multicolor printing press 
    146 5,111,579  Method for making a frameless acoustic cover panel 
    147 5,110,381  Ultrasonic welding with controlled seal compression 
    148 5,103,130  Sound reinforcing seal for slotted acoustic transducers 
    149 5,090,736  Multi-sheet laminated identification card with tamper resistant, ultrasonic weldments 
    150 5,058,705  Sound-absorbing cover element as a component in a gap-free acoustic cover 
    151 5,009,105  Apparatus for ultrasonic examination of BWR shroud access cover plate retaining welds 
    152 4,970,618  Disk cartridge case formed by ultrasonic welding 
    153 4,966,746  Ultrasonic examination of BWR shroud access cover plate retaining welds 
    154 D310,975  Ultrasonic transmitting and receiving case for alarm systems 
    155 4,779,563  Ultrasonic wave vibration apparatus for use in producing preform wire, sheet or tape for a fiber reinforced metal composite 
    156 4,761,451  Acoustic vibration sheet and polypropylene composition for the same 
    157 4,746,688  Remoldable, wood-filled acoustic sheet 
    158 4,719,322  Radio housing and expandable chassis with integral keypad and acoustic speaker seal 
    159 4,690,722  Ultrasonic apparatus for joining and severing sheet material 
    160 4,673,922  Cabled ultrasonic seal 
    161 4,671,841  Method of making an acoustic panel with a triaxial open-weave face sheet 
    162 4,658,878  Acoustic type folding door with separate cover sections 
    163 4,610,750  Ultrasonic cut and seal apparatus 
    164 4,593,699  Sterile cover for intraoperative ultrasonic diagnostic devices and method and kit for providing same 
    165 4,560,427  Ultrasonic seal and cut method and apparatus 
    166 4,513,404  Acoustic reflectometer for sheet feed sensing 
    167 4,467,935  Random coil ultrasonic seal 
    168 4,411,720  Ultrasonic welding method for sealing a thermoplastic cap to the neck of a thermoplastic container 
    169 4,389,267  Method of fabricating a flexible cover by ultrasonic vibrations 
    170 4,366,712  Ultrasonic testing of sheet and plate stock 
    171 4,355,914  Acoustic hood with glare shield 
    172 4,227,959  Sonic or ultrasonic apparatus for simultaneously cutting and seaming sheet material 
    173 4,206,801  Sand-seal for rotary acoustic sand-core shakeout 
    174 4,201,093  Ultrasonic sheet material testing apparatus 
    175 4,117,732  Method for checking thickness of sheet materials by using acoustic oscillation and device for effecting same 
    176 4,116,766  Ultrasonic dip seal maintenance system 
    177 3,934,219  Acoustic method and apparatus for determining effectiveness of mine passage seal 
