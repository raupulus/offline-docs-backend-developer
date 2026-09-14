---
title: imap_open
description: Abre un flujo IMAP hacia un buzón de correo
source_url: https://www.php.net/manual/es/function.imap-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38400
---

imap_open

Abre un flujo

IMAP

hacia un buzón de correo

## Descripción

```php
imap_open(string $mailbox, string $user, string $password, [int $flags], [int $retries], [array $options]): IMAP\Connection
```php

Abre un flujo IMAP hacia el buzón de correo `mailbox`.

Esta función también puede ser utilizada para abrir flujos en servidores POP3 y NNTP, pero algunas funciones y características solo están disponibles con servidores IMAP.

## Parámetros

`mailbox`  
Un nombre de buzón de correo está compuesto por una dirección de servidor y una dirección de buzón en ese servidor. La palabra reservada `INBOX` representa el buzón de correo del usuario actual. Los nombres de buzones de correo que contienen caracteres especiales (fuera del espacio ASCII) deben ser codificados con `imap_utf7_encode`.

> [!WARNING]
> Pasar datos no confiables a este parámetro es *inseguro*, a menos que [imap.enable_insecure_rsh](#ini.imap.enable-insecure-rsh) esté desactivado.

La dirección del servidor, entre llaves '{' y '}', está compuesta por el nombre del servidor o su dirección IP, una especificación de protocolo (comenzando por '/') y un puerto opcional (especificado con ':').

Esta parte es obligatoria en los parámetros del buzón de correo.

Todos los nombres que comienzan con `{` son nombres remotos y tienen la forma `"{" nombre_sistema_remoto [":" puerto] [flags] "}" [nombre_buzon]` donde :

- `remote_system_name` : Nombre de dominio de Internet o una dirección IP de servidor entre comillas.

- `puerto` : número de puerto TCP (opcional), el valor por defecto es el valor del puerto para este servicio.

- `flags` : opciones, ver la tabla siguiente.

- `mailbox_name` : nombre del buzón remoto, por defecto : INBOX

| Flag | Descripción |
|----|----|
| `/service=`*service* | servicio para el acceso al buzón, por defecto : "imap" |
| `/user=`*user* | nombre del usuario remoto para la identificación en el servidor |
| `/authuser=`*user* | usuario remoto de identificación; si se especifica, este será el nombre del usuario cuya contraseña se utiliza (e.g. administrador) |
| `/anonymous` | acceso remoto anónimo |
| `/debug` | la telemetría de registro del protocolo en los logs de depuración de la aplicación |
| `/secure` | no transmite una contraseña en claro a través de la red |
| `/imap`, `/imap2`, `/imap2bis`, `/imap4`, `/imap4rev1` | equivalente a `/service=imap` |
| `/pop3` | equivalente a `/service=pop3` |
| `/nntp` | equivalente a `/service=nntp` |
| `/norsh` | no utilizar rsh o ssh para establecer una sesión de pre identificación IMAP |
| `/ssl` | utiliza `Secure Socket Layer` para cifrar la sesión |
| `/validate-cert` | valida los certificados desde el servidor TLS/SSL (es el comportamiento por defecto) |
| `/novalidate-cert` | no valida los certificados desde el servidor TLS/SSL, necesario si el servidor utiliza certificados autofirmados |
| `/tls` | fuerza el uso de `start-TLS` para cifrar la sesión y rechaza las conexiones a los servidores que no lo soportan |
| `/notls` | no utiliza `start-TLS` para cifrar la sesión, incluso con los servidores que lo soportan |
| `/readonly` | solicita acceso de solo lectura en el buzón (solo IMAP; ignorado en NNTP, y un error con SMTP y POP3) |

Flags opcionales para los nombres

`user`  
El nombre de usuario

`password`  
La contraseña asociada con el usuario `user`

`flags`  
`flags` es una máscara de bits, que puede tomar uno o varios de los siguientes valores :

- `OP_READONLY` : Abre un buzón de correo en modo de solo lectura

- `OP_ANONYMOUS` : No utilizar, o modificar el fichero `.newsrc` para las noticias (solo NNTP)

- `OP_HALFOPEN` : Para los nombres IMAP y NNTP, abre una conexión pero no abre un buzón de correo.

- `CL_EXPUNGE` : Elimina automáticamente el buzón de correo de la lista, al finalizar el flujo (ver también `imap_delete` y `imap_expunge`)

- `OP_DEBUG` : negociaciones de depuración del protocolo

- `OP_SHORTCACHE` : Caché corta (`elt` solamente)

- `OP_SILENT` : No transmitir los eventos (uso interno)

- `OP_PROTOTYPE` : Devuelve el prototipo del controlador

- `OP_SECURE` : No realizar identificaciones no seguras

`retries`  
El número máximo de intentos de conexión.

`options`  
Parámetros de conexión; las claves pueden ser utilizadas para definir uno o varios parámetros de conexión :

- `DISABLE_AUTHENTICATOR` - Desactiva las propiedades de autenticación

## Valores devueltos

Devuelve una instancia de `IMAP\Connection` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `IMAP\Connection` ; anteriormente, un `resource` era devuelto. |

## Ejemplos

Diferentes usos de `imap_open`

```
<?php
// Para conectarse a un servidor IMAP funcionando en el puerto 143 de la
// máquina local, haga esto :
$mbox = imap_open("{localhost:143}INBOX", "user_id", "password");

// Para conectarse a un servidor POP3 funcionando en el puerto 110 del
// servidor local, haga esto :
$mbox = imap_open ("{localhost:110/pop3}INBOX", "user_id", "password");

// Para conectarse a un servidor SSL IMAP o POP3, añada /ssl
// después de la especificación del protocolo :
$mbox = imap_open ("{localhost:993/imap/ssl}INBOX", "user_id", "password");

// Para conectarse a un servidor SSL IMAP o POP3 con un certificado autofirmado
// añada /ssl/novalidate-cert después del protocolo :
$mbox = imap_open ("{localhost:995/pop3/ssl/novalidate-cert}", "user_id", "password");

// Para conectarse a un servidor NNTP que funciona en
// el puerto 119 de la máquina local se puede utilizar el comando:
$nntp = imap_open ("{localhost:119/nntp}comp.test", "", "");

// Para conectarse a un servidor remoto, reemplace "localhost" por
// el nombre o la dirección IP de la máquina.
?>

    
```php

Ejemplo con `imap_open`

```
<?php
$mbox = imap_open("{imap.example.org:143}", "username", "password");

echo "<h1>Buzones de correo</h1>\n";
$folders = imap_listmailbox($mbox, "{imap.example.org:143}", "*");

if ($folders == false) {
    echo "Llamada fallida<br />\n";
} else {
    foreach ($folders as $val) {
        echo $val . "<br />\n";
    </foreach>
}

echo "<h1>Encabezados en INBOX</h1>\n";
$headers = imap_headers($mbox);

if ($headers == false) {
    echo "Llamada fallida<br />\n";
} else {
    foreach ($headers as $val) {
        echo $val . "<br />\n";
    }
}

imap_close($mbox);
?>

    
```php

## Véase también

`imap_close`
