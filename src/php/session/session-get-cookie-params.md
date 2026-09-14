---
title: session_get_cookie_params
description: Lee la configuración del cookie de sesión
source_url: https://www.php.net/manual/es/function.session-get-cookie-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-get-cookie-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 35b95a56c
order: 73800
---

session_get_cookie_params

Lee la configuración del cookie de sesión

## Descripción

```php
session_get_cookie_params(): array
```php

Lee la configuración del cookie de sesión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array, que contiene los siguientes elementos:

- ["`lifetime`"](#ini.session.cookie-lifetime): duración de vida del cookie.

- ["`path`"](#ini.session.cookie-path): la ruta donde se almacenan las informaciones.

- ["`domain`"](#ini.session.cookie-domain): el dominio del cookie.

- ["`secure`"](#ini.session.cookie-secure): el cookie debe ser enviado solo en conexiones seguras.

- ["`httponly`"](#ini.session.cookie-httponly): el cookie será accesible solo vía el protocolo HTTP.

- ["`samesite`"](#ini.session.cookie-samesite): Controla el envío entre dominio (cross-domain) del cookie.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 7.3.0   | La entrada "`samesite`" ha sido añadida en el array devuelto. |

## Véase también

[session.cookie_lifetime](#ini.session.cookie-lifetime), [session.cookie_path](#ini.session.cookie-path), [session.cookie_domain](#ini.session.cookie-domain), [session.cookie_secure](#ini.session.cookie-secure), [session.cookie_httponly](#ini.session.cookie-httponly), [session.cookie_samesite](#ini.session.cookie-samesite), `session_set_cookie_params`
