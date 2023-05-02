# MPLS L3VPNs Deployment with Nornir

An MPLS Layer 3 Virtual Private Network (VPN) utilizes an MPLS provider core network to connect various sites. At each site, customer edge (CE) routers attach to one or more provider edge (PE) routers.

![topologoy](./topology/mpls-l3vpn.png)

An MPLS-based VPN operates at Layer 3 and follows a peer model, allowing the exchange of Layer 3 routing information between the service provider and the customer. The service provider transfers data between customer sites without customer involvement, making MPLS VPNs easier to manage and scale compared to traditional VPNs. Adding a new site to an MPLS VPN requires updating only the edge router of the service provider that serves that site.

The key components of an MPLS VPN are as follows:

* Provider (P) router: Located in the core of the provider network, this router performs MPLS switching and does not add VPN labels to routed packets. VPN labels help direct data packets to the correct private network or customer edge router.

* PE router: Attaches VPN labels and MPLS core labels to incoming packets based on the interface or subinterface where they were received. A PE router directly connects to a CE router.

* Customer (C) router: Found in the ISP or enterprise network.

* Customer edge (CE) router: Serves as the edge router on the ISP network, connecting to the PE router on the network. A CE router must interface with a PE router.