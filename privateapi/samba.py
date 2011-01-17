#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket, os


def is_installed():
    fpath = "/usr/sbin/smbd"
    return os.path.isfile(fpath)
           
def is_running():
	process = os.popen("ps x -o pid,args | grep -v grep | grep smbd").read()
	if process:
		return True
	return False

def start():
    if not is_running():
       start_command_raw = "/etc/rc.d/samba start"
       args = shlex.split(start_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if ":: Starting Samba Server" in newoutput:
                return True
       return False
    else:
        return True

def stop():
    if is_running():
       stop_command_raw = "/etc/rc.d/samba stop"
       args = shlex.split(stop_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if ":: Stopping Samba Server" in newoutput:
                return True
       return False
    else:
        return True
