#!/bin/bash
#set -x
cat results_*|jq '. | select(.data.get_slash.result.response.body) | select(.data.get_slash.result.response.body | contains("vsapres"))'|jq -r '[.data.get_slash.result.response.request.host]|@csv' > kaseyas.csv
cat results_*|jq '. | select((.data.get_env.result.response.body and (.data.get_env.result.response.body | contains("SystemVersion"))) or (.data.get_latest.result.response.body and (.data.get_latest.result.response.body | contains("versionInfo"))))' | jq -c '{ "host" : .data.get_env.result.response.request.host, "body_env":  .data.get_env.result.response.body, "body_latest" : .data.get_latest.result.response.body }' > versions.json


wc -l kaseyas.csv versions.json no_version.json