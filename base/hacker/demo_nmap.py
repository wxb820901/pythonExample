#!/usr/bin/env python
import nmap
# import nmap.py module
ip = '127.0.0.1'
nm = nmap.PortScanner() # instantiate nmap.PortScanner object
nm.scan(ip, '0-65000') # scan host 127.0.0.1, ports from 22 to 443
print(nm.command_line()) # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
print('----------------------------------------------------')
print(nm.scaninfo()) # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
print('----------------------------------------------------')
print(nm.all_hosts()) # get all hosts that were scanned
print('----------------------------------------------------')
print(nm[ip].hostname()) # get one hostname for host 127.0.0.1, usualy the user record
print('----------------------------------------------------')
print(nm[ip].hostnames()) # get list of hostnames for host 127.0.0.1 as a list of dict
print('----------------------------------------------------')
# [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
print(nm[ip].hostname()) # get hostname for host 127.0.0.1
print('----------------------------------------------------')
print(nm[ip].state()) # get state of host 127.0.0.1 (up|down|unknown|skipped)
print('----------------------------------------------------')
print(nm[ip].all_protocols()) # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
print('----------------------------------------------------')
print(nm[ip]['tcp'].keys()) # get all ports for tcp protocol
print('----------------------------------------------------')
print(nm[ip].all_tcp()) # get all ports for tcp protocol (sorted version)
print('----------------------------------------------------')
print(nm[ip].all_udp()) # get all ports for udp protocol (sorted version)
print('----------------------------------------------------')
print(nm[ip].all_ip()) # get all ports for ip protocol (sorted version)
print('----------------------------------------------------')
print(nm[ip].all_sctp()) # get all ports for sctp protocol (sorted version)
print('----------------------------------------------------')
print(nm[ip].has_tcp(22)) # is there any information for port 22/tcp on host 127.0.0.1
# nm[ip]['tcp'][22] # get infos about port 22 in tcp on host 127.0.0.1
# nm[ip].tcp(22) # get infos about port 22 in tcp on host 127.0.0.1
# nm[ip]['tcp'][22]['state'] # get state of port 22/tcp on host 127.0.0.1 (open


# a more usefull example :
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

# for proto in nm[host].all_protocols():
#     print('----------')
#     print('Protocol : %s' % proto)
#
# lport = nm[host][proto].keys()
# # lport.sort()
# for port in lport:
#     print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
#
# print('----------------------------------------------------')
# # print result as CSV
# print(nm.csv())
#
#
# print('----------------------------------------------------')
# # If you want to do a pingsweep on network 192.168.1.0/24:
# nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
# hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
# for host, status in hosts_list:
#     print('{0}:{1}'.format(host, status))
#
#
# print('----------------------------------------------------')
# # Asynchronous usage of PortScannerAsync
# nma = nmap.PortScannerAsync()
# def callback_result(host, scan_result):
#     print('----------------------------------------------------')
#     print(host, scan_result)
# nma.scan(hosts='192.168.1.0/30', arguments='-sP', callback=callback_result)
# while nma.still_scanning():
#     print("Waiting ...")
# nma.wait(2) # you can do whatever you want but I choose to wait after the end of the scan
