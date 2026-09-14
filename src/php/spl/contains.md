---
title: SplObjectStorage::contains
description: Comprueba si el almacenamiento contiene un objeto específico
source_url: https://www.php.net/manual/es/splobjectstorage.contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 85060
---

SplObjectStorage::contains

Comprueba si el almacenamiento contiene un objeto específico

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public SplObjectStorage::contains(object $object): bool
```php

Comprueba si el almacenamiento contiene al `object` proporcionado.

## Parámetros

`object`  
El `object` a ser comprobado.

## Valores devueltos

Devuelve `true` si el `object` está en el almacenamiento, en caso contrario `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Este método ha quedado obsoleto en favor de SplObjectStorage::offsetExists. |

## Ejemplos

Ejemplo de `SplObjectStorage::contains`

```
<?php
$o1 = new stdClass;
$o2 = new stdClass;

$s = new SplObjectStorage();

$s[$o1] = "hola";
var_dump($s->contains($o1));
var_dump($s->contains($o2));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)

## Véase también

SplObjectStorage::offsetExists
