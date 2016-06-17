""" Module for key definitions in the IGMspec database
"""
from __future__ import print_function, absolute_import, division, unicode_literals

from collections import OrderedDict

def z_priority():
    """ List of redshift priorities for setting the DB redshift
    Returns
    -------
    zpri : list

    """
    zpri = [
        str('BOSS_PCA'),   # PCA analysis by Paris et al. 2015 on BOSS spectra
        str('BOSS_PIPE'),  # BOSS Pipeline redshifts
        str('UNKN'),       # Unknown
    ]
    return zpri


def get_survey_dict():
    """ Return the survey dict
    Returns
    -------

    """
    survey_dict = OrderedDict()
    survey_dict['BOSS_DR12'] = 1
    survey_dict['SDSS_DR7'] = 2
    survey_dict['HD-LLS_DR1'] = 4   # Prochaska et al. 2015
    #
    return survey_dict


def survey_flag(survey, iflag=None):
    """ Defines bitwise survey flag for IGMspec
    Parameters
    ----------
    survey : str
      Name of the survey
    iflag : int, optional
    Returns
    -------
    flag_val : int

    """
    survey_dict = get_survey_dict()
    #
    return survey_dict[survey]

