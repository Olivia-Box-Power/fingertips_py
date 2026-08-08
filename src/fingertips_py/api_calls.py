"""
A group of functions to query the Fingertips api and retrieve data in a variety of formats.
"""


import requests
import json
import pandas as pd
from io import StringIO


def make_request(url, attr=None):
    """
    Makes a request to the given URL and returns the specified attribute.
    
    Parameters
    ----------
    url : str
        A URL to make a request.
    attr : str
        The attribute that needs to be returned.
    
    Returns
    -------
    dict
        A dictionary of the attribute and associated data.
    """
    try:
        req = requests.get(url)
    except requests.exceptions.SSLError:
        req = requests.get(url, verify=False)
    json_response = json.loads(req.content.decode('utf-8'))
    data = {}
    for item in json_response:
        name = item.pop(attr)
        data[name] = item
    return data


def get_json(url):
    """
    Makes a request to the given URL and returns a parsed JSON object.
    
    Parameters
    ----------
    url : str
        A URL to make a request.
    
    Returns
    -------
    dict
        A parsed JSON object.
    """
    try:
        req = requests.get(url)
    except requests.exceptions.SSLError:
        req = requests.get(url, verify=False)
    json_resp = json.loads(req.content.decode('utf-8'))
    return json_resp


def get_json_return_df(url, transpose=True):
    """
    Makes a request to the given URL and returns a dataframe generated from the JSON response.
    
    Parameters
    ----------
    url : str
        A URL to make a request.
    transpose : bool, optional
        Transposes dataframe. Default is True.
    
    Returns
    -------
    DataFrame
        Dataframe generated from JSON response.
    
    Notes
    -----
    This is a private method.

    :meta private:
    """
    try:
        req = requests.get(url)
    except requests.exceptions.SSLError:
        req = requests.get(url, verify=False)
    try:
        df = pd.read_json(req.content, encoding='utf-8')
    except TypeError:
        df = pd.DataFrame.from_dict([req.json()])
    if transpose:
        df = df.transpose()
    return df
    
    
def get_data_in_dict(url, key = None, value = None):
    """
    Makes a request to the given URL and returns a dictionary of data.
    
    Parameters
    ----------
    url : str
        A URL to make a request.
    key : str, optional
        The item in the JSON to be used as the dictionary key.
    value : str, optional
        The item in the JSON to be used as the dictionary value.
    
    Returns
    -------
    dict
        A dictionary of returned data using the first item as the dictionary key by default.
    
    Notes
    -----
    This is a private method.
    
    :meta private:
    """
    json_list = get_json(url)
    if key is None:
        key = list(json_list[0].keys())[0]
    json_dict = {}
    if value is None:
        for js in json_list:
            json_dict[js.get(key)] = js
    else:
        for js in json_list:
            json_dict[js.get(key)] = js.get(value)
    return json_dict


def deal_with_url_error(url):
    """
    Makes a request to the given URL and returns a dataframe, ignoring SSL errors.
    
    Parameters
    ----------
    url : str
        A URL that returns a URL Error based on SSL errors.
    
    Returns
    -------
    DataFrame
        A dataframe from the URL with verify set to false.
    
    Notes
    -----
    This is a private method.
    
    :meta private:
    """
    req = requests.get(url, verify=False)
    s = str(req.content, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    return df


base_url = 'https://fingertips.phe.org.uk/api/'


