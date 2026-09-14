---
title: session_cache_limiter
description: Lee y/o modifica el limitador de caché de sesión
source_url: https://www.php.net/manual/es/function.session-cache-limiter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/session/functions/session-cache-limiter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: session
translation_status: ready
translation_reviewed: true
translation_revision: 1cef066aa
order: 73730
---

session_cache_limiter

Lee y/o modifica el limitador de caché de sesión

## Descripción

```php
session_cache_limiter([string $value]): string
```php

`session_cache_limiter` devuelve la configuración actual del limitador de caché.

El limitador de caché controla los encabezados HTTP enviados al cliente. Algunos encabezados determinan las reglas de almacenamiento en caché de la página en el navegador. Al configurar este limitador a `nocache`, por ejemplo, el navegador no almacenará la página en su caché. El valor `public`, en cambio, permitirá el almacenamiento en caché. El valor `private` desactiva la caché para el proxy y autoriza al cliente a almacenar en caché el contenido.

En modo `private`, el encabezado Expire enviado al cliente puede causar problemas en algunos navegadores, como, por ejemplo, Mozilla. Este problema puede evitarse con el modo `private_no_expire`. El encabezado `Expire` nunca se envía al navegador para este modo.

El hecho de definir el limitador de caché a la valor `''` desactivará automáticamente y por completo el envío de los encabezados de caché.

El limitador de caché se restablece al valor por defecto de [`session.cache_limiter`](#ini.session.cache-limiter) en cada inicio de script PHP. Por lo tanto, deberá llamarse a `session_cache_limiter` en cada página, y antes de `session_start`.

## Parámetros

`value`  
Si `value` se proporciona y no es `null`, el limitador de caché se reconfigura con este valor.

<table>
<caption>Valores posibles</caption>
<thead>
<tr>
<th>Valores</th>
<th>Encabezados enviados</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>public</code></td>
<td><pre role="header"><code>Expires: (Algo en el futuro, según session.cache_expire)
Cache-Control: public, max-age=(Algo en el futuro, según session.cache_expire)
Last-Modified: (el timestamp del script actual)
&#10;           </code></pre></td>
</tr>
<tr>
<td><code>private_no_expire</code></td>
<td><pre role="header"><code>Cache-Control: private, max-age=(session.cache_expire en el futuro)
Last-Modified: (el timestamp del script actual)
&#10;           </code></pre></td>
</tr>
<tr>
<td><code>private</code></td>
<td><pre role="header"><code>Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: private, max-age=(session.cache_expire en el futuro)
Last-Modified: (el timestamp del script actual)
&#10;           </code></pre></td>
</tr>
<tr>
<td><code>nocache</code></td>
<td><pre role="header"><code>Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
&#10;           </code></pre></td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve el nombre del limitador de caché actual. En caso de error, se devuelve `false`.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `value` ahora es nullable. |

## Ejemplos

Ejemplo con `session_cache_limiter`

```
<?php

/* configura el limitador de caché a 'private' */

session_cache_limiter('private');
$cache_limiter = session_cache_limiter();

echo "El limitador de caché ahora vale $cache_limiter<br />";
?>

    
```php

## Véase también

[session.cache_limiter](#ini.session.cache-limiter)
