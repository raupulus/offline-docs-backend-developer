---
title: EvCheck::createStopped
description: Crea una instancia de un observador EvCheck detenido
source_url: https://www.php.net/manual/es/evcheck.createstopped.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/evcheck/createstopped.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17950
---

EvCheck::createStopped

Crea una instancia de un observador EvCheck detenido

## Descripción

```php
final public static EvCheck::createStopped(string $callback, [string $data], [string $priority]): object
```php

Crea una instancia de un observador EvCheck detenido.

## Parámetros

`callback`  
Ver las [retrollamadas de los observadores](#ev.watcher-callbacks).

`data`  
Datos personalizados para asociar con el observador.

`priority`  
[Prioridad del observador](#ev.constants.watcher-pri)

## Valores devueltos

Devuelve el objeto EvCheck en caso de éxito.

## Véase también

EvPrepare
