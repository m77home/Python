# Ethical Hacking With Kali

## Change MAC address
iwconfig to get wireless adapter name

'''
ifconfig wlan0 down

macchanger --random wlan0

ifconfig wlan0 up
'''

## Enable monitor mode
airmon-ng start wlan0
airmon-ng stop wlan0mon

ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up


