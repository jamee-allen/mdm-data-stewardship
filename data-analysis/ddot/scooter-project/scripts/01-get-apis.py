import os
import json
import requests
import numpy as np
import pandas as pd
import pprint as pp

project_dir = os.getcwd() + '/data-analysis/ddot/scooter-project'

ddot_apis = [
    {
        'company': 'Jump',
        'api_url': 'https://gbfs.uber.com/v1/dcs/free_bike_status.json'
    },
    {
        'company': 'Lime',
        'api_url': 'https://data.lime.bike/api/partners/v1/gbfs/washington_dc/free_bike_status.json'
    },
    {
        'company': 'Lyft',
        'api_url': 'https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/dca/free_bike_status.json'
    },
    {
        'company': 'Skip',
        'api_url': 'https://us-central1-waybots-production.cloudfunctions.net/ddotApi-dcFreeBikeStatus'
    },
    {
        'company': 'Spin',
        'api_url': 'https://web.spin.pm/api/gbfs/v1/washington_dc/free_bike_status'
    }
]

api_df = pd.DataFrame(ddot_apis)

def get_json(url):
    return(json.loads(requests.get(url).text))

api_df['json'] = api_df['api_url'].apply(get_json)

def parse_json(json):

    data = json.get('data', None)

    if data is None:
        bikes = json.get('bikes')
        return(bikes)

    if isinstance(json, list):
        return(bikes)
    
    bikes = data.get('bikes', None)

    return(bikes)

api_df['data'] = api_df['json'].apply(parse_json)

def parse_data(row):

    df = pd.DataFrame(row['data'])
    df = df[['bike_id', 'lat', 'lon']]
    df['company'] = row['company']

    return(df)

dfs = api_df.apply(parse_data, axis=1).to_list()

pd.concat(dfs).to_csv(project_dir + "/data/source/scooter_data.csv", index=False)
