#!/usr/bin/env python3

import sys
import json
import xmltodict
from json_stream_parser import load_iter

print('"ip","host","SystemVersion","PatchLevel","CustomerID","TimeZoneOffset","AgentVersion","from_latest"')
for obj in load_iter(sys.stdin):
	if "body_env" in obj:
		try:
			env = json.loads(obj['body_env'])
		except:
			env = None
	else:
		env = None
	if "body_latest" in obj:
		try:
			latest = xmltodict.parse(obj['body_latest'])
		except:
			latest = None
	else:
		latest = None
	#print(json.dumps(latest))
	#print(obj)
	#print(env)
	#print(latest)
	if env:
		SystemVersion = env['Result']['SystemVersion']
		PatchLevel = env['Result']['PatchLevel']
		CustomerID = env['Result']['CustomerID']
		TimeZoneOffset = env['Result']['TimeZoneOffset']
		AgentVersion = env['Result']['AgentVersion']
	else:
		SystemVersion = ""
		PatchLevel = ""
		CustomerID = ""
		TimeZoneOffset = ""
		AgentVersion = ""
	if latest and "versions" in latest:
		from_latest = latest['versions']['versionInfo']['@versionStr']
	else:
		from_latest = ""

	print('"{}","{}","{}","{}","{}","{}","{}","{}"'.format(
			obj['ip'],
			obj['host'],
			SystemVersion,
			PatchLevel,
			CustomerID,
			TimeZoneOffset,
			AgentVersion,
			from_latest
		)
	)
