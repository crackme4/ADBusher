# ADBusher
![adbusher](https://user-images.githubusercontent.com/110720210/235856930-ffb87dd8-ec13-4908-920f-ee979550fbd3.png)
___
_ADBusher_ is a script that includes ADB (Android Debug Bridge) and Scrcpy (Display and Control Device).Performs the function of connecting to devices under the Android operating system, with the adb 5555 port open, which is intended for remote control of the device. Once connected, the full functionality of this scrcpy is revealed.

__These are:__
1. Connecting to a device.
2. Disconnecting from all devices or from specific devices.
3. Switching to the interactive mode with the device.
4. After switching to the interactive mode, the following functions open.

        - con, connect -> Connect to devices (ex. connect 'ip')
        - dev, devices -> list all devices connected
        - kill, kill-all -> disconnect all devices
        - dis 0,1,2,3..., disconnect 0,1,2,3... -> disconnect list devices
        - exit -> exit from script
        - interact 'x' -> interact command on device in list
        - help -> help menu

__Interactive mode:__
1. Getting a screenshot from the device.
2. Get a list of installed applications
3. Scrcpy - display and control.
4. Downloading files from the device.
5. Uploading files to the device.
6. Get the list of files and directories on the device.
7. Executing shell command with parameters.
8. A wifi configuration dump with the history of connecting the device to wifi spots. It also stores the passwords for those wifi spots.
9. Executing keyevent for the device.

         - screenshot -> Take screenshot device
         - list-packages -> list packages installed on device
         - scrcpy -> Remote desktop manage device
         - download -> download <remote_path> <local_path>
         - upload -> upload <local_path> <remote_path>
         - ls -> list files in folders 
         - shell-com -> shell <command>, for once complete command
         - dump-wifi -> dump password wifi network on device
         - keyevent -> complete keyevent on device (ex. keyevent HOME and etc.). Information about events in events.txt
         - exit -> exit without interact
                
___

__Install__

sudo sh ./setup.sh

__Use__

python adbusher.py

_The help command will help you control the script_

__Also__

Attached is the events.txt file for a list of possible events.
