---
title: '`wipy`'
description: WiPy specific features
source_url: https://docs.micropython.org/en/latest/library/wipy.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/wipy.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 1010
---

# `wipy` -- WiPy specific features

wipy

The `wipy` module contains functions to control specific features of the WiPy, such as the heartbeat LED.

## Functions

heartbeat(\[enable\])

Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and returns boolean values (`True` or `False`).
