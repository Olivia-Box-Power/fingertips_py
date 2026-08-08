"""
Calls used to retrieve metadata about areas, ages, sexes, value notes, calculation methods, rates, and indicator
metadata.
"""

import pandas as pd
from urllib.error import HTTPError, URLError
from fingertips_py.api_calls import base_url, make_request, get_json, get_json_return_df, deal_with_url_error, get_data_in_dict


def get_all_ages(is_test=False):
    """
    Returns a dictionary of all the age categories and their IDs as the dictionary key.
    
    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        A dictionary of all values for the Age variable if is_test is False.
    tuple of (dict, str)
        A tuple of the expected return and the URL called to retrieve the data if is_test is True.

    """
    ages = get_data_in_dict(base_url + 'ages')
    if is_test:
        return ages, base_url + 'ages'
    return ages


def get_all_areas(is_test=False):
    """
    Retrieves all area types.

    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.

    Returns
    -------
    dict
        A dictionary of all values for the Area Type variable if `is_test` is False.
    tuple of (dict, str)
        A tuple of the expected return and the URL called to retrieve the data if `is_test` is True.
    """
    areas = make_request(base_url + 'area_types', 'Id')
    if is_test:
        return areas, base_url + 'area_types'
    return areas


def get_age_id(age, is_test=False):
    """
    Returns an ID based on the Age value given.
    
    Parameters
    ----------
    age : str
        Search term of an age or age range.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    int 
        The ID code for the selected Age value if `is_test` is False.
    tuple of (int, str)
        The Age value as a string if `is_test` is True.
    
    Examples
    --------
    >>> get_age_id('28 days - 1 yr', True)
    (295, 'https://fingertips.phe.org.uk/api/ages')
    >>> get_age_id('28 days - 1 yr')
    295
    """
    ages = make_request(base_url + 'ages', 'Name')
    if is_test:
        return ages[age]['Id'], base_url + 'ages'
    return ages[age]['Id']


def get_age_from_id(age_id, is_test=False):
    """
    Returns an Age name from given Age ID.
    
    Parameters
    ----------
    age_id : int
        Age id used in Fingertips.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    str
        Age, or age range if `is_test` is False.
    tuple of str
        A tuple of Age value and the URL called to retrieve the data if `is_test` is True.        
    """
    ages = make_request(base_url + 'ages', 'Id')
    if is_test:
        return ages[age_id]['Name'], base_url + 'ages'
    return ages[age_id]['Name']


def get_all_sexes(is_test=False):
    """
    Returns a dictionary of all sex categories and their IDs as dictionary key.
    
    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        Sex categories used in Fingertips with associated codes as a dictionary if `is_test` is False.
    tuple of (dict, str)
        A tuple of the expected return and the URL called to retrieve the data if is_test is True.
    """
    sexes = get_data_in_dict(base_url + 'sexes', value = 'Name')
    if is_test:
        return sexes, base_url + 'sexes'
    return sexes


def get_sex_id(sex, is_test=False):
    """
    Returns an ID for a given sex.
    
    Parameters
    ----------
    sex : str
        Sex category as string (Case sensitive).
    is_test : bool
        Used for testing to capture URL.
    
    Returns
    -------
    int
        ID used in Fingertips to represent Sex if `is_test` is False.
    tuple of (int, str)
        ID used in Fingertips to represent the Sex and the URL called to retrieve the data if `is_test` is True.
    """
    sexes = make_request(base_url + 'sexes', 'Name')
    if is_test:
        return sexes[sex]['Id'], base_url + 'sexes'
    return sexes[sex]['Id']


def get_sex_from_id(sex_id, is_test=False):
    """
    Returns a sex name given an ID.
    
    Parameters
    ----------
    sex_id : int
        ID used in Fingertips to represent the sex as integer.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    str
        Sex category if `is_test` is False.
    tuple of str
        Sex category and the URL called to retrieve the data if `is_test` is True.
    """
    sexes = make_request(base_url + 'sexes', 'Id')
    if is_test:
        return sexes[sex_id]['Name'], base_url + 'sexes'
    return sexes[sex_id]['Name']


