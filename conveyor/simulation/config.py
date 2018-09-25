template = """\
     --------#=====#-------------------------#=====#-------------------- 
   / *** *** # *** # *** *** *** *** *** *** # *** # *** *** *** *** *** \ 
  / ***   ---#=====#-------------------------#=====#---------------   *** \ 
 / ***  /                                                           \  *** \ 
 | *** |                                                             | *** | 
 | *** |                                                             | *** | 
 | *** |                                                             | *** | 
 #=====#                                                             |~~~~~| 
 # *** #                                                             | *** | 
 #=====#                                                             |~~~~~| 
 | *** |                                                             | *** | 
 | *** |                                                             | *** | 
 | *** |                                                             | *** | 
 | *** |                                                             | *** | 
 \ ***  \                                                           /  *** / 
  \ ***   -----------------------------------#=====#---------------   *** / 
   \ *** *** *** *** *** *** *** *** *** *** # *** # *** *** *** *** *** / 
     ----------------------------------------#=====#-------------------- \
"""

template_height = len(template.split('\n')) + 1
template_width = max(map(len, template.split('\n'))) + 1

# coordinates for tkinter tags
locks_is_open_symbols = [
    (('1.46', '1.51'), ('3.46', '3.51')),
    (('1.14', '1.19'), ('3.14', '3.19')),
    (('8.2', '8.7'), ('10.2', '10.7')),
    (('16.46', '16.51'), ('18.46', '18.51')),
]

locks_is_empty_symbols = [
    ('1.45', '2.45', '3.45', '1.51', '2.51', '3.51'),
    ('1.13', '2.13', '3.13', '1.19', '2.19', '3.19'),
    ('8.1', '9.1', '10.1', '8.7', '9.7', '10.7'),
    ('16.45', '17.45', '18.45', '16.51', '17.51', '18.51'),
]

deploy_pad_symbols = (('8.70', '8.75'), ('10.70', '10.75'))

template_for_format = """\
     --------#=====#-------------------------#=====#-------------------- 
   / {9} {8} # {7} # {6} {5} {4} {3} {2} {1} # {0} # {54} {53} {52} {51} {50} \ 
  / {10}   ---#=====#-------------------------#=====#---------------   {49} \ 
 / {11}  /                                                           \  {48} \ 
 | {12} |                                                             | {47} | 
 | {13} |                                                             | {46} | 
 | {14} |                                                             | {45} | 
 #=====#                                                             |~~~~~|  
 # {15} #                                                             | {44} | 
 #=====#                                                             |~~~~~|  
 | {16} |                                                             | {43} | 
 | {17} |                                                             | {42} | 
 | {18} |                                                             | {41} | 
 | {19} |                                                             | {40} | 
 \ {20}  \                                                           /  {39} / 
  \ {21}   -----------------------------------#=====#---------------   {38} / 
   \ {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} # {32} # {33} {34} {35} {36} {37} / 
     ----------------------------------------#=====#-------------------- \
"""

# absolute coordinates of assembly line elements
locks_coords_list = [0, 7, 15, 32]
deploy_coord = 44
conv_len = 54
