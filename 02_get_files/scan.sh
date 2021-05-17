#!/bin/bash
~/zgrab2/cmd/zgrab2/zgrab2 multiple -c multiple.ini http5721 -f $1 -o $2.json -l $2.log
