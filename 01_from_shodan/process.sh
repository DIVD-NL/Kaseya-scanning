#!/bin/bash
#set -x
cat from_shodan.json|jq -r "[.ip_str, .port, .ssl.cert.subject.C, .ssl.cert.subject.CN, .ssl.cert.subject.l, .ssl.cert.subject.o ]|@csv" > host_port_cert.csv
rm targets_*
cat from_shodan.json|jq -r '@sh "echo \(.ip_str) >> targets_\(.port).txt"' |bash
(cat from_shodan.json |jq -r '.port' && echo 5721)|sort -un > ports.txt
cp ../01_find_open_ports/targets_5721.txt .
wc -l targets_*|sort -nr | head
cat ports.txt | head