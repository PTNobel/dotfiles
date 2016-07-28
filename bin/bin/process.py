#!/usr/bin/python3

__all__ = [
    "is_comm_running",
    "get_comms_to_pids",
    "get_pids_to_comms",
    "get_pids_to_cmdlines",
    "get_pids_of_comm",
    "get_comm_of_pid",
    "get_pids",
    "get_comms",
    "get_pids_of_comm",
    "update_buffers",
    "get_cmdline_of_pid",
    ]


from os import listdir as _listdir
from os.path import join as _join
from typing import List, Dict

_buffer_map_pids_to_comms = {}  # type: Dict[str, str]
_buffer_map_pids_to_cmdlines = {}  # type: Dict[str, List[str]]
_buffer_map_comms_to_pids = {}  # type: Dict[str, List[str]]
_buffer_running_pids = []  # type: List[str]
_buffer_list_of_comms = []  # type: List[str]


def _map_pids_to_comms(rebuild_buffer: bool) -> Dict[str, str]:
    global _buffer_map_pids_to_comms
    output = dict()
    if _buffer_map_pids_to_comms == {} or rebuild_buffer:
        # Maps the contents of _bufer_running_pids to their comms.
        # The comm getting logic is in _get_comm_of_pid
        for i in _buffer_running_pids:
            output[i] = _get_comm_of_pid(i)
        _buffer_map_pids_to_comms = output
    else:
        output = _buffer_map_pids_to_comms
    return output


def _map_pids_to_cmdlines(rebuild_buffer: bool) -> Dict[str, List[str]]:
    global _buffer_map_pids_to_cmdlines
    output = dict()
    if _buffer_map_pids_to_cmdlines == {} or rebuild_buffer:
        # Maps the contents of _bufer_running_pids to their cmdline.
        # The cmdline getting logic is in _get_cmdline_of_pid
        for i in _buffer_running_pids:
            output[i] = _get_cmdline_of_pid(i)
        _buffer_map_pids_to_cmdlines = output
    else:
        output = _buffer_map_pids_to_cmdlines
    return output


def _get_running_pids(rebuild_buffer: bool) -> List[str]:
    global _buffer_running_pids
    output = list()  # type: List[str]
    if _buffer_running_pids == [] or rebuild_buffer:
        output = [pid for pid in _listdir('/proc') if pid.isdigit()]
        _buffer_running_pids = output
    else:
        output = _buffer_running_pids
    return output


def _get_comm_of_pid(pid: str) -> str:
    if pid in _buffer_map_pids_to_comms:
        comm = _buffer_map_pids_to_comms[pid]
    else:
        try:
            comm_file = open(_join('/proc', pid, 'comm'), 'r')
            comm = comm_file.read().rstrip('\n')
            comm_file.close()
        except FileNotFoundError:
            comm = str()
    return comm


def _get_cmdline_of_pid(pid: str) -> List[str]:
    if pid in _buffer_map_pids_to_cmdlines:
        cmdline = _buffer_map_pids_to_cmdlines[pid]
    else:
        try:
            cmd_file = open(_join('/proc', pid, 'cmdline'), 'r')
            cmd = cmd_file.read().rstrip('\n')
            cmd_file.close()
            cmdline = cmd.split('\x00')
        except FileNotFoundError:
            cmd = str()
            cmdline = cmd.split('\x00')
    return cmdline


def _get_pids_of_comm(comm: str) -> List[str]:
    try:
        pids = _buffer_map_comms_to_pids[comm]
    except KeyError:
        pids = []
    return pids


def _get_list_of_comms(rebuild_buffer: bool) -> List[str]:
    global _buffer_list_of_comms
    output = list()  # type: List[str]
    if _buffer_list_of_comms == [] or rebuild_buffer:
        for i in _buffer_map_pids_to_comms.items():
            if i[1] not in output:
                output.append(i[1])
        _buffer_list_of_comms = output
    else:
        output = _buffer_list_of_comms
    return output


def _map_comms_to_pids(rebuild_buffer: bool) -> Dict[str, List[str]]:
    global _buffer_map_comms_to_pids
    output = dict()  # type: Dict[str, List[str]]
    if _buffer_map_comms_to_pids == {} or rebuild_buffer:
        for i in _buffer_list_of_comms:
            output[i] = list()
        for j in _buffer_map_pids_to_comms.items():
            output[j[1]].append(j[0])
        _buffer_map_comms_to_pids = output
    else:
        output = _buffer_map_comms_to_pids
    return output


def _is_comm_running(comm: str) -> bool:
    return comm in _buffer_list_of_comms


def _build_buffers(rebuild: bool) -> None:
    _get_running_pids(rebuild)
    _map_pids_to_comms(rebuild)
    _map_pids_to_cmdlines(rebuild)
    _get_list_of_comms(rebuild)
    _map_comms_to_pids(rebuild)


def update_buffers() -> None:
    _build_buffers(True)


def get_pids() -> List[str]:
    """Returns a list of pids"""
    return _buffer_running_pids


def get_comms() -> List[str]:
    """Returns a list of comms"""
    return _buffer_list_of_comms


def get_comms_to_pids() -> Dict[str, List[str]]:
    """Returns a dict of comms as keys and a list of pids as values"""
    return _buffer_map_comms_to_pids


def get_pids_to_comms() -> Dict[str, str]:
    """Returns a dict of pids as keys and a string of the comm as values"""
    return _buffer_map_pids_to_comms


def get_pids_of_comm(comm: str) -> List[str]:
    """Returns a list of all pids with comm"""
    return _get_pids_of_comm(comm)


def get_pids_to_cmdlines() -> Dict[str, List[str]]:
    """Returns a dict of pids as keys and a string of the comm as values"""
    return _buffer_map_pids_to_cmdlines


def get_comm_of_pid(pid: str) -> str:
    """Returns the str of the comm of a pid"""
    return _get_comm_of_pid(pid)


def get_cmdline_of_pid(pid: str) -> List[str]:
    """Returns the list with each argv entry of pid as a different string"""
    return _get_cmdline_of_pid(pid)


def is_comm_running(comm: str) -> bool:
    """Returns a bool if any process with that comm is running"""
    return _is_comm_running(comm)


_build_buffers(False)
