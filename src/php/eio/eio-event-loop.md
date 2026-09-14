---
title: eio_event_loop
description: Monitorizar libeio hasta que todas las peticiones sean procesadas
source_url: https://www.php.net/manual/es/function.eio-event-loop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-event-loop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16750
---

eio_event_loop

Monitorizar libeio hasta que todas las peticiones sean procesadas

## Descripción

```php
eio_event_loop(): bool
```php

`eio_event_loop` monitoriza libeio hasta que todas las peticiones sean procesadas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`eio_event_loop` devuelve `true` en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `eio_event_loop`

```
<?php
$nombre_fichero_temp = "fichero-temp-eio.tmp";
touch($nombre_fichero_temp);

/* Es llamada cuando eio_chmod() finaliza */
function mi_llamada_retorno_chmod($datos, $resultado) {
    global $nombre_fichero_temp;

    if ($resultado == 0 && !is_readable($nombre_fichero_temp) && is_writable($nombre_fichero_temp)) {
        echo "eio_chmod_ok";
    }

    @unlink($nombre_fichero_temp);
}

eio_chmod($nombre_fichero_temp, 0200, EIO_PRI_DEFAULT, "mi_llamada_retorno_chmod");
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    eio_chmod_ok

## Véase también

eio_poll
