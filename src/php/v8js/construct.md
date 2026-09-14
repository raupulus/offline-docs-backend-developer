---
title: V8Js::__construct
description: Construye un nuevo objeto V8Js
source_url: https://www.php.net/manual/es/v8js.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/v8js/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_reviewed: false
translation_revision: c44e9cb68
order: 100330
---

V8Js::\_\_construct

Construye un nuevo objeto

V8Js

## Descripción

```php
public V8Js::__construct([string $object_name], [array $variables], [array $extensions], [bool $report_uncaught_exceptions])
```php

Construye un nuevo objeto `V8Js`.

## Parámetros

`object_name`  
El nombre del objeto pasado a Javascript.

`variables`  
Una lista de variables PHP que estarán disponibles en Javascript. Debe ser un `array` asociativo en el formato `array("nombre-para-js" => "nombre-de-la-variable-php")`. Por omisión, un array vacío.

`extensions`  
Lista de extensiones registradas utilizando el método `V8Js::registerExtension`, que deben estar disponibles en el contexto Javascript del objeto `V8Js` creado.

> [!NOTE]
> Las extensiones registradas de tal manera que estén automáticamente activas no necesitan ser listadas en este array. Además, si una extensión tiene dependencias, estas pueden ser omitidas. Por omisión, un array vacío.

`report_uncaught_exceptions`  
Controla si las excepciones Javascript no capturadas se reportan inmediatamente o no. Por omisión, vale `true`. Si se establece en `false`, se puede acceder a la excepción no capturada utilizando el método `V8Js::getPendingException`.
