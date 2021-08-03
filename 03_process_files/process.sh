#!/bin/bash
#set -x
cat results_*|jq '. | select(.data.get_slash.result.response.body) | select(.data.get_slash.result.response.body | contains("vsapres"))'|jq -r '[.data.get_slash.result.response.request.host]|@csv' > kaseyas.csv
cat results_*|jq '. | select((.data.get_env.result.response.body and (.data.get_env.result.response.body | contains("SystemVersion"))) or (.data.get_latest.result.response.body and (.data.get_latest.result.response.body | contains("versionInfo"))))' | jq -c '{ "ip" : .ip, "host" : .data.get_env.result.response.request.host, "body_env":  .data.get_env.result.response.body, "body_latest" : .data.get_latest.result.response.body }' > versions.json
cp ../01_from_shodan/host_port_cert.csv .

cat versions.json | ./process_json.py > kaseya_versions_old.csv
cat results_*| ./process2.py > kaseya_versions.csv
wc -l kaseyas.csv versions.json kaseya_versions*.csv
