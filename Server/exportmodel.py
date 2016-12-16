#!/usr/bin/python
#Exports our model for running on AWS server
#Note we use location clustering by KNN + linear regression
#because our best random forest model is too big
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.externals import joblib

# Load listing data
listing = pd.read_csv('../Data/data_after_predictor_selection.csv')
x = listing
x = x.drop('price', axis=1)
y = listing['price']

#dump model for webapi
loc_model = KNeighborsRegressor(n_neighbors=50, weights="uniform")
loc_model.fit(x[["longitude", "latitude"]], np.log(y))

x2 = x.copy()
x2["location"] = loc_model.predict(x[["longitude", "latitude"]])

model = LinearRegression()
model.fit(x2, np.log(y))
model.score(x2, np.log(y))

joblib.dump(loc_model, "loc_model.pkl")
joblib.dump(model, "model.pkl")



#### Test whether export is consistent ####
def predict(qs):
    default = {'accommodates': 2.8927789135514019,
     'bathrooms': 1.1143216997663552,
     'bed_type_0': 0.9592216705607477,
     'bed_type_1': 0.017669392523364486,
     'bed_type_2': 0.01197429906542056,
     'bed_type_3': 0.0074109228971962621,
     'bed_type_4': 0.003723714953271028,
     'bedrooms': 1.1349664135514019,
     'beds': 1.5329658294392523,
     'host_listing_count': 1.8150189836448598,
     'latitude': 40.733070086430153,
     'longitude': -73.964276120671585,
     'minimum_nights': 2.5682316004672896,
     'property_type_0': 0.9093530957943925,
     'property_type_1': 0.057498539719626166,
     'property_type_2': 0.021940712616822431,
     'property_type_3': 0.0062061915887850466,
     'property_type_4': 0.0017888434579439252,
     'property_type_5': 0.0032126168224299065,
     'review_scores_accuracy': 9.2488682827102799,
     'review_scores_checkin': 9.7113025700934585,
     'review_scores_cleanliness': 9.0075569509345801,
     'review_scores_communication': 9.771904205607477,
     'review_scores_value': 9.0856454439252339,
     'room_type_0': 0.58327248831775702,
     'room_type_1': 0.38646320093457942,
     'room_type_2': 0.030264310747663552}

    column_order = ['accommodates',
     'bathrooms',
     'bedrooms',
     'review_scores_checkin',
     'review_scores_communication',
     'latitude',
     'longitude',
     'property_type_0',
     'property_type_1',
     'property_type_2',
     'property_type_3',
     'property_type_4',
     'property_type_5',
     'room_type_0',
     'room_type_1',
     'room_type_2',
     'bed_type_0',
     'bed_type_1',
     'bed_type_2',
     'bed_type_3',
     'bed_type_4',
     'beds',
     'review_scores_value',
     'host_listing_count',
     'review_scores_cleanliness',
     'review_scores_accuracy',
     'minimum_nights',
     'location']

    #fill in predictors
    for predictor in qs:
        if predictor in default:
            default[predictor] = qs[predictor]

    #predict locations based on knn
    location_model = joblib.load('loc_model.pkl')
    loc_x = np.array([[default["longitude"], default["latitude"]]])
    default["location"] = location_model.predict(loc_x)[0]

    #predict price
    x = np.zeros((1, 28))
    for i, c in enumerate(column_order):
        x[0, i] = default[c]

    main_model = joblib.load('model.pkl')
    y = main_model.predict(x)
    return y[0]
    #return np.exp(y[0])

print predict(listing.iloc[0,:].to_dict())
print model.predict(x2)[0]