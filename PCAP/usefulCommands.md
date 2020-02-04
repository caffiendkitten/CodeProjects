This command gives info about the file and its read write ability
ls -alh sample-packets.pcap


The command below counts the total num of packets being used
tcpdump -qtnp -r sample-packets.pcap 2>/dev/null | wc -l


This code sorts and counts from the packet and shows a one line summery of the top 20.
tcpdump -qtnp -r sample-packets.pcap 2>/dev/null | egrep -v '(^ARP|ICMP6)' | sed -e 's/UDP,/udp/' | awk '{print $2 " " $5 "\n" $4 " " $5}' | sed -e 's/: / /' -e 's/^.*\.//' | sort | uniq -c | sort -nr | head -20


This command pulls out the 
tcpdump -qtnp -r sample-packets.pcap 'tcp port 443' 2>/dev/null | head -1
IP 10.0.0.60.64770 > 17.248.138.46.443: tcp 0
^^^the above line means this below
ID source address.port > destination ip.port: protocol used