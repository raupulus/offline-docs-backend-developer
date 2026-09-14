---
title: session_encode
description: Codifica los datos de sesión
source_url: https://www.php.net/manual/es/function.session-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 35b95a56c
order: 73780
---

session_encode

Codifica los datos de sesión

## Descripción

```php
session_encode(): string
```php

`session_encode` devuelve un string serializado que contiene las variables de la sesión actual codificadas almacenadas en la variable superglobal \$\_SESSION.

Por omisión, el método de serialización utilizado es interno a PHP, y no es el mismo que `serialize`. El método de serialización puede ser definido utilizando la opción de configuración [session.serialize_handler](#ini.session.serialize-handler).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido codificado de la sesión actual, o `false` si ocurre un error.

## Notas

> [!WARNING]
> Se debe llamar a la función `session_start` antes de utilizar la función `session_encode`.

## Véase también

`session_decode`, [session.serialize_handler](#ini.session.serialize-handler)
