#!/bin/bash

# Usage: ./gen_pr.sh <file containing target tournaments>

cat $1 | xargs python load_tourney.py | python ts.py | sort -n 

#end
