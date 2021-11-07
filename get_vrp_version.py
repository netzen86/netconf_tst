#!/usr/bin/env python3

import xmltodict
from pprint import pprint
from ncclient import manager


m = manager.connect(host='10.0.0.58', port=830, username='sgproot', password='Navy4ce', device_params={'name': 'huawei'})

vrp_version = '''
<system xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0"> 
    <systemInfo>
        <platformVer/>
    </systemInfo> 
</system> '''



get_ver = m.get(('subtree', vrp_version))
get_ver_pars = xmltodict.parse(str(get_ver))
pprint(get_ver_pars["rpc-reply"]["data"]["system"]["systemInfo"]["platformVer"])
