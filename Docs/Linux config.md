---
layout: default
title: Linux config
nav_order: 4
---

# Linux config before build
To be dated.


# Linux config after build

To change IP address from dynamic to static, you need to modify `/etc/network/interfaces` file.

Change file contents to:
```shell
auto eth0
iface eth0 inet static 
  address 192.168.x.x
  netmask 255.255.255.0
  gateway 192.168.x.x
```