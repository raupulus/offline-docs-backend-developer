---
title: Ds\Set::toArray
description: Convierte el conjunto en un array
source_url: https://www.php.net/manual/es/ds-set.toarray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/toarray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16030
---

Ds\Set::toArray

Convierte el conjunto en un

array

## Descripción

```php
public Ds\Set::toArray(): array
```php

Convierte el conjunto en un `array`.

> [!NOTE]
> La conversión en un `array` aún no es soportada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` que contiene todos los valores en el mismo orden que la secuencia.

## Ejemplos

Ejemplo de `Ds\Set::toArray`

```
<?php
$set = new \Ds\Set([1, 2, 3]);

var_dump($set->toArray());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
