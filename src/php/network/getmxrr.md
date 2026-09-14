---
title: getmxrr
description: Devuelve los registros MX de un host
source_url: https://www.php.net/manual/es/function.getmxrr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/getmxrr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_revision: 0c9c2dd66
order: 56320
---

getmxrr

Devuelve los registros MX de un host

## Descripción

```php
getmxrr(string $hostname, array $hosts, [array $weights]): bool
```php

Realiza una búsqueda DNS para obtener los registros MX del host `hostname`.

## Parámetros

`hostname`  
El nombre de host de Internet.

`hosts`  
La lista de registros MX se coloca en el array `hosts`.

`weights`  
Si se proporciona el array `weights`, será rellenado con la información de pesos.

## Valores devueltos

Devuelve `true` si se encuentran registros, y `false` si ocurre un error, o si la búsqueda falla.

## Notas

> [!NOTE]
> Esta función no debe utilizarse para verificar direcciones. Solo se devuelven los servidores de correo listados en los registros DNS. Según la [RFC 2821](https://datatracker.ietf.org/doc/html/rfc2821), cuando no se lista ningún servidor de correo, `hostname` debe usarse como servidor de correo, con prioridad `0`.

> [!NOTE]
> Para compatibilidad con versiones no soportadas, utilice la clase [PEAR](https://pear.php.net/): [Net_DNS](https://pear.php.net/package/Net_DNS).

## Véase también

`checkdnsrr`, `dns_get_record`, `gethostbyname`, `gethostbynamel`, `gethostbyaddr`, la página del manual `named(8)`
