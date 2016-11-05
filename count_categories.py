#!/usr/bin/python
import csv
from collections import Counter

filename = "listings.csv"
#filename = "listings_clean.csv"

columns = [
  #"city",
  "bed_type",
  "property_type",
  "room_type",
  #"neighbourhood_cleansed",
  "zipcode"
  #"bedrooms",
  #"bathrooms"
]

#initialize counter for each column
counters = {}
for column in columns:
  counters[column] = Counter()

#count the number of times each element appears in each column
with open("listings_clean.csv", "rU") as data:
  reader = csv.DictReader(data)
  for row in reader:
    for column in columns:
      value = row[column].upper()
      counters[column][value] += 1

for column, counter in counters.iteritems():
  print column
  print dict(counter)
  print