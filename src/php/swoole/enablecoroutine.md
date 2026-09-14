---
title: Swoole\Runtime::enableCoroutine
description: Habilitar corrutinas para funciones específicas
source_url: https://www.php.net/manual/es/swoole-runtime.enable-coroutine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/runtime/enableCoroutine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: f03cb84c3
order: 92460
---

Swoole\Runtime::enableCoroutine

Habilitar corrutinas para funciones específicas

## Descripción

```php
public static Swoole\Runtime::enableCoroutine([int $flags]): void
```php

Este método habilita el soporte de corrutinas para funciones PHP específicas según los flags proporcionados. Debe ser llamado una vez al inicio de la aplicación.

## Parámetros

`flags`  
Máscara de bits de flags que especifica qué funciones se deben interceptar. Puede combinarse usando el operador \|. Flags disponibles: `SWOOLE_HOOK_TCP`, `SWOOLE_HOOK_UDP`, `SWOOLE_HOOK_UNIX`, `SWOOLE_HOOK_UDG`, `SWOOLE_HOOK_SSL`, `SWOOLE_HOOK_TLS`, `SWOOLE_HOOK_SLEEP`, `SWOOLE_HOOK_FILE`, `SWOOLE_HOOK_STREAM_FUNCTION`, `SWOOLE_HOOK_BLOCKING_FUNCTION`, `SWOOLE_HOOK_PROC`, `SWOOLE_HOOK_CURL`, `SWOOLE_HOOK_NATIVE_CURL`, `SWOOLE_HOOK_SOCKETS`, `SWOOLE_HOOK_STDIO`, `SWOOLE_HOOK_PDO_PGSQL`, `SWOOLE_HOOK_PDO_ODBC`, `SWOOLE_HOOK_PDO_ORACLE`, `SWOOLE_HOOK_PDO_SQLITE`, o `SWOOLE_HOOK_ALL` para todos los flags.

## Valores devueltos

No se retorna ningún valor.
