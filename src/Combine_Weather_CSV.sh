#!/bin/bash

if $pwd | grep -q "Data" || $pwd | grep -q "src" ; then
    cd ..
fi

cd Data/Weather
cat "" > "Weather.csv"
for file in *.csv; do
    filename="${file%.*}"
    echo $filename
    searchstring="Weather"
    rest=${filename#*$searchstring}
    index=$((${#filename} - ${#rest} - ${#searchstring}))
    echo $index
    if [ "$index" -lt "-1" ]; then
        cat "$file" >> "Weather.csv"
    fi
done