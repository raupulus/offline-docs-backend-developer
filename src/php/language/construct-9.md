---
title: Exception::__construct
description: Constructor de la excepción
source_url: https://www.php.net/manual/es/exception.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 09c49da6f
order: 3300
---

Exception::\_\_construct

Constructor de la excepción

## Descripción

```php
public Exception::__construct([string $message], [int $code], [Throwable $previous])
```php

Construye el objeto Exception.

## Parámetros

`message`  
Mensaje de la excepción a lanzar.

`code`  
El código de la excepción.

`previous`  
La excepción previa utilizada por la serie de excepciones.

> [!NOTE]
> Llamar al constructor de la clase Exception de una subclase ignora los argumentos por omisión, si las propiedades \$code y \$message ya están establecidas.

## Notas

> [!NOTE]
> `message` *NO* es seguro binariamente.
