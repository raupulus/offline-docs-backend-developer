---
title: The Percentile Extension
source_url: https://www.sqlite.org/percentile.html
source_path: percentile.html
technology: sqlite
version: 3.53.4
license: Blessing
retrieved_at: '2026-09-15'
section: guides
order: 3700
---

# 1. Overview

The percentile extension provides four aggregate functions that compute a percentile score and/or the median value for a distribution.

## 1.1. Availability

The percentile extension has been part of [the amalgamation](amalgamation.md) since SQLite version 3.51.0 (2025-11-04). However, the percentile extension is disabled by default and must be activated at compile-time using the [-DSQLITE_ENABLE_PERCENTILE](compile.md#enable_percentile) compile-time option.

Prior to SQLite 3.51.0, the percentile extension was in a separate source code file that needed to be compiled independently and treated as a [loadable extension](loadext.md).

# 2. Aggregate Functions Implemented By Percentile

The percentile extension implements the aggregate SQL functions described below. The algorithms used by all of these functions use O(N) space and O(NlogN) time, where N is the number of non-NULL inputs. <span id="*medianfunc"></span>

## 2.1. The median(Y) aggregate function

The median(Y) function is an aggregate that computes the median value of all non-NULL inputs Y. If any Y input to median() is not NULL and is not a numeric value, an error is raised. If there are no non-NULL, numeric inputs, then the result of median() is NULL.

The median is the value of the center element when all the inputs are sorted and the number of inputs is odd. If the number of inputs is even, then the median is the average of the two center inputs.

The median(Y) function is equivalent to [percentile(Y,50)](lang_aggfunc.md#percentile). <span id="*percentilefunc"></span>

## 2.2. The percentile(Y,P) aggregate function

The percentile(Y,P) aggregate function computes an answer X which is a value that is greater than or equal to P percent of the non-NULL inputs and which is less than or equal to 100-P percent of the inputs. The parameter P must be a number between 0.0 and 100.0. The value of P must be the same for all terms of the aggregate and may not be NULL. Y inputs must be either NULL or numeric. NULL values for Y are ignored. Any non-NULL Y input that is not numeric causes an error to be raised.

The percentile() function works by sorting the non-NULL inputs and then computing the input or inputs that are closest to P percent from the first to the last. The return value is the weighted average of the two closest inputs. <span id="*percentilecontfunc"></span>

## 2.3. The percentile_cont(Y,P) aggregate function

The percentile_cont(Y,P) function works like [percentile(Y,P)](lang_aggfunc.md#percentile) except that the P value spans the range of 0.0 to 1.0 instead of 0.0 to 100.0. Thus the result of percentile_cont(Y,P) is the same as [percentile(Y,P\*100)](lang_aggfunc.md#percentile).

The percentile_cont() function is defined by SQL standards. However, instead of being a simple function call "percentile_cont(Y,P)", the SQL-standard syntax goes like this:

SELECT percentile_cont(P) WITHIN GROUP (ORDER BY Y) FROM tab;\

That is a lot of syntax to mean exactly the same thing as:

SELECT percentile_cont(Y,P) FROM tab;\

SQLite will support the SQL-standard syntax, but only if it is compiled (from canonical sources, not from the [amalgamation](amalgamation.md)) using the [-DSQLITE_ENABLE_ORDERED_SET_AGGREGATES=1](compile.md#enable_ordered_set_aggregates) compile-time option. Without that compile-time option, only the simpler "percentile_cont(Y,P)" form is supported. Since there are no advantages to the prolix SQL-standard format, and dramatic readability disadvantages, and because the [SQLITE_ENABLE_ORDERED_SET_AGGREGATES](compile.md#enable_ordered_set_aggregates) compile-time option causes the SQLite library to be larger, that option is omitted from most builds.

This author believes that the "\_cont" suffix on this function name is an abbreviation for "continuous" and reflects the fact that the return value is a weighted average of the two closest input values to the actual percentile rank. The name is an SQL standard, not something chosen by the SQLite developers. <span id="*percentilediscfunc"></span>

## 2.4. The percentile_disc(Y,P) aggregate function

The percentile_disc(Y,P) function works like [percentile_cont(Y,P)](lang_aggfunc.md#percentile_cont) except that instead of doing a weighted average of the closest available inputs, it always returns a value that is one of the input values - the smaller of the two possible choices. The percentile_disc(Y,P) function is defined by SQL standards. As with percentile_cont(), the prolix ordered-set aggregate syntax is required, but that syntax is only supported by SQLite when SQLite is compiled using the [SQLITE_ENABLE_ORDERED_SET_AGGREGATES](compile.md#enable_ordered_set_aggregates) compile-time option.

This author believes that the "\_disc" suffix on this function name is an abbreviation for "discrete". The name is an SQL standard, not something chosen by the SQLite developers.

# 3. Design Requirements

The following requirements define the percentile extension.

1.  The percentile(Y,P) function is an aggregate function taking exactly two arguments.

2.  If the P argument to percentile(Y,P) is not the same for every row in the aggregate then an error is thrown. The word "same" in the previous sentence means that the value differs by less than 0.001.

3.  If the P argument to percentile(Y,P) evaluates to anything other than a number in the range of 0.0 to 100.0 inclusive then an error is thrown.

4.  If any Y argument to percentile(Y,P) evaluates to a value that is not NULL and is not numeric then an error is thrown.

5.  If any Y argument to percentile(Y,P) evaluates to plus or minus infinity then an error is thrown. (SQLite always interprets NaN values as NULL.)

6.  Both Y and P in percentile(Y,P) can be arbitrary expressions, including CASE WHEN expressions.

7.  The percentile(Y,P) aggregate is able to handle inputs of at least one million (1,000,000) rows.

8.  If there are no non-NULL values for Y, then percentile(Y,P) returns NULL.

9.  If there is exactly one non-NULL value for Y, the percentile(Y,P) returns the one Y value.

10. If there are N non-NULL values of Y where N is two or more and the Y values are ordered from least to greatest and a graph is drawn from 0 to N-1 such that the height of the graph at J is the J-th Y value and such that straight lines are drawn between adjacent Y values, then the percentile(Y,P) function returns the height of the graph at P\*(N-1)/100.

11. The percentile(Y,P) function always returns either a floating point number or NULL.

12. The percentile(Y,P) is implemented as a single C99 source-code file that compiles into a shared-library or DLL that can be loaded into SQLite using the sqlite3_load_extension() interface.

13. A separate median(Y) function is the equivalent of percentile(Y,50).

14. A separate percentile_cont(Y,P) function returns the same result as percentile(Y,P\*100.0). In other words, the fraction value in the second argument to percentile_cont() should be in the range of 0 to 1 instead of 0 to 100 as it is for percentile().

15. A separate percentile_disc(Y,P) function is like percentile_cont(Y,P) except that instead of returning the weighted average of the nearest two input values, it returns the next lower value. So the percentile_disc(Y,P) will always return a value that was one of the inputs.

16. All of median(), percentile(Y,P), percentile_cont(Y,P) and percentile_disc(Y,P) can be used as window functions.
