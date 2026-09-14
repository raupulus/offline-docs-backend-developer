---
title: Ds\Set::allocate
description: Asigna suficiente memoria para una capacidad requerida
source_url: https://www.php.net/manual/es/ds-set.allocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/set/allocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 15770
---

Ds\Set::allocate

Asigna suficiente memoria para una capacidad requerida

## Descripción

```php
public Ds\Set::allocate(int $capacity): void
```php

Asigna suficiente memoria para una capacidad requerida.

## Parámetros

`capacity`  
El número de valores para los cuales la capacidad debe ser asignada.

> [!NOTE]
> La capacidad permanecerá igual si este valor es inferior o igual a la capacidad actual.

> [!NOTE]
> La capacidad siempre será redondeada a la potencia de 2 más cercana.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Set::allocate`

```
<?php
$set = new \Ds\Set();
var_dump($set->capacity());

$set->allocate(100);
var_dump($set->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(16)
    int(128)
