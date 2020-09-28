from pyzabbix import ZabbixAPI
z = ZabbixAPI('http://172.31.22.230/zabbix', user='Admin', password='admin')
answer = z.do_request('apiinfo.version')
print "Version:",answer['result']
