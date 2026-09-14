---
title: pg_socket_poll
description: Sondea un socket de conexión PostgreSQL para comprobar si está listo
  para lectura/escritura
source_url: https://www.php.net/manual/es/function.pg-socket-poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-socket-poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 491bd06bf
order: 63730
---

pg_socket_poll

Sondea un socket de conexión PostgreSQL para comprobar si está listo para lectura/escritura

## Descripción

```php
pg_socket_poll(resource $socket, int $read, int $write, [int $timeout]): int
```php

Sondea un socket de conexión PostgreSQL para comprobar si está listo para lectura y/o escritura. El socket puede obtenerse mediante `pg_socket`. Esta función es útil para implementar flujos de trabajo de consultas no bloqueantes y asíncronos.

## Parámetros

`socket`  
Un recurso de socket obtenido de `pg_socket`.

`read`  
Indica si se debe comprobar si está listo para lectura. Pase `1` para comprobarlo, `0` para omitirlo.

`write`  
Indica si se debe comprobar si está listo para escritura. Pase `1` para comprobarlo, `0` para omitirlo.

`timeout`  
El número máximo de milisegundos a esperar. Pase `-1` para esperar indefinidamente, o `0` para no esperar en absoluto.

## Valores devueltos

Devuelve un valor positivo si el socket está listo, `0` si se alcanzó el tiempo de espera, o `-1` en caso de error.

## Véase también

pg_socket

pg_consume_input

pg_send_query
