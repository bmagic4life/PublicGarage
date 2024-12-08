The GZ Network

In this lab, I configured a network for the GeeZee (GZ) corporation, which consists of a corporate LAN with a GZ-Server and a GZ-Client. The GZ-CE router connects the LAN to the Internet. The GZ-Server provides HTTP service on port 80, and the Pub-Server accepts SSH connections at IP 2.2.2.2. I performed several tasks to set up and verify the network:

1. Set the hostnames of all routers, adding my initials.
2. Configured IP addresses on all router interfaces and ensured they were activated.
3. Verified the configuration using `show ip int brief` and tested one-hop pings across each link.
4. Configured static routes to ensure all devices could ping each other and meet the specified routing requirements.
5. Set an enable password for each router.
6. Enabled HTTP service on the GZ-Server and tested it using Telnet from the GZ-Client.
7. Configured and tested SSH access on the Pub-Router, verifying connectivity from the GZ-Client. 

This lab helped ensure proper connectivity and service between devices in the GZ corporate network.