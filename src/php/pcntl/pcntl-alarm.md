---
title: pcntl_alarm
description: Programa una alarma para enviar una señal
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-alarm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 96c9d88ba
order: 61180
---

pcntl_alarm

Programa una alarma para enviar una señal

## Descripción

```php
pcntl_alarm(int $seconds): int
```php

Crea una cuenta atrás que enviará una señal `SIGALRM` al proceso después del número de segundos dado. Cualquier llamada a `pcntl_alarm` anulará las cuentas atrás previamente configuradas.

## Parámetros

`seconds`  
El número de segundos a esperar. Si `seconds` vale cero, no se creará ninguna nueva alarma.

## Valores devueltos

Devuelve el tiempo en segundos que queda antes de la ejecución de la alarma anterior, o `0` si no había ninguna alarma programada.
