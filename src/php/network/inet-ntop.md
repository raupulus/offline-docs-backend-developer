---
title: inet_ntop
description: Convierte un paquete de direcciones internet en una representación legible
  por humanos
source_url: https://www.php.net/manual/es/function.inet-ntop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/inet-ntop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56450
---

inet_ntop

Convierte un paquete de direcciones internet en una representación legible por humanos

## Descripción

```php
inet_ntop(string $ip): string
```php

Convierte una dirección IPv4 de 32 bits o IPv6 de 128 bits (si PHP ha sido compilado con soporte IPv6) en un string que representa una familia de direcciones.

## Parámetros

`ip`  
Una dirección IPv4 de 32 bits o IPv6 de 128 bits.

## Valores devueltos

Devuelve una representación de la dirección, en forma de un `string` o `false` si ocurre un error.

## Ejemplos

Ejemplo con `inet_ntop`

```
<?php
$packed = chr(127) . chr(0) . chr(0) . chr(1);
$expanded = inet_ntop($packed);

/* Muestra: 127.0.0.1 */
echo $expanded;

$packed = str_repeat(chr(0), 15) . chr(1);
$expanded = inet_ntop($packed);

/* Muestra: ::1 */
echo $expanded;
?>

    
```php

## Véase también

`long2ip`, `ip2long`, `inet_pton`
