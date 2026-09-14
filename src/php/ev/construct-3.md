---
title: EvEmbed::__construct
description: Construye un objeto EvEmbed
source_url: https://www.php.net/manual/es/evembed.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evembed/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18010
---

EvEmbed::\_\_construct

Construye un objeto EvEmbed

## Descripción

```php
public EvEmbed::__construct(object $other, [callable $callback], [mixed $data], [int $priority])
```php

Se trata de un tipo de watcher avanzado que permite integrar un bucle de eventos en otro (actualmente, solo los eventos IO son soportados en el bucle interno, otros tipos de watcher no deben ser utilizados).

Ver la [ documentación libev](http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_embed_code_when_one_backend_) para más detalles.

Este watcher es más útil en sistemas *BSD* donde `kqueue` no es utilizado, para poder manejar un gran número de sockets. Ver el ejemplo a continuación.

## Parámetros

`other`  
Una instancia de `EvLoop`. El bucle a integrar; debe ser encapsulable (ver el método Ev::embeddableBackends).

`callback`  
Ver las [funciones de retrollamada de los Watcher](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el watcher.

`priority`  
[Prioridad del Watcher](#ev.constants.watcher-pri)

## Ejemplos

Encapsulamiento de un bucle creado con el gestor kqueue en el bucle por omisión

```
<?php
/*
 * Verifica si kqueue está disponible y crea un gestor kqueue
 * para usarlo con los sockets (que funciona habitualmente con cualquier implementación
 * de kqueue. Almacena el bucle de eventos kqueue/socket solo, en loop_socket.
 * (opcionalmente, uso de EVFLAG_NOENV)
 *
 * Ejemplo tomado de
 * http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Examples_CONTENT-9
 */
$loop        = EvLoop::defaultLoop();
$socket_loop = NULL;
$embed       = NULL;

if (Ev::supportedBackends() & ~Ev::recommendedBackends() & Ev::BACKEND_KQUEUE) {
    if (($socket_loop = new EvLoop(Ev::BACKEND_KQUEUE))) {
        $embed = new EvEmbed($loop);
    }
}

if (!$socket_loop) {
    $socket_loop = $loop;
}

// Ahora, se usa $socket_loop para todos los sockets, y $loop para todo lo demás
?>

   
```php

## Véase también

Ev::embeddableBackends
