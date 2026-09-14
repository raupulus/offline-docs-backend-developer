---
title: Ev::supportedBackends
description: Devuelve el conjunto de backends soportados por la configuración actual
  de libev
source_url: https://www.php.net/manual/es/ev.supportedbackends.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/supportedbackends.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17890
---

Ev::supportedBackends

Devuelve el conjunto de backends soportados por la configuración actual de libev

## Descripción

```php
final public static Ev::supportedBackends(): int
```php

Devuelve el conjunto de backends soportados por la configuración actual de libev.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una máscara de bits que puede contener los [flags de backend](#ev.constants.watcher-backends) combinados utilizando el operador *OR*.

## Ejemplos

Bucle integrado creado con el backend kqueue en el bucle por defecto

```
<?php
/*
* Verifica si kqueue está disponible (pero no recomendado) y crea un backend kqueue
* para usarlo con sockets (lo cual funciona con cualquier implementación
* kqueue).
* Almacena el bucle de eventos kqueue (utilizable únicamente a través de sockets)
* en loop_socket. (uso opcional de EVFLAG_NOENV)
*
* Ejemplo tomado de la siguiente URL:
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

// Ahora, uso de $socket_loop para todos los sockets y $loop para todo lo demás
?>

  
```php

## Véase también

EvEmbed

Ev::recommendedBackends

Ev::embeddableBackends

Los flags de backend

Los ejemplos
