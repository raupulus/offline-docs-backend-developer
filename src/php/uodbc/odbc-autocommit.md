---
title: odbc_autocommit
description: Activa el modo de autovalidación
source_url: https://www.php.net/manual/es/function.odbc-autocommit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-autocommit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98630
---

odbc_autocommit

Activa el modo de autovalidación

## Descripción

```php
odbc_autocommit(Odbc\Connection $odbc, [bool $enable]): int
```php

Sin el argumento `enable`, `odbc_autocommit` devuelve el estado de autovalidación

Por omisión, la autovalidación está activada. Desactivar la autovalidación es equivalente a iniciar una transacción.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`enable`  
Si `enable` es `true`, la autovalidación está activada. Si es `false`, la autovalidación está desactivada. Si se pasa `null`, esta función devuelve el estado de autovalidación para `odbc`.

## Valores devueltos

Con un argumento `enable` igual a `null`, `odbc_autocommit` devuelve el estado de autovalidación de la conexión `odbc`. Un valor diferente de 0 si el modo está activado, 0 si no lo está, o `false` si ocurre un error.

Si `enable` no es null, esta función devuelve `true` en caso de éxito, y `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.3.0 | `enable` es ahora nullable. |

## Véase también

`odbc_commit`, `odbc_rollback`
