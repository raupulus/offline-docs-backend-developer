---
title: Stack push and pop
source_url: https://docs.micropython.org/en/latest/reference/asm_thumb2_stack.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: reference/asm_thumb2_stack.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: reference
order: 1210
---

# Stack push and pop

## Document conventions

The `push()` and `pop()` instructions accept as their argument a register set containing a subset, or possibly all, of the general-purpose registers R0-R12 and the link register (lr or R14). As with any Python set the order in which the registers are specified is immaterial. Thus the in the following example the pop() instruction would restore R1, R7 and R8 to their contents prior to the push():

- push({r1, r8, r7}) Save three registers on the stack.
- pop({r7, r1, r8}) Restore them

## Stack operations

- push({regset}) Push a set of registers onto the stack
- pop({regset}) Restore a set of registers from the stack
