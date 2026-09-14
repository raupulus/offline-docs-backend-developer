---
title: Fiber::resume
description: Reanuda la ejecución de la fibra con un valor
source_url: https://www.php.net/manual/es/fiber.resume.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/fiber/resume.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3480
---

Fiber::resume

Reanuda la ejecución de la fibra con un valor

## Descripción

```php
public Fiber::resume([mixed $value]): mixed
```php

Reanuda la fibra utilizando el valor dado como resultado de la llamada actual a Fiber::suspend.

Si la fibra no está suspendida al llamar a este método, se lanzará un `FiberError`.

## Parámetros

`value`  
El valor para reanudar la fibra. Este valor será el valor de retorno de la llamada Fiber::suspend en curso.

## Valores devueltos

El valor proporcionado a la próxima llamada a Fiber::suspend o `null` si la fibra retorna. Si la fibra lanza una excepción antes de suspenderse, será lanzada al llamar a este método.
