---
title: eio_mknod
description: Crear un fichero especial u ordinario
source_url: https://www.php.net/manual/es/function.eio-mknod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-mknod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16950
---

eio_mknod

Crear un fichero especial u ordinario

## Descripción

```php
eio_mknod(string $path, int $mode, int $dev, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_mknod` crea un fichero ordinario o especial (a menudo).

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`path`  
Ruta del nuevo nodo (fichero).

`mode`  
Especifica tanto los permisos a usar como el tipo de nodo a ser creado. Debería ser una combinación (usando el operador OR) de uno de los tipos de fichero listados abajo y los permisos para el nuevo nodo (p.ej. 0640). Los tipos de ficheros posibles son: `EIO_S_IFREG` (fichero regular), `EIO_S_IFCHR` (fichero de carácter), `EIO_S_IFBLK` (fichero especial de bloqueo), `EIO_S_IFIFO` (FIFO - tubería nominada) y `EIO_S_IFSOCK` (socket de dominio UNIX). Para especificar permisos se podrían usar constantes *EIO_S_I\**.

`dev`  
Si el tipo de fichero es `EIO_S_IFCHR` o `EIO_S_IFBLK`, dev especifica el número mayor y menor del recién creado fichero especial de dispositivo. De otro modo `dev` es ignorado. Véase *la página del manual mknod(2) para más detalles*.

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

`eio_mknod` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_mknod`

```
<?php
// Nombre FIFO
$nombre_fichero_temp = "/tmp/eio-temp-fifo";

/* Se llama cuando eio_mknod() finaliza */
function mi_llamada_retorno_mknod($datos, $resultado) {
    $s = stat($datos);
    var_dump($s);

    if ($resultado == 0) {
        echo "eio_mknod_ok";
    }

    @unlink($datos);
}

eio_mknod($nombre_fichero_temp, EIO_S_IFIFO, 0,
    EIO_PRI_DEFAULT, "mi_llamada_retorno_mknod", $nombre_fichero_temp);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(26) {
      [0]=>
      int(17)
      [1]=>
      int(2337608)
      [2]=>
      int(4096)
      [3]=>
      int(1)
      [4]=>
      int(1000)
      [5]=>
      int(100)
      [6]=>
      int(0)
      [7]=>
      int(0)
      [8]=>
      int(1318241261)
      [9]=>
      int(1318241261)
      [10]=>
      int(1318241261)
      [11]=>
      int(4096)
      [12]=>
      int(0)
      ["dev"]=>
      int(17)
      ["ino"]=>
      int(2337608)
      ["mode"]=>
      int(4096)
      ["nlink"]=>
      int(1)
      ["uid"]=>
      int(1000)
      ["gid"]=>
      int(100)
      ["rdev"]=>
      int(0)
      ["size"]=>
      int(0)
      ["atime"]=>
      int(1318241261)
      ["mtime"]=>
      int(1318241261)
      ["ctime"]=>
      int(1318241261)
      ["blksize"]=>
      int(4096)
      ["blocks"]=>
      int(0)
    }
    eio_mknod_ok

## Véase también

eio_open
