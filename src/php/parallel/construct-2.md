---
title: parallel\Runtime::__construct
description: Construcción de la ejecución
source_url: https://www.php.net/manual/es/parallel-runtime.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel/runtime/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60180
---

parallel\Runtime::\_\_construct

Construcción de la ejecución

## Descripción

```php
public parallel\Runtime::__construct()
```php

Construye una ejecución sin cargador automático.

```php
public parallel\Runtime::__construct(string $bootstrap)
```

Construye una ejecución amorcada.

## Parámetros

`bootstrap`  
La localización de un fichero de amorce, generalmente un cargador automático.

## Excepciones

> [!WARNING]
> Lanza una `parallel\Runtime\Error` si el hilo no ha podido ser creado.

> [!WARNING]
> Lanza una `parallel\Runtime\Bootstrap` si el amorce ha fallado.
