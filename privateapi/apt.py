#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket

def check():
    base_aptgetupdateupgrade_command_raw = "apt-get update && apt-get upgrade"
    args = shlex.split(base_pacmansyup_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        if not "0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded." in newoutput:
            continue
        elif "0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded." in newoutput:
            return False
    return True
           
def list_upgrades():
    base_aptgetupgrade_command_raw = "apt-get upgrade"
    args = shlex.split(base_aptgetupgrade_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        output_list.append(newoutput)
    return output_list

def doupdateos():
       base_upgrade_command_raw = "apt-get -y upgrade"
       args = shlex.split(base_upgrade_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       output_list = []
       for line in process.stdout.readlines():
              newoutput = line.rstrip('\n')
              output_list.append(newoutput)
              output_list.append('<br/>')
       return output_list
