#!/usr/bin/python3
import nmap3
import pprint
from datetime import datetime
now = datetime.now()
import pyfiglet
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
nmap = nmap3.Nmap()
from time import sleep
pyfiglet.print_figlet("Python  Nmap")
pp = pprint.PrettyPrinter(indent=4)
print(" Nmap Scan \n Choose the option")
print('------------------------------------------------------------------')
answer = input("   [1] OS and Version detection \n   [2] Port Scan \n   [3] Host Discovery \n   [4] Scan Techniques \n   [5] Exit Scanner \n  Which do you want:\n Enter a number : ") 
if answer == "q":
    sleep(0.5)
    print("\nAbort.")
    #exit()
print('\n------------------------------------------------------------------------------')


#[1] OS detection
if answer == "1":
    sleep(0.5)
    ask = input("\nConfigure OS Detection Scan: \n   [1] Enable OS detection (-O) \n   [2] Enable Service Version detection (-sV) \n   [3] Identify Nmap's Version (-V) \n   [q] Quit Scan \n   Choose an option: ")
   
    if ask == "1":
        print('\n--------------------------------------------')
        sleep(0.5)
        print("\nOS detection (-O) ✅")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_os_detection(hostname)
        pp.pprint(results)

    elif ask == "2":

        sleep(0.5)
        print('\n--------------------------------------------')
        sleep(0.5)
        print("\nService Version detection (-sV) ✅ ")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        
        print('\n-------------------------------------------')
        sleep(0.5)
        
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_version_detection(hostname)
        print(results)
           # exit()
    elif ask == "3":
        sleep(0.5)
        print('\n-------------------------------------------')
        sleep(0.5)
        print("\nIdentify Nmap's Version (-V) ✅")
        print('\n-----------------------------------------')
        print("\nNmap scan initiated at: " + dt_string)
        a = nmap.nmap_version()
        print ("\nThe version of Nmap running on this system is: " + str(a))

if answer == "2":
    sleep(0.5)
    ask2 = input("\nConfigure Port Scan: \n   [1] Fast Scan - 100 ports (-F) \n   Choose an option: ")
    if ask2 == "1":
        print('\n--------------------------------------------')
        sleep(0.5)
        print("\nFast Scan - 100 ports (-F) ✅")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        print('\n---------------------------------------------')
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.scan_top_ports(hostname)
        pp.pprint(results)

#[3] Host Discovery
if answer == "3":
    sleep(0.5)
    ask3 = input("Configure Host Discovery Scan: \n   [1] Only port scan (-Pn) \n   [2] Only host discover (-sn) \n   [3] ARP Discovery \n   [4] Disable DNS (-n) \n   Choose an option: ")
    if ask3 == "1":
        print('\n---------------------------------------------')
        sleep(0.5)
        print("\nOnly port scan (-Pn) ✅")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapHostDiscovery()
        print('\n-----------------------------------------------')
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_portscan_only(hostname)
        pprint(results)
           # exit()
    elif ask3 == "2": 
        print('\n---------------------------------------------')
        sleep(0.5)
        print("\nOnly host discover(-sn) ✅ ")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapHostDiscovery()
        print('\n-----------------------------------------------')
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_no_portscan(hostname)
        print(results)
            #exit()
    elif ask3 == "3":
        print('\n--------------------------------------------')
        sleep(0.5)
        print("\nARP Discovery (-PR) ✅ ")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapHostDiscovery()
        print('\n-----------------------------------------------')
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_arp_discovery(hostname)
        print(results)
           # exit()
    elif ask3 == "4":
        print('\n--------------------------------------------')
        sleep(0.5)
        print("\nDisable Dns (-n) ✅ ")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapHostDiscovery()
        print('\n-----------------------------------------------')
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_disable_dns(hostname)
        print(results)

#[4] Scan Techniques
if answer == "4":
    sleep(0.5)
    ask4 = input("\nConfigure Nmap Scan Techniques: \n   [1] TCP Scan (-sT) \n   [2] UDP Scan (-sU) \n   [3] SYN Scan (-sS) \n   [4] Ping Scan (-sP) \n   [5] Fin Scan (-sF) \n   [6] Idle Scan (-sL) \n   [q] Quit Scan \n   Enter a number: ")

    if ask4 == "1":
        print('\n---------------------------------------------')
        sleep(0.5)
        print("\nTCP Scan (-sT) ✅")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapScanTechniques()
        print('\n------------------------------------------------')
        sleep(0.5)
        pprint("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_tcp_scan(hostname, args = "-T4")
        pprint(results)
           # exit()

    elif ask4 == "2":
        sleep(0.5)
        print('\n------------------------------------------------')
        print("\nUDP Scan (-sU) ✅")
        sleep(0.5)
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapScanTechniques()
        print('\n--------------------------------------------------')
        sleep(0.5)
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_udp_scan(hostname, args = "-T4")
        print(results)
        
    elif ask4 == "3":
        sleep(0.5)
        print('\n------------------------------------------------')
        print("\nSYN Scan (-sS) ✅")
        hostname = input("Enter the target's IP Address or domain: ")
        nmap = nmap3.NmapScanTechniques()
        print('\n-------------------------------------------------')
        sleep(0.5)
        print("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_syn_scan(hostname, args = "-T4")
        pprint(results)
          #  exit()
    elif ask4 == "4":
        sleep(0.5)
        print('\n-------------------------------------------')
        print("\nPing Scan (-sP) ")
        hostname = input("Enter the target's IP Address or domain:  ")
        nmap = nmap3.NmapScanTechniques()
        print('\n--------------------------------------------')
        sleep(0.5)
        pprint("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_ping_scan(hostname, args = "-T4")
        pprint(results)
           # exit()
    elif ask4 == "5":
        sleep(0.5)
        print('\n-------------------------------------------')
        print("\nFIN Scan (-sF) ✅")
        hostname = input("Enter the target's IP Address or domain:  ")
        nmap = nmap3.NmapScanTechniques()
        print('\n--------------------------------------------')
        sleep(0.5)
        pprint("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_fin_scan(hostname, args = "-T4")
        pprint(results)
            #exit()
    elif ask4 == "6":
        sleep(0.5)
        print('\n-------------------------------------------')
        print("\nIdle Scan (-sL) ✅")
        hostname = input("Enter the target's IP Address or domain:  ")
        nmap = nmap3.NmapScanTechniques()
        print('\n--------------------------------------------')
        sleep(0.5)
        pprint("\nNmap scan initiated at: " + dt_string)
        results = nmap.nmap_idle_scan(hostname, args = "-T4")
        pprint(results)
#[5] Exit
if answer == "5":
    sleep(0.5)
    print("\nAbort.")