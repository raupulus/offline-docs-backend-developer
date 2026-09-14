---
title: eio_grp
description: Crear un grupo de peticiones
source_url: https://www.php.net/manual/es/function.eio-grp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-grp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16900
---

eio_grp

Crear un grupo de peticiones

## Descripción

```php
eio_grp(callable $callback, [string $data]): resource
```php

`eio_grp` crea un grupo de peticiones.

## Parámetros

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

`eio_grp` devuelve un recurso de grupo de peticiones en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_grp`

```
<?php
$nombre_fichero_temp = dirname(__FILE__) ."/fichero-eio.tmp";
$fp = fopen($nombre_fichero_temp, "w");
fwrite($fp, "algunos datos");
fclose($fp);
$mi_df_fichero = NULL;

/* Es llamada cuando el grupo de peticiones está hecho */
function mi_grupo_hecho($datos, $resultado) {
 // Eliminar el fichero, si aún existe
 @unlink($datos);
}

/* Es llamada al abrir el fichero temporal */
function mi_llamada_retorno_grupo_fichero_abierto($datos, $resultado) {
 global $mi_df_fichero, $grupo;

 $mi_df_fichero = $resultado;

 $petición = eio_read($mi_df_fichero, 4, 0,
   EIO_PRI_DEFAULT, "mi_llamada_retorno_grupo_fichero_leído");
 eio_grp_add($grupo, $petición);
}

/* Es llamada cuando el fichero es leído */
function mi_llamada_retorno_grupo_fichero_leído($datos, $resultado) {
 global $mi_df_fichero, $grupo;

 var_dump($resultado);

 // Crear una petición para cerrar el fichero
 $petición = eio_close($mi_df_fichero);

 // Añadir la petición al grupo
 eio_grp_add($grupo, $petición);
}

// Crear un grupo de peticiones
$grupo = eio_grp("mi_grupo_hecho", $nombre_fichero_temp);

// Crear una petición
$petición = eio_open($nombre_fichero_temp, EIO_O_RDWR | EIO_O_APPEND , NULL,
  EIO_PRI_DEFAULT, "mi_llamada_retorno_grupo_fichero_abierto", NULL);

// Añadir la petición al grupo
eio_grp_add($grupo, $petición);

// Procesar las peticiones
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(7) "algunos"

## Véase también

eio_grp_cancel

eio_grp_add
