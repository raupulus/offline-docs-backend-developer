---
title: EventUtil::getSocketFd
description: Devuelve el descriptor de fichero de un socket o de un flujo
source_url: https://www.php.net/manual/es/eventutil.getsocketfd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventutil/getsocketfd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: e41806c30
order: 20460
---

EventUtil::getSocketFd

Devuelve el descriptor de fichero de un socket o de un flujo

## Descripción

```php
public static EventUtil::getSocketFd(mixed $socket): int
```php

Devuelve el descriptor numérico de fichero de un socket o de un flujo especificado por el parámetro `socket`, como lo hace la extensión `Event` internamente para todos los métodos que aceptan un socket o un flujo.

## Parámetros

`socket`  
Socket o flujo.

## Valores devueltos

Devuelve el descriptor de fichero numérico en caso de éxito, `false` en caso contrario. EventUtil::getSocketFd devuelve `false` en el caso de que el tipo de fichero no haya podido ser reconocido, o bien cuando el descriptor de fichero asociado con el parámetro `socket` no es válido.
