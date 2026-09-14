---
title: ibase_wait_event
description: Espera un evento interBase
source_url: https://www.php.net/manual/es/function.ibase-wait-event.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-wait-event.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30570
---

ibase_wait_event

Espera un evento interBase

## Descripción

```php
ibase_wait_event(string $event_name, string ...$event_names): string
```php

```php
ibase_wait_event(resource $connection, string $event_name, string ...$event_names): string
```

`ibase_wait_event` suspende la ejecución del script hasta que uno de los eventos especificados sea publicado por la base de datos. El nombre del evento que ha sido publicado es entonces devuelto. Esta función acepta hasta 15 argumentos de eventos.

## Parámetros

`event_name`  
El nombre del evento.

`event_names`  

## Valores devueltos

Devuelve el nombre del evento que ha sido publicado.

## Véase también

ibase_set_event_handler

ibase_free_event_handler
