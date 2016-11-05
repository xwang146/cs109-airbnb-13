#!/usr/bin/python
import csv
from datetime import date

#default transformation
def transform_default(input_string):
  return input_string.upper().strip()

#transform a string date into string number of days after 1/1/08
start_date = date(2008, 1, 1)
def transform_date(date_string):
  if date_string == "":
    return ""
  elif "/" in date_string:
    month, day, year = date_string.split("/")
    end_date = date(2000 + int(year), int(month), int(day))
    return (end_date - start_date).days
  else:
    raise ValueError("Cannot parse date " + date_string)

#transform price
def transform_price(price_string):
  if price_string == "":
    return ""
  elif len(price_string) > 3 and price_string[0] == "$" and price_string[-3:] == ".00":
    return price_string[1:-3].replace(",", "")
  else:
    raise ValueError("Cannot parse price " + price_string)

#transform zip by removing extended part
def transform_zip(zip_string):
  if len(zip_string) <= 5:
    return zip_string
  elif len(zip_string) == 10 and "-" in zip_string:
    #zip + 4 format
    return zip_string.rsplit("-")[0]
  else:
    #invalid (e.g CALL FOR DETAILS)
    return ""

#transform room type to int
bed_type_map = {'REAL BED': 0, 'FUTON': 1, 'PULL-OUT SOFA': 2, 'AIRBED': 3, 'COUCH': 4}
def transform_bed_type(input_string):
  return bed_type_map[input_string.upper()]

#transform room type to int
room_type_map = {'ENTIRE HOME/APT': 0, 'PRIVATE ROOM': 1, 'SHARED ROOM': 2}
def transform_room_type(input_string):
  return room_type_map[input_string.upper()]

#transform property type to int, combining rare entries into other = 5
property_type_map = {'APARTMENT': 0, 'HOUSE': 1, 'LOFT': 2, 'BED & BREAKFAST': 3, 'DORM': 4,
'': 5, 'CHALET': 5,  'EARTH HOUSE': 5, 'CAMPER/RV': 5, 'CABIN': 5, 'LIGHTHOUSE': 5,
'VILLA': 5,  'CAVE': 5, 'TREEHOUSE': 5, 'HUT': 5, 'OTHER': 5, 'BOAT': 5, 'CASTLE': 5, 'TENT': 5}
def transform_property_type(input_string):
  return property_type_map[input_string.upper()]

#list of all columns to keep and their cleanup function
column_mapping = {
  "id": transform_default,
  #"scrape_id"
  #"last_scraped"
  #"name"
  #"picture_url"
  #"host_id"
  #"host_name"
  "host_since": transform_date,
  #"host_picture_url"
  #"street"
  #"neighbourhood"
  #"neighbourhood_cleansed": transform_default,
  #"city"
  #"state"
  "zipcode": transform_zip,
  #"market"
  #"country"
  "latitude": transform_default,
  "longitude": transform_default,
  #"is_location_exact"
  "property_type": transform_property_type,
  "room_type": transform_room_type,
  "accommodates": transform_default,
  "bathrooms": transform_default,
  "bedrooms": transform_default,
  "beds": transform_default,
  "bed_type": transform_bed_type,
  #"square_feet"
  "price": transform_price,
  #"weekly_price"
  #"monthly_price"
  "guests_included": transform_default,
  #"extra_people"
  "minimum_nights": transform_default,
  "maximum_nights": transform_default,
  #"calendar_updated"
  "availability_30": transform_default,
  "availability_60": transform_default,
  "availability_90": transform_default,
  "availability_365": transform_default,
  #"calendar_last_scraped"
  "number_of_reviews": transform_default,
  "first_review": transform_date,
  "last_review": transform_date,
  "review_scores_rating": transform_default,
  "review_scores_accuracy": transform_default,
  "review_scores_cleanliness": transform_default,
  "review_scores_checkin": transform_default,
  "review_scores_communication": transform_default,
  "review_scores_location": transform_default,
  "review_scores_value": transform_default,
  "host_listing_count": transform_default
}

with open("listings.csv", "rU") as original_data, open("listings_clean.csv", "w") as new_data:
  #create reader for data
  reader = csv.DictReader(original_data)

  #generate new headers
  headers = list(reader.fieldnames)
  new_headers = []
  for column in headers:
    if column in column_mapping.keys():
      new_headers.append(column)
  #move price to end
  new_headers.append(new_headers.pop(new_headers.index('price')))

  #create writer
  writer = csv.DictWriter(new_data, new_headers)
  writer.writeheader()

  for row in reader:
    new_row = {}
    #transform data
    for column, transformer in column_mapping.iteritems():
      new_row[column] = transformer(row[column])
    #write transformed data to new file
    writer.writerow(new_row)