def get_all_value_notes(is_test=False):
    """
    Returns a dictionary of all value notes and their IDs as dictionary key.
    
    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        Data value notes and their associated codes if `is_test` is False.
    tuple of (dict, str)
        Data value notes and their associated codes as a dictionary and the URL called to retrieve the data if `is_test` is True.
    """
    value_notes = get_data_in_dict(base_url + 'value_notes', value = 'Text')
    if is_test:
        return value_notes, base_url + 'value_notes'
    return value_notes


def get_value_note_id(value_note, is_test=False):
    """
    Returns a value note ID for a given value note.
    
    Parameters
    ----------
    value_note : str
        Value note as string.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    int
        ID used to represent the value note if `is_test` is False.
    tuple of (int, str)
        ID used  to represent the value note and the URL called to retrieve the data if `is_test` is True.
    """
    value_notes = make_request(base_url + 'value_notes', 'Text')
    if is_test:
        return value_notes[value_note]['Id'], base_url + 'value_notes'
    return value_notes[value_note]['Id']


def get_areas_for_area_type(area_type_id, is_test=False):
    """
    Returns a dictionary of areas that match an area type id given the id as integer or string.
    
    Parameters
    ----------
    area_type_id : int or str
        ID of area type (ID of General Practice is 7 etc) used in Fingertips as integer or string.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        A dictionary with area codes as the key if `is_test` is False.
    tuple of (dict, str)
        A dictionary with area codes as the key and the URL called to retrieve the data if `is_test` is True.
    """
    areas = make_request(base_url + 'areas/by_area_type?area_type_id=' + str(area_type_id), 'Code')
    if is_test:
        return areas, base_url + 'areas/by_area_type?area_type_id=' + str(area_type_id)
    return areas


def get_metadata_for_indicator(indicator_number, is_test=False):
    """
    Returns the metadata for an indicator given the indicator number as integer or string.
    
    Parameters
    ----------
    indicator_number : int or str
        Number used to identify an indicator within Fingertips as integer or string.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        Metadata for the given indicator if `is_test` is False.
    tuple of(dict, str)
        Metadata for the given indicator and the URL called to retrieve the data if is_test is True.
    """
    metadata = get_json(base_url + 'indicator_metadata/by_indicator_id?indicator_ids=' + str(indicator_number))
    metadata_dict = metadata.get(str(indicator_number))
    if is_test:
        return metadata, base_url + 'indicator_metadata/by_indicator_id?indicator_ids=' + str(indicator_number)
    return metadata_dict


def get_metadata_for_all_indicators_from_csv(is_test=False):
    """
    Returns a dataframe from the csv of all metadata for all indicators.
    
    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    DataFrame
        All metadata for all indicators if `is_test` is False.
    tuple of (DataFrame, str)
        A dataframe of all metadata for all indicators and the URL called to retrieve the data if is_test is True.
    """
    try:
        metadata = pd.read_csv(base_url + 'indicator_metadata/csv/all')
    except URLError:
        metadata = deal_with_url_error(base_url + 'indicator_metadata/csv/all')
    if is_test:
        return metadata, base_url + 'indicator_metadata/csv/all'
    return metadata


def get_metadata_for_all_indicators(include_definition=False, include_system_content=False, is_test=False):
    """
    Returns the metadata for all indicators in a dictionary.
    
    Parameters
    ----------
    include_definition : bool, optional
        Include definitions in the metadata.
    include_system_content : bool, optional
        Include system content in the metadata.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        Dictionary of all indicators if `is_test` is False.
    tuple of (dict, str)
        Dictionary of all indicators and the URL called to retrieve the data if `is_test` is True.
    """
    url_suffix = f'indicator_metadata/all?include_definition={"yes" if include_definition else "no"}&include_system_content={"yes" if include_system_content else "no"}'
    metadata_dict = get_json(base_url + url_suffix)
    if is_test:
        return metadata_dict, base_url + url_suffix
    return metadata_dict


