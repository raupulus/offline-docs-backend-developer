---
title: odbc_pconnect
description: Abre una conexión de base de datos persistente
source_url: https://www.php.net/manual/es/function.odbc-pconnect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-pconnect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_revision: c68bcb2af
order: 98980
---

odbc_pconnect

Abre una conexión de base de datos persistente

## Descripción

```php
#[\SensitiveParameter] odbc_pconnect(string $dsn, [string $user], [string $password], [int $cursor_option]): Odbc\Connection
```php

Abre una conexión de base de datos persistente.

Esta función es similar a `odbc_connect`, excepto que la conexión no se cierra realmente cuando el script ha terminado. Las futuras solicitudes de conexión con la misma combinación de `dsn`, `user`, `password` (a través de `odbc_connect` y `odbc_pconnect`) pueden reutilizar la conexión persistente.

## Parámetros

Consulte `odbc_connect` para obtener detalles.

## Valores devueltos

Devuelve una conexión ODBC, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Connection`; anteriormente, se devolvía un `resource`. |
| 8.4.0 | `user` y `password` ahora pueden ser nulos, también son opcionales y valen por defecto `null`. |
| 8.4.0 | Anteriormente, el uso de una cadena vacía para `password` no incluía `pwd` en la cadena de conexión generada para `dsn` . Ahora, `pwd` se incluye en la cadena de conexión, con un valor de cadena vacía. Para restaurar el comportamiento anterior, `password` puede ser definido como `null`. |
| 8.4.0 | Anteriormente, si `dsn` contenía `uid` o `pwd` , entonces los parámetros `user` y `password` eran ignorados. Ahora, `user` solo es ignorado si `dsn` contiene `uid`, y `password` solo es ignorado si `dsn` contiene `pwd`. |

## Notas

> [!NOTE]
> Las conexiones persistentes no tienen efecto si PHP se usa como un programa CGI.

## Véase también

`odbc_connect`, [Conexiones de base de datos persistentes](#features.persistent-connections)
