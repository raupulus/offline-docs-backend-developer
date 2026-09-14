---
title: clearstatcache
description: Elimina la caché de stat
source_url: https://www.php.net/manual/es/function.clearstatcache.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/clearstatcache.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: e82ff8a84
order: 23310
---

clearstatcache

Elimina la caché de

stat

## Descripción

```php
clearstatcache([bool $clear_realpath_cache], [string $filename]): void
```php

La llamada a la función `stat` o `lstat` es relativamente costosa en términos de tiempo de ejecución. Por ello, el resultado de la última llamada a una de las funciones de estado (ver la lista a continuación) se guarda para su reutilización. Si se desea forzar la verificación del estado de un fichero, en el caso de que el fichero hubiera podido ser modificado o hubiera desaparecido, se debe utilizar la función `clearstatcache` para borrar de la memoria los resultados de la última llamada a la función.

Tenga en cuenta que PHP no guarda en caché información sobre un fichero inexistente. Si se llama a `file_exists` sobre un fichero que no existe, la función devolverá `false` hasta que se cree el fichero. Si se crea el fichero, la función devolverá `true` incluso si se borra el fichero.

> [!NOTE]
> Esta función guarda en caché información sobre ficheros. Por lo tanto, solo es necesario llamar a `clearstatcache` si se realizan múltiples operaciones sobre el directorio, y se desea tener una versión actualizada de la información.

Las funciones afectadas incluyen : `stat`, `lstat`, `file_exists`, `is_writable`, `is_readable`, `is_executable`, `is_file`, `is_dir`, `is_link`, `filectime`, `fileatime`, `filemtime`, `fileinode`, `filegroup`, `fileowner`, `filesize`, `filetype`, y `fileperms`.

## Parámetros

`clear_realpath_cache`  
Si también debe vaciarse la caché de rutas reales.

`filename`  
Limpia la caché de ruta real de un fichero específico. Solo puede ser utilizado si el argumento `clear_realpath_cache` vale `true`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `clearstatcache`

```
<?php
$file = 'output_log.txt';

function get_owner($file)
{
    $stat = stat($file);
    $user = posix_getpwuid($stat['uid']);
    return $user['name'];
}

$format = "UID @ %s: %s\n";

printf($format, date('r'), get_owner($file));

chown($file, 'ross');
printf($format, date('r'), get_owner($file));

clearstatcache();
printf($format, date('r'), get_owner($file));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    UID @ Sun, 12 Oct 2008 20:48:28 +0100: root
    UID @ Sun, 12 Oct 2008 20:48:28 +0100: root
    UID @ Sun, 12 Oct 2008 20:48:28 +0100: ross
