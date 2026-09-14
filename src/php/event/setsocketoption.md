---
title: EventUtil::setSocketOption
description: Define las opciones del socket
source_url: https://www.php.net/manual/es/eventutil.setsocketoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventutil/setsocketoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 20480
---

EventUtil::setSocketOption

Define las opciones del socket

## Descripción

```php
public static EventUtil::setSocketOption(mixed $socket, int $level, int $optname, mixed $optval): bool
```php

Define las opciones del socket.

## Parámetros

`socket`  
Recurso de socket, flujo, o descriptor de fichero numérico asociado con el socket.

`level`  
Una constante `EventUtil::SOL_*`. Especifica el nivel del protocolo en el cual residen las opciones. Por ejemplo, para recuperar las opciones a nivel de socket, el parámetro `level` debe ser establecido al valor `EventUtil::SOL_SOCKET`. Otros niveles, como TCP, pueden ser utilizados especificando el número del protocolo de ese nivel. Los números de los protocolos pueden ser encontrados utilizando la función `getprotobyname`. Ver también las [constantes EventUtil](#eventutil.constants).

`optname`  
Nombre de la opción (tipo). Tiene el mismo significado que el parámetro correspondiente de la función `socket_get_option`. Ver también las [constantes EventUtil](#eventutil.constants).

`optval`  
Acepta los mismos valores que el parámetro `optval` de la función `socket_get_option`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

socket_get_option

socket_set_option
