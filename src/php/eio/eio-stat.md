---
title: eio_stat
description: Obtener el estado de un fichero
source_url: https://www.php.net/manual/es/function.eio-stat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-stat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17170
---

eio_stat

Obtener el estado de un fichero

## Descripción

```php
eio_stat(string $path, int $pri, callable $callback, [mixed $data]): resource
```php

`eio_stat` devuelve la información del estado de un fichero en el argumento `result` de `callback`

## Parámetros

`path`  
La ruta de archivo

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

`eio_stat`devuelve un recurso de petición en caso de éxito o `false` en caso de error. En caso de éxito asigna el argumento `result` de `callback` a un array.

## Ejemplos

Ejemplo de `eio_stat`

```
<?php
$nombre_fichero_temp = "fichero-eio.tmp";
touch($nombre_fichero_temp);

function my_res_cb($datos, $resultado) {
    var_dump($datos);
    var_dump($resultado);
}

function my_open_cb($datos, $resultado) {
    eio_close($resultado);
    eio_event_loop();

    @unlink($datos);
}

eio_stat($nombre_fichero_temp, EIO_PRI_DEFAULT, "my_res_cb", "eio_stat");
eio_open($nombre_fichero_temp, EIO_O_RDONLY, NULL,
 EIO_PRI_DEFAULT, "my_open_cb", $nombre_fichero_temp);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(8) "eio_stat"
    array(12) {
      ["st_dev"]=>
      int(2050)
      ["st_ino"]=>
      int(2489173)
      ["st_mode"]=>
      int(33188)
      ["st_nlink"]=>
      int(1)
      ["st_uid"]=>
      int(1000)
      ["st_gid"]=>
      int(100)
      ["st_rdev"]=>
      int(0)
      ["st_blksize"]=>
      int(4096)
      ["st_blocks"]=>
      int(0)
      ["st_atime"]=>
      int(1318250380)
      ["st_mtime"]=>
      int(1318250380)
      ["st_ctime"]=>
      int(1318250380)
    }

## Véase también

eio_lstat

eio_fstat
