# AdvancedScanner
Advanced TCP port Scan with options. 

Example 1:

py AdvancedScanner.py -H 192.168.1.254 -p 20,21,22,23,80,443,53

[+] Scan Results for: 192.168.1.254

[+] 80/tcp Open

[+] 53/tcp Open

[-] 22/tcp Closed

[-] 20/tcp Closed

[-] 21/tcp Closed

[-] 443/tcp Closed

[-] 23/tcp Closed

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Example 2:

py AdvancedScanner.py -H cisco.com -p 80,443

[+] Scan Results for: redirect-ns.cisco.com

[+] 80/tcp Open

[+] 443/tcp Open

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Example 3:
py AdvancedScanner.py -H 192.168.1.1 -i 1 -f 254 -p 80,443  

[+] Scan Results for: 192.168.1.11

[-] 80/tcp Closed
[-] 443/tcp Closed

[+] Scan Results for: 192.168.1.12
[-] 80/tcp Closed
[-] 443/tcp Closed

[+] Scan Results for: 192.168.1.13
[-] 80/tcp Closed
[-] 443/tcp Closed

[+] Scan Results for: 192.168.1.14
[-] 80/tcp Closed
[-] 443/tcp Closed

[+] Scan Results for: 192.168.1.15
[-] 443/tcp Closed
[-] 80/tcp Closed


