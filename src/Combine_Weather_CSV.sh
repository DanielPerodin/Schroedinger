#!/bin/bash

if $pwd | grep -q "Data" || $pwd | grep -q "src" ; then
    cd ..
fi

cd "Data/Weather/${1}"
cat "" > "${1}.csv"
for file in *.csv; do
    filename="${file%.*}"
    echo $filename
    searchstring="Weather"
    rest=${filename#*$searchstring}
    index=$((${#filename} - ${#rest} - ${#searchstring}))
    echo $index
    if [ "$index" -lt "-1" ]; then
        cat "$file" >> "${1}.csv"
    fi
done
mv "${1}.csv" "../${1}.csv"