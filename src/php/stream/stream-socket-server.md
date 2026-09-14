---
title: stream_socket_server
description: Crea un socket de servidor Unix o Internet
source_url: https://www.php.net/manual/es/function.stream-socket-server.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-server.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 88190
---

stream_socket_server

Crea un socket de servidor Unix o Internet

## Descripción

```php
stream_socket_server(string $address, [int $error_code], [string $error_message], [int $flags], [resource $context]): resource
```php

`stream_socket_server` crea un flujo o un datagrama en el socket especificado `address`.

`stream_socket_server` solo crea un socket y, para aceptar conexiones, se debe utilizar `stream_socket_accept`.

## Parámetros

`address`  
El tipo de socket creado se determina por el transporte especificado con el formato URL siguiente: `transport://target`.

Para un socket de Internet (`AF_INET`) como TCP y UDP, el `target` de `remote_socket` será una dirección IP o un nombre de host seguido de dos puntos y un número de puerto. Para un socket Unix, el `target` debe ser un fichero de socket del sistema.

Según el entorno, los sockets de dominio Unix pueden no estar disponibles. Una lista de los transportes disponibles se puede obtener mediante `stream_get_transports`. Consulte [???](#transports) para conocer la lista de transportes nativos.

`error_code`  
Si los argumentos opcionales `error_code` y `error_message` están presentes, se configurarán para indicar el nivel de error actual de las funciones del sistema `socket()`, `bind()` y `listen()`. Si el valor devuelto en `error_code` es `0` y la función devuelve `false`, esto indica que el error ocurrió antes de la llamada a `bind()`. Esto probablemente se deba a un problema de inicialización del socket. Tenga en cuenta que los argumentos `error_code` y `error_message` siempre se pasarán por referencia.

`error_message`  
Consulte la descripción de `error_code`.

`flags`  
Un campo de bits, que puede ser la combinación de cualquier opción de creación de socket.

> [!NOTE]
> Para los sockets UDP, se debe utilizar la constante `STREAM_SERVER_BIND` como valor del parámetro `flags`.

`context`  

## Valores devueltos

Devuelve el flujo creado, o bien `false` en caso de error.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `context` ahora es nullable. |

## Ejemplos

Ejemplo con `stream_socket_server`

```
<?php
$socket = stream_socket_server("tcp://0.0.0.0:8000", $errno, $errstr);
if (!$socket) {
  echo "$errstr ($errno)<br />\n";
} else {
  while ($conn = stream_socket_accept($socket)) {
    fputs ($conn, 'La hora local es ' . date('n/j/Y g:i a') . "\n");
    fclose ($conn);
  }
  fclose($socket);
}
?>

    
```php

El ejemplo siguiente muestra cómo leer la fecha y la hora en un servicio UDP (puerto 13) en su propia máquina, tal como se presenta con la función `stream_socket_client`:

> [!NOTE]
> La mayoría de los sistemas requieren acceso de administrador para abrir un socket en los puertos por debajo de 1024.

Utilizar un servidor de socket UDP

```
<?php
$socket = stream_socket_server("udp://0.0.0.0:13", $errno, $errstr, STREAM_SERVER_BIND);
if (!$socket) {
  echo "ERROR: $errno - $errstr<br />\n";
} else {
  while ($conn = stream_socket_accept($socket)) {
    fwrite($conn, date("D M j H:i:s Y\r\n"));
    fclose($conn);
  }
  fclose($socket);
}
?>

    
```php

## Notas

> [!NOTE]
> Al especificar direcciones IPv6 en formato numérico (ej. `fe80::1`) se debe colocar la dirección IP entre corchetes. Por ejemplo: `tcp://[fe80::1]:80`.

## Véase también

stream_socket_client

stream_set_blocking

stream_set_timeout

fgets

fgetss

fwrite

fclose

feof

Extensión Curl
