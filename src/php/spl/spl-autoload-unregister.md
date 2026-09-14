---
title: spl_autoload_unregister
description: Elimina una función dada de la implementación __autoload()
source_url: https://www.php.net/manual/es/function.spl-autoload-unregister.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-autoload-unregister.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: e5c8e7add
order: 82290
---

spl_autoload_unregister

Elimina una función dada de la implementación \_\_autoload()

## Descripción

```php
spl_autoload_unregister(callable $callback): bool
```php

Elimina una función de la pila autoload. Si la pila está activa y vacía después de eliminar la función dada, entonces será desactivada.

Cuando esta función activa una pila autoload, todas las funciones \_\_autoload existentes no serán reactivadas.

## Parámetros

`callback`  
La función autoload a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Pasar la función `spl_autoload_call` como argumento callback para desregistrar todos los autoloaders ha quedado obsoleto. En su lugar, iterar sobre el valor de retorno de `spl_autoload_functions` y llamar a `spl_autoload_unregister` para cada valor. |
