#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket
from system.models import SystemStats

def check():
    base_pacmansyup_command_raw = "pacman -Syup"
    args = shlex.split(base_pacmansyup_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    systemstats = SystemStats()
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        if not "there is nothing to do" in newoutput:
            continue
        elif "there is nothing to do" in newoutput:
            systemstats.updatesavailable = False
            systemstats.save()
            return False
    systemstats.updatesavailable = True
    systemstats.save()
    return True
           
def list_upgrades():
    base_pacmanqu_command_raw = "pacman -Qu"
    args = shlex.split(base_pacmanqu_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        output_list.append(newoutput)
    systemstats = SystemStats()
    systemstats.updatecount = str(len(output_list))
    systemstats.save()
    return output_list

def list_installed():
    base_pacmanqu_command_raw = "pacman -Q"
    args = shlex.split(base_pacmanqu_command_raw)
    process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
    output_list = []
    for line in process.stdout.readlines():
        newoutput = line.rstrip('\n')
        currentpackage = shlex.split(newoutput)
        output_list.append(currentpackage)
    return output_list


def doupdateos():
       base_update_command_raw = "pacman -Syu --noconfirm --noprogressbar"
       args = shlex.split(base_update_command_raw)
       process = subprocess.Popen(args,stdout=subprocess.PIPE,universal_newlines=True)
       output_list = []
       for line in process.stdout.readlines():
              newoutput = line.rstrip('\n')
              output_list.append(newoutput)
              output_list.append('<br/>')
       return output_list
