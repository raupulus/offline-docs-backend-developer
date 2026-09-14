---
title: Ev::embeddableBackends
description: Devuelve el conjunto de backends que pueden ser encapsulados en otros
  bucles de eventos
source_url: https://www.php.net/manual/es/ev.embeddablebackends.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/embeddablebackends.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17780
---

Ev::embeddableBackends

Devuelve el conjunto de backends que pueden ser encapsulados en otros bucles de eventos

## Descripción

```php
final public static Ev::embeddableBackends(): int
```php

Devuelve el conjunto de backends que pueden ser encapsulados en otros bucles de eventos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una máscara de octetos que puede contener los [flags de backend](#ev.constants.watcher-backends) combinados con el operador *OR*.

## Ejemplos

Encapsula un bucle creado con el backend kqueue en el bucle por defecto

```
<?php
/*
* Verifica si kqueue está disponible y crea un backend kqueue
* para usarlo con sockets (que funciona habitualmente con cualquier
* implementación de kqueue).
* Almacena el bucle de eventos kqueue/solo-sockets en loop_socket.
* (uso opcional de EVFLAG_NOENV)
*
* Ejemplo tomado de:
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

// Ahora, se utiliza $socket_loop para todos los sockets, y $loop para todo lo demás
?>

   
```php

## Véase también

EvEmbed

Ev::recommendedBackends

Ev::supportedBackends

Los flags de Backend

Los ejemplos
