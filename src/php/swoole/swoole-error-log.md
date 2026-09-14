---
title: swoole_error_log
description: Escribe los mensajes de error en el registro
source_url: https://www.php.net/manual/es/function.swoole-error-log.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/functions/swoole-error-log.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_revision: f03dfae1d
order: 90490
---

swoole_error_log

Escribe los mensajes de error en el registro

## Descripción

```php
swoole_error_log(int $level, string $msg): void
```php

Escribe los mensajes de error en el registro.

## Parámetros

`level`  
El nivel de registro, las siguientes constantes pueden ser utilizadas: `SWOOLE_LOG_DEBUG`, `SWOOLE_LOG_TRACE`, `SWOOLE_LOG_INFO`, `SWOOLE_LOG_NOTICE`, `SWOOLE_LOG_WARNING`, `SWOOLE_LOG_ERROR`, `SWOOLE_LOG_NONE`

`msg`  
El contenido del mensaje a escribir en el registro.

## Valores devueltos

No se retorna ningún valor.
