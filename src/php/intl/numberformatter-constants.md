---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/intl.numberformatter-constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter-constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 5e36b489f
order: 42350
---

## Constantes predefinidas

## Tipos de formato

Estos estilos son utilizados por `numfmt_create` para definir el tipo de formateador.

`NumberFormatter::PATTERN_DECIMAL` `int`  
Formato decimal definido por un patrón

`NumberFormatter::DECIMAL` `int`  
Formato decimal

`NumberFormatter::DECIMAL_COMPACT_SHORT` `int`  
Formato decimal expresado en notación compacta (forma corta), p.ej. "23K", "45B". Disponible a partir de PHP 8.5.0 e ICU 56.

`NumberFormatter::DECIMAL_COMPACT_LONG` `int`  
Formato decimal expresado en notación compacta (forma larga), p.ej. "23 thousand", "45 billion". Disponible a partir de PHP 8.5.0 e ICU 56.

`NumberFormatter::CURRENCY` `int`  
Formato monetario

`NumberFormatter::CURRENCY_ISO` `int`  
Formato monetario ISO (p.ej. "USD1.00"). Disponible a partir de PHP 8.5.0.

`NumberFormatter::CURRENCY_PLURAL` `int`  
Formato monetario plural (p.ej. "1.00 US dollar" y "3.00 US dollars"). Disponible a partir de PHP 8.5.0.

`NumberFormatter::CASH_CURRENCY` `int`  
Símbolo monetario dado el uso CASH, p.ej. "NT\$3" en lugar de "NT\$3.23". Disponible a partir de PHP 8.5.0 e ICU 54.

`NumberFormatter::CURRENCY_STANDARD` `int`  
Símbolo monetario, p.ej. "\$1.00", utilizando estilo no contable para valores negativos (p.ej. signo menos). Disponible a partir de PHP 8.5.0 e ICU 56.

`NumberFormatter::PERCENT` `int`  
Formato porcentual

`NumberFormatter::SCIENTIFIC` `int`  
Formato científico

`NumberFormatter::SPELLOUT` `int`  
Formato literal, basado en reglas

`NumberFormatter::ORDINAL` `int`  
Formato ordinal, basado en reglas

`NumberFormatter::DURATION` `int`  
Formato de duración, basado en reglas

`NumberFormatter::PATTERN_RULEBASED` `int`  
Formato de patrón, basado en reglas

`NumberFormatter::CURRENCY_ACCOUNTING` `int`  
Formato monetario para contabilidad, por ejemplo, `($3.00)` para un monto de moneda negativo en lugar de `-$3.00`. Disponible a partir de PHP 7.4.1 y ICU 53.

`NumberFormatter::DEFAULT_STYLE` `int`  
Formato por defecto para las convenciones locales

`NumberFormatter::IGNORE` `int`  
Alias de PATTERN_DECIMAL

## Especificadores de formato de número

Estas constantes definen el método de análisis y formato de los números. Deben ser utilizadas como argumentos de las funciones `numfmt_format` y `numfmt_parse`.

`NumberFormatter::TYPE_DEFAULT` `int`  
Deriva el tipo desde el tipo de variable

`NumberFormatter::TYPE_INT32` `int`  
Formatea/analiza un entero de 32 bits

`NumberFormatter::TYPE_INT64` `int`  
Formatea/analiza un entero de 64 bits

`NumberFormatter::TYPE_DOUBLE` `int`  
Formatea/analiza un número decimal

`NumberFormatter::TYPE_CURRENCY` `int`  
Formatea/analiza un valor monetario. Deprecado a partir de PHP 8.3.0

## Atributos de formato de número

Atributos de formatos de número utilizados por `numfmt_get_attribute` y `numfmt_set_attribute`.

`NumberFormatter::PARSE_INT_ONLY` `int`  
Analiza únicamente los enteros.

`NumberFormatter::GROUPING_USED` `int`  
Separador de grupos.

`NumberFormatter::DECIMAL_ALWAYS_SHOWN` `int`  
Muestra siempre una coma decimal.

`NumberFormatter::MAX_INTEGER_DIGITS` `int`  
Número máximo de dígitos.

`NumberFormatter::MIN_INTEGER_DIGITS` `int`  
Número mínimo de dígitos.

`NumberFormatter::INTEGER_DIGITS` `int`  
Número de dígitos.

`NumberFormatter::MAX_FRACTION_DIGITS` `int`  
Número máximo de decimales.

`NumberFormatter::MIN_FRACTION_DIGITS` `int`  
Número mínimo de decimales.

`NumberFormatter::FRACTION_DIGITS` `int`  
Número de decimales.

`NumberFormatter::MULTIPLIER` `int`  
Multiplicador.

`NumberFormatter::GROUPING_SIZE` `int`  
Tamaño de agrupamiento.

`NumberFormatter::ROUNDING_MODE` `int`  
Modo de redondeo.

`NumberFormatter::ROUNDING_INCREMENT` `int`  
Incremento de redondeo.

`NumberFormatter::FORMAT_WIDTH` `int`  
El ancho de relleno para el formato de un número.

`NumberFormatter::PADDING_POSITION` `int`  
La posición en la que se realiza el relleno. Véase las constantes de relleno para tener los diferentes valores posibles.

`NumberFormatter::SECONDARY_GROUPING_SIZE` `int`  
Tamaño secundario de agrupamiento.

`NumberFormatter::SIGNIFICANT_DIGITS_USED` `int`  
Utiliza los dígitos significativos.

`NumberFormatter::MIN_SIGNIFICANT_DIGITS` `int`  
Número mínimo de dígitos significativos.

`NumberFormatter::MAX_SIGNIFICANT_DIGITS` `int`  
Número máximo de dígitos significativos.

