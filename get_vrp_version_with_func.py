#!/usr/bin/env python3

import xmltodict
import yaml
from pprint import pprint
from ncclient import manager


def get_nc_vrp_ver(devices):
    with manager.connect(host=devices["host"], port=devices["port"], username=devices["username"], password=devices["password"], device_params=devices["device_params"]) as m:
        vrp_version = '''
        <system xmlns="http://www.huawei.com/netconf/vrp" format-version="1.0" content-version="1.0"> 
            <systemInfo>
                <platformVer/>
            </systemInfo> 
        </system> '''
        get_ver = m.get(('subtree', vrp_version))
        get_ver_pars = xmltodict.parse(str(get_ver))
    return get_ver_pars["rpc-reply"]["data"]["system"]["systemInfo"]["platformVer"]

if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        #print(devices)
    print(get_nc_vrp_ver(*devices))