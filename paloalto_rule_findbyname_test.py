#!/usr/bin/env python3
from module.paloalto import paloalto_rule_findbyname
from configs.setup import credential

__version__ = '0.1'
__author__ = 'Lauro Gomes'
__contact__ = 'laurobmb@gmail.com'
__maintainer__ = 'Lauro Gomes'
__status__ = 'Development'
__date__ = '2020-03-20'

pa_ip,pa_key = credential()
rule_name = 'acesso_remoto'
print( paloalto_rule_findbyname(pa_ip,pa_key,rule_name) )
