---
title: stream_socket_pair
description: Crea un par de sockets conectados e inseparables
source_url: https://www.php.net/manual/es/function.stream-socket-pair.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-socket-pair.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 88160
---

stream_socket_pair

Crea un par de sockets conectados e inseparables

## Descripción

```php
stream_socket_pair(int $domain, int $type, int $protocol): array
```php

`stream_socket_pair` crea un par de sockets conectados e inseparables. Esta función se utiliza comúnmente en IPC (`InterProcess Communication`).

## Parámetros

`domain`  
La familia de protocolo a utilizar: `STREAM_PF_INET`, `STREAM_PF_INET6` o `STREAM_PF_UNIX`

`type`  
El tipo de comunicación a utilizar: `STREAM_SOCK_DGRAM`, `STREAM_SOCK_RAW`, `STREAM_SOCK_RDM`, `STREAM_SOCK_SEQPACKET` o `STREAM_SOCK_STREAM`

`protocol`  
El protocolo a utilizar: `STREAM_IPPROTO_ICMP`, `STREAM_IPPROTO_IP`, `STREAM_IPPROTO_RAW`, `STREAM_IPPROTO_TCP` o `STREAM_IPPROTO_UDP`

> [!NOTE]
> Consulte la [lista de constantes de flujo](#stream.constants) para más detalles sobre cada constante.

## Valores devueltos

Devuelve un `array` que contiene los recursos de los dos sockets en caso de éxito, o `false` en caso de fallo.

## Ejemplos

Ejemplo con `stream_socket_pair`

Este ejemplo muestra un uso básico de `stream_socket_pair` en una comunicación interprocesos.

```
<?php

$sockets = stream_socket_pair(STREAM_PF_UNIX, STREAM_SOCK_STREAM, STREAM_IPPROTO_IP);
$pid     = pcntl_fork();

if ($pid == -1) {
  die('Imposible bifurcar');

} else if ($pid) {
  /* padre */
  fclose($sockets[0]);

  fwrite($sockets[1], "PID hijo: $pid\n");
  echo fgets($sockets[1]);

  fclose($sockets[1]);

} else {
  /* hijo */
  fclose($sockets[1]);

  fwrite($sockets[0], "mensaje del hijo\n");
  echo fgets($sockets[0]);

  fclose($sockets[0]);
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    PID hijo: 1378
    mensaje del hijo
