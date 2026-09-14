---
title: Ds\Set::reversed
description: Devuelve una copia invertida
source_url: https://www.php.net/manual/es/ds-set.reversed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/reversed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15980
---

Ds\Set::reversed

Devuelve una copia invertida

## Descripción

```php
public Ds\Set::reversed(): Ds\Set
```php

Devuelve una copia invertida de la secuencia.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una copia invertida de la secuencia.

> [!NOTE]
> La instancia actual no se ve afectada.

## Ejemplos

Ejemplo de `Ds\Set::reversed`

```
<?php
$set = new \Ds\Set(["a", "b", "c"]);

print_r($set->reversed());
print_r($set);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Set Object
    (
        [0] => c
        [1] => b
        [2] => a
    )
    Ds\Set Object
    (
        [0] => a
        [1] => b
        [2] => c
    )
