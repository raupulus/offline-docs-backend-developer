---
title: cubrid_set_autocommit
description: Define el modo auto-commit para la conexión
source_url: https://www.php.net/manual/es/function.cubrid-set-autocommit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-set-autocommit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 9490
---

cubrid_set_autocommit

Define el modo auto-commit para la conexión

## Descripción

```php
cubrid_set_autocommit(resource $conn_identifier, bool $mode): bool
```php

La función `cubrid_set_autocommit` se utiliza para definir el modo auto-commit para la conexión a la base de datos CUBRID.

En CUBRID PHP, el modo auto-commit está desactivado por omisión para la gestión de transacciones. Cuando el modo auto-commit pasa de Off a On, todos los trabajos pendientes son automáticamente validados.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`mode`  
El modo auto-commit. Las constantes siguientes pueden ser utilizadas:

CUBRID_AUTOCOMMIT_FALSE

CUBRID_AUTOCOMMIT_TRUE

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

cubrid_get_autocommit

cubrid_commit
