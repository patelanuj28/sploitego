#!/usr/bin/env python

from sploitego.cmdtools.nmap import NmapReportParser
from canari.framework import configure, superuser
from canari.maltego.entities import IPv4Address
from canari.maltego.message import UIMessage
from common.nmap import addreport, getscanner


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__author__ = 'Nadeem Douba'

__all__ = [
    'dotransform'
]


@superuser
@configure(
    label='To Nmap Report [Nmap -F]',
    description='This transform performs an active Nmap scan.',
    uuids=[ 'sploitego.v2.IPv4AddressToNmapReport_NmapF' ],
    inputs=[ ( 'Reconnaissance', IPv4Address ) ],
)
def dotransform(request, response):
    s = getscanner()
    args = ['-n', '-F', request.value] + request.params
    r = s.scan(args, NmapReportParser)
    if r is not None:
        addreport(r, response, ' '.join(args), s.cmd)
    else:
        response += UIMessage(s.error)
    return response