def get_multiplier_and_calculation_for_indicator(indicator_number):
    """
    Returns the multiplier and confidence interval calculation method for a given indicator.
    
    Parameters
    ----------
    indicator_number : int or str
        Number used to identify an indicator within Fingertips as integer or string.
    
    Returns
    -------
    tuple of (int, str)
        A tuple of multiplier and confidence interval calculation method from Fingertips metadata.
    
    Notes
    -----
    The confidence interval calculation method only shows for indicators where 
    'Wilson' or 'Byar' have been used. It does not account for other methods such 
    as normal approximation. 
    """
    metadata = get_metadata_for_indicator(indicator_number)
    multiplier = metadata.get('Unit').get('Value')
    calc_metadata = metadata.get('ConfidenceIntervalMethod').get('Name')
    if 'wilson' in calc_metadata.lower():
        calc = 'Wilson'
    elif 'byar' in calc_metadata.lower():
        calc = 'Byar'
    else:
        calc = None
    return multiplier, calc


def get_area_types_as_dict(is_test=False):
    """
    Returns all area types and related information such as ID and name with dictionary key value as ID.
    
    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        A dictionary of area types if `is_test` is False.
    tuple of (dict, str)
        A dictionary of area types and the URL called to retrieve the data if `is_test` is True.
    """
    areas = get_data_in_dict(base_url + 'area_types')
    if is_test:
        return areas, base_url + 'area_types'
    return areas


def get_profile_by_id(profile_id, is_test=False):
    """
    Returns a profile as a dictionary which contains information about domains and sequencing.
    
    Parameters
    ----------
    profile_id : int or str
        ID used in Fingertips to identify a profile as integer or string.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        Information about the profile if `is_test` is False.
    tuple of (dict, str)
        Information about the profile and the URL called to retrieve the data if `is_test` is True.
    """
    if is_test:
        return get_json(base_url + 'profile?profile_id=' + str(profile_id)), base_url + 'profile?profile_id=' + \
               str(profile_id)
    return get_json(base_url + 'profile?profile_id=' + str(profile_id))


def get_all_profiles(is_test=False):
    """
    Returns all profiles.
    
    Parameters
    ----------
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    dict
        All Fingertips profiles if `is_test` is False.
    tuple of (dict, str)
        All Fingertips profiles and the URL called to retrieve the data if `is_test` is True.
    """
    profiles = get_data_in_dict(base_url + 'profiles')
    if is_test:
        return profiles, base_url + 'profiles'
    return profiles


def get_domains_in_profile(profile_id):
    """
    Returns the domain IDs for a given profile.
    
    Parameters
    ----------
    profile_id : int or str
        ID used in Fingertips to identify a profile as integer or string.
    
    Returns
    -------
    list
        A list of domain IDs.
    """
    profile = get_profile_by_id(profile_id)
    return profile['GroupIds']


def get_area_types_for_profile(profile_id, is_test=False):
    """
    Retrieves all the area types that have data for a given profile.
    
    Parameters
    ----------
    profile_id : int or str
        ID used in Fingertips to identify a profile as integer or string.
    is_test : bool
        Used to retrieve the associated URL.
    
    Returns
    -------
    list
        A list of dictionaries of area types with relevant information if `is_test` is False.
    tuple of (list, str)
        A list of dictionaries of area types with relevant information and the URL called to retrieve the data if `is_test` is True.
    """
    if is_test:
        return get_data_in_dict(base_url + 'area_types?profile_ids=' + str(profile_id)), base_url + 'area_types?profile_ids=' + \
               str(profile_id)
    return get_data_in_dict(base_url + 'area_types?profile_ids=' + str(profile_id))


