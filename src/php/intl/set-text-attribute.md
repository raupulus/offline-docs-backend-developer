---
title: NumberFormatter::setTextAttribute
description: Modifica un atributo de texto
source_url: https://www.php.net/manual/es/numberformatter.settextattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/set-text-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42340
---

NumberFormatter::setTextAttribute

numfmt_set_text_attribute

Modifica un atributo de texto

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::setTextAttribute(int $attribute, string $value): bool
```php

Estilo procedimental

```php
numfmt_set_text_attribute(NumberFormatter $formatter, int $attribute, string $value): bool
```

Modifica el atributo de texto asociado al formateador. Un ejemplo de atributo de texto es el sufijo de los números positivos. Si el formateador no comprende el atributo, se produce un error `U_UNSUPPORTED_ERROR`. Los formateadores basados en reglas solo comprenden `NumberFormatter::DEFAULT_RULESET` y `NumberFormatter::PUBLIC_RULESETS`.

## Parámetros

`formatter`  
Un objeto `NumberFormatter`.

`attribute`  
Un especificador de atributo: una de las constantes de [atributo de texto](#intl.numberformatter-constants.unumberformattextattribute).

`value`  
El valor del atributo de texto.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `numfmt_set_text_attribute`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Prefix: ".numfmt_get_text_attribute($fmt, NumberFormatter::NEGATIVE_PREFIX)."\n";
echo numfmt_format($fmt, -1234567.891234567890000)."\n";
numfmt_set_text_attribute($fmt, NumberFormatter::NEGATIVE_PREFIX, "MINUS");
echo "Prefix: ".numfmt_get_text_attribute($fmt, NumberFormatter::NEGATIVE_PREFIX)."\n";
echo numfmt_format($fmt, -1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_set_text_attribute`, Estilo procedimental

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Prefix: ".$fmt->getTextAttribute(NumberFormatter::NEGATIVE_PREFIX)."\n";
echo $fmt->format(-1234567.891234567890000)."\n";
$fmt->setTextAttribute(NumberFormatter::NEGATIVE_PREFIX, "MINUS");
echo "Prefix: ".$fmt->getTextAttribute(NumberFormatter::NEGATIVE_PREFIX)."\n";
echo $fmt->format(-1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Prefix: -
    -1.234.567,891
    Prefix: MINUS
    MINUS1.234.567,891

      

## Véase también

`numfmt_get_error_code`, `numfmt_get_text_attribute`, `numfmt_set_attribute`
