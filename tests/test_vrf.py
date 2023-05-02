import os
import yaml
from rich import print as pretty
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from ntc_templates.parse import parse_output


main_vrfs = []

# The following code snippet creates a list of VRFs that are defined in the "groups.yaml" configuration file.

with open("groups.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)["pe"]["data"]["vrfs"]
    for vrf in data:
        main_vrfs.append(vrf["name"])


def test_vrf():

    """
    This is the main function for testing VRFs.
    """
    os.environ[
        "NET_TEXTFSM"
    ] = "./venv/lib/python3.9/site-packages/ntc_templates/templates"

    nornir = InitNornir(config_file="config.yaml")

    result = nornir.run(
        name="GET VRF",
        task=send_command,
        command="show vrf",
    )

    for host in nornir.inventory.hosts.keys():
        remote_vrfs = []
        vrf_parsed = parse_output(
            platform="cisco_ios", command="show vrf", data=result[host].result
        )

        # This code loops through all parsed VRFs and creates a new list based on the results.
        for remote_vrf in vrf_parsed:
            remote_vrfs.append(remote_vrf["name"])

        set_diff = set(main_vrfs) - set(remote_vrfs)

        # If the program detects a set difference, it will display a visually distinct red output to alert the user.
        if set_diff:
            pretty(
                f"[bold red]The VRFs listed below are not currently configured on {host}: {set_diff}[/bold red]"
            )
        else:
            pretty(f"[bold blue]All VRF tests have passed successfully on the router {host}[/bold blue]")


if __name__ == "__main__":
    test_vrf()
