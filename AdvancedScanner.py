from socket import *
import sys
import optparse
from threading import *
from termcolor import colored

def ConnectionScan(ip,port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((ip,port))
        print(colored("[+] %d/tcp Open" %port, "green"))
        try:
            banner = sock.recv(1024)
            if banner:
                print(colored("[+]{}:{} " + banner.decode('utf-8').rstrip('\n'), "green").format(ip, port))
        except timeout as e:
            print(e)
    except:
        print(colored("[-] %d/tcp Closed" % port, "red"))
    finally:
        sock.close()
        

def PortScan(tgthost, tgtports):
    try:
        tgtIP = gethostbyname(tgthost)
    except:
        print("Unknown Host %s " %tgthost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan Results for: " + tgtName[0])
    except:
        print("[+] Scan Results for: " + tgtIP)

    setdefaulttimeout(1)
    for port in tgtports:
        t = Thread(target = ConnectionScan, args =(tgtIP, int(port)))
        t.start()

def main():
    parser = optparse.OptionParser("Usage: " + "-H <target host> -p <target port>")
    parser.add_option("-H", dest = "targetHost", type = "string", help = "specify target host")
    parser.add_option("-p", dest = "targetPort", type = "string", help = "specify taget ports separated by comma")
    parser.add_option("-i", dest = "initialHost", type = "int", help = "specify initial host")
    parser.add_option("-f", dest = "finalHost", type = "int", help = "specify final host")
    options, args = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(",")
    initialHost = options.initialHost
    finalHost = options.finalHost
    if(targetHost == None or targetPorts[0] == None):
        print(parser.usage)
        sys.exit()
    elif(initialHost == None or finalHost == None):
        PortScan(targetHost, targetPorts)
    else:
        for i in range(initialHost,finalHost + 1):
            ip = targetHost + str(i)
            PortScan(ip, targetPorts)


if __name__ == '__main__':
    main()
