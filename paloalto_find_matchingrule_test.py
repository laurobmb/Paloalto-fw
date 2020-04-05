#!/usr/bin/env python3
from module.paloalto import paloalto_find_matchingrule
from configs.setup import credential

__version__ = '0.1'
__author__ = 'Lauro Gomes'
__contact__ = 'laurobmb@gmail.com'
__maintainer__ = 'Lauro Gomes'
__status__ = 'Development'
__date__ = '2020-03-20'

pa_ip,pa_key = credential()
rule_params = { 
    'dstZone': 'PROXY',
    'srcZone': 'INTERNET',
    'srcIP': '10.1.10.223',
    'dstIP': 'any',
    'application': 'any',
    'dstPort': 'any',
    'protocol': 'allow',
    }

print( paloalto_find_matchingrule(pa_ip,pa_key,rule_params) )

