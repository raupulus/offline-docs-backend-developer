---
title: PDO::inTransaction
description: Verifica si se encuentra en una transacción
source_url: https://www.php.net/manual/es/pdo.intransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/intransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 661e6858a
order: 61910
---

PDO::inTransaction

Verifica si se encuentra en una transacción

## Descripción

```php
public PDO::inTransaction(): bool
```php

Verifica si una transacción está actualmente activa en el driver. Este método solo funciona para los drivers de bases de datos que soportan transacciones.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si una transacción está actualmente activa, `false` en caso contrario.
