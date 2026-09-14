---
title: header
description: Envía un encabezado HTTP bruto
source_url: https://www.php.net/manual/es/function.header.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/header.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: 5c1ccc6e2
order: 56390
---

header

Envía un encabezado HTTP bruto

## Descripción

```php
header(string $header, [bool $replace], [int $response_code]): void
```php

`header` permite especificar el encabezado HTTP `string` al enviar los ficheros HTML. Consúltese [`HTTP/1.1 Specification`](https://datatracker.ietf.org/doc/html/rfc2616) para obtener más información sobre los encabezados HTTP.

Nunca se olvide que `header` debe ser llamada antes de que se envíe cualquier contenido, ya sea por líneas HTML habituales en el fichero, o por salidas PHP. Un error muy común es leer un fichero con `include` o `require`, y dejar espacios o líneas vacías, que producirán una salida antes de que la función `header` sea llamada. El mismo problema existe con los ficheros PHP/HTML estándar.

```
<html>
<?php
/* Esto producirá un error. Observe la salida anterior,
 * que se encuentra antes de la llamada a la función header() */
header('Location: http://www.example.com/');
exit;
?>

    
```php

## Parámetros

`header`  
El encabezado.

Existen dos encabezados especiales. El primero comienza con la cadena "`HTTP/`" (insensible a mayúsculas/minúsculas), que se utiliza para indicar el estado HTTP a enviar. Por ejemplo, si se ha configurado Apache para utilizar scripts PHP para manejar las peticiones hacia ficheros inexistentes (utilizando la directiva `ErrorDocument`), asegúrese de que el script genere un código de estado correcto.

```
<?php
// Este ejemplo ilustra el caso especial "HTTP/"
// Alternativas mejores en casos típicos de uso incluyen:
// 1. header($_SERVER["SERVER_PROTOCOL"] . " 404 Not Found");
//    (para sobrescribir mensajes de estado HTTP para clientes que aún usan HTTP/1.0)
// 2. http_response_code(404); (para usar el mensaje por defecto)
header("HTTP/1.1 404 Not Found");
?>

        
```php

El segundo tipo de llamada especial es `"Location:"`. No solo devuelve un encabezado al cliente, sino que además envía un estado `REDIRECT` (302) al navegador siempre que no se haya enviado un código de estado `201` o `3xx`.

```
<?php
header("Location: http://www.example.com/"); /* Redirección del navegador */

/* Asegúrese de que el código siguiente no se ejecute una vez realizada la redirección. */
exit;
?>

        
```php

`replace`  
El argumento opcional `replace` indica si la función `header` debe reemplazar un encabezado previamente enviado, o bien añadir otro encabezado del mismo tipo. Por omisión, un nuevo encabezado sobrescribirá el anterior, pero si se pasa `false` en este argumento, se pueden forzar múltiples encabezados para un mismo tipo de encabezado. Por ejemplo:

```
<?php
header('WWW-Authenticate: Negotiate');
header('WWW-Authenticate: NTLM', false);
?>

        
```php

`response_code`  
Fuerza el código de respuesta HTTP al valor especificado. Tenga en cuenta que este argumento solo tiene efecto si `header` no está vacío.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Cuando falla el intento de enviar un encabezado, `header` genera un error de nivel `E_WARNING`.

## Ejemplos

Caja de descarga

Si se desea que los usuarios reciban una alerta para guardar los ficheros generados, como si se genera un fichero PDF, se puede utilizar el encabezado [Content-Disposition](https://datatracker.ietf.org/doc/html/rfc2183) para proporcionar un nombre de fichero por defecto, a mostrar en el diálogo de guardado.

```
<?php
// Se desea mostrar un pdf
header('Content-Type: application/pdf');

// Será nombrado downloaded.pdf
header('Content-Disposition: attachment; filename="downloaded.pdf"');

// El origen del PDF original.pdf
readfile('original.pdf');
?>

    
```php

Directivas concernientes a la caché

Los scripts PHP generan a menudo HTML dinámico, que no debe ser almacenado en caché, ni por el cliente, ni por los proxy intermedios. Se puede forzar la desactivación de la caché de muchos clientes y proxy con:

```
<?php
header("Cache-Control: no-cache, must-revalidate"); // HTTP/1.1
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT"); // Fecha en el pasado
?>

    
```php

> [!NOTE]
> Puede darse cuenta de que sus páginas nunca son almacenadas en caché incluso si se utilizan todos los encabezados anteriores. Existe toda una colección de parámetros que los usuarios pueden modificar en su navegador para cambiar el comportamiento por defecto de la caché. Al enviar los encabezados anteriores, se pueden imponer sus propias valores.
>
> Además, los parámetros `session_cache_limiter` y `session.cache_limiter` pueden ser utilizados para generar los encabezados de caché correctos, cuando se utilizan sesiones.

Configurar una cookie

`setcookie` ofrece un medio práctico de configurar cookies. Para definir una cookie con atributos no soportados por `setcookie`, `header` puede ser utilizado.

Por ejemplo, el código siguiente define una cookie que incluye un atributo `Partitioned`.

```
<?php
header('Set-Cookie: name=value; Secure; Path=/; SameSite=None; Partitioned;');
?>

    
```php

## Notas

> [!NOTE]
> Los encabezados solo serán accesibles y se mostrarán cuando se utilice un SAPI que los soporte.

> [!NOTE]
> Se puede utilizar el sistema de caché (output buffering) para evitar este problema. Todo el texto generado será almacenado en buffer en el servidor hasta que se envíe. Se pueden utilizar las funciones `ob_start` y `ob_end_flush` en los scripts, o modificando la directiva de configuración `output_buffering` en el fichero `php.ini` o los ficheros de configuración del servidor.

> [!NOTE]
> El código de estado HTTP debe ser siempre el primero en enviarse al cliente, en relación con la actual `header` que puede ser el primero o no. El estado puede ser sobrescrito llamando a `header` con un nuevo estado en cualquier momento, incluso si el encabezado HTTP ya ha sido enviado.

> [!NOTE]
> La mayoría de los clientes modernos aceptan URIs relativas como argumento de [Location:](http://tools.ietf.org/html/rfc7231#section-7.1.2), pero algunos clientes más antiguos exigen una URI absoluta incluyendo el protocolo, el host y la ruta absoluta. Se puede utilizar generalmente las variables globales `$_SERVER['HTTP_HOST']`, `$_SERVER['PHP_SELF']` y `dirname` para construir una URI absoluta:
>
> <div class="informalexample">
>
> ```
> <?php
> /* Redirección hacia una página diferente del mismo directorio */
> $host  = $_SERVER['HTTP_HOST'];
> $uri   = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');
> $extra = 'mypage.php';
> header("Location: http://$host$uri/$extra");
> exit;
> ?>
>
>      
> ```
>
> </div>

> [!NOTE]
> El ID de sesión no es pasado con el encabezado Location incluso si [session.use_trans_sid](#ini.session.use-trans-sid) está activado. Debe ser pasado manualmente utilizando la constante `SID`.

## Véase también

`headers_sent`, `setcookie`, `http_response_code`, `header_remove`, `headers_list`, La sección sobre la'[autenticación HTTP](#features.http-auth)
