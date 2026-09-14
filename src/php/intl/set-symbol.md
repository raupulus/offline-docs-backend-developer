---
title: NumberFormatter::setSymbol
description: Configura el símbolo del formateador
source_url: https://www.php.net/manual/es/numberformatter.setsymbol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/set-symbol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42330
---

NumberFormatter::setSymbol

numfmt_set_symbol

Configura el símbolo del formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::setSymbol(int $symbol, string $value): bool
```php

Estilo procedimental

```php
numfmt_set_symbol(NumberFormatter $formatter, int $symbol, string $value): bool
```

Configura el símbolo del formateador. El formateador utiliza el símbolo para caracterizar números, como el porcentaje. Esta API no es soportada para los formateadores basados en reglas.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`symbol`  
El identificador de símbolo, entre las [constantes de símbolos](#intl.numberformatter-constants.unumberformatsymbol).

`value`  
El texto del símbolo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `numfmt_set_symbol`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Separador decimal : ".numfmt_get_symbol($fmt, NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
numfmt_set_symbol($fmt, NumberFormatter::GROUPING_SEPARATOR_SYMBOL, "*");
echo "Separador decimal : ".numfmt_get_symbol($fmt, NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_set_symbol`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Separador decimal : ".$fmt->getSymbol(NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
$fmt->setSymbol(NumberFormatter::GROUPING_SEPARATOR_SYMBOL, "*");
echo "Separador decimal : ".$fmt->getSymbol(NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Separador decimal : .
    1.234.567,891
    Separador decimal : *
    1*234*567,891

      

## Véase también

`numfmt_get_error_code`, `numfmt_get_symbol`
