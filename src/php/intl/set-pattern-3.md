---
title: NumberFormatter::setPattern
description: Configura el patrón del formateador
source_url: https://www.php.net/manual/es/numberformatter.setpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/set-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42320
---

NumberFormatter::setPattern

numfmt_set_pattern

Configura el patrón del formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::setPattern(string $pattern): bool
```php

Estilo procedimental

```php
numfmt_set_pattern(NumberFormatter $formatter, string $pattern): bool
```

Configura el patrón utilizado por el formateador. No puede ser utilizado con un formateador basado en reglas.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`pattern`  
El patrón, en la sintaxis descrita en la [documentación ICU DecimalFormat](https://unicode-org.github.io/icu-docs/apidoc/released/icu4c/classDecimalFormat.html).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `numfmt_set_pattern`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Patrón : ".numfmt_get_pattern($fmt)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
numfmt_set_pattern($fmt, "#0.# kg");
echo "Patrón : ".numfmt_get_pattern($fmt)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_set_pattern`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Patrón : ".$fmt->getPattern()."\n";
echo $fmt->format(1234567.891234567890000)."\n";
$fmt->setPattern("#0.# kg");
echo "Patrón : ".$fmt->getPattern()."\n";
echo $fmt->format(1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Patrón : #,##0.###
    1.234.567,891
    Patrón : #0.# kg
    1234567,9 kg

      

## Véase también

`numfmt_get_error_code`, `numfmt_create`, `numfmt_get_pattern`
