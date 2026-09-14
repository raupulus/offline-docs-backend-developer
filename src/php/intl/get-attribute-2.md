---
title: NumberFormatter::getAttribute
description: Lee un atributo
source_url: https://www.php.net/manual/es/numberformatter.getattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42220
---

NumberFormatter::getAttribute

numfmt_get_attribute

Lee un atributo

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getAttribute(int $attribute): int
```php

Estilo procedimental

```php
numfmt_get_attribute(NumberFormatter $formatter, int $attribute): int
```

Lee un atributo numérico del formateador. Un ejemplo de atributo numérico es el número de decimales que el formateador va a utilizar.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`attribute`  
La constante de atributo, una de la lista de [atributos numéricos](#intl.numberformatter-constants.unumberformatattribute).

## Valores devueltos

Devuelve el valor del atributo, en caso de éxito, y `false` en caso de error.

## Ejemplos

Ejemplo con `numfmt_get_attribute`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Decimales :  ".numfmt_get_attribute($fmt, NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
numfmt_set_attribute($fmt, NumberFormatter::MAX_FRACTION_DIGITS, 2);
echo "Decimales :  ".numfmt_get_attribute($fmt, NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_get_attribute`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Decimales :  ".$fmt->getAttribute(NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
$fmt->setAttribute(NumberFormatter::MAX_FRACTION_DIGITS, 2);
echo "Decimales :  ".$fmt->getAttribute(NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Decimales :  3
    1.234.567,891
    Decimales :  2
    1.234.567,89

      

## Véase también

`numfmt_get_error_code`, `numfmt_get_text_attribute`, `numfmt_set_attribute`
