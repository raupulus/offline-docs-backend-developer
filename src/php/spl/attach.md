---
title: SplObjectStorage::attach
description: Agrega un objeto en el almacenamiento
source_url: https://www.php.net/manual/es/splobjectstorage.attach.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splobjectstorage/attach.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 85050
---

SplObjectStorage::attach

Agrega un objeto en el almacenamiento

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] public SplObjectStorage::attach(object $object, [mixed $info]): void
```php

Añade un `object` dentro del almacenamiento, y opcionalmente se asocian a algunos datos.

Este método es un alias de SplObjectStorage::offsetSet.

## Parámetros

`object`  
El `object` a ser añadido.

`info`  
Los datos asociados con el `object`.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Este método ha quedado obsoleto en favor de SplObjectStorage::offsetSet. |

## Ejemplos

Ejemplo de `SplObjectStorage::attach`

```
<?php
$o1 = new stdClass;
$o2 = new stdClass;
$s = new SplObjectStorage();
$s->attach($o1); // similar a $s[$o1] = NULL;
$s->attach($o2, "hola"); // similar a $s[$o2] = "hola";

var_dump($s[$o1]);
var_dump($s[$o2]);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    NULL
    string(4) "hola"

## Véase también

SplObjectStorage::detach, SplObjectStorage::offsetSet
