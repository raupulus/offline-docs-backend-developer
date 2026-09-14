---
title: session_set_cookie_params
description: Modifica los parámetros de la cookie de sesión
source_url: https://www.php.net/manual/es/function.session-set-cookie-params.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-set-cookie-params.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_revision: 37be0e062
order: 73880
---

session_set_cookie_params

Modifica los parámetros de la cookie de sesión

## Descripción

```php
session_set_cookie_params(int $lifetime_or_options, [string $path], [string $domain], [bool $secure], [bool $httponly]): bool
```php

Firma alternativa disponible a partir de PHP 7.3.0:

```php
session_set_cookie_params(array $lifetime_or_options): bool
```

Modifica los parámetros de configuración de la cookie de sesión, que ha sido configurada en el archivo `php.ini`. El efecto de esta función solo dura durante la ejecución del script actual. Por lo tanto, debe llamarse a `session_set_cookie_params` para cada script y antes de la llamada a `session_start`.

Esta función modifica los parámetros ini correspondientes que pueden ser recuperados mediante `ini_get`.

## Parámetros

`lifetime_or_options`  
Al utilizar la primera firma, la duración de vida de la cookie, en segundos. Ver la directiva [lifetime](#ini.session.cookie-lifetime).

Al utilizar la segunda firma, un `array` asociativo que puede tener como claves `lifetime`, `path`, `domain`, `secure`, `httponly` y `samesite`. Los valores tienen la misma significación que los descritos para los parámetros con el mismo nombre. El valor del elemento `samesite` debe ser `Lax` o `Strict`. Si una opción autorizada no es proporcionada, su valor por defecto será idéntico al valor por defecto de los parámetros explícitos. Si el elemento `samesite` es omitido, entonces el atributo SameSite de la cookie no será definido.

`path`  
La ruta en el dominio donde la cookie será accesible. Utilice una barra simple ('/') para todos los caminos del dominio. Ver la directiva [path](#ini.session.cookie-path).

`domain`  
El dominio de la cookie, por ejemplo 'www.php.net'. Para hacer visibles las cookies en todos los subdominios, el dominio debe ser prefijado con un punto, tal como '.php.net'. Ver la directiva [domain](#ini.session.cookie-domain).

`secure`  
Si `true`, la cookie solo será enviada en una conexión segura. Ver la directiva [secure](#ini.session.cookie-secure).

`httponly`  
Si `true`, PHP intentará enviar la opción httponly durante la configuración de la cookie. Ver la directiva [httponly](#ini.session.cookie-httponly).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `path`, `domain`, `secure` y `httponly` ahora son nullable. |
| 7.3.0 | Se añadió una firma alternativa que soporta un `array` de `lifetime_or_options`. Esta firma soporta la definición del atributo SameSite de la cookie. |
| 7.2.0 | Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Anteriormente la función retornaba [void](#language.types.declarations.void). |

## Véase también

[session.cookie_lifetime](#ini.session.cookie-lifetime), [session.cookie_path](#ini.session.cookie-path), [session.cookie_domain](#ini.session.cookie-domain), [session.cookie_secure](#ini.session.cookie-secure), [session.cookie_httponly](#ini.session.cookie-httponly), [session.cookie_samesite](#ini.session.cookie-samesite), `session_get_cookie_params`
