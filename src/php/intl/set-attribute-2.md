---
title: NumberFormatter::setAttribute
description: Asigna un atributo al formateador
source_url: https://www.php.net/manual/es/numberformatter.setattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/set-attribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 89b92b42c
order: 42310
---

NumberFormatter::setAttribute

numfmt_set_attribute

Asigna un atributo al formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::setAttribute(int $attribute, int $value): bool
```php

Estilo procedimental

```php
numfmt_set_attribute(NumberFormatter $formatter, int $attribute, int $value): bool
```

Asigna un atributo numérico al formateador. Un ejemplo de atributo numérico es el número de decimales a mostrar por el formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

`attribute`  
El identificador de atributo: una de las constantes [atributos numéricos](#intl.numberformatter-constants.unumberformatattribute).

`value`  
El valor del atributo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `numfmt_set_attribute`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo "Digits: ".numfmt_get_attribute($fmt, NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
numfmt_set_attribute($fmt, NumberFormatter::MAX_FRACTION_DIGITS, 2);
echo "Digits: ".numfmt_get_attribute($fmt, NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
?>

   
```

Ejemplo con `numfmt_set_attribute`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo "Digits: ".$fmt->getAttribute(NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
$fmt->setAttribute(NumberFormatter::MAX_FRACTION_DIGITS, 2);
echo "Digits: ".$fmt->getAttribute(NumberFormatter::MAX_FRACTION_DIGITS)."\n";
echo $fmt->format(1234567.891234567890000)."\n";
?>

   
```

El ejemplo anterior mostrará:

    Digits: 3
    1.234.567,891
    Digits: 2
    1.234.567,89

Uso de `NumberFormatter::ROUNDING_MODE` para truncar valores

Por defecto, `NumberFormatter` redondea los valores. Usar `NumberFormatter::ROUND_DOWN` como `NumberFormatter::ROUNDING_MODE` trunca el valor al número especificado de dígitos fraccionarios sin redondear.

```php
<?php
$fmt = new NumberFormatter('en_US', NumberFormatter::DECIMAL);
$fmt->setAttribute(NumberFormatter::FRACTION_DIGITS, 2);

echo "Modo de redondeo por defecto:\n";
echo $fmt->format(3.789), "\n"; // 3.79 (redondeado hacia arriba)
echo $fmt->format(3.781), "\n"; // 3.78 (redondeado hacia abajo)

$fmt->setAttribute(NumberFormatter::ROUNDING_MODE, NumberFormatter::ROUND_DOWN);

echo "\nCon ROUND_DOWN (truncar):\n";
echo $fmt->format(3.789), "\n"; // 3.78 (truncado)
echo $fmt->format(3.781), "\n"; // 3.78 (truncado)
?>

   
```

El ejemplo anterior mostrará:

    Modo de redondeo por defecto:
    3.79
    3.78

    Con ROUND_DOWN (truncar):
    3.78
    3.78

## Véase también

`numfmt_get_error_code`, `numfmt_get_attribute`, `numfmt_set_text_attribute`
