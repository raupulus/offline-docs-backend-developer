---
title: umask
description: Cambia el "umask" actual
source_url: https://www.php.net/manual/es/function.umask.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/umask.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0bf2170a9
order: 24080
---

umask

Cambia el "umask" actual

## Descripción

```php
umask([int $mask]): int
```php

`umask` cambia el umask de PHP y lo reemplaza por `mask`: `mask & 0777` y, a continuación, devuelve el viejo umask. Cuando PHP se utiliza como módulo de servidor, el umask recupera su valor al final de cada script.

## Parámetros

`mask`  
El nuevo umask.

## Valores devueltos

Si `mask` es `null`, `umask` simplemente devuelve el umask actual de lo contrario se devuelve el antiguo umask.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `mask` ahora es nullable. |

## Ejemplos

Ejemplo con `umask`

```
<?php
$old = umask(0);
chmod("/path/some_dir/some_file.txt", 0755);
umask($old);

// Verificación
if ($old != umask()) {
    die('Ocurrió un error al modificar los permisos');
}
?>

    
```php

## Notas

> [!NOTE]
> Evítese el uso de esta función en un servidor Web multithread. Es preferible cambiar los permisos de un directorio con la función `chmod`, después de la creación del directorio. Al utilizar `umask`, puede encontrarse con comportamientos indefinidos a nivel de otros scripts y del servidor, ya que todos utilizan el mismo umask.
