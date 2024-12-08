Frame Relay Configuration and EIGRP Routing

This lab focuses on configuring Frame Relay with point-to-point subinterfaces and integrating EIGRP (Enhanced Interior Gateway Routing Protocol) to enable communication between routers and end devices. The network consists of three routers interconnected using Frame Relay and subinterfaces, which allow the routers to communicate with each other using Permanent Virtual Circuits (PVCs). The lab also involves verifying the successful configuration of Frame Relay, ensuring that the routers can communicate, and that end devices like PCs and laptops can ping each other and the web server.

#### Key Objectives:
1. **Configure Frame Relay Encapsulation**: You will configure Frame Relay encapsulation on the routers to enable communication over the Frame Relay network.
   
2. **Configure Frame Relay Point-to-Point Subinterfaces**: Each router will be configured with two subinterfaces, each associated with a specific DLCI (Data Link Connection Identifier), to create separate logical links between the routers.
   
3. **Configure EIGRP Routing**: EIGRP will be enabled on each router to advertise the Frame Relay subnets and ensure that the routers can exchange routing information.

4. **Verification and Testing**: After configuring the network, you will verify the Frame Relay setup by checking the connection status and routing tables. You will also test the network by pinging between routers, as well as between the connected PCs, laptops, and the web server, to ensure full network connectivity.

This lab helps reinforce the concepts of Frame Relay networking and dynamic routing using EIGRP, with an emphasis on ensuring that the configuration works as expected through systematic testing and verification.