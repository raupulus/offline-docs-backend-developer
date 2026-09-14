---
title: Ds\Vector::find
description: Intenta encontrar el índice de un valor.
source_url: https://www.php.net/manual/es/ds-vector.find.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/find.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16270
---

Ds\Vector::find

Intenta encontrar el índice de un valor.

## Descripción

```php
public Ds\Vector::find(mixed $value): mixed
```php

Devuelve el índice del `valor`, o `false` si no se encuentra.

## Parámetros

`value`  
El valor a encontrar.

## Valores devueltos

El índice del valor, o `false` si no se encuentra.

> [!NOTE]
> Los valores serán comparados por valor y por tipo.

## Ejemplos

Ejemplo de `Ds\Vector::find`

```
<?php
$vector = new \Ds\Vector(["a", 1, true]);

var_dump($vector->find("a")); // 0
var_dump($vector->find("b")); // false
var_dump($vector->find("1")); // false
var_dump($vector->find(1));   // 1
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(0)
    bool(false)
    bool(false)
    int(1)
