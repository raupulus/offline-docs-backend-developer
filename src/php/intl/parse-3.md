---
title: NumberFormatter::parse
description: Analiza un número
source_url: https://www.php.net/manual/es/numberformatter.parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42300
---

NumberFormatter::parse

numfmt_parse

Analiza un número

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::parse(string $string, [int $type], [int $offset]): int
```php

Estilo procedimental

```php
numfmt_parse(NumberFormatter $formatter, string $string, [int $type], [int $offset]): int
```

Analiza una cadena y extrae un número, utilizando las reglas del formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`string`  
La cadena a analizar para el número.

`type`  
El [tipo de formato](#intl.numberformatter-constants.types) a utilizar. Por omisión, `NumberFormatter::TYPE_DOUBLE` es utilizada. Tenga en cuenta que `NumberFormatter::TYPE_CURRENCY` no es soportado; utilice NumberFormatter::parseCurrency en su lugar.

`offset`  
La posición de inicio de análisis en la cadena. En retorno, este valor contendrá la posición de fin de análisis.

## Valores devueltos

El valor numérico analizado, o `false` en caso de error.

## Ejemplos

Ejemplo con `numfmt_parse`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
$num = "1.234.567,891";
echo numfmt_parse($fmt, $num)."\n";
echo numfmt_parse($fmt, $num, NumberFormatter::TYPE_INT32)."\n";
?>

   
```

Ejemplo con `numfmt_parse`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
$num = "1.234.567,891";
echo $fmt->parse($num)."\n";
echo $fmt->parse($num, NumberFormatter::TYPE_INT32)."\n";
?>

   
```

El ejemplo anterior mostrará:

    1234567.891
    1234567

      

## Véase también

`numfmt_get_error_code`, `numfmt_format`, `numfmt_parse_currency`
