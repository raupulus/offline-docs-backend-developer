---
title: setcookie
description: Envía una cookie
source_url: https://www.php.net/manual/es/function.setcookie.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/setcookie.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_revision: 6122a8317
order: 56530
---

setcookie

Envía una cookie

## Descripción

```php
setcookie(string $name, [string $value], [int $expires_or_options], [string $path], [string $domain], [bool $secure], [bool $httponly]): bool
```php

Firma alternativa disponible a partir de PHP 7.3.0 (no soportado con parámetros nombrados):

```php
setcookie(string $name, [string $value], [array $options]): bool
```

`setcookie` define una cookie que será enviada junto con el resto de los encabezados HTTP. Al igual que con otros encabezados, las cookies deben ser enviadas *antes* de cualquier salida del script (esto es una restricción del protocolo HTTP). Esto requiere que esta función sea llamada antes de cualquier salida, incluyendo las etiquetas `<html>` y `<head>` así como cualquier espacio en blanco.

Una vez que las cookies han sido establecidas, estarán disponibles durante el próximo cargado de página en el array `$_COOKIE`. Los valores de las cookies también pueden existir en la variable `$_REQUEST`.

## Parámetros

La [RFC 6265](https://datatracker.ietf.org/doc/html/rfc6265) es la referencia para la interpretación de los argumentos pasados a `setcookie`.

`name`  
El nombre de la cookie.

`value`  
El valor de la cookie. Este valor se almacena en el ordenador del cliente; no se deben almacenar información importante. Si el argumento `name` vale `'cookiename'`, este valor es recuperado con `$_COOKIE['cookiename']`.

`expires_or_options`  
El tiempo después del cual la cookie expira. Esto es un timestamp Unix, por lo tanto, será un número de segundos desde la época Unix (1 de enero de 1970). Una forma de definir este valor es añadiendo el número de segundos antes de que la cookie expire al resultado de una llamada a `time`. Por ejemplo `time()+60*60*24*30` configurará la cookie para que expire en 30 días. Otra posibilidad es utilizar la función `mktime`. Si no se especifica este argumento o si vale 0, la cookie expirará al final de la sesión (cuando el navegador se cierre).

> [!NOTE]
> El parámetro `expires_or_options` toma una marca de tiempo Unix, a diferencia del formato de fecha `Wdy, DD-Mon-YYYY HH:MM:SS GMT`, porque PHP realiza esta conversión internamente.

`path`  
La ruta en el servidor donde la cookie estará disponible. Si el valor es `'/'`, la cookie estará disponible en todo el dominio `domain`. Si el valor es `'/foo/'`, la cookie estará únicamente disponible en el directorio `/foo/` así como todos sus subdirectorios como `/foo/bar/` en el dominio `domain`. El valor por omisión es el directorio actual donde la cookie fue definida.

`domain`  
El (sub-)dominio para el cual la cookie está disponible. Definir esto a un subdominio (tal como `'www.example.com'`) hará que la cookie esté disponible para este subdominio así como todos sus subdominios (por ejemplo: w2.www.example.com). Para hacer que la cookie esté disponible en todo el dominio (así como todos sus subdominios), simplemente defina el valor con el nombre de dominio (`'example.com'`, en este ejemplo).

Los navegadores antiguos que continúan implementando la [RFC 2109](https://datatracker.ietf.org/doc/html/rfc2109) (obsoleta) pueden requerir un `.` para hacer disponible todos los subdominios.

`secure`  
Indica si la cookie debe ser transmitida únicamente a través de una conexión segura HTTPS desde el cliente. Cuando este argumento vale `true`, la cookie solo será enviada si la conexión es segura. Del lado del servidor, es responsabilidad del desarrollador enviar este tipo de cookie únicamente en conexiones seguras (por ejemplo, utilizando la variable `$_SERVER["HTTPS"]`).

`httponly`  
Cuando este argumento vale `true`, la cookie solo será accesible por el protocolo HTTP. Esto significa que la cookie no será accesible vía lenguajes de script, como Javascript. Se ha sugerido que esta configuración permite limitar ataques XSS (aunque no es soportada por todos los navegadores), sin embargo este hecho es frecuentemente cuestionado. `true` o `false`

`options`  
Un `array` asociativo que puede tener como claves `expires`, `path`, `domain`, `secure`, `httponly` y `samesite`.

Los valores tienen el mismo significado que los descritos para los argumentos con el mismo nombre. El valor del elemento `samesite` debe ser `None`, `Lax` o `Strict`. Si una opción autorizada no es dada, entonces su valor por omisión será idéntico al valor por omisión de los argumentos explícitos. Si el elemento `samesite` es omitido, entonces el atributo SameSite de la cookie no será definido.

> [!NOTE]
> Para definir una cookie que incluye atributos que no figuran entre las claves listadas, utilice `header`.

> [!NOTE]
> Si `samesite` es `"None"`, entonces `secure` también debe estar habilitado o el cliente bloqueará la cookie.

## Valores devueltos

Si algo fue enviado a la salida estándar antes de la llamada a esta función, `setcookie` fallará y retornará `false`. Si `setcookie` tiene éxito, retornará `true`. Esto no indica si el cliente acepta o no la cookie.

## Errores/Excepciones

Si el `array` `options` contiene claves no soportadas:

- Antes de PHP 8.0.0, se generaba un `E_WARNING`.

- A partir de PHP 8.0.0, se lanza una ValueError.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La fecha de la cookie está en formato `'D, d M Y H:i:s \G\M\T'`; previamente era `'D, d-M-Y H:i:s T'`. |
| 8.0.0 | Pasar claves no soportadas ahora lanza una ValueError en lugar de emitir un `E_WARNING`. |
| 7.3.0 | Se añadió una firma alternativa que soporta un array de `options`. Esta firma soporta la definición del atributo SameSite de la cookie. |

## Ejemplos

Los efectos de los siguientes ejemplos se pueden observar utilizando la lista de cookies de las herramientas para desarrolladores del navegador (normalmente en la pestaña Almacenamiento o Aplicación).

Ejemplo de envío de una cookie con `setcookie`

```php
<?php

$value = 'Valor de prueba';

// Establecer una "cookie de sesión" que caduca cuando se cierra el navegador
setcookie("TestCookie", $value);
// Establecer una cookie que expira en 1 hora
setcookie("TestCookie", $value, time()+3600);
// Establecer una cookie que se aplique solo a una ruta específica en un dominio específico.
// Tenga en cuenta que el dominio utilizado debe coincidir con el dominio del sitio.
setcookie("TestCookie", $value, time()+3600, "/~rasmus/", "example.com", true);
?>

   
```

Tenga en cuenta que PHP codificará y decodificará automáticamente la parte del valor de la cookie. Esto se puede evitar usando `setrawcookie`.

Para ver el contenido de las cookies configuradas en el ejemplo anterior en una solicitud posterior:

```php
<?php
// Mostrar una cookie
echo $_COOKIE["TestCookie"];

// Otro método para mostrar todas las cookies
print_r($_COOKIE);
?>

   
```

Ejemplo de borrado de una cookie con `setcookie`

Para eliminar una cookie, configure la fecha de expiración en un valor del pasado (pero no cero, que está reservado para las cookies de sesión).

Para eliminar las cookies establecidas en el ejemplo anterior:

```php
<?php
// Define la fecha de expiración a una hora antes de la fecha actual
setcookie("TestCookie", "", time() - 3600);
setcookie("TestCookie", "", time() - 3600, "/~rasmus/", "example.com", 1);
?>

   
```

`setcookie` y los arrays

Se puede establecer un "array de cookies" usando la notación de array en el nombre de la cookie. Esto permite configurar tantas cookies como elementos haya en el array, pero cuando el script recibe la cookie, todos los valores se colocan en un array con el nombre de la cookie:

```php
<?php
// Establece las cookies
setcookie("cookie[three]", "cookiethree");
setcookie("cookie[two]", "cookietwo");
setcookie("cookie[one]", "cookieone");

// Después del recargado de la página, las mostramos
if (isset($_COOKIE['cookie'])) {
    foreach ($_COOKIE['cookie'] as $name => $value) {
        $name = htmlspecialchars($name);
        $value = htmlspecialchars($value);
        echo "$name : $value <br />\n";
    }
}
?>

   
```

El ejemplo anterior mostrará:

    three : cookiethree
    two : cookietwo
    one : cookieone

> [!NOTE]
> El uso de caracteres de separación como `[` y `]` como parte del nombre de la cookie no es respetuoso con la RFC 6265, sección 4, pero se asume que es soportado por los agentes de usuario, siguiendo la RFC 6265, sección 5.

## Notas

> [!NOTE]
> El almacenamiento en búfer de salida permite la salida del script antes de llamar a esta función. Toda la salida se almacenará en búfer hasta que se vacíe (ya sea explícitamente o al final de la ejecución del script). Puede hacer esto llamando a `ob_start` y `ob_end_flush` en ek script, o activando la directiva `output_buffering` en su archivo de configuración `php.ini` o en el archivo de configuración de su servidor.

Errores comunes:

- Las cookies solo serán accesibles al cargar la próxima página, o al recargar la página actual. Para probar si una cookie ha sido definida con éxito, verifique la presencia de la cookie en el próximo cargado de página antes de que la cookie expire. El tiempo de expiración se define utilizando el argumento `expires_or_options`. Una forma sencilla de verificar el posicionamiento de la cookie es utilizar `print_r($_COOKIE);`.

- Las cookies deben ser borradas con los mismos argumentos que los utilizados durante su creación. Si el argumento `value` es una cadena vacía y los otros argumentos son exactamente los mismos que en una llamada `setcookie` previa, entonces la cookie será borrada del cliente. Internamente, el borrado se realiza posicionando el valor a `'deleted'` y la fecha de expiración a un año en el pasado.

- Dado que la asignación de un valor valiendo `false` a una cookie intentará borrarla, no se deben utilizar valores booleanos. En su lugar, utilice *0* para `false` y *1* para `true`.

- Los nombres de las cookies se pueden establecer como nombres de array y estarán disponibles para los scripts PHP como arrays, pero el navegador almacena cookies independientes. Considere usar `json_encode` para establecer una cookie con varios nombres y valores. No se recomienda usar `serialize` para este propósito, ya que puede generar vulnerabilidades de seguridad.

Las llamadas múltiples a la función `setcookie` se realizarán en orden.

## Véase también

header

setrawcookie

sección sobre cookies

RFC 6265

RFC 2109
