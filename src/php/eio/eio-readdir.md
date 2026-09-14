---
title: eio_readdir
description: Leer un directorio al completo
source_url: https://www.php.net/manual/es/function.eio-readdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-readdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17050
---

eio_readdir

Leer un directorio al completo

## Descripción

```php
eio_readdir(string $path, int $flags, int $pri, callable $callback, [string $data]): resource
```php

Leer un directorio al completo (mediante las llamadas al sistema de `opendir`, `readdir` y `closedir`) y devuelve o los nombres o un array en el argumento `result` de la función `callback`, dependiendo del argumento `flags`.

## Parámetros

`path`  
La ruta del directorio.

`flags`  
Una combinación de constantes *EIO_READDIR\_\**.

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

`eio_readdir` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error. Establece el argumento `result` de la función `callback` function según el parámetro `flags`:

`EIO_READDIR_DENTS` (`int`)  
Bandera `eio_readdir`. Si se especifica, el argumento resultante de la llamada de retorno se convierte en un array con las siguientes claves: `'names'` - array de nombres de directorios `'dents'` - array de `structura eio_dirent`-como los arrays pero teniendo las siguientes claves: `'name'` - el nombre del directorio; `'type'` - una de las constantes *EIO_DT\_\**; `'inode'` - el número de inodo, si está disponible, de otro modo sin especificar;

`EIO_READDIR_DIRS_FIRST` (`int`)  
Cuando se especifica esta bandera, los nombres serán devueltos en un orden donde probablemente los directorios vallan primero, en un orden de estadísticas óptimo.

`EIO_READDIR_STAT_ORDER` (`int`)  
Cuando se especifica esta bandera, los nombres serán devueltos en un orden apropiado para realizar estadísticas (`stat`) con cada uno. Cuando se planea usar la función `stat` para realizar estadísticas de todos los archivos del directorio dado, el orden devuelto probablemente sea más rápido.

`EIO_READDIR_FOUND_UNKNOWN` (`int`)  

Tipos de nodos:

`EIO_DT_UNKNOWN` (`int`)  
Tipo de nodo desconocido(muy común). Se necistan más estadísticas (`stat`).

`EIO_DT_FIFO` (`int`)  
Tipo de nodo FIFO

`EIO_DT_CHR` (`int`)  
Tipo de nodo

`EIO_DT_MPC` (`int`)  
Tipo de nodo de dispositivo de caracteres multiplexado (v7+coherent)

`EIO_DT_DIR` (`int`)  
Tipo de nodo de directorio

`EIO_DT_NAM` (`int`)  
Tipo de nodo de fichero Xenix nominado especial

`EIO_DT_BLK` (`int`)  
Tipo de nodo

`EIO_DT_MPB` (`int`)  
Dispositivo de bloqueo multiplexado (v7+coherent)

`EIO_DT_REG` (`int`)  
Tipo de nodo

`EIO_DT_NWK` (`int`)  

`EIO_DT_CMP` (`int`)  
Tipo de noto especial de red HP-UX

`EIO_DT_LNK` (`int`)  
Tipo de nodo de vínculo

`EIO_DT_SOCK` (`int`)  
Tipo de nodo socket

`EIO_DT_DOOR` (`int`)  
Tipo de nodo de puerta de Solaris

`EIO_DT_WHT` (`int`)  
Tipo de nodo

`EIO_DT_MAX` (`int`)  
Valor de tipo de nodo más alto

## Ejemplos

Ejemplo de `eio_readdir`

```
<?php
/* Es llamada cuando eio_readdir() finaliza */
function mi_llamada_retorno_readdir($datos, $resultado) {
    echo __FUNCTION__, " llamada\n";
    echo "datos: "; var_dump($datos);
    echo "resultado: "; var_dump($resultado);
    echo "\n";
}

eio_readdir("/var/spool/news", EIO_READDIR_STAT_ORDER | EIO_READDIR_DIRS_FIRST,
  EIO_PRI_DEFAULT, "mi_llamada_retorno_readdir");
eio_event_loop();
?>

      
```php

Resultado del ejemplo anterior es similar a:

    mi_llamada_retorno_readdir llamada
    datos: NULL
    resultado: array(2) {
     ["names"]=>
      array(7) {
       [0]=>
        string(7) "archive"
        [1]=>
        string(8) "articles"
        [2]=>
        string(8) "incoming"
        [3]=>
        string(7) "innfeed"
        [4]=>
        string(8) "outgoing"
        [5]=>
        string(8) "overview"
        [6]=>
        string(3) "tmp"
      }
     ["dents"]=>
      array(7) {
       [0]=>
        array(3)
        {
         ["name"]=>
          string(7)
          "archive"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393265)
        }
       [1]=>
        array(3)
        {
         ["name"]=>
          string(8)
          "articles"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393266)
        }
       [2]=>
        array(3)
        {
         ["name"]=>
          string(8)
          "incoming"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393267)
        }
       [3]=>
        array(3)
        {
         ["name"]=>
          string(7)
          "innfeed"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393269)
        }
       [4]=>
        array(3)
        {
         ["name"]=>
          string(8)
          "outgoing"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393270)
        }
       [5]=>
        array(3)
        {
         ["name"]=>
          string(8)
          "overview"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393271)
        }
       [6]=>
        array(3)
        {
         ["name"]=>
          string(3)
          "tmp"
          ["type"]=>
          int(4)
          ["inode"]=>
          int(393272)
        }
      }
    }
