# Smallshark

## Bind shell without port forwarding using fake video files.

### Features:

- Fake file extension (RTLO Attack) (.mp4 disguises as .exe file)
- Fake file icon
- Deactivates target's firewall
- Sends you ip address of targets who downloaded this file for further exploitation
- No port forwarding (Uses target's PC as server)
- Builder script both works on Windows and Linux

### Before sending file to target :
- 1 Run python3 Smallshark.py
- 2 Enter ip address you got from ngrok tool
- 3 Open ngrok tool and listen loopback interface from tcpdump
- 4 Add IP Logger link to ensure obtaining IP address of the target 

### Running this file will disable target's firewall and add bind shell to target's PC

### After target opens the file : 
- 1 Open Metasploit or it's equivalent
- 2 Choose bind shell 
- 3 Enter victim's ip as RHOST
- 4 Enter 8443 as RPORT
- 5 Exploit

![screenshot](https://github.com/Nemesis0U/Smallshark/assets/83503290/e4523575-8a98-4c6d-b44d-60a302126273)



New Results(2023, No longer FUD):

![3](https://github.com/Nemesis0U/Smallshark/assets/83503290/e47fc9e4-9f85-478d-aea4-c01e57be5ad1)


Generated ghost malware:

![RTLO](https://user-images.githubusercontent.com/83503290/157925846-b236f942-fe92-4dff-b730-ee9aab65aa3d.png)

### Disclaimer:
### This tool is created by Nemesis0U only for educational purposes and can only be used where strict consent has been given. Do not use this for illegal purposes.
