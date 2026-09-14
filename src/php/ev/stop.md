---
title: Ev::stop
description: Detiene el bucle de eventos predeterminado
source_url: https://www.php.net/manual/es/ev.stop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ev/ev/stop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ev
translation_status: ready
translation_reviewed: false
translation_revision: b4fbf4434
order: 17880
---

Ev::stop

Detiene el bucle de eventos predeterminado

## Descripción

```php
final public static Ev::stop([int $how]): void
```php

Detiene el bucle de eventos predeterminado.

## Parámetros

`how`  
Una [constante](#ev.constants.break-flags) entre las constantes *Ev::BREAK\_\**.

## Valores devueltos

No se retorna ningún valor.

## Véase también

Ev::run
