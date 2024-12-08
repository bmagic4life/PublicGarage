
Firewall with NAT Overview

In this lab, I configured a small internal corporate network using private IPs, involving a GZ-Server, GZ-Client, and a GZ-Firewall for network security and connectivity. The GZ-Server provides HTTP and HTTPS services, while the GZ-Client is part of the internal network. Additionally, a Public-Router and Public-Server are used to simulate external connections. The goal was to configure Network Address Translation (NAT) on the GZ-Firewall and implement Access Control Lists (ACLs) to control the flow of traffic between internal and external devices.

Key tasks included:
1. Configuring IP addresses and enabling HTTP/HTTPS services on the GZ-Server and Public-Server.
2. Setting up static routes on routers and GZ-Firewall for proper connectivity.
3. Configuring NAT on the GZ-Firewall to allow internal devices to access the internet using a public IP address via Port Address Translation (PAT).
4. Defining ACLs to control traffic, such as denying access to the GZ-Server HTTP service from specific IPs, allowing pings to/from GZ-Clients, and securing SSH access.
5. Testing the configuration by pinging, accessing services, and verifying the ACL rules.

This lab provided hands-on experience with firewall configurations, NAT, and ACL management, essential for securing and managing network traffic.
