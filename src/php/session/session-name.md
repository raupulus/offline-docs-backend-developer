---
title: session_name
description: Lee y/o modifica el nombre de la sesión
source_url: https://www.php.net/manual/es/function.session-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: d7a77b5f8
order: 73830
---

session_name

Lee y/o modifica el nombre de la sesión

## Descripción

```php
session_name([string $name]): string
```php

`session_name` devuelve el nombre de la sesión actual. Si se proporciona el argumento `name`, `session_name` modificará el nombre de la sesión y devolverá el *anterior* nombre de la sesión.

Si se proporciona un nuevo nombre de sesión `name`, `session_name` modifica la cookie HTTP (y el contenido de salida cuando [session.transid](#ini.session.use-trans-sid) está activado). Una vez enviada la cookie HTTP, llamar a `session_name` desencadena un `E_WARNING`. `session_name` debe ser llamado antes de `session_start` para que la sesión funcione correctamente.

El nombre de la sesión se reinicia al valor por defecto, almacenado en `session.name` al inicio. Por lo tanto, debe llamarse a `session_name` para cada petición (y antes de que `session_start` sea llamado).

## Parámetros

`name`  
El nombre de sesión se utiliza como nombre para las cookies y las URLs (es decir, `PHPSESSID`). Solo debe contener caracteres alfanuméricos; debe ser corto y descriptivo (especialmente para los usuarios que tienen activada la alerta de cookies). Si `name` se proporciona y no es `null`, el nombre de la sesión actual será reemplazado por este valor.

> [!WARNING]
> Los nombres de sesión no pueden contener solo números, al menos una letra debe estar presente. De lo contrario, se generará un identificador de sesión cada vez.

## Valores devueltos

Devuelve el nombre de la sesión actual. Si se proporciona el argumento `name` y la función actualiza el nombre de la sesión, entonces el *anterior* nombre de sesión será devuelto, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `name` ahora es nullable. |
| 7.2.0 | `session_name` verifica el estado de la sesión, anteriormente solo verificaba el estado de la cookie. Por lo tanto, las versiones anteriores de `session_name` permiten la llamada a `session_name` después de `session_start` lo que puede causar el fallo de PHP y puede dar lugar a comportamientos extraños. |

## Ejemplos

Ejemplo con `session_name`

```
<?php

/* elige el nombre de sesión: WebsiteID */

$previous_name = session_name("WebsiteID");

echo "El nombre anterior de la sesión era $previous_name<br />";
?>

    
```php

## Véase también

La directiva de configuración [session.name](#ini.session.name)
