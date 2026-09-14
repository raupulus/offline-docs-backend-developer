---
title: mb_scrub
description: Reemplaza las secuencias de bytes mal formadas por el carácter de sustitución.
source_url: https://www.php.net/manual/es/function.mb-scrub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-scrub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 77a60306b
order: 45370
---

mb_scrub

Reemplaza las secuencias de bytes mal formadas por el carácter de sustitución.

## Descripción

```php
mb_scrub(string $string, [string $encoding]): string
```php

Realiza una conversión de juego de caracteres desde la codificación especificada, o desde la codificación por omisión si no se ha especificado ninguna, hacia la misma codificación. Esto tiene como efecto reemplazar cualquier secuencia de bytes inválida por el carácter de sustitución.

## Parámetros

`string`  
La cadena de entrada.

`encoding`  
La codificación utilizada para interpretar `string`. Si se omite o es `null`, el parámetro [mbstring.internal_encoding](#ini.mbstring.internal-encoding) será utilizado si está definido, de lo contrario el parámetro [default_charset](#ini.default-charset) será utilizado.

## Valores devueltos

El resultado `string` con las secuencias de bytes inválidas reemplazadas.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `encoding` ahora acepta `null`. |
