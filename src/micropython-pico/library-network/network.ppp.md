---
title: PPP
description: create network connections over serial PPP
source_url: https://docs.micropython.org/en/latest/library/network.PPP.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/network.PPP.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-network
order: 550
---

# class PPP -- create network connections over serial PPP

This class allows you to create a network connection over a serial port using the PPP protocol.

> [!NOTE]
> Currently only the esp32 port has PPP support enabled in the default firmware build. PPP support can be enabled in custom builds of the stm32 and rp2 ports by enabling networking support and setting `MICROPY_PY_NETWORK_PPP_LWIP` to 1.

Example usage:

    import network

    ppp = network.PPP(uart)
    ppp.connect()

    while not ppp.isconnected():
        pass

    print(ppp.ipconfig("addr4"))

    # use the socket module as usual, etc

    ppp.disconnect()

## Constructors

Create a PPP driver object.

Arguments are:

> - *stream* is any object that supports the stream protocol, but is most commonly a `machine.UART` instance. This stream object must have an `irq()` method and an `IRQ_RXIDLE` constant, for use by `PPP.connect`.

## Methods

PPP.connect(security=SEC_NONE, user=None, key=None)

Initiate a PPP connection with the given parameters:

> - *security* is the type of security, either `PPP.SEC_NONE`, `PPP.SEC_PAP`, or `PPP.SEC_CHAP`.
> - *user* is an optional user name to use with the security mode.
> - *key* is an optional password to use with the security mode.

When this method is called the underlying stream has its interrupt configured to call `PPP.poll` via `stream.irq(ppp.poll, stream.IRQ_RXIDLE)`. This makes sure the stream is polled, and data passed up the PPP stack, wheverver data becomes available on the stream.

The connection proceeds asynchronously, in the background.

PPP.disconnect()

Terminate the connection. This must be called to cleanly close the PPP connection.

PPP.isconnected()

Returns `True` if the PPP link is connected and up. Returns `False` otherwise.

PPP.status()

Returns the PPP status.

PPP.config(config_parameters)

Sets or gets parameters of the PPP interface. The only parameter that can be retrieved and set is the underlying stream, using:

    stream = PPP.config("stream")
    PPP.config(stream=stream)

PPP.ipconfig('param') PPP.ipconfig(param=value, ...)

See `AbstractNIC.ipconfig`.

PPP.ifconfig(\[(ip, subnet, gateway, dns)\])

See `AbstractNIC.ifconfig`.

PPP.poll(\[irq_arg\])

Poll the underlying stream for data, and pass it up the PPP stack. This is called automatically if the stream is a UART with a RXIDLE interrupt, so it's not usually necessary to call it manually.

The optional *irq_arg* argument is ignored, this argument exists only so this function is compatible with the `machine.UART.irq` *handler* argument.

## Constants

PPP.SEC_NONE PPP.SEC_PAP PPP.SEC_CHAP

The type of connection security.
