---
title: eio_grp_cancel
description: Cancelar un grupo de peticiones
source_url: https://www.php.net/manual/es/function.eio-grp-cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-grp-cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16880
---

eio_grp_cancel

Cancelar un grupo de peticiones

## Descripción

```php
eio_grp_cancel(resource $grp): void
```php

`eio_grp_cancel` cancela un grupo de peticiones especificadas por el recurso de grupo de peticiones `grp`.

## Parámetros

`grp`  
El recurso de grupo de peticiones devuelto por `eio_grp`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

eio_grp

eio_grp_add
