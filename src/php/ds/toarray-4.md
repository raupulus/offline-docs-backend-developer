---
title: Ds\Pair::toArray
description: Convierte la pareja en un array
source_url: https://www.php.net/manual/es/ds-pair.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/pair/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15240
---

Ds\Pair::toArray

Convierte la pareja en un

array

## Descripción

```php
public Ds\Pair::toArray(): array
```php

Convierte la pareja en un `array`.

> [!NOTE]
> La conversión en `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los valores en el mismo orden que la pareja.

## Ejemplos

Ejemplo de `Ds\Pair::toArray`

```
<?php
$pair = new \Ds\Pair("a", 1);

var_dump($pair->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      ["key"]=>
      string(1) "a"
      ["value"]=>
      int(1)
    }
