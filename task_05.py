#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""BP measurements"""


BP_STATUS = raw_input('Enter BP' )
BP_STATUS = int(BP_STATUS)

if BP_STATUS <= 89:
    if True:
        print {'low'}
    
elif BP_STATUS >=90 <= 119:
    if True:
        print {'ideal'}
elif BP_STATUS >= 120 <= 139:
    if True:
        print {'warning'}
elif BP_STATUS >= 140 <=159:
    if True:
        print {'high'}
else:
    BP_STATUS >= 160
    if True:
        print{'emergency'}

