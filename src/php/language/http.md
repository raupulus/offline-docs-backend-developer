---
title: Opciones de contexto HTTP
description: Lista de opciones de contexto HTTP
source_url: https://www.php.net/manual/es/context.http.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/context/http.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 3abd17e61
order: 2000
---

Opciones de contexto HTTP

Lista de opciones de contexto HTTP

## Descripción

Opciones de contexto para los protocolos `http://` y `https://`.

## Opciones

`method` `string`  
`GET`, `POST`, o cualquier otro método HTTP soportado por el servidor remoto.

Por omisión, vale `GET`.

`header` `array` o `string`  
Encabezados adicionales a enviar durante la petición. Los valores de esta opción sobrescribirán otros valores (como `User-agent:`, `Host:`, y `Authentication:`), incluso al seguir redirecciones `Location:`. Por lo tanto, no se recomienda definir el encabezado `Host:`, si `follow_location` está activado.

Una cadena debe contener pares `Clave : valor` delimitados por `\r\n`, por ejemplo : `"Content-Type: application/json\r\nConnection: close"`. Un array debe contener una lista de pares `Clave : valor`, por ejemplo : `["Content-Type: application/json", "Connection: close"]`.

`user_agent` `string`  
Valor a enviar con el encabezado `User-Agent:`. Este valor solo debe ser utilizado si el agente de usuario *no* está especificado en la opción de contexto `header` anterior.

Por omisión, se utilizará el valor de la opción de configuración [user_agent](#ini.user-agent) del archivo `php.ini`.

`content` `string`  
Los datos adicionales a enviar después de los encabezados. Típicamente utilizados durante las peticiones POST o PUT.

`proxy` `string`  
URI de la dirección del proxy (ej. `tcp://proxy.example.com:5100`).

`request_fulluri` `bool`  
Cuando se define como `true`, la URI completa será utilizada al construir la petición (ej. `GET http://www.example.com/path/to/file.html HTTP/1.0`). Aunque este formato de petición no es estándar, algunos servidores de proxy lo requieren.

Por omisión, vale `false`.

`follow_location` `int`  
Sigue las redirecciones `Location`. Debe definirse como `0` para desactivar.

Por omisión, vale `1`.

`max_redirects` `int`  
El número máximo de redirecciones a seguir. El valor `1` o inferior significa que ninguna redirección será seguida.

Por omisión, vale `20`.

`protocol_version` `float`  
Versión del protocolo HTTP.

Por omisión, vale `1.1` a partir de PHP 8.0.0; antes de esta versión el valor por omisión era `1.0`.

`timeout` `float`  
Tiempo máximo de espera para la lectura, en forma de `float` (ej. `10.5`).

Por omisión, se utilizará el valor de la opción de configuración [default_socket_timeout](#ini.default-socket-timeout) del archivo `php.ini`.

`ignore_errors` `bool`  
Obtiene el contenido incluso al recibir un código de error.

Por omisión, vale `false`.

## Ejemplos

Obtención de una página y envío de datos POST

```php
<?php

$postdata = http_build_query(
    [
        'var1' => 'du contenu',
        'var2' => 'doh',
    ]
);

$opts = ['http' =>
    [
        'method'  => 'POST',
        'header'  => 'Content-type: application/x-www-form-urlencoded',
        'content' => $postdata,
    ]
];

$context = stream_context_create($opts);

$result = file_get_contents('http://example.com/submit.php', false, $context);

?>

    
```

Ignora las redirecciones pero obtiene los encabezados y el contenido

```php
<?php

$url = "http://www.example.org/header.php";

$opts = ['http' =>
    [
        'method' => 'GET',
        'max_redirects' => '0',
        'ignore_errors' => '1',
    ]
];

$context = stream_context_create($opts);
$stream = fopen($url, 'r', false, $context);

// información sobre los encabezados y metadatos del flujo
var_dump(stream_get_meta_data($stream));

// datos actuales de $url
var_dump(stream_get_contents($stream));
fclose($stream);
?>

    
```

## Notas

> [!NOTE]
> Opciones de contexto adicionales pueden ser soportadas por el [transporte subyacente](#transports.inet). Para los flujos `http://`, consulte las opciones de contexto del transporte `tcp://`. Para los flujos `https://`, consulte las opciones de contexto del transporte `ssl://`.

> [!NOTE]
> Cuando este manejador de flujo sigue una redirección, `wrapper_data`, devuelto por la función `stream_get_meta_data` no debe contener necesariamente la línea de estado HTTP que se aplica a los datos de contenido en el índice `0`.
>
>     array (
>       'wrapper_data' =>
>       array (
>         0 => 'HTTP/1.0 301 Moved Permanently',
>         1 => 'Cache-Control: no-cache',
>         2 => 'Connection: close',
>         3 => 'Location: http://example.com/foo.jpg',
>         4 => 'HTTP/1.1 200 OK',
>         ...
>
>        
>
> La primera petición devuelve una `301` (redirección permanente), por lo tanto, el manejador de flujo sigue automáticamente la redirección para obtener una respuesta `200` (índice = `4`).

## Véase también

[???](#wrappers.http), [???](#context.socket), [???](#context.ssl)
