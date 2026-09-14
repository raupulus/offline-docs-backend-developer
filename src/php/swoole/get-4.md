---
title: Swoole\Table::get
description: Devuelve el valor en la tabla Swoole mediante $key y $field.
source_url: https://www.php.net/manual/es/swoole-table.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/table/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: true
translation_revision: 7dd504405
order: 93010
---

Swoole\Table::get

Devuelve el valor en la tabla Swoole mediante \$key y \$field.

## Descripción

```php
public Swoole\Table::get(string $key, [string $field]): mixed
```php

Este método permite obtener un valor almacenado en una tabla Swoole mediante una clave y un campo específico.

## Parámetros

`key`  
La clave utilizada para identificar la fila en la tabla Swoole.

`field`  
El nombre del campo del cual se desea obtener el valor. Si no se especifica, se devuelve todo el array asociativo de la fila.

## Valores devueltos

El valor asociado a la clave y campo especificados, o el array completo de la fila si no se especifica campo. En caso de no existir la clave, se devuelve NULL.
