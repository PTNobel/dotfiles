#!/usr/bin/env python3

from __future__ import annotations
import requests
import subprocess
import re
from typing import Any, Dict


def pick_best_hive() -> str:
    is_hive_machine = re.compile(r"hive[1-9][1-9]?\.cs")
    r = requests.get(
        "https://www.ocf.berkeley.edu/%7Ehkn/hivemind/data/latest.json"
    )
    hive_statuses: Dict[str, Dict[str, Any]] = {
        server: desc
        for server, desc in r.json()['data'].items()
        if is_hive_machine.fullmatch(server) and desc != {}
    }

    def weighting_function(status):
        # The 5 minute load_average and a 2 percent penalty per user
        return status[1]['load_avgs'][-1] + 0.02 * len(status[1]['users'])

    return min(hive_statuses.items(), key=weighting_function)[0]


def ssh_to_hive(lowest_load_hive: str) -> None:
    subprocess.call([
        "ssh",
        "-i",
        "~/.ssh/id_berkeley",
        f"cs61c-aah@{lowest_load_hive}.berkeley.edu"
    ])


if __name__ == '__main__':
    hive = pick_best_hive()
    ssh_to_hive(hive)
