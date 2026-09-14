---
title: stream_get_contents
description: Lee todo un flujo en un string
source_url: https://www.php.net/manual/es/function.stream-get-contents.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-get-contents.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 8f0d3cbca
order: 87950
---

stream_get_contents

Lee todo un flujo en un string

## Descripción

```php
stream_get_contents(resource $stream, [int $length], [int $offset]): string
```php

`stream_get_contents` es idéntica a `file_get_contents`, salvo que opera sobre un puntero de fichero ya abierto y devuelve el contenido restante, hasta `length` bytes, en un string y comenzando en la posición `offset`.

## Parámetros

`stream` (`resource`)  
Un `resource` de flujo (por ejemplo, devuelto por la función `fopen`)

`length` (`int`)  
El número máximo de bytes a leer. Por omisión, `null` (lee todo el contenido restante del buffer).

`offset` (`int`)  
Se desplaza a la posición especificada antes de la lectura. Si el número pasado es negativo, no se realizará ningún desplazamiento y la lectura comenzará desde la posición actual.

## Valores devueltos

Devuelve un `string` o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` ahora es nullable. |

## Ejemplos

Ejemplo con `stream_get_contents`

```
<?php

if ($stream = fopen('http://www.example.com', 'r')) {
    // muestra toda la página, comenzando en la posición 10
    echo stream_get_contents($stream, -1, 10);

    fclose($stream);
}

if ($stream = fopen('http://www.exemple.net', 'r')) {
    // Muestra los 5 primeros bytes
    echo stream_get_contents($stream, 5);

    fclose($stream);
}

?>

   
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

> [!NOTE]
> Cuando se especifica un valor de `length` distinto de `null`, esta función asignará inmediatamente un buffer interno de ese tamaño, incluso si el contenido real es significativamente más corto.

## Véase también

`fgets`, `fread`, `fpassthru`
