PPP Configuration and OSPF Integration Lab  

#### Summary of Lab Objectives:  
This lab focuses on configuring Point-to-Point Protocol (PPP) with both unauthenticated and authenticated modes and setting up OSPF routing to enable communication across a network. Using Cisco Packet Tracer, the lab requires implementing a topology with three routers and two hosts. Key objectives include IP addressing, routing configuration, and testing connectivity.

---

### Key Steps and Configuration Details:  

1. **Network Design and Basic Setup**:  
   - Configure router hostnames with the format `<RouterName>-BS` (e.g., `R1-BS`).  
   - Assign IP addresses to all router and host interfaces based on the provided network diagram.  
   - Set default gateway addresses on hosts.  
   - Configure clock rates on the DCE ends of serial links.  

   **IP Address Assignments**:  
   - Ensure that all interfaces are correctly configured and verify with the `show ip int brief` command.  
   - Verify connectivity:  
     - Ping from hosts to their default gateways.  
     - Ping between directly connected router neighbors.  

2. **Unauthenticated PPP**:  
   - Configure PPP on all serial links without authentication.  
   - Verify proper operation by checking routing tables and confirming that directly connected subnets are listed using `show ip route`.  

3. **Dynamic Routing with OSPF**:  
   - Enable OSPF routing on all routers to allow end-to-end communication between the hosts.  
   - Verify connectivity by using ping and tracert between hosts.  

4. **Authenticated PPP Configuration**:  
   - Transition serial links to authenticated PPP:  
     - **Link 1**: Configure PAP authentication.  
       - R1 username: `R1-BS`  
       - R1 password: `R1-BS-pword`  
       - R2 username: `R2-BS`  
       - R2 password: `R2-BS-pword`  
     - **Link 2**: Configure CHAP authentication.  
       - Shared password: `ChapPass`  
   - On R1, use the `shutdown` and `no shutdown` commands to enable and verify serial links after authentication setup.  

5. **Final Testing**:  
   - Verify that authenticated PPP links operate correctly.  
   - Perform end-to-end connectivity tests between hosts using ping and tracert.  

---

This lab demonstrates configuring and verifying both unauthenticated and authenticated PPP links using PAP and CHAP. It integrates OSPF to establish seamless communication across the network while ensuring secure link authentication. The final deliverables include the completed Answers document and the configured Packet Tracer file.