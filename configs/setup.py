#!/usr/bin/python3
import json,os

file_name='configs/.setup.json'
full_file=os.path.abspath(os.path.join(file_name))

def credential():
	with open(full_file) as jsonfile:
		parsed = json.load(jsonfile)
		pa_ip = parsed['paloaltonetworks']['pa_ip']
		pa_key = parsed['paloaltonetworks']['pa_key']
	return pa_ip,pa_key

