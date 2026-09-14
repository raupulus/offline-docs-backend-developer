---
title: db2_free_stmt
description: Liberar un recurso indicado
source_url: https://www.php.net/manual/es/function.db2-free-stmt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-free-stmt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30900
---

db2_free_stmt

Liberar un recurso indicado

## Descripción

```php
db2_free_stmt(resource $stmt): bool
```php

Libera los recursos del Sistema y de la Base de Datos que están asociados con un determinado recurso (de sentencias). Los recursos son liberados automáticamente cuando un script finaliza, pero se puede llamar a `db2_free_stmt` para liberarlos en ese momento y no hasta que el script finalice.

## Parámetros

`stmt`  
Un recurso (de sentencias) válido.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

db2_free_result
