---
title: eio_grp_add
description: Añadir una petición al grupo de peticiones
source_url: https://www.php.net/manual/es/function.eio-grp-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-grp-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16870
---

eio_grp_add

Añadir una petición al grupo de peticiones

## Descripción

```php
eio_grp_add(resource $grp, resource $req): void
```php

`eio_grp_add` añade una petición al grupo de peticiones.

## Parámetros

`grp`  
El recurso de grupo de peticiones devuelto por `eio_grp`

`req`  
El recurso de petición

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Agrupar peticiones

```
<?php
/*
 * Crear un grupo de peticiones para abrir, leer y cerrar un fichero
 */

// Crear un fichero temporal y escribir algunos bytes en él
$nombre_fichero_temp = dirname(__FILE__) ."/fichero-eio.tmp";
$fp = fopen($nombre_fichero_temp, "w");
fwrite($fp, "algunos datos");
fclose($fp);

/* Es llamada cuando el grupo de peticiones está hecho */
function mi_grupo_hecho($datos, $resultado) {
 var_dump($resultado == 0);
 @unlink($datos);
}

/* Es llamada cuando eio_open() termina */
function mi_llamada_retorno_fichero_abierto($datos, $resultado) {
 global $grupo;

 // $resultado debería contener el descriptor del fichero
 var_dump($resultado > 0);

 // Crear una petición eio_read() y añadirla al grupo
 // Pasar el descriptor del fichero a la llamada de retorno
 $petición = eio_read($resultado, 4, 0,
   EIO_PRI_DEFAULT, "mi_llamada_retorno_grupo_fichero_leído", $resultado);
 eio_grp_add($grupo, $petición);
}

/* Es llamada cuando eio_read() termina */
function mi_llamada_retorno_grupo_fichero_leído($datos, $resultado) {
 global $grupo;

 // Leer bytes
 var_dump($resultado);

 // Crear una petición eio_close() y añadirla al grupo
 // $datos debería contener el descriptor del fichero
 $petición = eio_close($datos);
 eio_grp_add($grupo, $petición);
}

// Crear un grupo de peticiones
$grupo = eio_grp("mi_grupo_hecho", $nombre_fichero_temp);
var_dump($grupo);

// Crear una petición eio_open() y añadirla al grupo
$petición = eio_open($nombre_fichero_temp, EIO_O_RDWR | EIO_O_APPEND , NULL,
  EIO_PRI_DEFAULT, "mi_llamada_retorno_fichero_abierto", NULL);
eio_grp_add($grupo, $petición);

// Procesar las peticiones
eio_event_loop();
?>
```php

Resultado del ejemplo anterior es similar a:

    resource(6) of type (EIO Group Descriptor)
    bool(true)
    string(7) "algunos"
    bool(true)

## Véase también

eio_grp

eio_grp_cancel

eio_grp_limit
