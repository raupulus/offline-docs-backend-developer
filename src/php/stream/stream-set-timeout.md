---
title: stream_set_timeout
description: Configura el tiempo de espera de un flujo
source_url: https://www.php.net/manual/es/function.stream-set-timeout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-set-timeout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: af6fdf16a
order: 88100
---

stream_set_timeout

Configura el tiempo de espera de un flujo

## Descripción

```php
stream_set_timeout(resource $stream, int $seconds, [int $microseconds]): bool
```php

`stream_set_timeout` configura el tiempo de espera del flujo `stream`, expresado como la duración de `seconds` segundos y `microseconds` microsegundos.

Cuando el flujo se agota, la clave 'timed_out' del array devuelto por `stream_get_meta_data` se establece a `true`, sin embargo, no se genera ningún error o alerta.

## Parámetros

`stream`  
El flujo objetivo.

`seconds`  
El número de segundos enteros del tiempo de espera.

`microseconds`  
El número de microsegundos enteros del tiempo de espera.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_set_timeout`

```
<?php
$fp = fsockopen("www.example.com", 80);
if (!$fp) {
     echo "No se puede abrir\n";
} else {

  fwrite($fp, "GET / HTTP/1.0\r\n\r\n");
  stream_set_timeout($fp, 2);
  $res = fread($fp, 2000);

  $info = stream_get_meta_data($fp);
  fclose($fp);

  if ($info['timed_out']) {
     echo '¡Tiempo de conexión agotado!';
  } else {
     echo $res;
  }

}
?>

    
```php

## Notas

> [!NOTE]
> Esta función no funciona con operaciones avanzadas como `stream_socket_recvfrom`, utilice en su lugar `stream_select` con un tiempo de espera como parámetro.

Esta función se llamaba anteriormente `set_socket_timeout`, y también `socket_set_timeout`, pero estos nombres están obsoletos.

## Véase también

fsockopen

fopen
