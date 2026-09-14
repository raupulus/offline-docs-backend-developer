---
title: getservbyport
description: Devuelve el servicio de Internet que corresponde al puerto y protocolo
source_url: https://www.php.net/manual/es/function.getservbyport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/getservbyport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56360
---

getservbyport

Devuelve el servicio de Internet que corresponde al puerto y protocolo

## Descripción

```php
getservbyport(int $port, string $protocol): string
```php

`getservbyport` busca el servicio de Internet asociado al puerto `port` para el protocolo `protocol` como en `/etc/services`.

## Parámetros

`port`  
El número del puerto.

`protocol`  
`protocol` puede ser `"tcp"` o `"udp"` (en minúsculas).

## Valores devueltos

Devuelve el nombre del servicio de Internet, en forma de `string`, o `false` si ocurre un error.

## Véase también

`getservbyname`
