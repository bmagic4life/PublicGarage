ISP Network Configuration and OSPF Routing Lab

#### Summary of Lab Objectives:  
This lab involves configuring and verifying a simulated ISP network using Cisco Packet Tracer. The network includes ISP routers in four locations: San Francisco (SF), Los Angeles (LA), Chicago (CHI), and Texas (TX). It also connects a customer home network and a Chicago server. The lab focuses on designing the network topology, configuring IP addressing, and implementing OSPF dynamic routing.

Key objectives include:  

1. **Network Design**:  
   - Establish physical connections using correct cable types.  
   - Assign IP addresses to Layer 3 interfaces and set default gateways:  
     - **SF Host**: `44.1.1.10/24`, Default Gateway: `44.1.1.1`  
     - **Home Router VLAN1**: `44.1.1.1/24`  
     - **Home Router Fa0/0**: `69.12.55.18/30`  
     - **SF Fa0/0**: `69.12.55.17/30`  
     - **SF Gi0/2/0**: `100.x.1.1/30`  
     - **SF Se0/1/0**: `100.x.1.13/30`  
     - **LA Gi0/2/0**: `100.x.1.2/30`  
     - **LA Gi0/3/0**: `100.x.1.5/30`  
     - **TX Gi0/2/0**: `100.x.1.6/30`  
     - **TX Gi0/3/0**: `100.x.1.10/30`  
     - **CHI Se0/1/0**: `100.x.1.14/30`  
     - **CHI Gi0/2/0**: `77.3.1.1/24`  
     - **CHI Gi0/3/0**: `100.x.1.9/30`  
     - **CHI Server**: `77.3.1.10/24`, Default Gateway: `77.3.1.1`  

2. **Interface and Link Configuration**:  
   - Configure serial links with clock rates (`4000000` bps) and bandwidth (`4000 Kbps`).  
   - Set PPP encapsulation for serial connections between SF and CHI.  
   - Verify connectivity through ping tests between routers and hosts.  

3. **Dynamic Routing with OSPF**:  
   - Enable OSPF on all ISP routers with assigned Router IDs:  
     - SF: `1.1.1.1`  
     - LA: `2.2.2.2`  
     - CHI: `3.3.3.3`  
     - TX: `4.4.4.4`  
   - Set specific interfaces (e.g., SF Fa0/0 and CHI Gi0/2/0) as passive.  
   - Redistribute static routes to integrate the home network into the OSPF domain.  

4. **Network Functionality Testing**:  
   - Verify routing tables and confirm connectivity between all network components.  
   - Test end-to-end communication, ensuring successful pings from the SF Host to the Chicago Server.  

This lab illustrates the configuration of a robust ISP network, integrating static and dynamic routing protocols to ensure seamless communication across multiple locations.