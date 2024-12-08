Configuring Multi-Area OSPF with Cisco Packet Tracer

### Summary:  
This lab focused on implementing and testing a multi-area OSPF network using Cisco Packet Tracer. The lab included configuring a network based on a provided diagram and IP addressing requirements, with specific attention to the segmentation of OSPF areas and proper subnet allocation.  

The network was divided into two OSPF areas: Area 2 (containing Subnet A, Link 1, Link 2, Link 3, and Router R1 and R2 Loopback0 interfaces) and Area 0 (containing Subnets B and C and Router R3 and R4 Loopback0 interfaces). The DCE interfaces were assigned higher IPs in their respective subnets, and the FastEthernet interfaces were configured with the first and second valid host IPs, respectively.  

### Steps Performed:  
1. **Network Setup:**  
   - Connected all routers and switches as per the diagram.  
   - Configured hostnames, interface IPs, and default gateways.  
   - Ensured correct clock rates on DCE ends of serial links and verified the connectivity using pings.  
   - Verified directly connected subnets in routing tables using the `show ip route` command.  

2. **OSPF Configuration:**  
   - Activated OSPF process #50 on all routers and manually set unique router IDs (e.g., 1.1.1.1 for R1).  
   - Assigned interfaces to their respective OSPF areas based on the diagram.  
   - Set the 4 Loopback interfaces, R1 Fa0/0, and R4 Fa0/0 as passive.  
   - Verified OSPF activation, inclusion of correct subnets, and adjacency formation with the `show ip protocol` and `show ip ospf neighbor` commands.  

3. **Testing and Analysis:**  
   - Verified interface configurations and routing tables.  
   - Answered all questions in the accompanying documentation and adjusted configurations as necessary.  
