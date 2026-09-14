---
title: eio_realpath
description: Obtener el nombre de ruta absoluto canonizado
source_url: https://www.php.net/manual/es/function.eio-realpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-realpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 940ea8c1b
order: 17070
---

eio_realpath

Obtener el nombre de ruta absoluto canonizado

## Descripción

```php
eio_realpath(string $path, int $pri, callable $callback, [string $data]): resource
```php

`eio_realpath` devuelve el nombre de ruta absoluto canonizado en el argumento `result` de la función `callback`.

## Parámetros

`path`  
EL nombre abreviado

`pri`  

`callback`  

`data`  

## Valores devueltos

## Ejemplos

Ejemplo de`eio_realpath`

```
<?php
var_dump(getcwd());

function mi_llamada_retorno_realpath($datos, $resultado) {
    var_dump($resultado);
}

eio_realpath("../", EIO_PRI_DEFAULT, "mi_llamada_retorno_realpath");
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(12) "/home/ruslan"
    string(5) "/home"
