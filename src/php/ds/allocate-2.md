---
title: Ds\Map::allocate
description: Asigna suficiente memoria para una capacidad requerida
source_url: https://www.php.net/manual/es/ds-map.allocate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/map/allocate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 14810
---

Ds\Map::allocate

Asigna suficiente memoria para una capacidad requerida

## Descripción

```php
public Ds\Map::allocate(int $capacity): void
```php

Asigna suficiente memoria para una capacidad requerida.

## Parámetros

`capacity`  
El número de valores para los cuales la capacidad debe ser asignada.

> [!NOTE]
> La capacidad permanecerá igual si este valor es inferior o igual a la capacidad actual.

> [!NOTE]
> La capacidad será siempre redondeada a la potencia de 2 más cercana.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Ds\Map::allocate`

```
<?php
$map = new \Ds\Map();
var_dump($map->capacity());

$map->allocate(100);
var_dump($map->capacity());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(16)
    int(128)
