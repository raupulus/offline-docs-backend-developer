---
title: NumberFormatter::formatCurrency
description: Formatea un valor monetario
source_url: https://www.php.net/manual/es/numberformatter.formatcurrency.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/format-currency.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42200
---

NumberFormatter::formatCurrency

numfmt_format_currency

Formatea un valor monetario

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::formatCurrency(float $amount, string $currency): string
```php

Estilo procedimental

```php
numfmt_format_currency(NumberFormatter $formatter, float $amount, string $currency): string
```

Formatea un valor monetario, según las reglas del formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`amount`  
El valor numérico.

`currency`  
El código ISO 4217 de tres letras de la moneda a utilizar.

## Valores devueltos

La cadena que representa el valor monetario formateado, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `numfmt_format_currency`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::CURRENCY );
echo numfmt_format_currency($fmt, 1234567.891234567890000, "EUR")."\n";
echo numfmt_format_currency($fmt, 1234567.891234567890000, "RUR")."\n";
$fmt = numfmt_create( 'ru_RU', NumberFormatter::CURRENCY );
echo numfmt_format_currency($fmt, 1234567.891234567890000, "EUR")."\n";
echo numfmt_format_currency($fmt, 1234567.891234567890000, "RUR")."\n";
?>

   
```

Ejemplo con `numfmt_format_currency`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::CURRENCY );
echo $fmt->formatCurrency(1234567.891234567890000, "EUR")."\n";
echo $fmt->formatCurrency(1234567.891234567890000, "RUR")."\n";
$fmt = new NumberFormatter( 'ru_RU', NumberFormatter::CURRENCY );
echo $fmt->formatCurrency(1234567.891234567890000, "EUR")."\n";
echo $fmt->formatCurrency(1234567.891234567890000, "RUR")."\n";
?>

   
```

El ejemplo anterior mostrará:

    1.234.567,89 €
    1.234.567,89 RUR
    1 234 567,89€
    1 234 567,89р.

      

## Notas

> [!NOTE]
> Los formatos realizables por este método de formateo no pueden utilizar plenamente las posibilidades de la biblioteca ICU subyacente, como por ejemplo el formateo de moneda con un símbolo monetario corto.
>
> Para utilizarlas plenamente, utilice `msgfmt_format_message`.

## Véase también

`numfmt_get_error_code`, `numfmt_format`, `numfmt_parse_currency`, `msgfmt_format_message`
