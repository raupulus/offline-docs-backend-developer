---
title: '`math`'
description: mathematical functions
source_url: https://docs.micropython.org/en/latest/library/math.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/math.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 490
---

# `math` -- mathematical functions

math

\|see_cpython_module\| `python:math`.

The `math` module provides some basic mathematical functions for working with floating-point numbers.

*Note:* On the pyboard, floating-point numbers have 32-bit precision.

Availability: not available on WiPy. Floating point support required for this module.

## Functions

acos(x)

Return the inverse cosine of `x`.

acosh(x)

Return the inverse hyperbolic cosine of `x`.

asin(x)

Return the inverse sine of `x`.

asinh(x)

Return the inverse hyperbolic sine of `x`.

atan(x)

Return the inverse tangent of `x`.

atan2(y, x)

Return the principal value of the inverse tangent of `y/x`.

atanh(x)

Return the inverse hyperbolic tangent of `x`.

ceil(x)

Return an integer, being `x` rounded towards positive infinity.

copysign(x, y)

Return `x` with the sign of `y`.

cos(x)

Return the cosine of `x`.

cosh(x)

Return the hyperbolic cosine of `x`.

degrees(x)

Return radians `x` converted to degrees.

erf(x)

Return the error function of `x`.

erfc(x)

Return the complementary error function of `x`.

exp(x)

Return the exponential of `x`.

expm1(x)

Return `exp(x) - 1`.

fabs(x)

Return the absolute value of `x`.

floor(x)

Return an integer, being `x` rounded towards negative infinity.

fmod(x, y)

Return the remainder of `x/y`.

frexp(x)

Decomposes a floating-point number into its mantissa and exponent. The returned value is the tuple `(m, e)` such that `x == m * 2**e` exactly. If `x == 0` then the function returns `(0.0, 0)`, otherwise the relation `0.5 <= abs(m) < 1` holds.

gamma(x)

Return the gamma function of `x`.

isfinite(x)

Return `True` if `x` is finite.

isinf(x)

Return `True` if `x` is infinite.

isnan(x)

Return `True` if `x` is not-a-number

ldexp(x, exp)

Return `x * (2**exp)`.

lgamma(x)

Return the natural logarithm of the gamma function of `x`.

log(x) log(x, base)

With one argument, return the natural logarithm of *x*.

With two arguments, return the logarithm of *x* to the given *base*.

log10(x)

Return the base-10 logarithm of `x`.

log2(x)

Return the base-2 logarithm of `x`.

modf(x)

Return a tuple of two floats, being the fractional and integral parts of `x`. Both return values have the same sign as `x`.

pow(x, y)

Returns `x` to the power of `y`.

radians(x)

Return degrees `x` converted to radians.

sin(x)

Return the sine of `x`.

sinh(x)

Return the hyperbolic sine of `x`.

sqrt(x)

Return the square root of `x`.

tan(x)

Return the tangent of `x`.

tanh(x)

Return the hyperbolic tangent of `x`.

trunc(x)

Return an integer, being `x` rounded towards 0.

## Constants

e

base of the natural logarithm

pi

the ratio of a circle's circumference to its diameter
