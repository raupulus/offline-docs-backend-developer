---
title: eio_link
description: Crear un enlace duro par un fichero
source_url: https://www.php.net/manual/es/function.eio-link.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-link.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16920
---

eio_link

Crear un enlace duro par un fichero

## Descripción

```php
eio_link(string $path, string $new_path, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_link` crea el enlace duro dado por `new_path` para un fichero especificado por `path`.

## Parámetros

`path`  
La ruta del fichero origen.

`new_path`  
La ruta del fichero destino.

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

## Ejemplos

Ejemplo de `eio_link`

```
<?php
$nombre_fichero = dirname(__FILE__)."/symlink.dat";
touch($nombre_fichero);
$enlace = dirname(__FILE__)."/symlink.link";
$enlace_duro = dirname(__FILE__)."/hardlink.link";

function mi_llamada_retorno_hardlink($datos, $resultado) {
    global $enlace, $nombre_fichero;
    var_dump(file_exists($datos) && !is_link($datos));
    @unlink($datos);

    eio_symlink($nombre_fichero, $enlace, EIO_PRI_DEFAULT, "mi_llamada_retorno_symlink", $enlace);
}

function mi_llamada_retorno_symlink($datos, $resultado) {
    global $enlace, $nombre_fichero;
    var_dump(file_exists($data) && is_link($datos));

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

eio_link($nombre_fichero, $enlace_duro, EIO_PRI_DEFAULT, "mi_llamada_retorno_hardlink", $enlace_duro);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    string(%d) "%ssymlink.dat"

## Véase también

eio_symlink
