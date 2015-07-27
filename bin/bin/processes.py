#!/usr/bin/python3


import os


class processes:
    _buffer_map_pids_to_comms = dict()
    _buffer_map_comms_to_pids = dict()
    _buffer_running_pids = list()
    _buffer_list_of_comms = list()

    def __init__(self):
        self._build_buffers(False)

    def _get_running_pids(self, rebuild_buffer):
        output = list()
        if self._buffer_running_pids == [] or rebuild_buffer:
            output = [pid for pid in os.listdir('/proc') if pid.isdigit()]
            self._buffer_running_pids = output
        else:
            output = self._buffer_running_pids
        return output

    def _get_comm_of_pid(self, pid):
        if pid in self._buffer_map_pids_to_comms:
            comm = self._buffer_map_pids_to_comms[pid]
        else:
            try:
                comm_file = open(os.path.join('/proc', pid, 'comm'), 'r')
                comm = comm_file.read().rstrip('\n')
                comm_file.close()
            except FileNotFoundError:
                comm = str()
        return comm

    def _get_pids_of_comm(self, comm):
        try:
            pids = self._buffer_map_pids_to_comms[comm]
        except KeyError:
            pids = []
        return pids

    def _map_pids_to_comms(self, rebuild_buffer):
        output = dict()
        if self._buffer_map_pids_to_comms == {} or rebuild_buffer:
            for i in self._buffer_running_pids:
                output[i] = self._get_comm_of_pid(i)
            self._buffer_map_pids_to_comms = output
        else:
            output = self._buffer_map_pids_to_comms
        return output

    def _get_list_of_comms(self, rebuild_buffer):
        output = list()
        if self._buffer_list_of_comms == [] or rebuild_buffer:
            for i in self._buffer_map_pids_to_comms.items():
                if i[1] not in output:
                    output.append(i[1])
            self._buffer_list_of_comms = output
        else:
            output = self._buffer_list_of_comms
        return output

    def _map_comms_to_pids(self, rebuild_buffer):
        output = dict()
        if self._buffer_map_comms_to_pids == {} or rebuild_buffer:
            for i in self._buffer_list_of_comms:
                output[i] = list()
            for i in self._buffer_map_pids_to_comms.items():
                output[i[1]].append(i[0])
            self._buffer_map_comms_to_pids = output
        else:
            output = self._buffer_map_comms_to_pids
        return output

    def _is_comm_running(self, comm):
        return comm in self._buffer_list_of_comms

    def _build_buffers(self, rebuild):
        self._get_running_pids(rebuild)
        self._map_pids_to_comms(rebuild)
        self._get_list_of_comms(rebuild)
        self._map_comms_to_pids(rebuild)

    def update_snapshot(self):
        self._build_buffers(True)

    def get_pids(self):
        return self._get_running_pids()

    def get_comms_to_pids(self):
        return self._map_comms_to_pids()

    def get_pids_to_comms(self):
        return self._map_pids_to_comms()

    def get_pids_of_comm(self, comm):
        return self._get_pids_of_comm(comm)

    def get_comm_of_pid(self, pid):
        return self._get_comm_of_pid(pid)

    def is_comm_running(self, comm):
        return self._is_comm_running(comm)


def main():
    pass


if __name__ == '__main__':
    main()