def get_area_type_ids_for_profile(profile_id):
    """
    Returns a list of area types used within a given profile.
    
    Parameters
    ----------
    profile_id : int or str
        ID used in Fingertips to identify a profile as integer or string.
    
    Returns
    -------
    list
        A list of area type IDs used within a given profile.
    """
    area_type_obj = get_area_types_for_profile(profile_id)
    area_type_list = [value.get('Id') for value in area_type_obj.values()]
    return area_type_list


def get_profile_by_name(profile_name):
    """
    Returns a profile object given a name to search for.
    
    Parameters
    ----------
    profile_name : str
        A string or part of a string that is used as the profile name.
    
    Returns
    -------
    dict
        A dictionary of the profile metadata including domain information or an error message.
    
    Notes
    -----
    For better results, try to be specific with the profile name.
    """
    all_profiles = get_all_profiles()
    profile_obj = ''
    for profile in all_profiles.values():
        if profile_name.lower() in profile.get('Name').lower():
            profile_obj = profile
    if not profile_obj:
        return 'Profile could not be found'
    else:
        return profile_obj


def get_profile_by_key(profile_key):
    """
    Returns a profile object given a key (as the stub following 'profile' in the website URL).
    
    Parameters
    ----------
    profile_key : str
        The exact key for the profile.
    
    Returns
    -------
    dict
        A dictionary of the profile metadata including domain information or an error message.
    
    Notes
    -----
    For example,
    Profile keys can be found in the Fingertips URL. For example, for `https://fingertips.phe.org.uk/profile/general-practice/data#page/3/gid/2000...`,
    the key is 'general-practice'.
    """
    all_profiles = get_all_profiles()
    for profile_id, profile_object in all_profiles.items():
        if profile_object.get('Key') == profile_key:
            return profile_object
    return 'Profile could not be found'


def get_metadata_for_indicator_as_dataframe(indicator_ids, is_test=False):
    """
    Returns a dataframe of metadata for a given indicator ID or list of indicator IDs.
    
    Parameters
    ----------
    indicator_ids : int, str, or list of (int or str)
        Number or list of numbers used to identify an indicator within Fingertips
    
    Returns
    -------
    DataFrame
        Dataframe object with metadata for the indicator ID if `is_test` is False.
    tuple of (DataFrame, str)
        A tuple of the dataframe object with metadata for the indicator ID and the URL called to retrieve the data if `is_test` is True.
    """
    url_suffix = "indicator_metadata/csv/by_indicator_id?indicator_ids={}"
    if isinstance(indicator_ids, list):
        indicator_ids = ','.join(list(map(str, indicator_ids)))
    try:
        df = pd.read_csv(base_url + url_suffix.format(str(indicator_ids)))
    except HTTPError:
        raise NameError(f'Indicator {indicator_ids} does not exist')
    except URLError:
        df = deal_with_url_error(base_url + url_suffix.format(str(indicator_ids)))
    if is_test:
        return df, base_url + url_suffix.format(str(indicator_ids))
    return df


def get_metadata_for_domain_as_dataframe(group_ids, is_test=False):
    """
    Returns a dataframe of metadata for a given domain ID or list of domain IDs.
    
    Parameters
    ----------
    group_ids : int, str, or list of int or str
        Number or list of numbers used to identify a domain within Fingertips as integer or string.
    
    Returns
    -------
    DataFrame
        Metadata for the indicators for a given domain ID if `is_test` is False.
    tuple of (DataFrame, str)
        Metadata for the indicators for a given domain ID and the URL called to retrieve the data if `is_test` is True.
    """
    url_suffix = "indicator_metadata/csv/by_group_id?group_id={}"
    if isinstance(group_ids, list):
        df = pd.DataFrame()
        for group_id in group_ids:
            try:
                df = pd.concat([df, pd.read_csv(base_url + url_suffix.format(str(group_id)))])
            except HTTPError:
                raise NameError(f'Domain {group_id} does not exist')
            except URLError:
                df = deal_with_url_error(base_url + url_suffix.format(str(group_id)))
    else:
        try:
            df = pd.read_csv(base_url + url_suffix.format(str(group_ids)))
        except HTTPError:
            raise NameError(f'Domain {group_ids} does not exist')
        except URLError:
            df = deal_with_url_error(base_url + url_suffix.format(str(group_ids)))
    if is_test:
        return df, base_url + url_suffix.format(str(group_ids))
    return df


