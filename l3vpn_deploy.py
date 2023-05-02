"""
This script is designed for deploying MPLS L3VPNs using the Nornir automation framework.
"""

from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result
from net_utils import address, mask


def l3vpn(task):

    """
    This is the main function created for L3VPN deployment tasks.
    """
    task1_result = task.run(
        name=f"{task.host.name}: VRFs Configuration Creating",
        task=template_file,
        template="vrf.j2",
        path="templates/",
        data=task.host["vrfs"],
    )
    vrf_config = task1_result[0].result

    task2_result = task.run(
        name=f"{task.host.name}: VRFs Configuring on PE Router",
        task=send_configs,
        configs=vrf_config.split("\n"),
    )

    task3_result = task.run(
        name=f"{task.host.name}: VRFs Create for Interfaces Configuration",
        task=template_file,
        template=f"interfaces.j2",
        path="templates/",
        data=task.host.data,
        address=address,
        mask=mask,
    )
    int_config = task3_result[0].result

    task4_result = task.run(
        name=f"{task.host.name}: Interfaces VRFs Configuration",
        task=send_configs,
        configs=int_config.split("\n"),
    )

    task5_result = task.run(
        name=f"{task.host.name}: BGP Neighbor Configuration Create",
        task=template_file,
        template=f"bgp.j2",
        path="templates/",
        data=task.host.data,
    )
    bgp_config = task5_result[0].result

    task6_result = task.run(
        name=f"{task.host.name}: BGP Neighbors Configuring on VRFs",
        task=send_configs,
        configs=bgp_config.split("\n"),
    )

    backup_result = task.run(
        name="Get Configuration", task=napalm_get, getters=["config"]
    )

    task.run(
        task=write_file,
        content=str(backup_result[0].result["config"]["running"]),
        filename=f"backups/{task.host.name}_CFG.txt",
    )


def main():

    """
    This is the main function that invokes the L3VPN function.
    """

    nornir = InitNornir(config_file="config.yaml")
    print("Nornir initialized with the following hosts:\n")
    for host in nornir.inventory.hosts.keys():
        print(f"{host}\n")

    result = nornir.run(task=l3vpn)

    print_result(result)


if __name__ == "__main__":
    main()
