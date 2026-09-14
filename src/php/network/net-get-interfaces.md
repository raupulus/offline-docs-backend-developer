---
title: net_get_interfaces
description: Devuelve las interfaces de red
source_url: https://www.php.net/manual/es/function.net-get-interfaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/net-get-interfaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: c4ac6c0cf
order: 56490
---

net_get_interfaces

Devuelve las interfaces de red

## Descripción

```php
net_get_interfaces(): array
```php

Devuelve una enumeración de las interfaces de red (adaptadores) en la máquina local.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` asociativo donde la clave es el nombre de la interfaz y el valor es un array asociativo de los atributos de la interfaz, o `false` si ocurre un error.

Cada array asociativo de interfaz contiene:

| Nombre | Descripción |
|----|----|
| description | Un valor de string opcional para la descripción de la interfaz. Solo Windows. |
| mac | Un valor de string opcional para la dirección MAC de la interfaz. Solo Windows. |
| mtu | Un valor integer para la unidad de transmisión máxima (MTU) de la interfaz. Solo Windows. |
| unicast | Un array de arrays asociativos, ver los atributos Unicast a continuación. |
| up | Un bool para el estado (on/off) de la interfaz. |

Atributos de Interfaz

| Nombre  | Descripción                                               |
|---------|-----------------------------------------------------------|
| flags   | Un valor integer.                                         |
| family  | Un valor integer.                                         |
| address | Un valor string para la dirección en IPv4 o IPv6.         |
| netmask | Un valor string para la máscara de subred en IPv4 o IPv6. |

Atributos de Unicast

## Errores/Excepciones

Emite un error `E_WARNING` en caso de fallo al obtener la información de la interfaz.