def get_metadata_for_profile_as_dataframe(profile_ids):
    """
    Returns a dataframe of metadata for a given profile ID or list of profile IDs.
    
    Parameters
    ----------
    profile_ids : int, str, or list of (int or str)
        ID or list of IDs used in Fingertips to identify a profile as integer or string.
    
    Returns
    -------
    DataFrame
        Metadata for the indicators for a given group ID.
    """
    url_suffix = "indicator_metadata/csv/by_profile_id?profile_id={}"
    if isinstance(profile_ids, list):
        df = pd.DataFrame()
        for profile_id in profile_ids:
            try:
                df = pd.concat([df, pd.read_csv(base_url + url_suffix.format(str(profile_id)))])
            except HTTPError:
                raise NameError(f'Profile {profile_id} does not exist')
            except URLError:
                df = deal_with_url_error(base_url + url_suffix.format(str(profile_id)))
    else:
        try:
            df = pd.read_csv(base_url + url_suffix.format(str(profile_ids)))
        except HTTPError:
            raise NameError(f'Profile {profile_ids} does not exist')
        except URLError:
            df = deal_with_url_error(base_url + url_suffix.format(str(profile_ids)))
    return df


def get_metadata(indicator_ids=None, domain_ids=None, profile_ids=None):
    """
    Returns a dataframe object of metadata for a given indicator, domain, and/or profile given the relevant IDs. At
    least one of these IDs has to be given otherwise an error is raised.
    
    Parameters
    ----------
    indicator_ids : int, str, or list of int or str, optional
        Number used to identify an indicator within Fingertips as integer or string.
    domain_ids : int, str, or list of int or str, optional
        Number used to identify a domain within Fingertips as integer or string.
    profile_ids : int, str, or list of int or str, optional
        ID used in Fingertips to identify a profile as integer or string.
    
    Returns
    -------
    DataFrame
        Metadata for the given IDs.
    
    Raises
    ------
    NameError
        If no IDs are provided.
    """
    if indicator_ids and domain_ids and profile_ids:
        df = get_metadata_for_profile_as_dataframe(profile_ids)
        df = pd.concat([df, get_metadata_for_domain_as_dataframe(domain_ids)])
        df = pd.concat([df, get_metadata_for_indicator_as_dataframe(indicator_ids)])
        return df
    if indicator_ids and domain_ids:
        df = get_metadata_for_domain_as_dataframe(domain_ids)
        df = pd.concat([df, get_metadata_for_indicator_as_dataframe(indicator_ids)])
        return df
    if indicator_ids and profile_ids:
        df = get_metadata_for_profile_as_dataframe(profile_ids)
        df = pd.concat([df, get_metadata_for_indicator_as_dataframe(indicator_ids)])
        return df
    if domain_ids and profile_ids:
        df = get_metadata_for_profile_as_dataframe(profile_ids)
        df = pd.concat([df, get_metadata_for_domain_as_dataframe(domain_ids)])
        return df
    if profile_ids:
        return get_metadata_for_profile_as_dataframe(profile_ids)
    if domain_ids:
        return get_metadata_for_domain_as_dataframe(domain_ids)
    if indicator_ids:
        return get_metadata_for_indicator_as_dataframe(indicator_ids)
    if not indicator_ids and not domain_ids and not profile_ids:
        raise NameError("At least one of indicator_ids, domain_ids, or profile_ids must be provided.")
