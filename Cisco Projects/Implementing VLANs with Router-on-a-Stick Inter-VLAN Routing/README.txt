Implementing VLANs with Router-on-a-Stick Inter-VLAN Routing

Summary: I designed and configured a network using VLANs in a simulated environment. The network consists of three subnets (Students, Faculty, and Management), four hosts, three Layer 2 switches, and a router configured for inter-VLAN routing. Key steps included creating and naming VLANs, assigning VLAN access ports, configuring trunk ports, and setting up a router-on-a-stick to enable communication between VLANs.
Key Tasks:
	1	Pre-Configuration Tasks:
	◦	Defined subnet information and device IP addresses based on my assigned number.
	◦	Populated tables with subnet and MAC address details.
	2	Switch Configuration:
	◦	Created and named VLANs: VLAN 10 (Students), VLAN 20 (Faculty), and VLAN 99 (Management).
	◦	Assigned VLAN access ports and configured trunk ports for inter-switch connectivity.
	3	Router Configuration:
	◦	Implemented subinterfaces on the router to enable inter-VLAN communication.
	4	Testing and Validation:
	◦	Tested ping and traceroute between devices on the same and different VLANs to verify connectivity.
	◦	Validated switch configurations using commands like show vlan brief and show interface trunk.
	5	Final Documentation:
	◦	Completed and submitted answers based on observations and test results.
	◦	
This lab emphasized the fundamentals of VLANs, VLAN trunking, and inter-VLAN routing using the router-on-a-stick method, ensuring practical application of theoretical networking concepts.
