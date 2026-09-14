---
title: session_write_close
description: Escribe los datos de sesión y cierra la sesión
source_url: https://www.php.net/manual/es/function.session-write-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-write-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 35b95a56c
order: 73930
---

session_write_close

Escribe los datos de sesión y cierra la sesión

## Descripción

```php
session_write_close(): bool
```php

Finaliza la sesión actual, después de almacenar los datos.

Los datos de sesión se almacenan generalmente al final del script, automáticamente, sin necesidad de llamar explícitamente a `session_write_close`. Pero durante toda la ejecución del script, los datos de sesión están bloqueados en escritura, y un solo script puede operar sobre la sesión a la vez. Cuando se utilizan frames con sesiones, esto se nota al ver cómo las frames se actualizan una tras otra. Puede reducirse el tiempo de cálculo de estas páginas cerrando la sesión tan pronto como sea posible, lo que libera los datos para otros scripts.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El tipo de retorno de esta función es ahora `bool`. Anteriormente, era [void](#language.types.declarations.void). |

## Véase también

`session_register_shutdown`
