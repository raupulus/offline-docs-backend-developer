---
title: IntlChar::isbase
description: Verifica si un punto de código es un carácter de base
source_url: https://www.php.net/manual/es/intlchar.isbase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isbase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40970
---

IntlChar::isbase

Verifica si un punto de código es un carácter de base

## Descripción

```php
public static IntlChar::isbase(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter de base. `true` para las categorías generales "L" (letras), "N" (números), "Mc" (marcas de combinación de espaciado), y "Me" (marcas de encuadre).

> [!NOTE]
> Esto difiere de la definición Unicode en el capítulo 3.5, cláusula de conformidad D13, que define los caracteres de base como todos los caracteres (no Cn) que no se combinan gráficamente con los caracteres anteriores (M) y que no son caracteres de control (Cc) ni caracteres de formato (Cf).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter de base, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isbase("A"));
var_dump(IntlChar::isbase("1"));
var_dump(IntlChar::isbase("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)

## Véase también

`IntlChar::isalpha`, `IntlChar::isdigit`
