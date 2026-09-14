---
title: NumberFormatter::getTextAttribute
description: Lee un atributo textual
source_url: https://www.php.net/manual/es/numberformatter.gettextattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-text-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42280
---

NumberFormatter::getTextAttribute

numfmt_get_text_attribute

Lee un atributo textual

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getTextAttribute(int $attribute): string
```php

Estilo procedimental

```php
numfmt_get_text_attribute(NumberFormatter $formatter, int $attribute): string
```

Lee un atributo textual asociado a un formateador. Un ejemplo de atributo textual es el sufijo para los números positivos. Si el formateador no comprende este atributo, se produce un error `U_UNSUPPORTED_ERROR`. Los formateadores de reglas comprenden únicamente `NumberFormatter::DEFAULT_RULESET` y `NumberFormatter::PUBLIC_RULESETS`.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`attribute`  
El identificador del atributo: una de las constantes [de atributo textual](#intl.numberformatter-constants.unumberformattextattribute).

## Valores devueltos

Devuelve el valor del atributo en caso de éxito, y `false` en caso contrario.

## Ejemplos

Ejemplo con `numfmt_get_text_attribute`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Prefijo : ".numfmt_get_text_attribute($fmt, NumberFormatter::NEGATIVE_PREFIX)."\n";
echo numfmt_format($fmt, -1234567.891234567890000)."\n";
numfmt_set_text_attribute($fmt, NumberFormatter::NEGATIVE_PREFIX, "MINUS");
echo "Prefijo : ".numfmt_get_text_attribute($fmt, NumberFormatter::NEGATIVE_PREFIX)."\n";
echo numfmt_format($fmt, -1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_get_text_attribute`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Prefijo : ".$fmt->getTextAttribute(NumberFormatter::NEGATIVE_PREFIX)."\n";
echo $fmt->format(-1234567.891234567890000)."\n";
$fmt->setTextAttribute(NumberFormatter::NEGATIVE_PREFIX, "MINUS");
echo "Prefijo : ".$fmt->getTextAttribute(NumberFormatter::NEGATIVE_PREFIX)."\n";
echo $fmt->format(-1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Prefijo : -
    -1.234.567,891
    Prefijo : MINUS
    MINUS1.234.567,891

      

## Véase también

`numfmt_get_error_code`, `numfmt_get_attribute`, `numfmt_set_text_attribute`
