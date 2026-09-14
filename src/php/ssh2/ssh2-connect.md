---
title: ssh2_connect
description: Conexión a un servidor SSH
source_url: https://www.php.net/manual/es/function.ssh2-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: true
translation_revision: 74ef2355c
order: 86470
---

ssh2_connect

Conexión a un servidor SSH

## Descripción

```php
ssh2_connect(string $host, [int $port], [array $methods], [array $callbacks]): resource
```php

Establece una conexión a un servidor SSH remoto.

Una vez conectado, el cliente debe verificar la clave de host del servidor utilizando la función `ssh2_fingerprint`, luego identificarse utilizando un password o una clave pública.

## Parámetros

`host`  

`port`  

`methods`  
`methods` puede ser un array asociativo de hasta cuatro parámetros, como se describe a continuación.

| Índice | Significado | Valores soportados \* |
|----|----|----|
| kex | La lista de métodos de intercambio a anunciar, separados por una coma, por orden de preferencia. | `diffie-hellman-group1-sha1`, `diffie-hellman-group14-sha1`, y `diffie-hellman-group-exchange-sha1` |
| hostkey | La lista de métodos de claves de host a anunciar, separados por una coma, por orden de preferencia. | `ssh-rsa` y `ssh-dss` |
| client_to_server | Array asociativo que contiene los códigos de los métodos de cifrado, compresión y mensajes de autenticación (MAC) preferidos para el envío de mensajes desde el cliente al servidor. |  |
| server_to_client | Array asociativo que contiene los códigos de los métodos de cifrado, compresión y mensajes de autenticación (MAC) preferidos para el envío de mensajes desde el servidor al cliente. |  |

`methods` puede ser un array asociativo con cualquiera o todos los parámetros siguientes.

\* - Los valores soportados dependen de los métodos soportados por la biblioteca. Consulte la documentación [libssh2](http://libssh2.org/) para más información.

| Índice | Significado | Valores soportados \* |
|----|----|----|
| crypt | Lista de métodos de cifrado a anunciar, separados por una coma, por orden de preferencia. | `rijndael-cbc@lysator.liu.se`, `aes256-cbc`, `aes192-cbc`, `aes128-cbc`, `3des-cbc`, `blowfish-cbc`, `cast128-cbc`, `arcfour`, y `none**` |
| comp | Lista de métodos de compresión a anunciar, separados por una coma, por orden de preferencia. | `zlib` y `none` |
| mac | Lista de métodos MAC a anunciar, separados por una coma, por orden de preferencia. | `hmac-sha1`, `hmac-sha1-96`, `hmac-ripemd160`, `hmac-ripemd160@openssh.com`, y `none**` |

`client_to_server` y `server_to_client` deben ser un array asociativo con cualquiera o todos los parámetros siguientes.

> [!NOTE]
> Por razones de seguridad, `none` está desactivado por la biblioteca [libssh2](http://libssh2.org/) a menos que se active explícitamente durante la compilación utilizando las opciones apropiadas de ./configure. Consulte la documentación de la biblioteca para más información.

`callbacks`  
`callbacks` debe ser un array asociativo que contiene cualquiera o todos los parámetros siguientes.

| Índice | Significado | Prototipo |
|----|----|----|
| ignore | Nombre de la función a llamar cuando se recibe un paquete `SSH2_MSG_IGNORE` | `void ignore_cb($message)` |
| debug | Nombre de la función a llamar cuando se recibe un paquete `SSH2_MSG_DEBUG` | `void debug_cb($message, $language, $always_display)` |
| macerror | Nombre de la función a llamar cuando se recibe un paquete pero el código de mensaje de autenticación falla. Si la función de retrollamada devuelve `true`, el error será ignorado, de lo contrario, la conexión terminará. | `bool macerror_cb($packet)` |
| disconnect | Nombre de la función a llamar cuando se recibe un paquete `SSH2_MSG_DISCONNECT` | `void disconnect_cb($reason, $message, $language)` |

Parámetros de retrollamada

## Valores devueltos

Devuelve un recurso en caso de éxito, o `false` en caso de error.

## Ejemplos

Ejemplo con `ssh2_connect`

Apertura de una conexión forzando 3des-cbc al enviar paquetes, cualquier cifrado AES al recibir paquetes, ninguna compresión en ambas direcciones, y un intercambio de claves Group1.

```
<?php
/* Notificación al usuario si el servidor termina la conexión */
function my_ssh_disconnect($reason, $message, $language) {
  printf("Servidor desconectado con código de razón [%d] y mensaje: %s\n",
         $reason, $message);
}

$methods = array(
  'kex' => 'diffie-hellman-group1-sha1',
  'client_to_server' => array(
  'crypt'            => '3des-cbc',
  'comp'             => 'none'),
  'server_to_client' => array(
  'crypt'            => 'aes256-cbc,aes192-cbc,aes128-cbc',
  'comp'             => 'none'));

$callbacks = array('disconnect' => 'my_ssh_disconnect');

$connection = ssh2_connect('shell.example.com', 22, $methods, $callbacks);
if (!$connection) die('Fallo en la conexión');
?>

   
```php

## Véase también

ssh2_fingerprint

ssh2_auth_none

ssh2_auth_password

ssh2_auth_pubkey

ssh2_auth_pubkey_file

ssh2_disconnect
