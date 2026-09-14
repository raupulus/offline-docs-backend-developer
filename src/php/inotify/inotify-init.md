---
title: inotify_init
description: Inicializa una instancia inotify
source_url: https://www.php.net/manual/es/function.inotify-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/inotify/functions/inotify-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: inotify
translation_status: ready
translation_reviewed: false
translation_revision: ab6d54b20
order: 39310
---

inotify_init

Inicializa una instancia inotify

## Descripción

```php
inotify_init(): resource
```php

Inicializa una instancia inotify para ser utilizada con la función `inotify_add_watch`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un flujo o `false` en caso de error.

## Ejemplos

Ejemplo de utilización de inotify

```
<?php
// Crea una instancia inotify
$fd = inotify_init();

// Vigila las modificaciones de los metadatos del fichero __FILE__ (e.g. mtime)
$watch_descriptor = inotify_add_watch($fd, __FILE__, IN_ATTRIB);

// Genera un evento
touch(__FILE__);

// Lee los eventos
$events = inotify_read($fd);
print_r($events);

// Los métodos siguientes permiten utilizar las funciones inotify sin bloquear sobre inotify_read():

// - Utilizar stream_select() sobre $fd:
$read = array($fd);
$write = null;
$except = null;
stream_select($read,$write,$except,0);

// - Utilizar stream_set_blocking() sobre $fd
stream_set_blocking($fd, 0);
inotify_read($fd); // No bloquea, y devuelve false si no hay eventos pendientes

// - Utilizar inotify_queue_len() para verificar el tamaño de la cola
$queue_len = inotify_queue_len($fd); // Si > 0, inotify_read() no bloqueará

// Detener la vigilancia de __FILE__
inotify_rm_watch($fd, $watch_descriptor);

// Destrucción de la instancia inotify
// Esto habría detenido todas las vigilancias si no se hubiera hecho ya
fclose($fd);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(
      array(
        'wd' => 1,     // Igual al $watch_descriptor
        'mask' => 4,   // El bit IN_ATTRIB está activado
        'cookie' => 0, // Identificador único para vincular eventos (e.g.
                       // IN_MOVE_FROM y IN_MOVE_TO)
        'name' => '',  // El nombre del fichero (e.g. si un directorio estaba bajo vigilancia)
      ),
    );

## Véase también

inotify_add_watch

inotify_rm_watch

inotify_queue_len

inotify_read

fclose
