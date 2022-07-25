##Matt Hamilton
##Module 04 Homework

import os
import getpass
import shutil


the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)


with open('alert_data.csv','w') as f:
    f.write('Date,Time,Priority,Classification,Description,Source IP,Destination IP\n')

with open('alert.fast.maccdc2012_00000.pcap', 'r') as f:
    for line in f:
        split1 = line.split('[**]')
        date_time = split1[0]
        attack_date = date_time[:5]
        attack_time = date_time[6:11]
        split2 = split1[1].split(']')
        description = split2[1].strip()
        split3 = split1[2].split('[]')
        split3 = split1[2].split(']')
        classification = split3[0]
        classification = classification.strip('[')
        classification = classification[18:]
        split4 = split1[2].split(' [Priority: ')
        priority = split4[1]
        priority = priority[:1]
        split5 = split4[1]
        split5 = split5.split('} ')
        split6 = split5[1].split(' -> ')
        sourceip = split6[0]
        destinationip = split6[1]




        
        with open('alert_data.csv','a') as f:
            f.write(str(attack_date) + ','
                  + attack_time + ','
                  + priority + ',' + classification + ','
                    + description + ',' + sourceip + ','
                    + destinationip)


print('Process complete. Press Enter to exit the script.')
input()
        
        
