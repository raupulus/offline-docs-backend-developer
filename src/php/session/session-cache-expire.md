---
title: session_cache_expire
description: Obtiene y/o define el tiempo de expiración de la caché
source_url: https://www.php.net/manual/es/function.session-cache-expire.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-cache-expire.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 151e61773
order: 73720
---

session_cache_expire

Obtiene y/o define el tiempo de expiración de la caché

## Descripción

```php
session_cache_expire([int $value]): int
```php

`session_cache_expire` devuelve la configuración actual de `session.cache_expire`.

El tiempo de expiración de la caché se reestablece a su valor por omisión de 180, almacenado en [session.cache_limiter](#ini.session.cache-expire), al inicio de la petición. Por lo tanto, debe llamarse `session_cache_expire` en cada petición (y antes de que `session_start` sea llamada).

## Parámetros

`value`  
Si `value` es proporcionado y no `null`, la configuración actual de cache expire será reemplazada por `value`.

> [!NOTE]
> La directiva `value` solo tiene efecto si `session.cache_limiter` tiene un valor *diferente* de `nocache`.

## Valores devueltos

Devuelve la configuración actual de `session.cache_expire`. El valor devuelto debe leerse en minutos, y por omisión, es 180. En caso de fallo al modificar el valor, `false` es devuelto.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `value` ahora es nullable. |

## Ejemplos

Ejemplo con `session_cache_expire`

```
<?php

/* Configura el limitador de caché a 'private' */

session_cache_limiter('private');
$cache_limiter = session_cache_limiter();

/* Configura el tiempo de expiración a 30 minutos */
session_cache_expire(30);
$cache_expire = session_cache_expire();

/* Inicia la sesión */

session_start();

echo "El limitador de caché ahora está fijado a $cache_limiter<br />";
echo "La sesión en caché expirará después de $cache_expire minutos";
?>

    
```php

## Véase también

[session.cache_expire](#ini.session.cache-expire), [session.cache_limiter](#ini.session.cache-limiter), `session_cache_limiter`