`NumberFormatter::LENIENT_PARSE` `int`  
Modo de análisis utilizado por los formatos basados en reglas.

## Atributos de texto de formato de número

Atributos de texto para los formatos de números, utilizados por `numfmt_get_text_attribute` y `numfmt_set_text_attribute`.

`NumberFormatter::POSITIVE_PREFIX` `int`  
Prefijo positivo.

`NumberFormatter::POSITIVE_SUFFIX` `int`  
Sufijo positivo.

`NumberFormatter::NEGATIVE_PREFIX` `int`  
Prefijo negativo.

`NumberFormatter::NEGATIVE_SUFFIX` `int`  
Sufijo negativo.

`NumberFormatter::PADDING_CHARACTER` `int`  
El carácter a utilizar para rellenar los formatos hasta el tamaño.

`NumberFormatter::CURRENCY_CODE` `int`  
El código de moneda ISO.

`NumberFormatter::DEFAULT_RULESET` `int`  
El conjunto de reglas por defecto. Solo es utilizable con los formateadores basados en reglas.

`NumberFormatter::PUBLIC_RULESETS` `int`  
El conjunto de reglas públicas. Esto solo está disponible con los formateadores basados en reglas. Es un atributo de solo lectura. Las reglas públicas se devuelven en forma de una sola cadena, y cada regla está delimitada por un punto y coma ';'.

## Especificación de los símbolos de formato

Los símbolos de formato utilizados por `numfmt_get_symbol` y `numfmt_set_symbol`.

`NumberFormatter::DECIMAL_SEPARATOR_SYMBOL` `int`  
El separador decimal.

`NumberFormatter::GROUPING_SEPARATOR_SYMBOL` `int`  
El separador de grupos.

`NumberFormatter::PATTERN_SEPARATOR_SYMBOL` `int`  
El separador de patrón.

`NumberFormatter::PERCENT_SYMBOL` `int`  
El símbolo de porcentaje.

`NumberFormatter::ZERO_DIGIT_SYMBOL` `int`  
Cero.

`NumberFormatter::DIGIT_SYMBOL` `int`  
Un carácter que representa un dígito en un patrón.

`NumberFormatter::MINUS_SIGN_SYMBOL` `int`  
El signo menos.

`NumberFormatter::PLUS_SIGN_SYMBOL` `int`  
El signo más.

`NumberFormatter::CURRENCY_SYMBOL` `int`  
El símbolo de moneda.

`NumberFormatter::INTL_CURRENCY_SYMBOL` `int`  
El símbolo internacional de moneda.

`NumberFormatter::MONETARY_SEPARATOR_SYMBOL` `int`  
El separador monetario.

`NumberFormatter::EXPONENTIAL_SYMBOL` `int`  
El símbolo exponencial.

`NumberFormatter::PERMILL_SYMBOL` `int`  
El símbolo por mil.

`NumberFormatter::PAD_ESCAPE_SYMBOL` `int`  
El carácter de escape de símbolos.

`NumberFormatter::INFINITY_SYMBOL` `int`  
El símbolo de infinito.

`NumberFormatter::NAN_SYMBOL` `int`  
El símbolo "no es un número".

`NumberFormatter::SIGNIFICANT_DIGIT_SYMBOL` `int`  
El símbolo de dígitos significativos.

`NumberFormatter::MONETARY_GROUPING_SEPARATOR_SYMBOL` `int`  
El separador de grupos monetarios.

## Modos de redondeo

Los modos de redondeo utilizados por las funciones `numfmt_get_attribute` y `numfmt_set_attribute` con el atributo `NumberFormatter::ROUNDING_MODE`.

`NumberFormatter::ROUND_AWAY_FROM_ZERO`  
Alias de `NumberFormatter::ROUND_UP`.

`NumberFormatter::ROUND_CEILING`  
Modo de redondeo hacia el infinito positivo.

`NumberFormatter::ROUND_DOWN` `int`  
Modo de redondeo hacia cero.

`NumberFormatter::ROUND_FLOOR` `int`  
Modo de redondeo hacia el infinito negativo.

`NumberFormatter::ROUND_HALFDOWN` `int`  
Modo de redondeo hacia el entero más cercano, a menos que estén equidistantes: redondeo inferior en este caso.

`NumberFormatter::ROUND_HALFEVEN` `int`  
Modo de redondeo hacia el entero más cercano, a menos que estén equidistantes: redondeo hacia el número par en este caso.

`NumberFormatter::ROUND_HALFODD`  
Modo de redondeo hacia el « vecino impar ».

`NumberFormatter::ROUND_HALFUP`  
Modo de redondeo hacia el entero más cercano, a menos que estén equidistantes: redondeo superior en este caso.

`NumberFormatter::ROUND_TOWARD_ZERO`  
Alias de `NumberFormatter::ROUND_DOWN`.

`NumberFormatter::ROUND_UP` `int`  
Modo de redondeo que aleja de cero.

## Especificadores de relleno

Valores de relleno utilizados por `numfmt_get_attribute` y `numfmt_set_attribute` con el atributo `NumberFormatter::PADDING_POSITION`.

`NumberFormatter::PAD_AFTER_PREFIX` `int`  
Caracteres de relleno añadidos después del prefijo.

`NumberFormatter::PAD_AFTER_SUFFIX` `int`  
Caracteres de relleno añadidos después del sufijo.

`NumberFormatter::PAD_BEFORE_PREFIX` `int`  
Caracteres de relleno añadidos antes del prefijo.

`NumberFormatter::PAD_BEFORE_SUFFIX` `int`  
Caracteres de relleno añadidos antes del sufijo.
