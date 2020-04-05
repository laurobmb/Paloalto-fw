#!/usr/bin/env python3
from module.paloalto import paloalto_rule_add
from configs.setup import credential

__version__ = '0.1'
__author__ = 'Lauro Gomes'
__contact__ = 'laurobmb@gmail.com'
__maintainer__ = 'Lauro Gomes'
__status__ = 'Development'
__date__ = '2020-03-20'

pa_ip,pa_key = credential()

rule_params = { 
    'name': 'teste',
    'dstZone': 'PROXY',
    'srcZone': 'EXPANSAO',
    'srcIP': '10.1.11.0',
    'dstIP': '10.5.40.11',
    'application': 'any',
    'service': 'TCP_8000',
    'action': 'allow',
    'spg': 'Prefil%20BLK'
    }
 
print(paloalto_rule_add(pa_ip,pa_key,rule_params))
