---
title: eio_grp_limit
description: Establecer el límite de un grupo
source_url: https://www.php.net/manual/es/function.eio-grp-limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-grp-limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16890
---

eio_grp_limit

Establecer el límite de un grupo

## Descripción

```php
eio_grp_limit(resource $grp, int $limit): void
```php

Número límite de peticiones en un grupo de peticiones.

## Parámetros

`grp`  
El recurso de grupo de peticiones.

`limit`  
El número de peticiones del grupo.

## Valores devueltos

No se retorna ningún valor.

## Véase también

eio_grp_add
