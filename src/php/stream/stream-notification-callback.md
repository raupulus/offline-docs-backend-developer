---
title: stream_notification_callback
description: Una función de retrollamada para el parámetro de contexto notification
source_url: https://www.php.net/manual/es/function.stream-notification-callback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-notification-callback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 561e36d64
order: 88030
---

stream_notification_callback

Una función de retrollamada para el parámetro de contexto

notification

## Descripción

```php
stream_notification_callback(int $notification_code, int $severity, string $message, int $message_code, int $bytes_transferred, int $bytes_max): void
```php

Una función de retrollamada de tipo `callable`, utilizada por el [parámetro de contexto notification](#context.params.notification), llamada durante un evento.

> [!NOTE]
> Esto *no* es una función real, únicamente un prototipo de cómo debe ser la función.

## Parámetros

`notification_code`  
Una de las constantes de notificación `STREAM_NOTIFY_*`.

`severity`  
Una de las constantes de notificación `STREAM_NOTIFY_SEVERITY_*`.

`message`  
Pasado si un mensaje descriptivo está disponible para este evento.

`message_code`  
Pasado si un código de mensaje descriptivo está disponible para este evento.

El significado de este valor depende del gestor específico utilizado.

`bytes_transferred`  
Si es posible, `bytes_transferred` será rellenado.

`bytes_max`  
Si es posible, `bytes_max` será rellenado.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Soporte para `STREAM_NOTIFY_COMPLETED` implementado, las versiones anteriores de PHP nunca desencadenaban esta notificación. |

## Ejemplos

Ejemplo con `stream_notification_callback`

```
<?php
function stream_notification_callback($notification_code, $severity, $message, $message_code, $bytes_transferred, $bytes_max) {

    switch($notification_code) {
        case STREAM_NOTIFY_RESOLVE:
        case STREAM_NOTIFY_AUTH_REQUIRED:
        case STREAM_NOTIFY_COMPLETED:
        case STREAM_NOTIFY_FAILURE:
        case STREAM_NOTIFY_AUTH_RESULT:
            var_dump($notification_code, $severity, $message, $message_code, $bytes_transferred, $bytes_max);
            /* Ignorar */
            break;

        case STREAM_NOTIFY_REDIRECTED:
            echo "Redirección a: ", $message;
            break;

        case STREAM_NOTIFY_CONNECT:
            echo "Conectado...";
            break;

        case STREAM_NOTIFY_FILE_SIZE_IS:
            echo "Obteniendo el tamaño del fichero: ", $bytes_max;
            break;

        case STREAM_NOTIFY_MIME_TYPE_IS:
            echo "Tipo mime encontrado: ", $message;
            break;

        case STREAM_NOTIFY_PROGRESS:
            echo "Descargando, ya ", $bytes_transferred, " bytes transferidos";
            break;
    }
    echo "\n";
}

$ctx = stream_context_create();
stream_context_set_params($ctx, array("notification" => "stream_notification_callback"));

file_get_contents("http://php.net/contact", false, $ctx);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Conectado...
    Tipo mime encontrado: text/html; charset=utf-8
    Redirección a: http://no.php.net/contact
    Conectado...
    Obteniendo el tamaño del fichero: 0
    Tipo mime encontrado: text/html; charset=utf-8
    Redirección a: http://no.php.net/contact.php
    Conectado...
    Obteniendo el tamaño del fichero: 4589
    Tipo mime encontrado: text/html;charset=utf-8
    Descargando, ya 0 bytes transferidos
    Descargando, ya 0 bytes transferidos
    Descargando, ya 0 bytes transferidos
    Descargando, ya 1440 bytes transferidos
    Descargando, ya 2880 bytes transferidos
    Descargando, ya 4320 bytes transferidos
    Descargando, ya 5760 bytes transferidos
    Descargando, ya 6381 bytes transferidos
    Descargando, ya 7002 bytes transferidos

Barra de progreso simple para un cliente de descarga en línea de comandos

```
<?php
function usage($argv) {
    echo "Uso:\n";
    printf("\tphp %s <http://example.com/file> <localfile>\n", $argv[0]);
    exit(1);
}

function stream_notification_callback($notification_code, $severity, $message, $message_code, $bytes_transferred, $bytes_max) {
    static $filesize = null;

    switch($notification_code) {
    case STREAM_NOTIFY_RESOLVE:
    case STREAM_NOTIFY_AUTH_REQUIRED:
    case STREAM_NOTIFY_COMPLETED:
    case STREAM_NOTIFY_FAILURE:
    case STREAM_NOTIFY_AUTH_RESULT:
        /* Ignorar */
        break;

    case STREAM_NOTIFY_REDIRECTED:
        echo "Redirección a: ", $message, "\n";
        break;

    case STREAM_NOTIFY_CONNECT:
        echo "Conectado...\n";
        break;

    case STREAM_NOTIFY_FILE_SIZE_IS:
        $filesize = $bytes_max;
        echo "Tamaño del fichero: ", $filesize, "\n";
        break;

    case STREAM_NOTIFY_MIME_TYPE_IS:
        echo "Tipo Mime: ", $message, "\n";
        break;

    case STREAM_NOTIFY_PROGRESS:
        if ($bytes_transferred > 0) {
            if (!isset($filesize)) {
                printf("\rTamaño del fichero desconocido.. %2d kb hechos..", $bytes_transferred/1024);
            } else {
                $length = (int) (($bytes_transferred/$filesize)*100);
                printf("\r[%-100s] %d%% (%2d/%2d kb)", str_repeat("=", $length). ">", $length, ($bytes_transferred/1024), $filesize/1024);
            }
        }
        break;
    }
}

isset($argv[1], $argv[2]) or usage($argv);

$ctx = stream_context_create();
stream_context_set_params($ctx, array("notification" => "stream_notification_callback"));

$fp = fopen($argv[1], "r", false, $ctx);
if (is_resource($fp) && file_put_contents($argv[2], $fp)) {
    echo "\n¡Hecho!\n";
    exit(0);
}

$err = error_get_last();
echo "\n¡Error!\n", $err["message"], "\n";
exit(1);
?>

    
```php

Ejecute el ejemplo anterior con: `php -n fetch.php http://no2.php.net/get/php-5-LATEST.tar.bz2/from/this/mirror php-latest.tar.bz2` mostrará algo similar a:

    Conectado...
    Tipo Mime: text/html; charset=utf-8
    Redirección a: http://no2.php.net/distributions/php-5.2.5.tar.bz2
    Conectado...
    Tamaño del fichero: 7773024
    Tipo Mime: application/octet-stream
    [========================================>                                                           ] 40% (3076/7590 kb)

## Véase también

[???](#context.params)
