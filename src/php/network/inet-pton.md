---
title: inet_pton
description: Convierte una dirección IP legible en su representación in_addr
source_url: https://www.php.net/manual/es/function.inet-pton.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/inet-pton.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56460
---

inet_pton

Convierte una dirección IP legible en su representación in_addr

## Descripción

```php
inet_pton(string $ip): string
```php

Convierte una dirección IPv4 o IPv6 (si PHP ha sido compilado con el soporte IPv6) legible por humanos en una estructura binaria adecuada de familia de direcciones de 32 bits o 128 bits.

## Parámetros

`ip`  
Una dirección IPv4 o IPv6.

## Valores devueltos

Devuelve la representación `in_addr` de la dirección proporcionada por el argumento `ip` o `false` si el argumento `ip` proporcionado tiene una sintaxis inválida (por ejemplo, una dirección IPv4 sin punto, o una dirección IPv6 sin dos puntos).

## Ejemplos

Ejemplo con `inet_pton`

```
<?php
$in_addr = inet_pton('127.0.0.1');

$in6_addr = inet_pton('::1');
?>

    
```php

## Véase también

`ip2long`, `long2ip`, `inet_ntop`
