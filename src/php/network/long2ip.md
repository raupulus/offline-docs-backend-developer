---
title: long2ip
description: Convierte un entero largo (IPv4) a su notación decimal con puntos
source_url: https://www.php.net/manual/es/function.long2ip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/long2ip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 2537e56cc
order: 56480
---

long2ip

Convierte un entero largo (IPv4) a su notación decimal con puntos

## Descripción

```php
long2ip(int $ip): string
```php

La función `long2ip` genera una dirección Internet en notación decimal con puntos (formato aaa.bbb.ccc.ddd) a partir de su representación como entero largo.

## Parámetros

`ip`  
Una representación adecuada de una dirección en forma de entero largo

## Valores devueltos

Devuelve la dirección IP Internet, en forma de `string`.

## Historial de cambios

| Versión | Descripción                                                    |
|---------|----------------------------------------------------------------|
| 8.4.0   | El tipo de retorno se cambió de `stringfalse` a `string`.      |
| 7.1.0   | El tipo del argumento `ip` fue modificado de `string` a `int`. |

## Notas

> [!NOTE]
> En arquitecturas de 32 bits, convertir la representación de direcciones IP de `string` a `int` no dará resultados correctos para los números que exceden `PHP_INT_MAX`.

## Véase también

`ip2long`
