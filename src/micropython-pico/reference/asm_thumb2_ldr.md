---
title: Load register from memory
source_url: https://docs.micropython.org/en/latest/reference/asm_thumb2_ldr.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: reference/asm_thumb2_ldr.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: reference
order: 1170
---

# Load register from memory

## Document conventions

Notation: `Rt, Rn` denote ARM registers R0-R7 except where stated. `immN` represents an immediate value having a width of N bits hence `imm5` is constrained to the range 0-31. `[Rn + immN]` is the contents of the memory address obtained by adding Rn and the offset `immN`. Offsets are measured in bytes. These instructions affect the condition flags.

## Register Load

- ldr(Rt, \[Rn, imm7\]) `Rt = [Rn + imm7]` Load a 32 bit word
- ldrb(Rt, \[Rn, imm5\]) `Rt = [Rn + imm5]` Load a byte
- ldrh(Rt, \[Rn, imm6\]) `Rt = [Rn + imm6]` Load a 16 bit half word

Where a byte or half word is loaded, it is zero-extended to 32 bits.

The specified immediate offsets are measured in bytes. Hence in the case of `ldr` the 7 bit value enables 32 bit word aligned values to be accessed with a maximum offset of 31 words. In the case of `ldrh` the 6 bit value enables 16 bit half-word aligned values to be accessed with a maximum offset of 31 half-words.
