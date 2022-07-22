# MPLS L3VPNs Deployment with Nornir

A Multiprotocol Label Switching (MPLS) Layer 3 Virtual Private Network (VPN) consists of a set of sites that are interconnected by means of an MPLS provider core network. At each customer site, one or more customer edge (CE) routers attach to one or more provider edge (PE) routers. 

![topologoy](./topology/mpls-l3vpn.png)

MPLS-based VPNs are created in Layer 3 and are based on the peer model. The peer model enables the service provider and the customer to exchange Layer 3 routing information. The service provider relays the data between the customer sites without customer involvement.

MPLS VPNs are easier to manage and expand than conventional VPNs. When a new site is added to an MPLS VPN, only the edge router of the service provider that provides services to the customer site needs to be updated.

The components of the MPLS VPN are described as follows:

* Provider (P) router—Router in the core of the provider network. PE routers run MPLS switching and do not attach VPN labels to routed packets. VPN labels are used to direct data packets to the correct private network or customer edge router.

* PE router—Router that attaches the VPN label to incoming packets based on the interface or subinterface on which they are received, and also attaches the MPLS core labels. A PE router attaches directly to a CE router.

* Customer (C) router—Router in the Internet service provider (ISP) or enterprise network.

* Customer edge (CE) router—Edge router on the network of the ISP that connects to the PE router on the network. A CE router must interface with a PE router.

## Getting Started

### Clone Repo

```bash
git clone https://github.com/sbarissonmez/mpls-l3vpns-deploy.git
cd auto_mpls_l3vpn
```
### Create venv

```bash
python3 -m venv venv
```

### Activate venv

```bash
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

