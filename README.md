# Rough Coding for USPTO Patent Search

## 0. Introduction   
    I just want to get the patent summary(title texts and pdf summary files) from the USPTO patent site for each a day.   
    this is the code that use with the libraries from Python and open API, receiving the html source and send http messages to get information.   
    but it's just a rough code, and I programmed to just one text file in a day.   
    if you have to try again to search, you have to delete the text file.   
    And please delete my example files(txt and pdf both) if you test my code.

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
              -pp = os.path.join(path, "patent_pdf"),    
              note that file directory will be created if there NOT exists directory

## 3. Simple Example   
-----------------
    Python uspto_search.py -i search   
    
    Python uspto_search.py -i search -q "TTL/(something OR something ..) OR .."   
    (note that it just uses TTL and OR and AND operator, others will occur error)
    
    Python uspto_search.py -i compare   
    (note that it will compare today text file with yesterday text file.   
    And renew pdf files when the new patent appears)
    
    Python uspto_search.py -i download   
    (it will download pdf summary file, using default query)

    Python uspto_search.py -i search -q "TTL/(something OR something ..) OR .." -fp "text path" -pp "pdf path"   
    (you can change the file(txt) path and pdf path while using the -q command)
    
    Python uspto_search.py -i merge -pp "pdf path"   
    (it will merge the pdf file in the path of "pdf path")

## 4. Results(Default)
### TXT file
------------
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
    
