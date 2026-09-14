---
title: stream_socket_client
description: Abre una conexión de socket de Internet o Unix
source_url: https://www.php.net/manual/es/function.stream-socket-client.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-client.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 181e9c557
order: 88130
---

stream_socket_client

Abre una conexión de socket de Internet o Unix

## Descripción

```php
stream_socket_client(string $address, [int $error_code], [string $error_message], [float $timeout], [int $flags], [resource $context]): resource
```php

Inicia un flujo o una conexión de datagrama con el destino `address`. El tipo de socket creado se determina por el transporte especificado con el formato URL siguiente: `transport://target`. Para un socket de Internet, (AF_INET) como TCP y UDP, el `objetivo` de `address` será una dirección IP o un nombre de host. Para un socket Unix, el `objetivo` debe ser un fichero de socket del sistema.

> [!NOTE]
> El flujo se abrirá por omisión en modo bloqueante. Puede pasarse a modo no bloqueante utilizando la función `stream_set_blocking`.

## Parámetros

`address`  
La dirección del socket.

`error_code`  
Contendrá el número del error del sistema si la conexión falla.

`error_message`  
Contendrá el mensaje del error del sistema si la conexión falla.

`timeout`  
Tiempo límite, en segundos, para la llamada al sistema `connect()`. Por omisión, se utiliza [default_socket_timeout](#ini.default-socket-timeout).

> [!NOTE]
> Este parámetro solo se aplica para conexiones que no son asíncronas.

> [!NOTE]
> Para definir un tiempo límite al leer/escribir datos a través de un socket, utilice la función `stream_set_timeout`, ya que el parámetro `timeout` solo se aplica durante la conexión al socket.

`flags`  
Campo de bits que puede ser la combinación de cualquier opción de conexión. Actualmente, los valores posibles para estas opciones son `STREAM_CLIENT_CONNECT` (por omisión), `STREAM_CLIENT_ASYNC_CONNECT` y `STREAM_CLIENT_PERSISTENT`.

`context`  
Un recurso de contexto válido, creado por la función `stream_context_create`.

## Valores devueltos

En caso de éxito, se devuelve un recurso de flujo, que puede ser utilizado con otras funciones de ficheros, como `fgets`, `fgetss`, `fwrite`, `fclose`, y `feof`, `false` si ocurre un error.

## Errores/Excepciones

Si la llamada falla, `stream_socket_client` devolverá `false` y si los parámetros opcionales `error_code` y `error_message` son proporcionados, recibirán el error exacto que ocurrió en el sistema durante la llamada a `connect()`. Si el valor devuelto en `error_code` es `0` y la función ha devuelto `false`, es una indicación de que el error ocurrió antes de la llamada a `connect()`. Esto es probablemente debido a un problema de inicialización del socket. Tenga en cuenta que `error_code` y `error_message` deben ser pasados por referencia.

## Historial de cambios

| Versión | Descripción                                   |
|---------|-----------------------------------------------|
| 8.0.0   | `timeout` y `context` ahora pueden ser nulos. |

## Ejemplos

Ejemplo con `stream_socket_client`

```
<?php
$fp = stream_socket_client("tcp://www.example.com:80", $errno, $errstr, 30);
if (!$fp) {
    echo "$errstr ($errno)<br />\n";
} else {
    fwrite($fp, "GET / HTTP/1.0\r\nHost: www.example.com\r\nAccept: */*\r\n\r\n");
    while (!feof($fp)) {
        echo fgets($fp, 1024);
    }
    fclose($fp);
}
?>

    
```php

Uso de conexiones UDP

Lee la fecha y hora en un servicio UDP de tipo "`daytime`" (puerto 13) en su propia máquina:

```
<?php
$fp = stream_socket_client("udp://127.0.0.1:13", $errno, $errstr);
if (!$fp) {
    echo "ERROR: $errno - $errstr<br />\n";
} else {
    fwrite($fp, "\n");
    echo fread($fp, 26);
    fclose($fp);
}
?>

    
```php

## Notas

> [!WARNING]
> Los sockets UDP a veces parecerán abrirse sin error, incluso si el host remoto no es accesible. Este error solo se hará aparente cuando se intente leer o escribir datos con este socket. La razón es que UDP es un protocolo sin conexión, lo que significa que el sistema operativo no tiene que establecer un enlace para el socket, hasta que comience a intercambiar datos.

> [!NOTE]
> Al especificar direcciones IPv6 en formato numérico (ej. `fe80::1`) se debe colocar la dirección IP entre corchetes. Por ejemplo: `tcp://[fe80::1]:80`.

> [!NOTE]
> Según su entorno, los sockets Unix o el tiempo límite pueden no estar disponibles. Una lista de los transportes disponibles en el sistema es accesible mediante `stream_get_transports`. Consulte [???](#transports) para una lista de transportes nativos.

## Véase también

`stream_socket_server`, `stream_set_blocking`, `stream_set_timeout`, `stream_select`, `fgets`, `fgetss`, `fwrite`, `fclose`, `feof`, [???](#ref.curl)
