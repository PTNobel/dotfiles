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


_buffer_map_pids_to_comms = {}
_buffer_map_pids_to_cmdlines = {}
_buffer_map_comms_to_pids = {}
_buffer_running_pids = []
_buffer_list_of_comms = []


def _map_pids_to_comms(rebuild_buffer):
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


def _map_pids_to_cmdlines(rebuild_buffer):
    global _buffer_map_pids_to_cmdlines
    output = dict()
    if _buffer_map_pids_to_cmdlines == {} or rebuild_buffer:
        # Maps the contents of _bufer_running_pids to their cmdline.
        # The cmdline getting logic is in _get_cmdline_of_pid
        for i in _buffer_running_pids:
            output[i] = _get_cmdline_of_pid(i)
        _buffer_map_pids_to_cmdlines = output
    else:
        output = _buffer_map_pids_to_comms
    return output


def _get_running_pids(rebuild_buffer):
    global _buffer_running_pids
    output = list()
    if _buffer_running_pids == [] or rebuild_buffer:
        output = [pid for pid in _listdir('/proc') if pid.isdigit()]
        _buffer_running_pids = output
    else:
        output = _buffer_running_pids
    return output


def _get_comm_of_pid(pid):
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


def _get_cmdline_of_pid(pid):
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


def _get_pids_of_comm(comm):
    try:
        pids = _buffer_map_comms_to_pids[comm]
    except KeyError:
        pids = []
    return pids


def _get_list_of_comms(rebuild_buffer):
    global _buffer_list_of_comms
    output = list()
    if _buffer_list_of_comms == [] or rebuild_buffer:
        for i in _buffer_map_pids_to_comms.items():
            if i[1] not in output:
                output.append(i[1])
        _buffer_list_of_comms = output
    else:
        output = _buffer_list_of_comms
    return output


def _map_comms_to_pids(rebuild_buffer):
    global _buffer_map_comms_to_pids
    output = dict()
    if _buffer_map_comms_to_pids == {} or rebuild_buffer:
        for i in _buffer_list_of_comms:
            output[i] = list()
        for i in _buffer_map_pids_to_comms.items():
            output[i[1]].append(i[0])
        _buffer_map_comms_to_pids = output
    else:
        output = _buffer_map_comms_to_pids
    return output


def _is_comm_running(comm):
    return comm in _buffer_list_of_comms


def _build_buffers(rebuild):
    _get_running_pids(rebuild)
    _map_pids_to_comms(rebuild)
    _map_pids_to_cmdlines(rebuild)
    _get_list_of_comms(rebuild)
    _map_comms_to_pids(rebuild)


def update_buffers():
    _build_buffers(True)


def get_pids():
    """Returns a list of pids"""
    return _buffer_running_pids


def get_comms():
    """Returns a list of comms"""
    return _buffer_list_of_comms


def get_comms_to_pids():
    """Returns a dict of comms as keys and a list of pids as values"""
    return _buffer_map_comms_to_pids


def get_pids_to_comms():
    """Returns a dict of pids as keys and a string of the comm as values"""
    return _buffer_map_pids_to_comms


def get_pids_of_comm(comm):
    """Returns a list of all pids with comm"""
    return _get_pids_of_comm(comm)


def get_pids_to_cmdlines():
    """Returns a dict of pids as keys and a string of the comm as values"""
    return _buffer_map_pids_to_cmdlines


def get_comm_of_pid(pid):
    """Returns the str of the comm of a pid"""
    return _get_comm_of_pid(pid)


def get_cmdline_of_pid(pid):
    """Returns the bytes of the cmdline of a pid"""
    return _get_cmdline_of_pid(pid)


def is_comm_running(comm):
    """Returns a bool if any process with that comm is running"""
    return _is_comm_running(comm)


_build_buffers(False)
