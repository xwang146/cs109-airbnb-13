#!/bin/bash
#This script converts all ipynb in this folder into html
for f in *ipynb
do
 echo "Processing $f"
 jupyter nbconvert --to html --template full --output ../../Website/${f%.*}.html $f
done
