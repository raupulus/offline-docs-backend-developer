---
title: fsockopen
description: Abre un socket de conexión Internet o Unix
source_url: https://www.php.net/manual/es/function.fsockopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/fsockopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: 4e6f0774f
order: 56270
---

fsockopen

Abre un socket de conexión Internet o Unix

## Descripción

```php
fsockopen(string $hostname, [int $port], [int $error_code], [string $error_message], [float $timeout]): resource
```php

Inicializa una conexión por socket al recurso especificado por `hostname`.

PHP soporta los objetivos en los dominios Internet y Unix como se describe en [???](#transports). Una lista de los tipos de transportes también puede ser encontrada utilizando la función `stream_get_transports`.

El socket se abrirá por omisión en modo bloqueante. Se puede cambiar de modo utilizando: `stream_set_blocking`.

La función `stream_socket_client` es similar pero proporciona más opciones, incluyendo la conexión no bloqueante y la posibilidad de proporcionar un contexto de flujo.

## Parámetros

`hostname`  
Si el soporte OpenSSL [está instalado](#openssl.installation), se puede prefijar `hostname` con `ssl://` o `tls://` para utilizar una conexión cliente SSL o TLS sobre TCP/IP para conectarse al host remoto.

`port`  
El número del puerto. Este argumento puede ser omitido e ignorado utilizando el valor `-1` para los transportes que no utilizan puertos, como `unix://`.

`error_code`  
Si se proporciona, contiene el número del error del sistema que ocurre durante la llamada al sistema `connect()`.

Si el valor devuelto por `error_code` es `0` y la función devuelve `false`, puede ser una indicación de que el error ocurrió antes de la llamada a `connect()`. La mayoría de las veces, esto se debe a un problema de inicialización del socket.

`error_message`  
El mensaje de error, en forma de `string`.

`timeout`  
El tiempo máximo de espera, en segundos. Si es `null` el parámetro `php.ini` [default_socket_timeout](#ini.default-socket-timeout) es utilizado.

> [!NOTE]
> Si se necesita establecer un tiempo límite para leer/escribir datos a través de este socket, utilice la función `stream_set_timeout`, ya que el argumento `timeout` de la función `fsockopen` se aplica únicamente durante la conexión del socket.

## Valores devueltos

`fsockopen` devuelve un puntero de fichero que puede ser utilizado con otras funciones de ficheros, tales como `fgets`, `fgetss`, `fputs`, `fclose` y `feof`. Si la llamada falla, la función devuelve `false`.

## Errores/Excepciones

Lanza una alerta de tipo `E_WARNING` si el argumento `hostname` no es un dominio válido.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `timeout` es ahora nullable. |

## Ejemplos

Ejemplo con `fsockopen`

```
<?php
$fp = fsockopen("www.example.com", 80, $errno, $errstr, 30);
if (!$fp) {
    echo "$errstr ($errno)<br />\n";
} else {
    $out = "GET / HTTP/1.1\r\n";
    $out .= "Host: www.example.com\r\n";
    $out .= "Connection: Close\r\n\r\n";

    fwrite($fp, $out);
    while (!feof($fp)) {
        echo fgets($fp, 128);
    }
    fclose($fp);
}
?>

    
```php

Uso de una conexión UDP

El ejemplo a continuación describe cómo leer la fecha y la hora gracias a un servicio UDP "daytime" (puerto 13), en su propia máquina.

```
<?php
$fp = fsockopen("udp://127.0.0.1", 13, $errno, $errstr);
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

> [!NOTE]
> Dependiendo de los entornos, el tipo 'dominio Unix' o la opción `timeout` no siempre están disponibles.

> [!WARNING]
> Los sockets UDP parecen haber sido abiertos sin error, incluso si el host remoto no es accesible. El error aparece entonces solo cuando se intenta leer/escribir en el socket. La razón de esto es que UDP es un protocolo `"connectionless"`, lo que significa que el sistema no intentará establecer un enlace para el socket hasta que no deba recibir/enviar datos.

> [!NOTE]
> Al especificar direcciones IPv6 en formato numérico (ej. `fe80::1`) se debe colocar la dirección IP entre corchetes. Por ejemplo: `tcp://[fe80::1]:80`.

## Véase también

`pfsockopen`, `stream_socket_client`, `stream_set_blocking`, `stream_set_timeout`, `fgets`, `fgetss`, `fwrite`, `fclose`, `feof`, `socket_connect`, La [extensión Curl](#ref.curl)
