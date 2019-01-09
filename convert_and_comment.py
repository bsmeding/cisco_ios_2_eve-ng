##################################################
#
# convert script for Cisco IOS config for compaitble EVE-NG
#
# Created by Bart Smeding
#
# usage : pyhton convert_and_comment.py /path/to/configs/    must be *.confg
# all new configs will be available in ./eve-ng/
#
##################################################
import os, glob


delete_lines = ['enable ', ' password ' ,'boot-', 'boot system', 'banner', '*'] 
comment_lines = ['aaa a', 'vtp mode', 'mls ',' action-type', ' group ', 'spanning-tree ', 'diagnostic ', 'power enable', 'redundancy', ' main-cpu', 'auto-sync running-config', 'mode sso', 'vlan ', 'errdisable ', '-queue','message-digest', 'tacacs-server ', 'nsf']
change_ints = {
    "TenGigabitEthernet1/1":"GigabitEthernet0/0", 
    "TenGigabitEthernet1/2":"GigabitEthernet0/1",
    "TenGigabitEthernet1/3":"GigabitEthernet0/2", 
    "TenGigabitEthernet1/4":"GigabitEthernet0/3", 
    "TenGigabitEthernet5/1":"GigabitEthernet0/4",
    "TenGigabitEthernet5/2":"GigabitEthernet0/5",
    "TenGigabitEthernet5/3":"GigabitEthernet0/6",
    "GigabitEthernet5/1":"GigabitEthernet0/4",
    "GigabitEthernet5/2":"GigabitEthernet0/5",
    "GigabitEthernet5/3":"GigabitEthernet0/6",    
    "TenGigabitEthernet5/4":"GigabitEthernet0/7",
    "TenGigabitEthernet5/5":"GigabitEthernet0/8",
    }


## create output directory

directory = os.getcwd()
outdir = directory + '/eve-ng'
try:
    os.stat(outdir)
except:
    os.mkdir(outdir)       

## loop trough directory with configs


os.chdir(directory)
for file in glob.glob("*confg"):
    print(file)

    with open(file) as oldfile, open(outdir+'/'+file+'.eveng', 'w') as newfile:
        for line in oldfile:
            if not any(delete_line in line for delete_line in delete_lines):
                if any(comment_line in line for comment_line in comment_lines):
                    newfile.write('!--remove_for_eveng--'+line)
                else:
                    for interface in change_ints.keys():
                        if interface in line.split():
                            line = line.replace(interface, change_ints[interface])
                    newfile.write(line)
