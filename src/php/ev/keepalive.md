---
title: EvWatcher::keepalive
description: Mantiene el bucle activo
source_url: https://www.php.net/manual/es/evwatcher.keepalive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evwatcher/keepalive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 18700
---

EvWatcher::keepalive

Mantiene el bucle activo

## Descripción

```php
public EvWatcher::keepalive([bool $value]): bool
```php

Mantiene el bucle activo. Con un parámetro `value` definido a `false`, el Watcher no evitará que los métodos Ev::run/EvLoop::run se detengan incluso si el Watcher está activo.

Los Watchers tienen, por omisión, un parámetro `value` definido a `true`.

Limpiar el estado "keepalive" es útil al regresar de los métodos Ev::run/EvLoop::run, en cuyo caso el Watcher ya no es deseado. Puede ser un Watcher de socket UDP que continúa funcionando durante mucho tiempo.

## Parámetros

`value`  
Si es `false`, el Watcher no evitará que los métodos Ev::run/EvLoop::run terminen, incluso si el Watcher está activo.

## Valores devueltos

Devuelve el estado anterior.

## Ejemplos

Registra un Watcher E/S para sockets UDP

```
<?php
$udp_socket = ...
$udp_watcher = new EvIo($udp_socket, Ev::READ, function () { /* ... */ });
$udp_watcher->keepalive(FALSE);
?>

   
```php
