---
title: La clase NumberFormatter
source_url: https://www.php.net/manual/es/class.numberformatter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 5e36b489f
order: 42360
---

## Introducción

Los programas almacenan y manipulan números utilizando una representación local, binaria e independiente. Al mostrar un número, este se convierte en una versión particular. Por ejemplo, un número como 12345.67 se escribe "12,345.67" en los USA, "12 345,67" en Francia y "12.345,67" en Alemania.

Al llamar a los métodos proporcionados por `NumberFormatter`, se pueden formatear números, montos de divisas y porcentajes, según las convenciones locales. `NumberFormatter` tiene en cuenta las convenciones, por lo que debe crearse un nuevo objeto `NumberFormatter` para cada convención. Las métodos de `NumberFormatter` formatean tipos primitivos como números decimales, y producen un string.

Para las monedas, se puede utilizar el formato monetario para crear un formateador que devuelve un string, con el símbolo de divisa apropiado. Por supuesto, `NumberFormatter` no conoce los tipos de cambio, por lo que el formato se realizará, cualquiera sea la divisa solicitada. Esto significa que el mismo número tendrá diferentes valores monetarios según la configuración local. Por ejemplo, el número 9988776.65 se mostrará: 9 988 776,65 € en Francia, 9.988.776,65 € en Alemania, \$9,988,776.65 en los USA

Para formatear porcentajes, debe crearse un formateador local, con un tipo de formato porcentaje. Con este formateador, una fracción decimal como 0.75 se mostrará como 75%.

Para formatos más complejos, como números escritos literalmente, se utilizan formateadores basados en reglas.

## Sinopsis de la clase

NumberFormatter

Constantes

public

const

int

NumberFormatter::PATTERN_DECIMAL

public

const

int

NumberFormatter::DECIMAL

public

const

int

NumberFormatter::DECIMAL_COMPACT_SHORT

public

const

int

NumberFormatter::DECIMAL_COMPACT_LONG

public

const

int

NumberFormatter::CURRENCY

public

const

int

NumberFormatter::PERCENT

public

const

int

NumberFormatter::SCIENTIFIC

public

const

int

NumberFormatter::SPELLOUT

public

const

int

NumberFormatter::ORDINAL

public

const

int

NumberFormatter::DURATION

public

const

int

NumberFormatter::PATTERN_RULEBASED

public

const

int

NumberFormatter::IGNORE

public

const

int

NumberFormatter::CURRENCY_ISO

public

const

int

NumberFormatter::CURRENCY_PLURAL

public

const

int

NumberFormatter::CURRENCY_ACCOUNTING

public

const

int

NumberFormatter::CASH_CURRENCY

public

const

int

NumberFormatter::CURRENCY_STANDARD

public

const

int

NumberFormatter::DEFAULT_STYLE

public

const

int

NumberFormatter::ROUND_CEILING

public

const

int

NumberFormatter::ROUND_FLOOR

public

const

int

NumberFormatter::ROUND_DOWN

public

const

int

NumberFormatter::ROUND_UP

public

const

int

NumberFormatter::ROUND_TOWARD_ZERO

public

const

int

NumberFormatter::ROUND_AWAY_FROM_ZERO

public

const

int

NumberFormatter::ROUND_HALFEVEN

public

const

int

NumberFormatter::ROUND_HALFODD

public

const

int

NumberFormatter::ROUND_HALFDOWN

public

const

int

NumberFormatter::ROUND_HALFUP

public

const

int

NumberFormatter::PAD_BEFORE_PREFIX

public

const

int

NumberFormatter::PAD_AFTER_PREFIX

public

const

int

NumberFormatter::PAD_BEFORE_SUFFIX

public

const

int

NumberFormatter::PAD_AFTER_SUFFIX

public

const

int

NumberFormatter::PARSE_INT_ONLY

public

const

int

NumberFormatter::GROUPING_USED

public

const

int

NumberFormatter::DECIMAL_ALWAYS_SHOWN

public

const

int

NumberFormatter::MAX_INTEGER_DIGITS

public

const

int

NumberFormatter::MIN_INTEGER_DIGITS

public

const

int

NumberFormatter::INTEGER_DIGITS

public

const

int

