---
title: eio_symlink
description: Crear un enlace simbólico
source_url: https://www.php.net/manual/es/function.eio-symlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-symlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17190
---

eio_symlink

Crear un enlace simbólico

## Descripción

```php
eio_symlink(string $path, string $new_path, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_symlink` crea un enlace simbólico `new_path` hacia `path`.

## Parámetros

`path`  
La ruta fuente

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

`eio_symlink` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_symlink`

```
<?php
$nombre_fichero = dirname(__FILE__)."/symlink.dat";
touch($nombre_fichero);
$enlace = dirname(__FILE__)."/symlink.link";

function mi_llamada_retorno_symlink($datos, $resultado) {
    global $enlace, $nombre_fichero;
    var_dump(file_exists($datos) && is_link($datos));

    if (!eio_readlink($datos, EIO_PRI_DEFAULT, "mi_llamada_retorno_readlink", NULL)) {
        @unlink($enlace);
        @unlink($nombre_fichero);
    }
}

function mi_llamada_retorno_readlink($datos, $resultado) {
    global $nombre_fichero, $enlace;
    var_dump($resultado);

    @unlink($enlace);
    @unlink($nombre_fichero);
}

eio_symlink($nombre_fichero, $enlace, EIO_PRI_DEFAULT, "mi_llamada_retorno_symlink", $enlace);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    string(16) "/tmp/symlink.dat"

## Véase también

eio_link
