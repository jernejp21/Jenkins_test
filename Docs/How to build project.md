---
layout: default
title: How to build
nav_order: 3
---

# How to build linux

Building linux is done based on [the article](https://forum.digikey.com/t/debian-getting-started-with-the-stm32mp157/12459) on DigiKey.

Clone [STM32MP157_Debian repository](https://github.com/jernejp21/STM32MP157_Debian) and run `linux.sh` script. It will take some time, because the script download linux kernel repository and builds the kernel.

When linux kernel menuconfig opens, enable `Device Drivers -> Charctar Devices -> RPMSG tty driver`, save config and exit. 

After script is done, copy image file to a SD card using Balena Ettcher or something else. When the process finishes, you will need to manually resize available (unused) space. Do this with built-in partition manager tool. For Plasma desktop this tool is *KDE partition manager*.

Default user name: debian
Defaul password: temppwd

# How to build klipper and run it

Build klipper as you would for and other controller board. In the menu choose STM family and STM32MP157D device. After build is done, copy *klipper.elf* file to the STM32MP157D device using `scp` command or USB flash drive.

After you have copied to linux, you will need to copy it to Cortex-M coprocessor and run the coprocessor.

For command below, you will need root privileges. Recommended way is to use `sudo -s` and from root user execute commands.

Copy elf file:
```
cp klipper.elf /lib/firmware/
```

Tell coprocessor which file to run:
```
echo klipper.elf > /sys/class/remoteproc/remoteproc0/firmware 
```

Run the coprocessor
```
echo start > /sys/class/remoteproc/remoteproc0/status 
```

Stop the coprocessor
```
echo stop > /sys/class/remoteproc/remoteproc0/status
```