---
title: eio_mkdir
description: Crear un directorio
source_url: https://www.php.net/manual/es/function.eio-mkdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-mkdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16940
---

eio_mkdir

Crear un directorio

## Descripción

```php
eio_mkdir(string $path, int $mode, [int $pri], [callable $callback], [mixed $data]): resource
```php

`eio_mkdir` crea un directorio con el acceso especificado por `mode`.

## Parámetros

`path`  
La ruta del nuevo directorio.

`mode`  
Modo de acceso, p.ej. 0755

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

`eio_mkdir` devuelve un recurso de petición en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_mkdir`

```
<?php
$nombre_directorio_temp = "dir-tmp-eio";

/* Es llamada cuando eio_mkdir() finaliza */
function mi_llamada_retorno_mkdir($datos, $resultado) {
 if ($resultado == 0 && is_dir($nombre_directorio_temp)
   && !is_readable($nombre_directorio_temp)
   && is_writable($nombre_directorio_temp)) {
  echo "eio_mkdir_ok";
 }

 // Eliminar el directorio
    if (file_exists($datos))
        rmdir($nombre_directorio_temp);
}

// Crear un directorio con modo de acceso 0300
eio_mkdir($nombre_directorio_temp, 0300, EIO_PRI_DEFAULT, "mi_llamada_retorno_mkdir", $nombre_directorio_temp);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    eio_mkdir_ok

## Véase también

eio_rmdir