NumberFormatter::MAX_FRACTION_DIGITS

public

const

int

NumberFormatter::MIN_FRACTION_DIGITS

public

const

int

NumberFormatter::FRACTION_DIGITS

public

const

int

NumberFormatter::MULTIPLIER

public

const

int

NumberFormatter::GROUPING_SIZE

public

const

int

NumberFormatter::ROUNDING_MODE

public

const

int

NumberFormatter::ROUNDING_INCREMENT

public

const

int

NumberFormatter::FORMAT_WIDTH

public

const

int

NumberFormatter::PADDING_POSITION

public

const

int

NumberFormatter::SECONDARY_GROUPING_SIZE

public

const

int

NumberFormatter::SIGNIFICANT_DIGITS_USED

public

const

int

NumberFormatter::MIN_SIGNIFICANT_DIGITS

public

const

int

NumberFormatter::MAX_SIGNIFICANT_DIGITS

public

const

int

NumberFormatter::LENIENT_PARSE

public

const

int

NumberFormatter::POSITIVE_PREFIX

public

const

int

NumberFormatter::POSITIVE_SUFFIX

public

const

int

NumberFormatter::NEGATIVE_PREFIX

public

const

int

NumberFormatter::NEGATIVE_SUFFIX

public

const

int

NumberFormatter::PADDING_CHARACTER

public

const

int

NumberFormatter::CURRENCY_CODE

public

const

int

NumberFormatter::DEFAULT_RULESET

public

const

int

NumberFormatter::PUBLIC_RULESETS

public

const

int

NumberFormatter::DECIMAL_SEPARATOR_SYMBOL

public

const

int

NumberFormatter::GROUPING_SEPARATOR_SYMBOL

public

const

int

NumberFormatter::PATTERN_SEPARATOR_SYMBOL

public

const

int

NumberFormatter::PERCENT_SYMBOL

public

const

int

NumberFormatter::ZERO_DIGIT_SYMBOL

public

const

int

NumberFormatter::DIGIT_SYMBOL

public

const

int

NumberFormatter::MINUS_SIGN_SYMBOL

public

const

int

NumberFormatter::PLUS_SIGN_SYMBOL

public

const

int

NumberFormatter::CURRENCY_SYMBOL

public

const

int

NumberFormatter::INTL_CURRENCY_SYMBOL

public

const

int

NumberFormatter::MONETARY_SEPARATOR_SYMBOL

public

const

int

NumberFormatter::EXPONENTIAL_SYMBOL

public

const

int

NumberFormatter::PERMILL_SYMBOL

public

const

int

NumberFormatter::PAD_ESCAPE_SYMBOL

public

const

int

NumberFormatter::INFINITY_SYMBOL

public

const

int

NumberFormatter::NAN_SYMBOL

public

const

int

NumberFormatter::SIGNIFICANT_DIGIT_SYMBOL

public

const

int

NumberFormatter::MONETARY_GROUPING_SEPARATOR_SYMBOL

public

const

int

NumberFormatter::TYPE_DEFAULT

public

const

int

NumberFormatter::TYPE_INT32

public

const

int

NumberFormatter::TYPE_INT64

public

const

int

NumberFormatter::TYPE_DOUBLE

public

const

int

NumberFormatter::TYPE_CURRENCY

Métodos

## Véase también

[Documentación de formato ICU](https://unicode-org.github.io/icu/userguide/format_parse/), [Formateadores de números ICU](https://unicode-org.github.io/icu/userguide/format_parse/numbers/), [Formateador de números decimales ICU](https://unicode-org.github.io/icu-docs/apidoc/released/icu4c/classDecimalFormat.html), [Formateadores basados en reglas de ICU](https://unicode-org.github.io/icu/userguide/format_parse/numbers/rbnf.html)

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Se añadieron `NumberFormatter::DECIMAL_COMPACT_SHORT`, `NumberFormatter::DECIMAL_COMPACT_LONG`, `NumberFormatter::CURRENCY_ISO`, `NumberFormatter::CURRENCY_PLURAL`, `NumberFormatter::CASH_CURRENCY`, `NumberFormatter::CURRENCY_STANDARD`. |
| 8.4.0 | Las constantes de clase ahora están tipadas. |
