---
title: hash_update_stream
description: Introduce datos en un contexto de hash activo desde un flujo abierto
source_url: https://www.php.net/manual/es/function.hash-update-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-update-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: a19139232
order: 29350
---

hash_update_stream

Introduce datos en un contexto de hash activo desde un flujo abierto

## Descripción

```php
hash_update_stream(HashContext $context, resource $stream, [int $length]): int
```php

## Parámetros

`context`  
Contexto de hash devuelto por `hash_init`.

`stream`  
Gestor de fichero abierto como el devuelto por cualquier función de creación de flujos.

`length`  
Número máximo de caracteres a copiar desde `stream` al contexto de hash.

## Valores devueltos

Número real de bytes añadidos al contexto de hash desde `stream`.

## Historial de cambios

| Versión | Descripción                                |
|---------|--------------------------------------------|
| 7.2.0   | Acepta `HashContext` en lugar de resource. |

## Ejemplos

Ejemplo de `hash_update_stream`

```
<?php
$fp = tmpfile();
fwrite($fp, 'jumped over the lazy dog.');
rewind($fp);

$ctx = hash_init('sha256');
hash_update($ctx, 'The quick brown fox ');
hash_update_stream($ctx, $fp);
echo hash_final($ctx);
?>

    
```php

El ejemplo anterior mostrará:

    68b1282b91de2c054c36629cb8dd447f12f096d3e3c587978dc2248444633483

## Véase también

`hash_init`, `hash_update`, `hash_final`
