---
title: Floating Point Numbers
source_url: https://www.sqlite.org/floatingpoint.html
source_path: floatingpoint.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 2880
---

# 1. How SQLite Stores Numbers

SQLite stores integer values in the 64-bit [twos-complement](https://en.wikipedia.org/wiki/Two%27s_complement) format¹. This gives a storage range of -9223372036854775808 to +9223372036854775807, inclusive. Integers within this range are exact. <span id="fpapprox"></span>

So-called "REAL" or floating point values are stored in the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) [Binary-64](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) format¹. This gives a range of positive values between approximately 1.7976931348623157e+308 and 4.9406564584124654e-324 with an equivalent range of negative values. A binary-64 can also be 0.0 (and -0.0), positive and negative infinity and "NaN" or "Not-a-Number". Floating point values are approximate.

Pay close attention to the previous sentence:

> **Floating point values are approximate.**

If you need an exact answer, you should not use binary-64 floating-point values, in SQLite or in any other product. This is not an SQLite limitation. It is a mathematical limitation inherent in the design of floating-point numbers.

—\
¹ Exception: The [R-Tree extension](rtree.md) stores information as 32-bit floating point or integer values.

## 1.1. Floating-Point Accuracy

SQLite will preserve as many significant digits of a floating point value as it can. But an IEEE 754 double only holds about 15.95 significant digits. Furthermore, SQLite makes no guarantees that the accuracy of computations on floating point values will even be this accurate, because no such guarantees are possible. Performing math on floating-point values introduces error. For example, consider what happens if you attempt to subtract two floating-point numbers of similar magnitude:

> <table data-border="0" data-cellpadding="0" data-cellspacing="0">
> <colgroup>
> <col style="width: 100%" />
> </colgroup>
> <tbody>
> <tr>
> <td style="text-align: right;">1152693165.1106291898</td>
> </tr>
> <tr>
> <td style="text-align: right;">-1152693165.1106280772</td>
> </tr>
> <tr>
> <td style="text-align: right;"><hr /></td>
> </tr>
> <tr>
> <td style="text-align: right;">0.0000011126</td>
> </tr>
> </tbody>
> </table>

The result shown above (0.0000011126) is the correct answer. But if you do this computation using binary-64 floating-point, the answer you get is 0.00000095367431640625 - an error of about 14%. If you do many similar computations as part of your program, the errors add up so that your final result might be completely meaningless.

The error arises because only about 15.95 significant digits of each number are stored accurately using the IEEE 754 binary-64 format, and the first difference between the two numbers being subtracted is in the 16th digit.

## 1.2. Floating Point Numbers

The binary-64 floating-point format uses 64 bits per number. Hence there are 1.845e+19 different possible floating point values. On the other hand there are infinitely many real numbers in the range of 1.7977e+308 and 4.9407e-324. It follows then that binary-64 cannot possibly represent all possible real numbers within that range. Approximations are required.

An IEEE 754 floating-point value is an integer multiplied by a power of two:

> M × 2<sup><span class="small">E</span></sup>

The M value is the "mantissa" and E is the "exponent". Both M and E are integers.

For Binary-64, M is a 53-bit integer and E is an 11-bit integer that is offset so that represents a range of values between -1074 and +972, inclusive.

*(NB: The usual description of IEEE 754 is more complex, and it is important to understand the added complexity if you really want to appreciate the details, merits, and limitations of IEEE 754. However, the integer description shown here, while not exactly right, is easier to understand and is sufficient for the purposes of this article.)*

### 1.2.1. Unrepresentable numbers

Not every decimal number with fewer than 16 significant digits can be represented exactly as a binary-64 number. In fact, most decimal numbers with digits to the right of the decimal point lack an exact binary-64 equivalent. For example, if you have a database column that is intended to hold an item price in dollars and cents, the only cents value that can be exactly represented are 0.00, 0.25, 0.50, and 0.75. Any other numbers to the right of the decimal point result in an approximation. If you provide a "price" value of 47.49, that number will be represented in binary-64 as:

