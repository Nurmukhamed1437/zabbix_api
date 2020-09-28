from pyzabbix import ZabbixAPI
from pyparsing import *
import re
ZABBIX_SERVER = 'http://172.31.22.230/zabbix'
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('Admin','admin')

'''groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
	print group['groupid'],group['name']'''
#a = dict( eventids='16862',acknowledged=True)
#b = input("Enter event id")
triggers = str( zapi.event.get(
  
			select_acknowledges='extend',
			acknowledged = True,
			eventids = 17033			 		  
))



surname = re.findall(r'surname\'\:\ \u\'\w+', triggers)
surname = str(surname)
surname = surname.replace('[','')
surname = surname.replace(']','')
surname = surname.replace('"','')
surname = surname.replace('u','')
surname = surname.replace("'",'')
surname = surname.split(':')

surname = surname[-1]


print(surname)
f = open('surname.txt','w')
f.write(surname)
#print(triggers)
