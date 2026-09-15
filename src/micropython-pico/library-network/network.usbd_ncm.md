---
title: USBD_NCM
description: USB NCM network interface
source_url: https://docs.micropython.org/en/latest/library/network.USBD_NCM.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/network.USBD_NCM.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-network
order: 560
---

# class USBD_NCM -- USB NCM network interface

This class provides a network interface over USB using the NCM (Network Control Model) protocol. The host computer sees this device as a USB Ethernet adapter and assigns it an IP address via DHCP (served by the MicroPython device).

> [!NOTE]
> `network.USBD_NCM` requires a port with TinyUSB and NCM support, enabled at build time by defining `MICROPY_PY_NETWORK_USBD_NCM` (off by default).

Example usage:

    import network

    nic = network.USBD_NCM()
    nic.active(True)
    # wait for USB host to configure the NCM interface
    while not nic.isconnected():
        pass

    print(nic.ipconfig("addr4"))

## Constructors

Create and return a USBD_NCM object. This initialises the NCM network interface if it has not already been initialised. Only one instance exists (singleton).

## Methods

USBD_NCM.active(\[is_active\])

Activate or deactivate the network interface. Without argument returns current state as a bool.

The interface is brought up automatically before USB enumeration, so this returns `True` from boot.

USBD_NCM.isconnected()

Returns `True` if the USB host has configured the NCM interface, `False` otherwise.

When USB is disconnected, this returns `False` and network traffic stops. The interface remains registered with lwIP and can resume when the host reconnects and re-enumerates the device.

USBD_NCM.status()

Returns the link status as an integer: `1` if the interface is up, `0` otherwise.

USBD_NCM.ipconfig('param') USBD_NCM.ipconfig(param=value, ...)

See `AbstractNIC.ipconfig`.

USBD_NCM.ifconfig(\[(ip, subnet, gateway, dns)\])

See `AbstractNIC.ifconfig`.

## Notes

**Link-local IP address:** The device IP (169.254.x.1) is derived deterministically from the device MAC address. RFC 3927 ARP probe/announce (conflict detection) is not implemented, so if two devices happen to derive the same address on the same network segment, the conflict will go undetected.

**MAC address uniqueness:** The device and host-side MAC addresses are derived from the value returned by `mp_hal_get_mac()`. If two boards have the same hardware MAC (e.g. the port does not use a hardware UID), they will present the same network addresses and cause ARP conflicts.
