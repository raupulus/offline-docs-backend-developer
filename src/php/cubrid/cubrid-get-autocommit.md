---
title: cubrid_get_autocommit
description: Recupera el modo auto-commit de la conexión
source_url: https://www.php.net/manual/es/function.cubrid-get-autocommit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get-autocommit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9050
---

cubrid_get_autocommit

Recupera el modo auto-commit de la conexión

## Descripción

```php
cubrid_get_autocommit(resource $conn_identifier): bool
```php

La función `cubrid_get_autocommit` se utiliza para recuperar el estado del modo auto-commit de la conexión a la base de datos CUBRID.

En CUBRID 8.4.0, el modo auto-commit está desactivado por omisión para la gestión de las transacciones.

En CUBRID 8.4.1, el modo auto-commit está activado por omisión para la gestión de las transacciones.

## Parámetros

`conn_identifier`  
Identificador de conexión.

## Valores devueltos

`true`, cuando el modo auto-commit está activo.

`false`, cuando el modo auto-commit está inactivo.

`null` Si ocurre un error.

## Véase también

cubrid_set_autocommit

cubrid_commit
