---
title: touch
description: Modifica la fecha de modificación y de último acceso de un fichero
source_url: https://www.php.net/manual/es/function.touch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/touch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 2b56c905f
order: 24070
---

touch

Modifica la fecha de modificación y de último acceso de un fichero

## Descripción

```php
touch(string $filename, [int $mtime], [int $atime]): bool
```php

Intenta forzar la fecha de modificación del fichero designado por el parámetro `filename` a la fecha especificada por el parámetro `mtime`. Tenga en cuenta que la fecha de último acceso se modifica, independientemente del número de argumentos.

Si el fichero no existe, PHP intentará crearlo.

## Parámetros

`filename`  
El nombre del fichero a crear.

`mtime`  
La fecha de creación. Si `mtime` es omitido, se utiliza la hora actual `time`.

`atime`  
Si no es `null`, la hora de acceso al fichero proporcionado se establecerá a la valor del parámetro `atime`. De lo contrario, se establecerá a la valor pasada al parámetro `mtime`. Si ambos son `null`, se utilizará la hora actual del sistema.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                           |
|---------|---------------------------------------|
| 8.0.0   | `mtime` y `atime` ahora son nullable. |

## Ejemplos

Ejemplo con `touch`

```
<?php
if (touch($FileName)) {
    echo "La fecha de modificación de $FileName ha sido modificada a la fecha actual";
} else {
    echo "Lo sentimos, no es posible cambiar la fecha de modificación de $FileName";
}
?>

    
```php

Ejemplo con `touch` utilizando el parámetro `mtime`

```
<?php
/*
 * Esta es la fecha y hora del último acceso, le añadimos 1 hora
 * en el pasado.
 */
$time = time() - 3600;

/* ¡Toquemos el fichero! */
if (!touch('some_file.txt', $time)) {
    echo '¡Ups, ha ocurrido un error...';
} else {
    echo 'La llamada a la función touch() ha tenido éxito';
}
?>

    
```php

## Notas

> [!NOTE]
> Tenga en cuenta que la precisión temporal puede variar según el sistema de archivos utilizado.
