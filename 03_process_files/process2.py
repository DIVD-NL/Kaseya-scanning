#!/usr/bin/env python3

import sys
import json
import xmltodict
from json_stream_parser import load_iter

print('"ip","port","SystemVersion","PatchLevel","CustomerID","TimeZoneOffset","AgentVersion","from_latest"')
for obj in load_iter(sys.stdin):
	if "ip" in obj:
		# Should have this
		ip = obj['ip']
		# Find out it is a KaseyaVSA
		if obj['data']['get_slash']['status'] == "success":
			include = False
			# Could get /
			#print(obj['data']['get_slash']['result']['response'])
			if "body" in obj['data']['get_slash']['result']['response'] and obj['data']['get_slash']['result']['response']['body'].lower().find("vsapres"):
				# Yes it is Kaseya VSA
				include = True
				#print(obj['data']['get_slash']['result'])
				port = obj['data']['get_slash']['result']['response']['request']['host'].split(":")[1]

			try:
				#print(obj['data']['get_env']['result'])
				env = json.loads(obj['data']['get_env']['result']['response']['body'])				
			except:
				env = None

			try:
				#print(obj['data']['get_latest']['result'])
				latest = xmltodict.parse(obj['data']['get_latest']['result']['response']['body'])
			except:
				latest = {}



			if env:
				SystemVersion = env['Result']['SystemVersion']
				PatchLevel = env['Result']['PatchLevel']
				CustomerID = env['Result']['CustomerID']
				TimeZoneOffset = env['Result']['TimeZoneOffset']
				AgentVersion = env['Result']['AgentVersion']
				include = True
				port = obj['data']['get_env']['result']['response']['request']['host'].split(":")[1]
			else:
				SystemVersion = "<unknown>"
				PatchLevel = "<unknown>"
				CustomerID = "<unknown>"
				TimeZoneOffset = "<unknown>"
				AgentVersion = "<unknown>"
			if "versions" in latest:
				from_latest = latest['versions']['versionInfo']['@versionStr']
				include = True
				port = obj['data']['get_latest']['result']['response']['request']['host'].split(":")[1]
			else:
				from_latest = "<unknown>"

			if include:
				print('"{}","{}","{}","{}","{}","{}","{}"'.format(
						ip,
						port,
						SystemVersion,
						PatchLevel,
						CustomerID,
						TimeZoneOffset,
						AgentVersion,
						from_latest
					)
				)