> 6683623321994527 × 2<sup><span class="small">-47</span></sup>

Which works out to be:

> 47.49000000000000198951966012828052043914794921875

That number is very close to 47.49, but it is not exact. It is a little too big. If we reduce M by one to 6683623321994526 so that we have the next smaller possible binary-64 value, we get:

> 47.4899999999999948840923025272786617279052734375

This second number is too small. The first number is closer to the desired value of 47.49, so that is the one that gets used. But it is not exact. Most decimal values work this way in IEEE 754. Remember the key point we made above:

> **Floating point values are approximate.**

If you remember nothing else about floating-point values, please don't forget this one key idea.

### 1.2.2. Is it close enough?

The precision provided by IEEE 754 Binary-64 is sufficient for most computations. For example, if "47.49" represents a price and inflation is running at 2% per year, then the price is going up by about 0.0000000301 dollars per second. The error in the recorded value of 47.49 represents about 66 nanoseconds worth of inflation. So if the 47.49 price is exact when you enter it, then the effects of inflation will cause the true value to exactly equal the value actually stored (47.4900000000000019895196601282805204391479492187) in less than one ten-millionth of a second. Surely that level of precision is sufficient for most purposes? <span id="*rounding"></span>

## 1.3. Rounding Floating-Point Numbers For Display

