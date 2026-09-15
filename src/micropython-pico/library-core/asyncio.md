---
title: '`asyncio`'
description: asynchronous I/O scheduler
source_url: https://docs.micropython.org/en/latest/library/asyncio.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/asyncio.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 30
---

# `asyncio` --- asynchronous I/O scheduler

asyncio

\|see_cpython_module\| [asyncio](https://docs.python.org/3.8/library/asyncio.html)

Example:

    import asyncio

    async def blink(led, period_ms):
        while True:
            led.on()
            await asyncio.sleep_ms(5)
            led.off()
            await asyncio.sleep_ms(period_ms)

    async def main(led1, led2):
        asyncio.create_task(blink(led1, 700))
        asyncio.create_task(blink(led2, 400))
        await asyncio.sleep_ms(10_000)

    # Running on a pyboard
    from pyb import LED
    asyncio.run(main(LED(1), LED(2)))

    # Running on a generic board
    from machine import Pin
    asyncio.run(main(Pin(1), Pin(2)))

## Core functions

create_task(coro)

Create a new task from the given coroutine and schedule it to run.

Returns the corresponding `Task` object.

current_task()

Return the `Task` object associated with the currently running task.

run(coro)

Create a new task from the given coroutine and run it until it completes.

Returns the value returned by *coro*.

sleep(t)

Sleep for *t* seconds (can be a float).

This is a coroutine.

sleep_ms(t)

Sleep for *t* milliseconds.

This is a coroutine, and a MicroPython extension.

## Additional functions

wait_for(awaitable, timeout)

Wait for the *awaitable* to complete, but cancel it if it takes longer than *timeout* seconds. If *awaitable* is not a task then a task will be created from it.

If a timeout occurs, it cancels the task and raises `asyncio.TimeoutError`: this should be trapped by the caller. The task receives `asyncio.CancelledError` which may be ignored or trapped using `try...except` or `try...finally` to run cleanup code.

Returns the return value of *awaitable*.

This is a coroutine.

wait_for_ms(awaitable, timeout)

Similar to `wait_for` but *timeout* is an integer in milliseconds.

This is a coroutine, and a MicroPython extension.

gather(\*awaitables, return_exceptions=False)

Run all *awaitables* concurrently. Any *awaitables* that are not tasks are promoted to tasks.

Returns a list of return values of all *awaitables*.

This is a coroutine.

## class Task

This object wraps a coroutine into a running task. Tasks can be waited on using `await task`, which will wait for the task to complete and return the return value of the task.

Tasks should not be created directly, rather use `create_task` to create them.

Task.cancel()

Cancel the task by injecting `asyncio.CancelledError` into it. The task may ignore this exception. Cleanup code may be run by trapping it, or via `try ... finally`.

## class Event

Create a new event which can be used to synchronise tasks. Events start in the cleared state.

Event.is_set()

Returns `True` if the event is set, `False` otherwise.

Event.set()

Set the event. Any tasks waiting on the event will be scheduled to run.

Note: This must be called from within a task. It is not safe to call this from an IRQ, scheduler callback, or other thread. See `ThreadSafeFlag`.

Event.clear()

Clear the event.

Event.wait()

Wait for the event to be set. If the event is already set then it returns immediately.

This is a coroutine.

## class ThreadSafeFlag

Create a new flag which can be used to synchronise a task with code running outside the asyncio loop, such as other threads, IRQs, or scheduler callbacks. Flags start in the cleared state.

ThreadSafeFlag.set()

Set the flag. If there is a task waiting on the flag, it will be scheduled to run.

ThreadSafeFlag.clear()

Clear the flag. This may be used to ensure that a possibly previously-set flag is clear before waiting for it.

ThreadSafeFlag.wait()

Wait for the flag to be set. If the flag is already set then it returns immediately. The flag is automatically reset upon return from `wait`.

A flag may only be waited on by a single task at a time.

This is a coroutine.

## class Lock

Create a new lock which can be used to coordinate tasks. Locks start in the unlocked state.

In addition to the methods below, locks can be used in an `async with` statement.

Lock.locked()

Returns `True` if the lock is locked, otherwise `False`.

Lock.acquire()

Wait for the lock to be in the unlocked state and then lock it in an atomic way. Only one task can acquire the lock at any one time.

This is a coroutine.

Lock.release()

Release the lock. If any tasks are waiting on the lock then the next one in the queue is scheduled to run and the lock remains locked. Otherwise, no tasks are waiting an the lock becomes unlocked.

## TCP stream connections

open_connection(host, port, ssl=None)

Open a TCP connection to the given *host* and *port*. The *host* address will be resolved using `socket.getaddrinfo`, which is currently a blocking call. If *ssl* is a `ssl.SSLContext` object, this context is used to create the transport; if *ssl* is `True`, a default context is used.

Returns a pair of streams: a reader and a writer stream. Will raise a socket-specific `OSError` if the host could not be resolved or if the connection could not be made.

This is a coroutine.

start_server(callback, host, port, backlog=5, ssl=None)

Start a TCP server on the given *host* and *port*. The *callback* will be called with incoming, accepted connections, and be passed 2 arguments: reader and writer streams for the connection.

If *ssl* is a `ssl.SSLContext` object, this context is used to create the transport.

Returns a `Server` object.

This is a coroutine.

This represents a TCP stream connection. To minimise code this class implements both a reader and a writer, and both `StreamReader` and `StreamWriter` alias to this class.

Stream.get_extra_info(v)

Get extra information about the stream, given by *v*. The valid values for *v* are: `peername`.

Stream.close()

Close the stream.

Stream.wait_closed()

Wait for the stream to close.

This is a coroutine.

Stream.read(n=-1)

Read up to *n* bytes and return them. If *n* is not provided or -1 then read all bytes until EOF. The returned value will be an empty bytes object if EOF is encountered before any bytes are read.

This is a coroutine.

Stream.readinto(buf)

Read up to n bytes into *buf* with n being equal to the length of *buf*.

Return the number of bytes read into *buf*.

This is a coroutine, and a MicroPython extension.

Stream.readexactly(n)

Read exactly *n* bytes and return them as a bytes object.

Raises an `EOFError` exception if the stream ends before reading *n* bytes.

This is a coroutine.

Stream.readline()

Read a line and return it.

This is a coroutine.

Stream.write(buf)

Accumulated *buf* to the output buffer. The data is only flushed when `Stream.drain` is called. It is recommended to call `Stream.drain` immediately after calling this function.

Stream.drain()

Drain (write) all buffered output data out to the stream.

This is a coroutine.

This represents the server class returned from `start_server`. It can be used in an `async with` statement to close the server upon exit.

Server.close()

Close the server.

Server.wait_closed()

Wait for the server to close.

This is a coroutine.

## Event Loop

get_event_loop()

Return the event loop used to schedule and run tasks. See `Loop`.

new_event_loop()

Reset the event loop and return it.

Note: since MicroPython only has a single event loop this function just resets the loop's state, it does not create a new one.

This represents the object which schedules and runs tasks. It cannot be created, use `get_event_loop` instead.

Loop.create_task(coro)

Create a task from the given *coro* and return the new `Task` object.

Loop.run_forever()

Run the event loop until `stop()` is called.

Loop.run_until_complete(awaitable)

Run the given *awaitable* until it completes. If *awaitable* is not a task then it will be promoted to one.

Loop.stop()

Stop the event loop.

Loop.close()

Close the event loop.

Loop.set_exception_handler(handler)

Set the exception handler to call when a Task raises an exception that is not caught. The *handler* should accept two arguments: `(loop, context)`.

Loop.get_exception_handler()

Get the current exception handler. Returns the handler, or `None` if no custom handler is set.

Loop.default_exception_handler(context)

The default exception handler that is called.

Loop.call_exception_handler(context)

Call the current exception handler. The argument *context* is passed through and is a dictionary containing keys: `'message'`, `'exception'`, `'future'`.
