---
title: Store register to memory
source_url: https://docs.micropython.org/en/latest/reference/asm_thumb2_str.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: reference/asm_thumb2_str.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: reference
order: 1220
---

# Store register to memory

## Document conventions

Notation: `Rt, Rn` denote ARM registers R0-R7 except where stated. `immN` represents an immediate value having a width of N bits hence `imm5` is constrained to the range 0-31. `[Rn + imm5]` is the contents of the memory address obtained by adding Rn and the offset `imm5`. Offsets are measured in bytes. These instructions do not affect the condition flags.

## Register Store

- str(Rt, \[Rn, imm7\]) `[Rn + imm7] = Rt` Store a 32 bit word
- strb(Rt, \[Rn, imm5\]) `[Rn + imm5] = Rt` Store a byte (b0-b7)
- strh(Rt, \[Rn, imm6\]) `[Rn + imm6] = Rt` Store a 16 bit half word (b0-b15)

The specified immediate offsets are measured in bytes. Hence in the case of `str` the 7 bit value enables 32 bit word aligned values to be accessed with a maximum offset of 31 words. In the case of `strh` the 6 bit value enables 16 bit half-word aligned values to be accessed with a maximum offset of 31 half-words.
