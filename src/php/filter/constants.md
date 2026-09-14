---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/filter.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_revision: 911fe79de
order: 24130
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`INPUT_POST` (`int`)  
Variables [POST](#reserved.variables.post).

`INPUT_GET` (`int`)  
Variables [GET](#reserved.variables.get).

`INPUT_COOKIE` (`int`)  
Variables [COOKIE](#reserved.variables.cookies).

`INPUT_ENV` (`int`)  
Variables [ENV](#reserved.variables.environment).

`INPUT_SERVER` (`int`)  
Variables [SERVER](#reserved.variables.server).

`INPUT_SESSION` (`int`)  
Variables [SESSION](#reserved.variables.session). (Eliminado a partir de PHP 8.0.0; no estaba implementado previamente)

`INPUT_REQUEST` (`int`)  
Variables [REQUEST](#reserved.variables.request). (Eliminado a partir de PHP 8.0.0; no estaba implementado previamente)

<!-- -->

`FILTER_FLAG_NONE` (`int`)  
Sin flags.

`FILTER_REQUIRE_SCALAR` (`int`)  
Flag utilizado para requerir que la entrada del filtro sea un escalar.

`FILTER_REQUIRE_ARRAY` (`int`)  
Flag utilizado para requerir que la entrada del filtro sea un `array`.

`FILTER_FORCE_ARRAY` (`int`)  
Este flag envuelve las entradas escalares en un `array` de un elemento para filtros que operan sobre arrays.

`FILTER_NULL_ON_FAILURE` (`int`)  
Usar `null` en lugar de `false` en caso de fallo.

Utilizable con cualquier filtro de validación `FILTER_VALIDATE_*`.

`FILTER_THROW_ON_FAILURE` (`int`)  
Lanza una Filter\FilterFailedException cuando un filtro de validación falla, en lugar de devolver `false`.

Utilizable con cualquier filtro de validación `FILTER_VALIDATE_*`.

Disponible a partir de PHP 8.5.0.

<!-- -->

`FILTER_FLAG_STRIP_LOW` (`int`)  
Elimina caracteres con valor ASCII menor que 32.

`FILTER_FLAG_STRIP_HIGH` (`int`)  
Elimina caracteres con valor ASCII mayor que 127.

`FILTER_FLAG_STRIP_BACKTICK` (`int`)  
Elimina caracteres de comilla invertida (`` ` ``).

`FILTER_FLAG_ENCODE_LOW` (`int`)  
Codifica caracteres con valor ASCII menor que 32.

`FILTER_FLAG_ENCODE_HIGH` (`int`)  
Codifica caracteres con valor ASCII mayor que 127.

`FILTER_FLAG_ENCODE_AMP` (`int`)  
Codifica `&`.

`FILTER_FLAG_NO_ENCODE_QUOTES` (`int`)  
Las comillas simples y dobles (`'` y `"`) no serán codificadas.

`FILTER_FLAG_EMPTY_STRING_NULL` (`int`)  
Si el saneamiento de un string resulta en un string vacío, convierte el valor a `null`

<!-- -->

`FILTER_VALIDATE_BOOL` (`int`)  
Devuelve `true` para `"1"`, `1` incluyendo notaciones binarias, octales y hexadecimales, `1.0` incluyendo notación científica, `"true"`, `true`, `"on"`, y `"yes"`.

Devuelve `false` para `"0"`, `0` incluyendo notaciones binarias, octales y hexadecimales, `0.0` incluyendo notación científica, `"false"`, `false`, `"off"`, `"no"`, y `""`.

Los valores de string se comparan sin distinguir entre mayúsculas y minúsculas. El valor de retorno para valores no booleanos depende de `FILTER_NULL_ON_FAILURE`. Si está configurado, se devuelve `null`, de lo contrario se devuelve `false`.

`default`  
Valor a devolver en caso de que el filtro falle.

Disponible a partir de PHP 8.0.0.

`FILTER_VALIDATE_BOOLEAN` (`int`)  
Alias de `FILTER_VALIDATE_BOOL`. El alias estaba disponible antes de la introducción de su nombre canónico en PHP 8.0.0.

`FILTER_VALIDATE_INT` (`int`)  
Valida si el valor es un entero, en caso de éxito se convierte al tipo `int`.

> [!NOTE]
> Los valores string son recortados usando `trim` antes de la validación.

`default`  
Valor a devolver en caso de que el filtro falle.

`min_range`  
El valor solo es válido si es mayor o igual que el valor proporcionado.

`max_range`  
El valor solo es válido si es menor o igual que el valor proporcionado.

`FILTER_FLAG_ALLOW_OCTAL` (`int`)  
Permite enteros en notación octal (`0[0-7]+`).

`FILTER_FLAG_ALLOW_HEX` (`int`)  
Permite enteros en notación hexadecimal (`0x[0-9a-fA-F]+`).

`FILTER_VALIDATE_FLOAT` (`int`)  
Valida si el valor es un float, en caso de éxito se convierte al tipo `float`.

> [!NOTE]
> Los valores string son recortados usando `trim` antes de la validación.

`default`  
Valor a devolver en caso de que el filtro falle.

`decimal`  

`min_range`  
El valor solo es válido si es mayor o igual que el valor proporcionado. Disponible a partir de PHP 7.4.0.

`max_range`  
El valor solo es válido si es menor o igual que el valor proporcionado. Disponible a partir de PHP 7.4.0.

`FILTER_FLAG_ALLOW_THOUSAND` (`int`)  
Acepta comas (`,`), que normalmente representan el separador de miles.

`FILTER_VALIDATE_REGEXP` (`int`)  
Valida el valor contra la expresión regular proporcionada por la opción `regexp`.

`default`  
Valor a devolver en caso de que el filtro falle.

`regexp`  
Expresión regular [compatible con Perl](#book.pcre).

`FILTER_VALIDATE_URL` (`int`)  
Valida si la URL es válido según [RFC 2396](https://datatracker.ietf.org/doc/html/rfc2396).

`default`  
Valor a devolver en caso de que el filtro falle.

`FILTER_FLAG_SCHEME_REQUIRED` (`int`)  
Requiere que la URL contenga una parte de esquema.

> [!WARNING]
> *OBSOLETO* a partir de PHP 7.3.0 y *ELIMINADO* a partir de PHP 8.0.0. Esto se debe a que siempre está implícito por el filtro `FILTER_VALIDATE_URL`.

`FILTER_FLAG_HOST_REQUIRED` (`int`)  
Requiere que la URL contenga una parte de host.

> [!WARNING]
> *OBSOLETO* a partir de PHP 7.3.0 y *ELIMINADO* a partir de PHP 8.0.0. Esto se debe a que siempre está implícito por el filtro `FILTER_VALIDATE_URL`.

`FILTER_FLAG_PATH_REQUIRED` (`int`)  
Requiere que la URL contenga una parte de ruta.

`FILTER_FLAG_QUERY_REQUIRED` (`int`)  
Requiere que la URL contenga una parte de consulta.

> [!WARNING]
> Una URL válida puede no especificar el protocolo HTTP (`http://`). Por lo tanto, puede ser necesaria una validación adicional para determinar si la URL usa un protocolo esperado, por ejemplo, `ssh://` o `mailto:`.

> [!WARNING]
> Este filtro solo funciona con URLs ASCII. Esto significa que los Nombres de Dominio Internacionalizados (IDN) siempre serán rechazados.

`FILTER_VALIDATE_DOMAIN` (`int`)  
Valida si el nombre de dominio es válido según [RFC 952](https://datatracker.ietf.org/doc/html/rfc952), [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034), [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035), [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1034), [RFC 2732](https://datatracker.ietf.org/doc/html/rfc1034), y [RFC 2181](https://datatracker.ietf.org/doc/html/rfc2181).

`default`  
Valor a devolver en caso de que el filtro falle.

`FILTER_FLAG_HOSTNAME` (`int`)  
Requiere que los nombres de host comiencen con un carácter alfanumérico y contengan solo caracteres alfanuméricos o guiones.

`FILTER_VALIDATE_EMAIL` (`int`)  
Valida si el valor es una dirección de correo electrónico "válida".

La validación se realiza contra la sintaxis `addr-spec` en [RFC 822](https://datatracker.ietf.org/doc/html/rfc822). Sin embargo, los comentarios, el plegado de espacios en blanco y los nombres de dominio sin puntos no están soportados, y por lo tanto serán rechazados.

`default`  
Valor a devolver en caso de que el filtro falle.

`FILTER_FLAG_EMAIL_UNICODE` (`int`)  
Acepta caracteres Unicode en la parte local. Disponible a partir de PHP 7.1.0.

> [!WARNING]
> La validación de correo electrónico es compleja y la única forma verdadera de confirmar que un correo electrónico es válido y existe es enviar un correo electrónico a la dirección.

`FILTER_VALIDATE_IP` (`int`)  
Valida el valor como dirección IP.

`default`  
Valor a devolver en caso de que el filtro falle.

`FILTER_FLAG_IPV4` (`int`)  
Permite direcciones IPv4.

`FILTER_FLAG_IPV6` (`int`)  
Permite direcciones IPv6.

`FILTER_FLAG_NO_RES_RANGE` (`int`)  
Deniega direcciones reservadas.

Estos son los rangos que están marcados como `Reserved-By-Protocol` en [RFC 6890](https://datatracker.ietf.org/doc/html/rfc6890).

Que para IPv4 corresponden a los siguientes rangos: `0.0.0.0/8`, `169.254.0.0/16`, `127.0.0.0/8`, `240.0.0.0/4`.

Y para IPv6 corresponden a los siguientes rangos: `::1/128`, `::/128`, `::FFFF:0:0/96`, `FE80::/10`.

`FILTER_FLAG_NO_PRIV_RANGE` (`int`)  
Deniega direcciones privadas.

Estas son direcciones IPv4 que están en los siguientes rangos: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.

Estas son direcciones IPv6 que comienzan con `FD` o `FC`.

`FILTER_FLAG_GLOBAL_RANGE` (`int`)  
Solo permite direcciones globales. Estas se pueden encontrar en [RFC 6890](https://datatracker.ietf.org/doc/html/rfc6890) donde el atributo `Global` es `True`. Disponible a partir de PHP 8.2.0.

`FILTER_VALIDATE_MAC` (`int`)  
Valida si el valor es una dirección MAC.

`default`  
Valor a devolver en caso de que el filtro falle.

<!-- -->

`FILTER_UNSAFE_RAW` (`int`)  
Este filtro no hace nada.

Sin embargo, puede eliminar o codificar caracteres especiales si se usa junto con los flags de saneamiento de filtro `FILTER_FLAG_STRIP_*` y `FILTER_FLAG_ENCODE_*`.

`FILTER_DEFAULT` (`int`)  
Alias de `FILTER_UNSAFE_RAW`.

`FILTER_SANITIZE_STRING` (`int`)  
Este filtro elimina etiquetas y codifica en HTML comillas dobles y simples.

Opcionalmente puede eliminar o codificar caracteres especificados si se usa junto con los flags de saneamiento de filtro `FILTER_FLAG_STRIP_*` y `FILTER_FLAG_ENCODE_*`.

El comportamiento de codificación de comillas puede desactivarse usando el flag de filtro `FILTER_FLAG_NO_ENCODE_QUOTES`.

> [!WARNING]
> *Obsoleto* a partir de PHP 8.1.0, use `htmlspecialchars` en su lugar.

> [!WARNING]
> La forma en que este filtro elimina etiquetas no es equivalente a `strip_tags`.

`FILTER_SANITIZE_STRIPPED` (`int`)  
Alias de `FILTER_SANITIZE_STRING`.

> [!WARNING]
> *Obsoleto* a partir de PHP 8.1.0, use `htmlspecialchars` en su lugar.

`FILTER_SANITIZE_ENCODED` (`int`)  
Este filtro codifica una cadena en URL.

Opcionalmente puede eliminar o codificar caracteres especificados si se usa junto con los flags de saneamiento de filtro `FILTER_FLAG_STRIP_*` y `FILTER_FLAG_ENCODE_*`.

`FILTER_SANITIZE_SPECIAL_CHARS` (`int`)  
Este filtro codifica en HTML `'`, `"`, `<`, `>`, `&` y caracteres con un valor ASCII menor que 32. A diferencia del filtro `FILTER_SANITIZE_FULL_SPECIAL_CHARS`, el filtro `FILTER_SANITIZE_SPECIAL_CHARS` ignora el flag `FILTER_FLAG_NO_ENCODE_QUOTES`.

Opcionalmente puede eliminar caracteres especificados si se usa junto con los flags de saneamiento de filtro `FILTER_FLAG_STRIP_*`, y puede codificar caracteres con valor ASCII mayor que 127 usando `FILTER_FLAG_ENCODE_HIGH`.

`FILTER_SANITIZE_FULL_SPECIAL_CHARS` (`int`)  
Este filtro es equivalente a llamar a `htmlspecialchars` con `ENT_QUOTES` configurado.

El comportamiento de codificación de comillas puede desactivarse usando el flag de filtro `FILTER_FLAG_NO_ENCODE_QUOTES`.

> [!WARNING]
> Al igual que `htmlspecialchars`, este filtro es consciente de la configuración INI [default_charset](#ini.default-charset). Si se detecta una secuencia de bytes que forma un carácter no válido en el juego de caracteres actual, entonces toda la cadena es rechazada resultando en que se devuelva una cadena vacía.

`FILTER_SANITIZE_EMAIL` (`int`)  
Sanea la cadena eliminando todos los caracteres excepto letras latinas (`[a-zA-Z]`), dígitos (`[0-9]`), y los caracteres especiales `` !#$%&'*+-=?^_`{|}~@.[] ``.

`FILTER_SANITIZE_URL` (`int`)  
Sanea la cadena eliminando todos los caracteres excepto letras latinas (`[a-zA-Z]`), dígitos (`[0-9]`), y los caracteres especiales `` $-_.+!*'(),{}|\\^~[]`<>#%";/?:@&= ``.

`FILTER_SANITIZE_NUMBER_INT` (`int`)  
Sanea la cadena eliminando todos los caracteres excepto dígitos (`[0-9]`), signo más (`+`), y signo menos (`-`).

`FILTER_SANITIZE_NUMBER_FLOAT` (`int`)  
Sanea la cadena eliminando todos los caracteres excepto dígitos (`[0-9]`), signo más (`+`), y signo menos (`-`).

`FILTER_FLAG_ALLOW_FRACTION` (`int`)  
Acepta el carácter punto (`.`), que normalmente representa el separador entre las partes entera y fraccionaria.

`FILTER_FLAG_ALLOW_THOUSAND` (`int`)  
Acepta el carácter coma (`,`), que normalmente representa el separador de miles.

`FILTER_FLAG_ALLOW_SCIENTIFIC` (`int`)  
Acepta números en notación científica permitiendo los caracteres `e` y `E`.

> [!WARNING]
> Si no se usa el flag `FILTER_FLAG_ALLOW_FRACTION`, entonces el separador decimal es eliminado, alterando el valor recibido.
>
> <div class="informalexample">
>
> ```
> <?php
> $number = '12.34';
>
> var_dump(filter_var($number, FILTER_SANITIZE_NUMBER_FLOAT));
> var_dump(filter_var($number, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION));
> ?>
>
>       
> ```
>
> El ejemplo anterior mostrará:
>
>     string(4) "1234"
>     string(5) "12.34"
>
>           
>
> </div>

`FILTER_SANITIZE_ADD_SLASHES` (`int`)  
Aplica `addslashes` a la entrada. Disponible a partir de PHP 7.3.0.

`FILTER_SANITIZE_MAGIC_QUOTES` (`int`)  
Alias de `FILTER_SANITIZE_ADD_SLASHES`.

> [!WARNING]
> *OBSOLETO* a partir de PHP 7.3.0 y *ELIMINADO* a partir de PHP 8.0.0.

<!-- -->

`FILTER_CALLBACK` (`int`)  
Este filtro delega el filtrado a una función definida por el usuario. El `callable` se pasa a través del parámetro `options` como el valor asociado a la clave `'options'`.

La retrollamada debe tener la siguiente firma:

```php
callback(string $value): mixed
```php

`value`  
El valor que está siendo filtrado.

> [!NOTE]
> El valor devuelto por la retrollamada será el valor devuelto por la función de filtro invocada.

Ejemplo de uso de `FILTER_CALLBACK` para validar un nombre de inicio de sesión

```
<?php
function validate_login(string $value): ?string
{
    if (strlen($value) >= 5 && ctype_alnum($value)) {
        return $value;
    }
    return null;
}

$login = "val1dL0gin";
$filtered_login = filter_var($login, FILTER_CALLBACK, ['options' => 'validate_login']);
var_dump($filtered_login);

$login = "f&ke login";
$filtered_login = filter_var($login, FILTER_CALLBACK, ['options' => 'validate_login']);
var_dump($filtered_login);
?>

     
```php

El ejemplo anterior mostrará:

    string(10) "val1dL0gin"
    NULL

> [!WARNING]
> Este filtro no puede usarse con ningún otro flag de filtro, por ejemplo, `FILTER_NULL_ON_FAILURE`.
