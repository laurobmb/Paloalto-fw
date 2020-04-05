#!/usr/bin/env python3
from module.paloalto import paloalto_rule_delete
from configs.setup import credential

__version__ = '0.1'
__author__ = 'Lauro Gomes'
__contact__ = 'laurobmb@gmail.com'
__maintainer__ = 'Lauro Gomes'
__status__ = 'Development'
__date__ = '2020-03-20'

pa_ip,pa_key = credential()
rule_name = 'Liberacao_temporaria'
print ( paloalto_rule_delete(pa_ip,pa_key,rule_name) )
