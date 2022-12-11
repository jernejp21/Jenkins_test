---
layout: default
title: OpenAMP
nav_order: 5
---

# Porting OpenAMP from STM32 library (demo project) to Klipper

We will use STM's OpenAMP version for the project. It differs from original OpenAMP in low level parts - inter processor communication interrupts and registers.

# What do we need for porting?

We will start with [OpenAMP tty echo](https://github.com/jernejp21/STM32CubeMP1/tree/master/Projects/STM32MP157C-DK2/Applications/OpenAMP/OpenAMP_TTY_echo) example. If this example works, it means linux in configured correctly.

We have to check if `/dev/ttyRPMSG` is created and if `/sys/kernel/debug/remoteproc/remoteproc0/trace0` is created. If these 2 files are created, porting is successful and we can focus on removing HAL librareis and integrate code into Klipper.

# Creting new project with STM32CubeIDE

What do we need to create new working OpenAMP project?

## Creating new project with default settings

- In *main.c*, include `#include "openamp_log.h`
- In *openamp_conf.h:60*, uncomment `#define VIRTUAL_UART_MODULE_ENABLED`
- On CM4 core properties, go under *C/C++ Build -> Settings -> Tool Settings -> MCU GCC Compiler -> Preprocessor* and add `__LOG_TRACE_IO_`. Without this, `printf()` doesn't work.

## Creating new, clean project (no settings enabled)

- In *System Core*, enable *IPCC* for both cores and activate it.
- When you activate *IPCC*, you can enable *OpenAMP* middleware. Enable and activate it.
- After this, follow instructions under [Creating new project with default settings](#creating-new-project-with-default-settings)