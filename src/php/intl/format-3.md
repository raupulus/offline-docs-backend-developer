---
title: NumberFormatter::format
description: Formatear un número
source_url: https://www.php.net/manual/es/numberformatter.format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 42210
---

NumberFormatter::format

numfmt_format

Formatear un número

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::format(int $num, [int $type]): string
```php

Estilo procedimental

```php
numfmt_format(NumberFormatter $formatter, int $num, [int $type]): string
```

Formatea un valor numérico según las reglas del formateador.

## Parámetros

`formatter`  
Objeto `NumberFormatter`.

`num`  
El valor a formatear. Puede ser `int` o `float`, otros valores serán convertidos a un valor numérico.

`type`  
El [ tipo de formato](#intl.numberformatter-constants.types) a usar. Tenga en cuenta que `NumberFormatter::TYPE_CURRENCY` no está soportado; use NumberFormatter::formatCurrency en su lugar.

## Valores devueltos

Devuelve el string que contiene el valor formateado, o `false` en caso de error.

## Ejemplos

Ejemplo de `numfmt_format`

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
$data = numfmt_format($fmt, 1234567.891234567890000);
var_dump($data);
?>

   
```

Ejemplo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
$data = $fmt->format(1234567.891234567890000);
var_dump($data);
?>

   
```

El ejemplo anterior mostrará:

    string(13) "1.234.567,891"

      

## Notas

> [!NOTE]
> Los formatos alcanzables por este método de formateo no pueden utilizar completamente las posibilidades de la biblioteca ICU subyacente, como por ejemplo formatear moneda con símbolo de moneda estrecho.
>
> Para utilizarlas completamente use `msgfmt_format_message`.

## Véase también

`numfmt_get_error_code`, `numfmt_format_currency`, `numfmt_parse`, `msgfmt_format_message`
