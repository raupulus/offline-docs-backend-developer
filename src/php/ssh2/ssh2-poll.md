---
title: ssh2_poll
description: Consulta los canales/observadores/flujos para eventos
source_url: https://www.php.net/manual/es/function.ssh2-poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86550
---

ssh2_poll

Consulta los canales/observadores/flujos para eventos

## Descripción

```php
ssh2_poll(array $desc, [int $timeout]): int
```php

Consulta los canales/observadores/flujos para eventos, y devuelve el número de descriptores que han devuelto eventos no nulos.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`desc`  
Un array indexado de sub-arrays con las claves `'resource'` y `'events'`. El valor de la ressource es un flujo (de canal) o una ressource de tipo SSH2 Listener. El valor del evento es un máscara de bits SSH2_POLL\*. Cada sub-array será poblado con un elemento `'revents'` al final, cuyos valores son máscaras de bits SSH2_POLL\* de los eventos que han ocurrido.

`timeout`  
El tiempo de espera en segundos.

## Valores devueltos

Devuelve el número de descriptores que han devuelto eventos no nulos.
