---
title: Closure::fromCallable
description: Convierte un 'callable' en un cierre
source_url: https://www.php.net/manual/es/closure.fromcallable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/closure/fromcallable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 9c74079f1
order: 3080
---

Closure::fromCallable

Convierte un 'callable' en un cierre

## Descripción

```php
public static Closure::fromCallable(callable $callback): Closure
```php

Crea y devuelve una nueva [función anónima](#functions.anonymous) desde el `callback` dado empleando el ámbito actual. Este método comprueba si `callback` es llamable en el ámbito actual, lanzando un `TypeError` si no lo es.

> [!NOTE]
> A partir de PHP 8.1.0, [Sintaxis de llamada de primera clase](#functions.first_class_callable_syntax) tiene la misma semántica que este método.

## Parámetros

`callback`  
El «callable» a convertir.

## Valores devueltos

Devuelve el recién creado `Closure` o lanza un `TypeError` si `callback` no es llamable en el ámbito actual.

## Véase también

Funciones anónimas

Sintaxis de las llamadas de primera clase
