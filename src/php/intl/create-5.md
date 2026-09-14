---
title: NumberFormatter::create
description: Crea un formateador de números
source_url: https://www.php.net/manual/es/numberformatter.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: b35a2269f
order: 42190
---

NumberFormatter::create

numfmt_create

NumberFormatter::\_\_construct

Crea un formateador de números

## Descripción

Estilo orientado a objetos (método)

```php
public static NumberFormatter::create(string $locale, int $style, [string $pattern]): NumberFormatter
```php

Estilo procedimental

```php
numfmt_create(string $locale, int $style, [string $pattern]): NumberFormatter
```

Estilo orientado a objetos (constructor)

```php
public NumberFormatter::__construct(string $locale, int $style, [string $pattern])
```php

Crea un formateador de números

## Parámetros

`locale`  
La configuración local con la cual los números serán formateados (i.e. en_CA).

`style`  
El estilo de formato, una de las constantes [de estilo de formato](#intl.numberformatter-constants.unumberformatstyle). Si `NumberFormatter::PATTERN_DECIMAL` o `NumberFormatter::PATTERN_RULEBASED` es utilizado entonces el formato de número es abierto con el patrón proporcionado, que debe ser compatible con la sintaxis descrita por la [documentación ICU DecimalFormat](https://unicode-org.github.io/icu-docs/apidoc/released/icu4c/classDecimalFormat.html) o [documentación ICU RuleBasedNumberFormat](https://unicode-org.github.io/icu/userguide/format_parse/numbers/rbnf.html), respectivamente.

`pattern`  
La cadena de patrón, en función del estilo de formato elegido.

## Valores devueltos

Devuelve un objeto `NumberFormatter` o `null` en caso de error.

## Errores/Excepciones

Se levanta una ValueError si `locale` es inválido.

## Historial de cambios

| Versión | Descripción                                        |
|---------|----------------------------------------------------|
| 8.4.0   | Se levanta una ValueError si `locale` es inválido. |
| 8.0.0   | `pattern` ahora es nullable.                       |

## Ejemplos

Ejemplo con `numfmt_create::create`, Estilo procedimental

```
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
echo numfmt_format($fmt, 1234567.891234567890000)."\n";
$fmt = numfmt_create( 'it', NumberFormatter::SPELLOUT );
echo numfmt_format($fmt, 1142)."\n";
?>

   
```php

Ejemplo con `numfmt_create::create`, estilo POO

```
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
echo $fmt->format(1234567.891234567890000)."\n";
$fmt = new NumberFormatter( 'it', NumberFormatter::SPELLOUT );
echo $fmt->format(1142)."\n";
?>

   
```php

El ejemplo anterior mostrará:

    1.234.567,891
    millicentoquarantadue

      

## Véase también

`numfmt_format`, `numfmt_parse`
