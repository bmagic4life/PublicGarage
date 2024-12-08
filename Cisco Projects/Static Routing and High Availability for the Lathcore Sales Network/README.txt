
### Summary:  
In this lab I configured and tested static routing for a simulated multi-site network. This lab focused on enabling communication between three geographically dispersed sites (Los Angeles, Chicago, and Washington, DC) using IPv4 and IPv6. Additionally, I implemented floating static routes to ensure high availability in case of link failure, adhering to the lab’s requirements for shortest path routing and failover capabilities.

---

### Key Tasks:

#### Pre-Configuration Steps:
1. **Subnet Planning**:  
   - Completed IPv4 and IPv6 subnet allocation in **Table #1a** and **Table #1b**, ensuring compliance with the lab's address requirements.
   - Assigned appropriate IP addresses for all devices, detailed in **Table #2a** (IPv4) and **Table #2b** (IPv6). 

2. **Static Route Planning**:  
   - Mapped out IPv4 and IPv6 static routes required for shortest path routing.  
   - Included floating static routes with higher administrative distances to maintain connectivity during link failure.  
   - Documented routes in **Table #3a** (IPv4) and **Table #3b** (IPv6).

---

#### Implementation Steps:
1. **Device Configuration**:  
   - Configured hostnames for all routers and switches based on their location and initials.  
   - Set up VLAN1 SVI and interface IP addresses for each device.  
   - Activated IPv6 unicast routing on dual-stack routers (Chicago and DC).  

2. **Routing**:  
   - Added static routes to all routers, specifying shortest path routes for normal operation and floating static routes as backups.

3. **Testing**:  
   - Verified Layer 1 connectivity (interface status).  
   - Conducted Layer 2 and Layer 3 checks using commands like `show ip interface brief` and `ping`.  
   - Performed traceroute tests to confirm packets followed the shortest path.

4. **Failover Testing**:  
   - Simulated link failure on S-Link 1 by shutting down the LA router’s interface.  
   - Validated that floating static routes maintained network connectivity.

---

### Learning Outcomes:  
This lab reinforced my skills in static routing, subnet planning, and high availability configurations. I demonstrated the ability to design and implement a resilient network that supports both IPv4 and IPv6 communication, meeting the requirements for shortest path routing and failover capabilities.