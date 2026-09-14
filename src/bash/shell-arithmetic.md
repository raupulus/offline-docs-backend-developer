---
title: Shell Arithmetic
source_url: https://www.gnu.org/software/bash/manual
source_path: 027-shell-arithmetic.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 270
---

## Shell Arithmetic

arithmetic, shell

shell arithmetic

expressions, arithmetic

evaluation, arithmetic

arithmetic evaluation

The shell allows arithmetic expressions to be evaluated, as one of the shell expansions or by using the `((` compound command, the `let` and `declare` builtins, the arithmetic `for` command, the `[[` conditional command, or the `-i` option to the `declare` builtin.

Evaluation is done in the largest fixed-width integers available, with no check for overflow, though division by 0 is trapped and flagged as an error. The operators and their precedence, associativity, and values are the same as in the C language. The following list of operators is grouped into levels of equal-precedence operators. The levels are listed in order of decreasing precedence.

`id++ id--`  
variable post-increment and post-decrement

`++id --id`  
variable pre-increment and pre-decrement

`- +`  
unary minus and plus

`! ~`  
logical and bitwise negation

`**`  
exponentiation

`* / %`  
multiplication, division, remainder

`+ -`  
addition, subtraction

`<< >>`  
left and right bitwise shifts

`<= >= < >`  
comparison

`== !=`  
equality and inequality

`&`  
bitwise AND

`^`  
bitwise exclusive OR

`|`  
bitwise OR

`&&`  
logical AND

`||`  
logical OR

`expr ? if-true-expr : if-false-expr`  
conditional operator

`= *= /= %= += -= <<= >>= &= ^= |=`  
assignment

`expr1 , expr2`  
comma

Shell variables are allowed as operands; parameter expansion is performed before the expression is evaluated. Within an expression, shell variables may also be referenced by name without using the parameter expansion syntax. This means you can use \<x\>, where \<x\> is a shell variable name, in an arithmetic expression, and the shell will evaluate its value as an expression and use the result. A shell variable that is null or unset evaluates to 0 when referenced by name in an expression.

The value of a variable is evaluated as an arithmetic expression when it is referenced, or when a variable which has been given the `integer` attribute using ‘`declare -i`’ is assigned a value. A null value evaluates to 0. A shell variable need not have its `integer` attribute turned on to be used in an expression.

Integer constants follow the C language definition, without suffixes or character constants. Constants with a leading 0 are interpreted as octal numbers. A leading ‘`0x`’ or ‘`0X`’ denotes hexadecimal. Otherwise, numbers take the form \[\<base\>`#`\]\<n\>, where the optional \<base\> is a decimal number between 2 and 64 representing the arithmetic base, and \<n\> is a number in that base. If \<base\>`#` is omitted, then base 10 is used. When specifying \<n\>, if a non-digit is required, the digits greater than 9 are represented by the lowercase letters, the uppercase letters, ‘`@`’, and ‘`_`’, in that order. If \<base\> is less than or equal to 36, lowercase and uppercase letters may be used interchangeably to represent numbers between 10 and 35.

Operators are evaluated in precedence order. Sub-expressions in parentheses are evaluated first and may override the precedence rules above.
