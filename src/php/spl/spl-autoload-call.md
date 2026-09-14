---
title: spl_autoload_call
description: Intenta todas las funciones __autoload() registradas para cargar la clase
  solicitada
source_url: https://www.php.net/manual/es/function.spl-autoload-call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-autoload-call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: afb063c84
order: 82250
---

spl_autoload_call

Intenta todas las funciones \_\_autoload() registradas para cargar la clase solicitada

## Descripción

```php
spl_autoload_call(string $class): void
```php

Esta función puede ser utilizada para buscar manualmente una clase, una interfaz, un trait o una enumeración utilizando las funciones registradas \_\_autoload.

## Parámetros

`class`  
El nombre de la clase buscada.

## Valores devueltos

No se retorna ningún valor.
