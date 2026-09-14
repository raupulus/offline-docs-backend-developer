---
title: socket_recv
description: Recibe datos de un socket conectado
source_url: https://www.php.net/manual/es/function.socket-recv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-recv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: false
translation_revision: '765056369'
order: 75750
---

socket_recv

Recibe datos de un socket conectado

## Descripción

```php
socket_recv(Socket $socket, string $data, int $length, int $flags): int
```php

La función `socket_recv` recibe `length` bytes de datos en `data` desde `socket`. `socket_recv` puede ser utilizada para recuperar datos desde sockets conectados. Asimismo, los flags permiten modificar el comportamiento de la función.

`data` se pasa por referencia, por lo que debe estar presente en la lista de argumentos. Los datos recibidos desde la `socket` por `socket_recv` serán devueltos en `data`.

## Parámetros

`socket`  
`socket` debe ser una instancia de `Socket` previamente creada por `socket_create`.

`data`  
Los datos recibidos serán transmitidos en `data`. Si ocurre un error, si la conexión está cerrada o si no hay datos disponibles, `data` valdrá entonces `null`.

`length`  
Hasta `length` bytes serán leídos desde el host remoto.

`flags`  
El valor de `flags` puede ser una combinación de los siguientes flags, agrupados mediante el operador OR binario (`|`).

| Flag | Descripción |
|----|----|
| `MSG_OOB` | Trata datos fuera de banda. |
| `MSG_PEEK` | Recibe los datos desde el inicio de la cola sin eliminarlos de la cola. |
| `MSG_WAITALL` | Bloquea antes de que al menos `length` bytes sean recibidos. Sin embargo, si se intercepta una señal o la conexión se termina, la función puede devolver menos datos. |
| `MSG_DONTWAIT` | Si este flag está especificado, la función devolverá datos cuando normalmente habría bloqueado. |

Valores posibles de `flags`

## Valores devueltos

`socket_recv` devuelve el número de bytes recibidos, o `false` si ha ocurrido un error. El código de error actual puede ser recuperado llamando a `socket_last_error`. Este código de error puede ser pasado a la función `socket_strerror` para obtener una representación textual del error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Ejemplos

Ejemplos con `socket_recv`

Este ejemplo es una reescritura del ejemplo tomado en [???](#sockets.examples) para utilizar `socket_recv`.

```
<?php
error_reporting(E_ALL);

echo "<h2>Conexión TCP/IP</h2>\n";

/* Obtiene el puerto del servicio WWW. */
$service_port = getservbyname('www', 'tcp');

/* Obtiene la dirección IP del host objetivo. */
$address = gethostbyname('www.example.com');

/* Crea un socket TCP/IP. */
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() ha fallado: razón: " . socket_strerror(socket_last_error()) . "\n";
} else {
    echo "OK.\n";
}

echo "Intentando conectar a '$address' en el puerto '$service_port'...";
$result = socket_connect($socket, $address, $service_port);
if ($result === false) {
    echo "socket_connect() ha fallado.\nRazón: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
} else {
    echo "OK.\n";
}

$in = "HEAD / HTTP/1.1\r\n";
$in .= "Host: www.example.com\r\n";
$in .= "Connection: close\r\n\r\n";
$out = '';

echo "Enviando una solicitud HTTP HEAD...";
socket_write($socket, $in, strlen($in));
echo "OK.\n";

echo "Leyendo la respuesta:\n\n";
$buf = 'Este es mi búfer.';
if (false !== ($bytes = socket_recv($socket, $buf, 2048, MSG_WAITALL))) {
    echo "$bytes bytes leídos desde socket_recv(). Cerrando el socket...";
} else {
    echo "socket_recv() ha fallado; razón: " . socket_strerror(socket_last_error($socket)) . "\n";
}
socket_close($socket);

echo $buf . "\n";
echo "OK.\n\n";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    <h2>Conexión TCP/IP</h2>
    OK.
    Intentando conectar a '208.77.188.166' en el puerto '80'...OK.
    Enviando una solicitud HTTP HEAD...OK.
    Leyendo la respuesta:

    123 bytes leídos desde socket_recv(). Cerrando el socket...HTTP/1.1 200 OK
    Date: Mon, 14 Sep 2009 08:56:36 GMT
    Server: Apache/2.2.3 (Red Hat)
    Last-Modified: Tue, 15 Nov 2005 13:24:10 GMT
    ETag: "b80f4-1b6-80bfd280"
    Accept-Ranges: bytes
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    OK.
