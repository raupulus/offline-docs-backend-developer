---
title: UI\Executor::__construct
description: Construye un nuevo ejecutor
source_url: https://www.php.net/manual/es/ui-executor.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/executor/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 97690
---

UI\Executor::\_\_construct

Construye un nuevo ejecutor

## Descripción

```php
public UI\Executor::__construct()
```php

```php
public UI\Executor::__construct(int $microseconds)
```

```php
public UI\Executor::__construct(int $seconds, int $microseconds)
```php

Construye un ejecutor con el intervalo dado, no empezará a ejecutarse hasta que se entre en el bucle principal

## Parámetros

`seconds`  
El número de segundos entre ejecuciones

`microseconds`  
El número de microsegundos entre ejecuciones
