---
title: NumberFormatter::getPattern
description: Lee el modelo del formateador
source_url: https://www.php.net/manual/es/numberformatter.getpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42260
---

NumberFormatter::getPattern

numfmt_get_pattern

Lee el modelo del formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getPattern(): string
```php

Estilo procedimental

```php
numfmt_get_pattern(NumberFormatter $formatter): string
```

Extrae el modelo utilizado por el formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

## Valores devueltos

El `string` de modelo, que es utilizado por el formateador, o `false` en caso de error.

## Ejemplos

Ejemplo con `numfmt_get_pattern`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Modelo : ".numfmt_get_pattern($fmt)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
numfmt_set_pattern($fmt, "#0.# kg");
echo "Modelo : ".numfmt_get_pattern($fmt)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_get_pattern`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Modelo : ".$fmt->getPattern()."\n";
echo $fmt->format(1234567.891234567890000)."\n";
$fmt->setPattern("#0.# kg");
echo "Modelo : ".$fmt->getPattern()."\n";
echo $fmt->format(1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Modelo : #,##0.###
    1.234.567,891
    Modelo : #0.# kg
    1234567,9 kg

      

## Véase también

`numfmt_get_error_code`, `numfmt_set_pattern`, `numfmt_create`
