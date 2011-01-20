#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket, os, fileinput, sys

def is_installed():
    fpath = "/usr/sbin/minidlna"
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
           
def is_running():
    fpath = "/var/run/minidlna.pid"
    return os.path.isfile(fpath)

def start():
    if is_installed():
       base_start_command_raw = "/etc/rc.d/minidlna start"
       args = shlex.split(base_start_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if not ":: Starting MiniDLNA UPnP Media Server" in newoutput:
                continue
            elif ":: Starting MiniDLNA UPnP Media Server" in newoutput:
                return True
       return False
    else:
        return False

def stop():
    if is_installed():
       base_stop_command_raw = "/etc/rc.d/minidlna stop"
       args = shlex.split(base_stop_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       for line in process.stdout.readlines():
            newoutput = line.rstrip('\n')
            if not ":: Stopping MiniDLNA UPnP Media Server" in newoutput:
                continue
            elif ":: Stopping MiniDLNA UPnP Media Server" in newoutput:
                return True
       return False
    else:
        return False
	
def get_config(file="/etc/minidlna.conf", delim='='):
	try:
		d = {}
		for line in fileinput.input(file):
			if not line.strip(): # skip empty or space padded lines
				continue
			if re.compile('^#').search(line) is not None: # skip commented lines
				continue
			else: # pick up key and value pairs
				kvp = line.strip().split(delim)
				if kvp[1].strip().split('#') is not None:
					d[kvp[0].strip()] = kvp[1].split('#')[0].strip()
				else:
					d[kvp[0].strip()] = kvp[1].strip()
		if d['strict_dlna'] == 'no':
			d['strict_dlna'] = False
		else:
			d['strict_dlna'] = True
		if d['enable_tivo'] == 'no':
			d['enable_tivo'] = False
		else:
			d['enable_tivo'] = True		
	
		return d
	except:
		return {}
		
def set_config(configdict):
    #cf = open("/etc/minidlna.conf", "r")
    #lns = cf.readlines()
    # close it so that we can open for writing later
    #cf.close()

    # assumes LASTKNOWN and CURRENT are strings with dotted notation IP addresses
    #lns = "".join(lns)
    #lns = re.sub(LASTKNOWN, CURRENT, lns)  # This replaces all occurences of LASTKNOWN with CURRENT

    #cf = open("/etc/minidlna.conf", "w")
    #cf.write(lns)
    #cf.close()
	port_line = "port=" + configdict['port']
	media_dir_line = "media_dir=" + configdict['media_dir']
	inotify_line = "inotify=" + configdict['inotify']
	tivo_line = "enable_tivo=" + configdict['enable_tivo']
	dlna_line = "strict_dlna=" + configdict['strict_dlna']
	oldfile = open('/etc/minidlna.conf','r')
	newfile = open('/etc/~minidlna.conf','a')
	for line in oldfile:
		if "port=" in line:
			line = port_line
		elif "media_dir=" in line:
			line = media_dir_line
		elif "inotify=" in line:
			line = inotify_line
		elif "enable_tivo=" in line:
			line = tivo_line
		elif "strict_dlna=" in line:
			line = dlna_line
		else:
			line = line
		newfile.write(line)
	newfile.close()
	oldfile.close()
	return True
		
	
	
	