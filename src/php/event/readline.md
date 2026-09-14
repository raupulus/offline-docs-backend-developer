---
title: EventBuffer::readLine
description: Extrae una línea desde el inicio del búfer
source_url: https://www.php.net/manual/es/eventbuffer.readline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/readline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19300
---

EventBuffer::readLine

Extrae una línea desde el inicio del búfer

## Descripción

```php
public EventBuffer::readLine(int $eol_style): string
```php

Extrae una línea desde el inicio del búfer y la devuelve en una nueva string asignada. Si no hay una línea completa para leer, el método devuelve `null`. La terminación de la línea no está incluida en la string copiada.

## Parámetros

`eol_style`  
Una constante [EventBuffer:EOL\_\*](#eventbuffer.constants).

## Valores devueltos

En caso de éxito, devuelve la línea leída desde el búfer, `null` en caso contrario.

## Véase también

EventBuffer::copyout

EventBuffer::drain

EventBuffer::pullup

EventBuffer::read

EventBuffer::appendFrom
