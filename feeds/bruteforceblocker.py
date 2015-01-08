#!/usr/bin/env python

from core.common import retrieve_content
from core.common import BLACKLIST

__type__ = (BLACKLIST.IP,)
__url__ = "http://danger.rulez.sk/projects/bruteforceblocker/blist.php"
__check__ = "Last Reported"
__info__ = "brute forcer"
__reference__ = "danger.rulez.sk"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[BLACKLIST.IP][line.split('\t')[0]] = (__info__, __reference__)

    return retval
