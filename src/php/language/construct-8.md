---
title: ErrorException::__construct
description: Constructor de la excepción
source_url: https://www.php.net/manual/es/errorexception.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/errorexception/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 09c49da6f
order: 3260
---

ErrorException::\_\_construct

Constructor de la excepción

## Descripción

```php
public ErrorException::__construct([string $message], [int $code], [int $severity], [string $filename], [int $line], [Throwable $previous])
```php

Construye el objeto Exception.

## Parámetros

`message`  
Mensaje de la excepción a lanzar.

`code`  
El código de la excepción.

`severity`  
Nivel de la severidad de la excepción.

> [!NOTE]
> Aunque la severidad puede ser cuaquier valor de tipo `int`, se pretende que se empleen las [constantes de error](#errorfunc.constants).

`filename`  
Nombre del fichero donde se lanzó la excepción.

`line`  
Número de la línea donde se produjo la excepción.

`previous`  
La anterior excepción utilizada para la excepción de encadenamiento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `filename` y `line` ahora son anulables. Anteriormente, sus valores predeterminados eran `__FILE__` y `__LINE__`, respectivamente. |
