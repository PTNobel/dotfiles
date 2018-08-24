#!/usr/bin/python3

__all__ = [
    "Processes",
]

from os import listdir as _listdir
from os.path import join as _join
from typing import List, Dict
from time import ctime as _ctime


class Processes:
    _buffer_map_pids_to_comms: Dict[str, str]
    _buffer_map_pids_to_cmdlines: Dict[str, List[str]]
    _buffer_map_comms_to_pids: Dict[str, List[str]]
    _buffer_running_pids: List[str]
    _buffer_list_of_comms: List[str]
    time_of_init: str

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<Processes at " + self.time_of_init + ">"

    def __init__(self):
        self._buffer_map_pids_to_comms = {}
        self._buffer_map_pids_to_cmdlines = {}
        self._buffer_list_of_comms = []
        self._buffer_map_comms_to_pids = {}

        self._buffer_running_pids = [
            pid for pid in _listdir('/proc') if pid.isdigit()
        ]

        for index, pid in enumerate(self._buffer_running_pids):
            try:
                comm_file = open(_join('/proc', pid, 'comm'), 'r')
                comm = comm_file.read().rstrip('\n')
                comm_file.close()
                self._buffer_map_pids_to_comms[pid] = comm

                cmd_file = open(_join('/proc', pid, 'cmdline'), 'r')
                cmd = cmd_file.read().rstrip('\n')
                cmd_file.close()
                cmdline = cmd.split('\x00')

                self._buffer_map_pids_to_cmdlines[pid] = cmdline

                if comm not in self._buffer_list_of_comms:
                    self._buffer_list_of_comms.append(comm)
                    self._buffer_map_comms_to_pids[comm] = list()

                self._buffer_map_comms_to_pids[comm].append(pid)

            except FileNotFoundError:
                self._buffer_running_pids.pop(index)

        self.time_of_init = _ctime()

    def update_snapshot(self):
        self.__init__()
        raise DeprecationWarning("Please create a new instance instead.")

    def get_pids(self) -> List[str]:
        """Returns a list of pids"""
        return self._buffer_running_pids

    def get_comms(self) -> List[str]:
        """Returns a list of comms"""
        return self._buffer_list_of_comms

    def get_comms_to_pids(self) -> Dict[str, List[str]]:
        """Returns a dict of comms as keys and a list of pids as values"""
        return self._buffer_map_comms_to_pids

    def get_pids_to_comms(self) -> Dict[str, str]:
        """Returns a dict of pids as keys and a string of the comm as values"""
        return self._buffer_map_pids_to_comms

    def get_pids_to_cmdlines(self) -> Dict[str, List[str]]:
        """Returns a dict of pids as keys and a string of the comm as values"""
        return self._buffer_map_pids_to_cmdlines

    def get_pids_of_comm(self, comm: str) -> List[str]:
        """Returns a list of all pids with comm"""
        return self._buffer_map_comms_to_pids.get(comm, [])

    def get_comm_of_pid(self, pid: str) -> str:
        """Returns the comm of a pid"""
        return self._buffer_map_pids_to_comms[pid]

    def get_cmdline_of_pid(self, pid: str) -> List[str]:
        """Returns the argv of pid"""
        return self._buffer_map_pids_to_cmdlines[pid]

    def is_comm_running(self, comm: str) -> bool:
        """Returns a bool if any process with that comm is running"""
        return comm in self._buffer_list_of_comms
