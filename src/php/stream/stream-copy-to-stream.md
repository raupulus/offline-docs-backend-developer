---
title: stream_copy_to_stream
description: Copia datos desde un flujo hacia otro
source_url: https://www.php.net/manual/es/function.stream-copy-to-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-copy-to-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 6a5b22785
order: 87900
---

stream_copy_to_stream

Copia datos desde un flujo hacia otro

## Descripción

```php
stream_copy_to_stream(resource $from, resource $to, [int $length], [int $offset]): int
```php

Realiza una copia de hasta `length` bytes de datos desde la posición actual del puntero (o desde la posición `offset`, si se especifica) en el flujo `from` hacia el parámetro `to`. Si `length` no está especificado, se copiará todo el resto del flujo `from`.

## Parámetros

`from`  
El flujo de origen

`to`  
El flujo de destino

`length`  
Número máximo de bytes a copiar. Por omisión, se copian todos los bytes restantes.

`offset`  
El desplazamiento donde comenzar la copia de datos

## Valores devueltos

Devuelve el número total de bytes copiados, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` ahora es nullable. |

## Ejemplos

Ejemplo con `stream_copy_to_stream`

```
<?php
$src = fopen('http://www.example.com', 'r');
$dest1 = fopen('first1k.txt', 'w');
$dest2 = fopen('remainder.txt', 'w');

echo stream_copy_to_stream($src, $dest1, 1024) . " bytes copiados a first1k.txt\n";
echo stream_copy_to_stream($src, $dest2) . " bytes copiados a remainder.txt\n";

?>

    
```php

## Véase también

`copy`
