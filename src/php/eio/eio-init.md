---
title: eio_init
description: (Re-)inicializa Eio
source_url: https://www.php.net/manual/es/function.eio-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_reviewed: false
translation_revision: 4e5389401
order: 16910
---

eio_init

(Re-)inicializa Eio

## Descripción

```php
eio_init(): void
```php

`eio_init` (re-)inicializa Eio. Asigna memoria para estructuras internas de libeio y Eio. Se puede llamar a `eio_init` antes de usar las funciones de Eio. De otro modo, será invocada internamente la primera vez que se invoque a una función de Eio en un proceso.

> [!NOTE]
> Esta función fue eliminada en la versión 3.0.0RC1 de la extensión eio para PHP versión 8 y superiores.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.
