---
title: UI\Executor::setInterval
description: Manipulación de intervalos
source_url: https://www.php.net/manual/es/ui-executor.setinterval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ui/ui/executor/setinterval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ui
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 97720
---

UI\Executor::setInterval

Manipulación de intervalos

## Descripción

```php
public UI\Executor::setInterval(int $microseconds): bool
```php

```php
public UI\Executor::setInterval(int $seconds, int $microseconds): bool
```

Define el nuevo intervalo. Un intervalo de 0 pondrá en pausa el ejecutor hasta que se defina un nuevo intervalo.

## Parámetros

`seconds`  

`microseconds`  

## Valores devueltos

Indicación de éxito
