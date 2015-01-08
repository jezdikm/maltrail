#!/usr/bin/env python

import re

from core.common import retrieve_content
from core.common import BLACKLIST

__type__ = (BLACKLIST.IP,)
__url__ = "https://www.maxmind.com/en/anonymous_proxies"
__check__ = "Anonymous Proxies "
__info__ = "anonymous proxy"
__reference__ = "maxmind.com"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for match in re.finditer(r"proxy/([\d.]+)", content):
            retval[BLACKLIST.IP][match.group(1)] = (__info__, __reference__)

    return retval
