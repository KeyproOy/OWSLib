# -*- coding: utf-8 -*-
# =============================================================================
# Copyright (c) 2004, 2006 Sean C. Gillies
# Copyright (c) 2009 STFC <http://www.stfc.ac.uk>
#
# Authors :
#          Dominic Lowe <dominic.lowe@stfc.ac.uk>
#
# Contact email: dominic.lowe@stfc.ac.uk
# =============================================================================

"""
Web Feature Server (WFS) methods and metadata. Factory function.
"""

from __future__ import (absolute_import, division, print_function)

from .feature import wfs100, wfs110, wfs200


def WebFeatureService(url, version='1.0.0', xml=None, parse_remote_metadata=False,
                      timeout=30, username=None, password=None, req_kwargs=None):
    ''' wfs factory function, returns a version specific WebFeatureService object

    @type url: string
    @param url: url of WFS capabilities document
    @type xml: string
    @param xml: elementtree object
    @type parse_remote_metadata: boolean
    @param parse_remote_metadata: whether to fully process MetadataURL elements
    @param timeout: time (in seconds) after which requests should timeout
    @param username: service authentication username
    @param password: service authentication password
    @param req_kwargs: a dictionary of additional HTTP requests parameters
    @return: initialized WebFeatureService_2_0_0 object
    '''
    kwargs = {
        'timeout': timeout,
        'username': username,
        'password': password,
        'req_kwargs': req_kwargs,
    }
    if version in  ['1.0', '1.0.0']:
        return wfs100.WebFeatureService_1_0_0(url, version, xml, parse_remote_metadata, **kwargs)
    elif version in  ['1.1', '1.1.0']:
        return wfs110.WebFeatureService_1_1_0(url, version, xml, parse_remote_metadata, **kwargs)
    elif version in ['2.0', '2.0.0']:
        return wfs200.WebFeatureService_2_0_0(url,  version, xml, parse_remote_metadata, **kwargs)