When converting a binary-64 number into text for display purposes (for example by calling [sqlite3_column_text()](c3ref/column_blob.md) or [sqlite3_value_text()](c3ref/value_blob.md) or by using the [CAST operator](lang_expr.md#castexpr) in SQL), the value is normally rounded to a reasonable number of significant digits. One rarely wants to see all 49 signficant digits of 6683623321994527×pow(2,-47). The first four digits, "47.49" in this case, is usually a better display option.

There are also performance reasons for rounding. 6683623321994527×pow(2,-47) can be converted into "47.49" relatively quickly, but generating the full 49-digit expansion requires a lot more computation.

At what point should rounding occur? Rounding to 17 significant digits or more results in text that, when coverted back into binary-64, gives the exact same value that we started with. Rounding to 15 significant digits or less can often gives this exact round-trip result, but not always. On the other hand, rounding to 15 digits tends to give results that are more pleasing to human readers, whereas rounding to 17 digits can result in long numbers with a lot of '0's or '9's in the middle.

Prior to SQLite 3.52.0 (2026-03-06), if you tried to round 6683623321994527×pow(2,-47) to 17 digits, SQLite would look at the first 18 digits ("47.4900000000000019"), see that the last digit was 5 or more and hence round up to "47.490000000000002". For that reason, in earlier versions of SQLite, rounding occurred at 15 digits. It would look at the 16th digit, see that it was zero and hence just truncate, then remove trailing zeros, and you are left with "47.49", which is the answer most people want. And it turns out that converting text "47.49" back to binary-64 results in 6683623321994527×pow(2,-47), so the value does not change if you round-trip binary-64→text→binary-64. All is well.

But this does not work for every case. Consider, for example, the product of 1.23 and 2.34. The number 1.23 is:

> 2769713770832855 × 2<sup><span class="small">-51</span></sup>\
>    = 1.229999999999999982236431605997495353221893310546875

And 2.34 is:

> 5269211564023480 × 2<sup><span class="small">-51</span></sup>\
>    = 2.339999999999999857891452847979962825775146484375

If you do an exact multiplication of those two values you get:

> 2.878199999999999783639736961049495926597557229698714817531408904915934954260592348873615264892578125

Which cannot be represented in binary-64. The floating point hardware in your CPU truncates this to:

> 6481130223748880 × 2<sup><span class="small">-51</span></sup>\
>    = 2.87819999999999964757080306299030780792236328125

If you round that last value to 15 significant digits, you get 2.8782, which is the answer most people expect. If you round to 17 digits, you get 2.8781999999999997 instead. However, 2.8782 and 2.8781999999999997 are not the same number in binary-64.

> 2.8782 → 6481130223748881 × 2<sup><span class="small">-51</span></sup>\
> 2.8781999999999997 → 6481130223748880 × 2<sup><span class="small">-51</span></sup>

The mantissa is different by one. So converting the text "2.8782" back to binary-64 will <u>not</u> go back to the original product of 1.23×2.34. It will be very close, but not exact. Converting the text "2.8781999999999997" back to binary-64 <u>does</u> go back to original value though. And so in that sense, 2.8781999999999997 is a more accurate answer. <span id="*fpdigits"></span>

### 1.3.1. Choosing The Number Of Floating-Point Digits To Display

So there is a trade-off. Do you (A) round to 15 digits, and provide answers that are closer to what humans expect to see, or do you (B) round to 17 digits and provide answers that sometimes have lots '0's or '9's after the decimal point but which will round-trip back to the original binary-64?

With SQLite 3.51.2 and earlier, solution (A) was the only option. Beginning with SQLite 3.52.0 (2026-03-06), solution (B) is available and is the default, though applications can choose to do back to solution (A). In C-code, one can choose option (A) by running code like this:

> sqlite3_db_config(db, [SQLITE_DBCONFIG_FP_DIGITS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits), 15, 0);

Or in the [CLI](cli.md), one can do:

> .dbconfig fp_digits 15

This change occurred because in version 3.52.0, the rounding algorithm was enhanced to work something like this:

1.  Round to 15 digits.
2.  Convert the text result back to binary-64.
3.  If the binary-64 value from the previous step is different, then:\
      • Redo step (a) with 17-digit rounding.

Rounding to 15 digits is usually enough. Step (c) seldom occurs. The text renderings with lots of '0's and '9's only appear in the unusual cases where they make a difference. The reason this enhancement was made in version 3.52.0 was that the binary-64→text→binary-64 conversion routines were rewritten to use 64-bit integer arithmetic instead of floating-point computations, and so step (b) in the algorithm above became computationally reasonable to perform. The binary-64→text conversion in 3.52.0 is still faster than before, even with the addition of steps (b) and (c). If you do not want the (negligible) overhead of step (b) and (c), just set [SQLITE_DBCONFIG_FP_DIGITS](c3ref/c_dbconfig_defensive.md#sqlitedbconfigfpdigits) to 15.

# 2. Extensions For Dealing With Floating Point Numbers

<span id="ieee754ext"></span>

## 2.1. The ieee754.c Extension

The ieee754 extension converts a floating point number between its binary-64 representation and the M×2<sup><span class="small">E</span></sup> format. In other words in the expression:

> F = M × 2<sup><span class="small">E</span></sup>

The ieee754 extension converts between F and (M,E) and back again.

The ieee754 extension is not part of the [amalgamation](amalgamation.md), but it is included by default in the [CLI](cli.md). If you want to include the ieee754 extension in your application, you will need to compile and load it separately. <span id="ieee754"></span>

### 2.1.1. The ieee754() function

The ieee754(F) SQL function takes a single floating-point argument as its input and returns a string that looks like this:

> 'ieee754(M,E)'

Except that the M and E are replaced by the mantissa and exponent of the floating point number. For example:

sqlite\> .mode box\
sqlite\> SELECT ieee754(47.49) AS x;\
┌───────────────────────────────┐\
│               x               │\
├───────────────────────────────┤\
│ ieee754(6683623321994527,-47) │\
└───────────────────────────────┘\

Going in the other direction, the 2-argument version of ieee754() takes the M and E values and converts them into the corresponding F value:

sqlite\> select ieee754(6683623321994527,-47) as x;\
┌───────┐\
│   x   │\
├───────┤\
│ 47.49 │\
└───────┘\

<span id="ieee754m"></span>

### 2.1.2. The ieee754_mantissa() and ieee754_exponent() functions

The text output of the one-argument form of ieee754() is great for human readability, but it is awkward to use as part of a larger expression. Hence the ieee754_mantissa() and ieee754_exponent() routines were added to return the M and E values corresponding to their single argument F value. For example:

sqlite\> .mode box\
sqlite\> SELECT ieee754_mantissa(47.49) AS M, ieee754_exponent(47.49) AS E;\
┌──────────────────┬─────┐\
│        M         │  E  │\
├──────────────────┼─────┤\
│ 6683623321994527 │ -47 │\
└──────────────────┴─────┘\

<span id="ieee754b"></span>

### 2.1.3. The ieee754_from_blob() and ieee754_to_blob() functions

The ieee754_to_blob(F) SQL function converts the floating point number F into an 8-byte BLOB that is the big-endian binary-64 encoding of that number. The ieee754_from_blob(B) function goes the other way, converting an 8-byte blob into the floating-point value that the binary-64 encoding represents.

So, for example, if you read [on Wikipedia](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) that the encoding for the minimum positive binary-64 value is 0x0000000000000001, then you can find the corresponding floating point value like this:

sqlite\> .mode box\
sqlite\> SELECT ieee754_from_blob(x'0000000000000001') AS F;\
┌───────────────────────┐\
│           F           │\
├───────────────────────┤\
│ 4.94065645841247e-324 │\
└───────────────────────┘\

Or go the other way:

sqlite\> .mode box\
sqlite\> SELECT quote(ieee754_to_blob(4.94065645841247e-324)) AS binary-64;\
┌─────────────────────┐\
│      binary-64      │\
├─────────────────────┤\
│ X'0000000000000001' │\
└─────────────────────┘\

<span id="decext"></span>

## 2.2. The decimal.c Extension

The decimal extension provides arbitrary-precision decimal arithmetic on numbers stored as text strings. Because the numbers are stored to arbitrary precision and as text, no approximations are needed. Computations can be done exactly.

The decimal extension is not (currently) part of the SQLite [amalgamation](amalgamation.md). However, it is included in the [CLI](cli.md). The source code to this extension can be found at [ext/misc/decimal.c](https://sqlite.org/src/file/ext/misc/decimal.c?ci=trunk).

The decimal extension supports the following SQL functions and collating sequences: <span id="*decmth"></span>

### 2.2.1. The decimal_add(A,B), decimal_sub(A,B), and decimal_mul(A,B) functions

These functions compute the sum, difference, and product, respectively, of the two inputs A and B and return the result as text. The inputs can be either decimal text or numeric values. Numeric inputs are converted into decimal text before the computation is performed.

There is no "decimal_div(A,B)" function because division does not always have a finite-length decimal result. <span id="decimal_pow2"></span>

### 2.2.2. The decimal_pow2(N) function

The decimal_pow2(N) function computes the exact decimal representation of the N-th power of 2. N must be an integer between -20000 and +20000.

This function can be slow and can use a lot of memory for large values of N. <span id="decimal"></span>

### 2.2.3. The decimal(X) and decimal_exp(X) functions

The decimal(X) and decimal_exp(X) generate a decimal representation for input X. The input X can be an integer or a floating point number, or a text decimal. The decimal_exp(X) function returns the result in exponential notation (with a "e+NN" at the end) and decimal(X) returns a pure decimal (without the "e+NN").

If the input X is a floating point value, it is expanded to its exact decimal equivalent. For example:

sqlite\> .mode qbox\
sqlite\> select decimal(47.49);\
┌──────────────────────────────────────────────────────┐\
│                    decimal(47.49)                    │\
├──────────────────────────────────────────────────────┤\
│ '47.49000000000000198951966012828052043914794921875' │\
└──────────────────────────────────────────────────────┘\

<span id="decimal_cmp"></span>

### 2.2.4. The decimal_cmp(X) function

The decimal_cmp(A,B) function compares two decimal values A and B. The result will be negative, zero, or positive if A is less than, equal to, or greater than B, respectively. <span id="decimal_sum"></span>

### 2.2.5. The decimal_sum(X) aggregate function

The decimal_sum(X) function is an aggregate, like the built-in [total() aggregate function](lang_aggfunc.md#sumunc), except that decimal_sum() computes its result to arbitrary precision and is therefore precise. <span id="*deccseq"></span>

### 2.2.6. The decimal collating sequence

The decimal extension provides the "decimal" collating sequence that compares decimal text strings in numeric order.
