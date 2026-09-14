---
title: openlog
description: Abre la conexión al historial del sistema
source_url: https://www.php.net/manual/es/function.openlog.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/openlog.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 35ca7f108
order: 56500
---

openlog

Abre la conexión al historial del sistema

## Descripción

```php
openlog(string $prefix, int $flags, int $facility): true
```php

`openlog` abre la conexión al historial del sistema.

El uso de `openlog` es opcional. Esta función será llamada automáticamente por la función `syslog` si es necesario, en cuyo caso `prefix` valdrá por omisión `false`.

## Parámetros

`prefix`  
El string `prefix` será añadido a cada mensaje.

`flags`  
Máscara de bits de las constantes siguientes: `LOG_CONS`, `LOG_NDELAY`, `LOG_ODELAY`, `LOG_NOWAIT`, `LOG_PERROR`, `LOG_PID`

`facility`  
El argumento `facility` se utiliza para especificar el tipo de programa que registra el mensaje. Esto permite al fichero de configuración especificar que los mensajes provenientes de diferentes instalaciones serán tratados de manera distinta. Debe ser una de las constantes siguientes: `LOG_AUTH`, `LOG_AUTHPRIV`, `LOG_CRON`, `LOG_DAEMON`, `LOG_KERN`, `LOG_LOCAL[0-7]`, `LOG_LPR`, `LOG_MAIL`, `LOG_NEWS`, `LOG_SYSLOG`, `LOG_USER`, `LOG_UUCP`

> [!NOTE]
> Este parámetro es ignorado en Windows.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La función ahora siempre retorna `true`. Anteriormente, retornaba `false` en caso de fallo. |

## Véase también

`syslog`, `closelog`
