---
title: SplObjectStorage::detach
description: Quita un object del almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.detach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/detach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 85090
---

SplObjectStorage::detach

Quita un

object

del almacenamiento

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public SplObjectStorage::detach(object $object): void
```php

Quita un `object` de el almacenamiento.

## Parámetros

`object`  
El `object` a ser eliminado.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Este método ha quedado obsoleto en favor de SplObjectStorage::offsetUnset. |

## Ejemplos

Ejemplo de `SplObjectStorage::detach`

```
<?php
$o = new stdClass;
$s = new SplObjectStorage();
$s->attach($o);
var_dump(count($s));
$s->detach($o);
var_dump(count($s));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(1)
    int(0)

## Véase también

SplObjectStorage::attach, SplObjectStorage::removeAll
