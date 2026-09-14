---
title: eio_statvfs
description: Obtener las estadísticas del sistema de ficheros
source_url: https://www.php.net/manual/es/function.eio-statvfs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-statvfs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17180
---

eio_statvfs

Obtener las estadísticas del sistema de ficheros

## Descripción

```php
eio_statvfs(string $path, int $pri, callable $callback, [mixed $data]): resource
```php

`eio_statvfs` devuelve la información de las estadísticas del sistema de ficheros en el argumento `result` de `callback`

## Parámetros

`path`  
El nombre de ruta de cualquier fichero dentro del sistema de ficheros montado

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

`eio_statvfs` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error. En caso de éxito asigna el argumento `result` de `callback` a un array.

## Ejemplos

Ejemplo de `eio_statvfs`

```
<?php
$nombre_fichero_temp = '/tmp/fichero-eio.tmp';
touch($nombre_fichero_temp);

function mi_llamada_retorno_statvfs($datos, $resultado) {
    var_dump($datos);
    var_dump($resultado);

 @unlink($datos);
}

eio_statvfs($nombre_fichero_temp, EIO_PRI_DEFAULT, "mi_llamada_retorno_statvfs", $nombre_fichero_temp);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(17) "/tmp/eio-file.tmp"
    array(11) {
      ["f_bsize"]=>
      int(4096)
      ["f_frsize"]=>
      int(4096)
      ["f_blocks"]=>
      int(262144)
      ["f_bfree"]=>
      int(262111)
      ["f_bavail"]=>
      int(262111)
      ["f_files"]=>
      int(1540815)
      ["f_ffree"]=>
      int(1540743)
      ["f_favail"]=>
      int(1540743)
      ["f_fsid"]=>
      int(0)
      ["f_flag"]=>
      int(4102)
      ["f_namemax"]=>
      int(255)
    }
