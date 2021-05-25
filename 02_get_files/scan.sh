#!/bin/bash
echo -n "" > grabs.log 
for PORT in $(cat ports.txt ); do
	HOSTCOUNT=$(cat targets_$PORT.txt|wc -l)
	echo "===== $PORT =====" >> grabs.log
	echo "Scanning $HOSTCOUNT ips on port $PORT..."
	echo "
[http]
name=\"get_env\"
port=$PORT
endpoint=\"/api/v1.5/cw/environment\"
[http]
name=\"get_slash\"
port=$PORT
endpoint=\"/\"
[http]
name=\"get_latest\"
port=$PORT
endpoint=\"/install/kaseyalatestversion.xml\"
" > multiple.ini
	~/zgrab2/cmd/zgrab2/zgrab2 multiple -c multiple.ini -f targets_$PORT.txt -o results_$PORT.json -l zgrab.log |tee -a grabs.log
	cat zgrab.log >> grabs.log
	echo "Done"
done
