---
title: ip2long
description: Convierte una cadena que contiene una dirección (IPv4) en notación decimal
  con puntos en una dirección entera larga
source_url: https://www.php.net/manual/es/function.ip2long.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/ip2long.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: 184f3f7bd
order: 56470
---

ip2long

Convierte una cadena que contiene una dirección (IPv4) en notación decimal con puntos en una dirección entera larga

## Descripción

```php
ip2long(string $ip): int
```php

La función `ip2long` genera una representación en entero largo de una dirección IPv4 desde su formato estándar (notación decimal con puntos)

`ip2long` también funciona con direcciones IP incompletas. Leer <http://ps-2.kev009.com/wisclibrary/aix52/usr/share/man/info/en_US/a_doc_lib/libs/commtrf2/inet_addr.htm> para más información.

## Parámetros

`ip`  
Una dirección en formato estándar.

## Valores devueltos

Devuelve el entero largo, o `false` si `ip` es inválido.

## Ejemplos

Ejemplo con `ip2long`

```
<?php
$ip = gethostbyname('www.example.com');
$out = "Las URL siguientes son equivalentes :<br />\n";
$out .= 'http://www.example.com/, http://' . $ip . '/, and http://' . sprintf("%u", ip2long($ip)) . "/<br />\n";
echo $out;
?>

    
```php

Mostrar una dirección IP

Este segundo ejemplo muestra cómo mostrar una dirección convertida a través de la función `printf`:

```
<?php
$ip   = gethostbyname('www.example.com');
$long = ip2long($ip);

if ($long == -1 || $long === FALSE) {
    echo 'IP inválida, por favor intente de nuevo';
} else {
    echo $ip   . "\n";            // 192.0.34.166
    echo $long . "\n";            // 3221234342 (-1073732954 en los sistemas de 32-bit, debido al desbordamiento de entero)
    printf("%u\n", ip2long($ip)); // 3221234342
}
?>

    
```php

## Notas

> [!NOTE]
> Como los `int` PHP son firmados y muchas direcciones IP resultarán en enteros negativos en las arquitecturas de 32-bits, se debe utilizar el patrón "%u" de la función `sprintf` o de la función `printf` para obtener la representación en forma de `string` de una dirección IP no firmada.

> [!NOTE]
> `ip2long` devolverá `-1` para la IP `255.255.255.255` en los sistemas de 32-bits debido al desbordamiento del valor entero.

## Véase también

`long2ip`, `sprintf`
