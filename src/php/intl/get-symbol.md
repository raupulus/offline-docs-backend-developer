---
title: NumberFormatter::getSymbol
description: Lee el valor del símbolo
source_url: https://www.php.net/manual/es/numberformatter.getsymbol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-symbol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42270
---

NumberFormatter::getSymbol

numfmt_get_symbol

Lee el valor del símbolo

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getSymbol(int $symbol): string
```php

Estilo procedimental

```php
numfmt_get_symbol(NumberFormatter $formatter, int $symbol): string
```

Lee el símbolo asociado al formateador. El formateador utiliza símbolos para representar caracteres dependientes de las convenciones locales, como el signo de porcentaje. Esta API no es soportada por los formateadores basados en reglas.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`symbol`  
La constante de símbolo, una de la lista de constantes [de símbolos de formato](#intl.numberformatter-constants.unumberformatsymbol).

## Valores devueltos

La cadena de símbolo o `false` en caso de error.

## Ejemplos

Ejemplo con `numfmt_get_symbol`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Separador : ".numfmt_get_symbol($fmt, NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
numfmt_set_symbol($fmt, NumberFormatter::GROUPING_SEPARATOR_SYMBOL, "*");
echo "Separador : ".numfmt_get_symbol($fmt, NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_get_symbol`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Separador : ".$fmt->getSymbol(NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
$fmt->setSymbol(NumberFormatter::GROUPING_SEPARATOR_SYMBOL, "*");
echo "Separador : ".$fmt->getSymbol(NumberFormatter::GROUPING_SEPARATOR_SYMBOL)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Separador : .
    1.234.567,891
    Separador : *
    1*234*567,891

      

## Véase también

`numfmt_get_error_code`, `numfmt_set_symbol`
