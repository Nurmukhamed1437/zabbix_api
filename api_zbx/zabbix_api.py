from pyzabbix import ZabbixAPI
from zabbix_api import 
ZABBIX_SERVER = 'http://172.31.22.230/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)

zapi.login('Admin','admin')

'''triggers = zapi.trigger.get(only_true=1,
                            skipDependent=1,
                            monitored=1,
                            active=1,
                            output='extend',
                            expandDescription=1,
                            selectHosts=['host'],
                            )'''

unack_triggers = zapi.trigger.get(only_true=1,
                                  withAcknowledgedEvents=1
                                  )
'''unack_trigger_ids = [t['triggerid'] for t in unack_triggers]
for t in triggers:
    t['unacknowledged'] = True if t['triggerid'] in unack_trigger_ids \
        else False'''
print(unack_triggers)
#print(triggers)
#print(unack_triggers)
