---
title: Logical & bitwise instructions
source_url: https://docs.micropython.org/en/latest/reference/asm_thumb2_logical_bit.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: reference/asm_thumb2_logical_bit.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: reference
order: 1180
---

# Logical & bitwise instructions

## Document conventions

Notation: `Rd, Rn` denote ARM registers R0-R7 except in the case of the special instructions where R0-R15 may be used. `Rn<a-b>` denotes an ARM register whose contents must lie in range `a <= contents <= b`. In the case of instructions with two register arguments, it is permissible for them to be identical. For example the following will zero R0 (Python `R0 ^= R0`) regardless of its initial contents.

- eor(r0, r0)

These instructions affect the condition flags except where stated.

## Logical instructions

- and\_(Rd, Rn) `Rd &= Rn`
- orr(Rd, Rn) `Rd |= Rn`
- eor(Rd, Rn) `Rd ^= Rn`
- mvn(Rd, Rn) `Rd = Rn ^ 0xffffffff` i.e. Rd = 1's complement of Rn
- bic(Rd, Rn) `Rd &= ~Rn` bit clear Rd using mask in Rn

Note the use of "and\_" instead of "and", because "and" is a reserved keyword in Python.

## Shift and rotation instructions

- lsl(Rd, Rn\<0-31\>) `Rd <<= Rn`
- lsr(Rd, Rn\<1-32\>) `Rd = (Rd & 0xffffffff) >> Rn` Logical shift right
- asr(Rd, Rn\<1-32\>) `Rd >>= Rn` arithmetic shift right
- ror(Rd, Rn\<1-31\>) `Rd = rotate_right(Rd, Rn)` Rd is rotated right Rn bits.

A rotation by (for example) three bits works as follows. If Rd initially contains bits `b31 b30..b0` after rotation it will contain `b2 b1 b0 b31 b30..b3`

## Special instructions

Condition codes are unaffected by these instructions.

- clz(Rd, Rn) `Rd = count_leading_zeros(Rn)`

count_leading_zeros(Rn) returns the number of binary zero bits before the first binary one bit in Rn.

- rbit(Rd, Rn) `Rd = bit_reverse(Rn)`

bit_reverse(Rn) returns the bit-reversed contents of Rn. If Rn contains bits `b31 b30..b0` Rd will be set to `b0 b1 b2..b31`

Trailing zeros may be counted by performing a bit reverse prior to executing clz.
