---
title: eio_rename
description: Cambiar el nombre o la ubicación de un fichero
source_url: https://www.php.net/manual/es/function.eio-rename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-rename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17080
---

eio_rename

Cambiar el nombre o la ubicación de un fichero

## Descripción

```php
eio_rename(string $path, string $new_path, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_rename` renombra o mueve un fichero a una nueva ubicación.

## Parámetros

`path`  
La ruta de origen

`new_path`  
La ruta destino

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

`eio_rename` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_rename`

```
<?php
$nombre_fichero = dirname(__FILE__)."/fichero-eio-temp.dat";
touch($nombre_fichero);
$nuevo_nombre_fichero = dirname(__FILE__)."/nuevo-fichero-eio-temp.dat";

function mi_llamada_retorno_rename($datos, $resultado) {
    global $nombre_fichero, $nuevo_nombre_fichero;

    if ($resultado == 0 && !file_exists($nombre_fichero) && file_exists($nuevo_nombre_fichero)) {
        @unlink($nuevo_nombre_fichero);
        echo "eio_rename_ok";
    } else {
        @unlink($nombre_fichero);
    }
}

eio_rename($nombre_fichero, $nuevo_nombre_fichero, EIO_PRI_DEFAULT, "mi_llamada_retorno_rename", $nombre_fichero);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    eio_rename_ok
