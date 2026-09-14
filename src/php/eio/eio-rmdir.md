---
title: eio_rmdir
description: Eliminar un directorio
source_url: https://www.php.net/manual/es/function.eio-rmdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-rmdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17090
---

eio_rmdir

Eliminar un directorio

## Descripción

```php
eio_rmdir(string $path, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_rmdir` elimina un directorio.

## Parámetros

`path`  
La ruta del directorio

`pri`  
La prioridad de la petición: `EIO_PRI_DEFAULT`, `EIO_PRI_MIN`, `EIO_PRI_MAX`, o `null`. Si `null` es pasado, el parámetro `pri`, internamente, es definido a `EIO_PRI_DEFAULT`.

`callback`  
La función de retrollamada `callback` es llamada cuando la petición está terminada. Debe corresponder al siguiente prototipo:

```
void callback(mixed $data, int $result[, resource $req]);
```php

`data`  
representa los datos personalizados pasados a la petición.

`result`  
representa el valor resultante específico de la petición; básicamente, el valor retornado por la llamada al sistema correspondiente.

`req`  
es el recurso opcional de la petición que puede ser utilizado con funciones como `eio_get_last_error`.

`data`  
Variable arbitraria pasada a `callback`.

## Valores devueltos

`eio_rmdir` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_rmdir`

```
<?php
$nombre_directorio_temp = "dir-tmp-eio";
mkdir($nombre_directorio_temp);

function mi_llamada_retorno_rmdir($datos, $resultado) {
    if ($resultado == 0 && !file_exists($datos)) {
        echo "eio_rmdir_ok";
    } else if (file_exists($datos)) {
        rmdir($datos);
    }
}

eio_rmdir($nombre_directorio_temp, EIO_PRI_DEFAULT, "mi_llamada_retorno_rmdir", $nombre_directorio_temp);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    eio_rmdir_ok

## Véase también

eio_mkdir