### pdf files and merge pdf file
--------------------------------
    2020-05-28  오후 05:33            52,499 10110981.pdf
    2020-05-28  오후 05:33            60,551 10129623.pdf
    2020-05-28  오후 05:33            49,651 10142748.pdf
    2020-05-28  오후 05:33            49,557 10149661.pdf
    2020-05-28  오후 05:33            74,720 10200802.pdf
    2020-05-28  오후 05:33            42,358 10219054.pdf
    2020-05-28  오후 05:33            62,757 10220474.pdf
    2020-05-28  오후 05:33            54,756 10232804.pdf
    2020-05-28  오후 05:33            62,586 10264374.pdf
    2020-05-28  오후 05:33            50,969 10277989.pdf
    2020-05-28  오후 05:33            53,583 10293575.pdf
    2020-05-28  오후 05:32            49,987 10398288.pdf
    2020-05-28  오후 05:32            58,821 10398409.pdf
    2020-05-28  오후 05:32            50,756 10413314.pdf
    2020-05-28  오후 05:32            59,689 10415242.pdf
    2020-05-28  오후 05:32            56,215 10498310.pdf
    2020-05-28  오후 05:32            61,499 10499158.pdf
    2020-05-28  오후 05:32            57,149 10543687.pdf
    2020-05-28  오후 05:32            62,239 10549661.pdf
    2020-05-28  오후 05:32            61,578 10574208.pdf
    2020-05-28  오후 05:32            46,038 10584606.pdf
    2020-05-28  오후 05:32            52,062 10595823.pdf
    2020-05-28  오후 05:32            62,082 10639008.pdf
    2020-06-04  오전 10:33            53,033 10670271.pdf
    2020-05-28  오후 05:36            62,653 3934219.pdf
    2020-05-28  오후 05:36            47,579 4116766.pdf
    2020-05-28  오후 05:36            58,508 4117732.pdf
    2020-05-28  오후 05:36            81,502 4201093.pdf
    2020-05-28  오후 05:36            62,838 4206801.pdf
    2020-05-28  오후 05:36            59,381 4227959.pdf
    2020-05-28  오후 05:36            60,258 4355914.pdf
    2020-05-28  오후 05:36            61,847 4366712.pdf
    2020-05-28  오후 05:36            29,726 4389267.pdf
    2020-05-28  오후 05:36            35,751 4411720.pdf
    2020-05-28  오후 05:36            45,964 4467935.pdf
    2020-05-28  오후 05:36            62,083 4513404.pdf
    2020-05-28  오후 05:36            37,651 4560427.pdf
    2020-05-28  오후 05:35            38,872 4593699.pdf
    2020-05-28  오후 05:35            37,000 4610750.pdf
    2020-05-28  오후 05:35            63,925 4658878.pdf
    2020-05-28  오후 05:35            62,265 4671841.pdf
    2020-05-28  오후 05:35            37,232 4673922.pdf
    2020-05-28  오후 05:35            38,798 4690722.pdf
    2020-05-28  오후 05:35            71,089 4719322.pdf
    2020-05-28  오후 05:35            36,926 4746688.pdf
    2020-05-28  오후 05:35            35,617 4761451.pdf
    2020-05-28  오후 05:35            38,019 4779563.pdf
    2020-05-28  오후 05:35            56,810 4966746.pdf
    2020-05-28  오후 05:35            37,337 4970618.pdf
    2020-05-28  오후 05:35            59,718 5009105.pdf
    2020-05-28  오후 05:35            45,159 5058705.pdf
    2020-05-28  오후 05:35            47,265 5090736.pdf
    2020-05-28  오후 05:35            37,269 5103130.pdf
    2020-05-28  오후 05:35            49,237 5110381.pdf
    2020-05-28  오후 05:35            65,110 5111579.pdf
    2020-05-28  오후 05:35            49,285 5117752.pdf
    2020-05-28  오후 05:35            47,927 5199593.pdf
    2020-05-28  오후 05:35            63,104 5233258.pdf
    2020-05-28  오후 05:35            42,502 5259383.pdf
    2020-05-28  오후 05:35            48,844 5288350.pdf
    2020-05-28  오후 05:35            56,996 5354392.pdf
    2020-05-28  오후 05:35            54,777 5359895.pdf
    2020-05-28  오후 05:35            54,741 5364681.pdf
    2020-05-28  오후 05:35            55,561 5372042.pdf
    2020-05-28  오후 05:35            57,738 5444181.pdf
    2020-05-28  오후 05:35            75,474 5522878.pdf
    2020-05-28  오후 05:35            49,931 5565635.pdf
    2020-05-28  오후 05:35            61,150 5598050.pdf
    2020-05-28  오후 05:35            89,079 5632844.pdf
    2020-05-28  오후 05:35            49,503 5660909.pdf
    2020-05-28  오후 05:35            47,787 5676159.pdf
    2020-05-28  오후 05:35            56,851 5681408.pdf
    2020-05-28  오후 05:35            66,031 5729185.pdf
    2020-05-28  오후 05:35            52,111 5784054.pdf
    2020-05-28  오후 05:35            35,591 5830300.pdf
    2020-05-28  오후 05:35            40,371 5897503.pdf
    2020-05-28  오후 05:35            34,961 5919539.pdf
    2020-05-28  오후 05:35            47,096 6059260.pdf
    2020-05-28  오후 05:35            42,325 6132378.pdf
    2020-05-28  오후 05:35            45,273 6186578.pdf
    2020-05-28  오후 05:35            41,983 6202702.pdf
    2020-05-28  오후 05:35            42,871 6267726.pdf
    2020-05-28  오후 05:35            43,113 6324889.pdf
    2020-05-28  오후 05:35            35,837 6402695.pdf
    2020-05-28  오후 05:35            45,261 6407964.pdf
    2020-05-28  오후 05:34            56,235 6411287.pdf
    2020-05-28  오후 05:34            46,262 6437412.pdf
    2020-05-28  오후 05:34            56,204 6441703.pdf
    2020-05-28  오후 05:34            44,488 6493180.pdf
    2020-05-28  오후 05:34            45,150 6499592.pdf
    2020-05-28  오후 05:34            49,812 6512834.pdf
    2020-05-28  오후 05:34            55,004 6543288.pdf
    2020-05-28  오후 05:34            60,409 6564711.pdf
    2020-05-28  오후 05:34            50,645 6580198.pdf
    2020-05-28  오후 05:34            47,196 6604630.pdf
    2020-05-28  오후 05:34            62,009 6622821.pdf
    2020-05-28  오후 05:34            51,770 6654333.pdf
    2020-05-28  오후 05:34            65,497 6687377.pdf
    2020-05-28  오후 05:34            45,282 6821367.pdf
    2020-05-28  오후 05:34            39,200 6887204.pdf
    2020-05-28  오후 05:34            60,569 6932187.pdf
    2020-05-28  오후 05:34            45,037 6966957.pdf
    2020-05-28  오후 05:34            56,451 7045385.pdf
    2020-05-28  오후 05:34            56,183 7086648.pdf
    2020-05-28  오후 05:34            52,727 7110536.pdf
    2020-05-28  오후 05:34            51,257 7226656.pdf
    2020-05-28  오후 05:34            44,277 7283359.pdf
    2020-05-28  오후 05:34            74,866 7328771.pdf
    2020-05-28  오후 05:34            46,237 7400501.pdf
    2020-05-28  오후 05:34            48,931 7404559.pdf
    2020-05-28  오후 05:34            49,630 7434659.pdf
    2020-05-28  오후 05:34            57,209 7510052.pdf
    2020-05-28  오후 05:34            37,870 7654522.pdf
    2020-05-28  오후 05:34            47,762 7684726.pdf
    2020-05-28  오후 05:34            53,878 7707711.pdf
    2020-05-28  오후 05:34            51,955 7749595.pdf
    2020-05-28  오후 05:34            50,605 7757809.pdf
    2020-05-28  오후 05:34            50,100 7779710.pdf
    2020-05-28  오후 05:34            51,597 7794213.pdf
    2020-05-28  오후 05:34            61,753 7797809.pdf
    2020-05-28  오후 05:34            49,512 7854298.pdf
    2020-05-28  오후 05:34            52,222 7984788.pdf
    2020-05-28  오후 05:34            56,962 8066097.pdf
    2020-05-28  오후 05:34            48,196 8066098.pdf
    2020-05-28  오후 05:34            56,432 8080922.pdf
    2020-05-28  오후 05:34            76,207 8122866.pdf
    2020-05-28  오후 05:34            51,067 8144897.pdf
    2020-05-28  오후 05:34            60,417 8148879.pdf
    2020-05-28  오후 05:33            64,297 8186229.pdf
    2020-05-28  오후 05:33            66,258 8351295.pdf
    2020-05-28  오후 05:33            50,002 8381591.pdf
    2020-05-28  오후 05:33            55,774 8403184.pdf
    2020-05-28  오후 05:33            49,316 8500642.pdf
    2020-05-28  오후 05:33            75,837 8591679.pdf
    2020-05-28  오후 05:33            46,509 8708093.pdf
    2020-05-28  오후 05:33            66,038 8734597.pdf
    2020-05-28  오후 05:33            54,143 8795183.pdf
    2020-05-28  오후 05:33            57,060 8798279.pdf
    2020-05-28  오후 05:33            57,732 8841823.pdf
    2020-05-28  오후 05:33            53,241 8915538.pdf
    2020-05-28  오후 05:33            53,168 9038773.pdf
    2020-05-28  오후 05:33            48,542 9071918.pdf
    2020-05-28  오후 05:33            60,968 9120442.pdf
    2020-05-28  오후 05:33            57,800 9131921.pdf
    2020-05-28  오후 05:33            61,644 9149259.pdf
    2020-05-28  오후 05:33            55,001 9157241.pdf
    2020-05-28  오후 05:33            61,881 9200537.pdf
    2020-05-28  오후 05:33            56,817 9207217.pdf
    2020-05-28  오후 05:33            65,235 9309666.pdf
    2020-05-28  오후 05:33            65,148 9362799.pdf
    2020-05-28  오후 05:33            55,262 9433271.pdf
    2020-05-28  오후 05:33            65,486 9436161.pdf
    2020-05-28  오후 05:33            53,726 9496695.pdf
    2020-05-28  오후 05:33            63,400 9541431.pdf
    2020-05-28  오후 05:33            52,382 9605328.pdf
    2020-05-28  오후 05:33            66,379 9641938.pdf
    2020-05-28  오후 05:33            60,203 9662829.pdf
    2020-05-28  오후 05:33            48,522 9667226.pdf
    2020-05-28  오후 05:33            64,370 9874842.pdf
    2020-05-28  오후 05:33            52,393 9908485.pdf
    2020-05-28  오후 05:33            59,130 9937659.pdf
    2020-05-28  오후 05:33            60,052 9973169.pdf
    2020-05-28  오후 05:33            73,507 9975292.pdf
    2020-05-28  오후 05:33            72,192 9980065.pdf
    2020-05-28  오후 05:33            52,446 9980700.pdf
    2020-05-28  오후 05:33            44,809 9993967.pdf
    2020-05-28  오후 05:33            42,528 9998814.pdf
    2020-05-28  오후 05:35            51,882 D310975.pdf
    2020-05-28  오후 05:35            58,471 D387867.pdf
    2020-05-28  오후 05:35            57,228 D406850.pdf
    2020-05-28  오후 05:34            69,148 D469877.pdf
    2020-05-28  오후 05:34            53,145 D562456.pdf
    2020-05-28  오후 05:34            51,768 D585556.pdf
    2020-05-28  오후 05:34            44,028 D629526.pdf
    2020-05-28  오후 05:34            44,108 D629527.pdf
    2020-05-28  오후 05:34            53,923 D639466.pdf
    2020-05-28  오후 05:33            65,433 D678500.pdf
    2020-05-28  오후 05:33            59,727 D724745.pdf
    2020-05-28  오후 05:36            9,430,217 merge.pdf
    
