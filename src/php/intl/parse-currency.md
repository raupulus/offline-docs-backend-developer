---
title: NumberFormatter::parseCurrency
description: Analiza un número monetario
source_url: https://www.php.net/manual/es/numberformatter.parsecurrency.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/parse-currency.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42290
---

NumberFormatter::parseCurrency

numfmt_parse_currency

Analiza un número monetario

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::parseCurrency(string $string, string $currency, [int $offset]): float
```php

Estilo procedimental

```php
numfmt_parse_currency(NumberFormatter $formatter, string $string, string $currency, [int $offset]): float
```

Analiza una cadena en un número flotante y una moneda, utilizando el formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`currency`  
El nombre de la moneda (el código ISO 4217 de 3 letras).

`offset`  
La posición de inicio de análisis en la cadena. A su vez, este valor contendrá la posición de fin de análisis.

## Valores devueltos

El número decimal así leído, o `false` en caso de error.

## Ejemplos

Ejemplo con `numfmt_parse_currency`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::CURRENCY );
$num = "1.234.567,89\xc2\xa0$";
echo "Tenemos ".numfmt_parse_currency($fmt, $num, $curr)." en $curr\n";
?>

   
```

Ejemplo con `numfmt_parse_currency`, Estilo procedimental

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::CURRENCY );
$num = "1.234.567,89\xc2\xa0$";
echo "Tenemos ".$fmt->parseCurrency($num, $curr)." en $curr\n";
?>

   
```

El ejemplo anterior mostrará:

    Tenemos 1234567.89 en USD

      

## Véase también

`numfmt_get_error_code`, `numfmt_parse`, `numfmt_format_currency`
