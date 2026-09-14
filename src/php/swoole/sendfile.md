---
title: Swoole\Client::sendfile
description: Envía un fichero al socket TCP remoto.
source_url: https://www.php.net/manual/es/swoole-client.sendfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/client/sendfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 91090
---

Swoole\Client::sendfile

Envía un fichero al socket TCP remoto.

## Descripción

```php
public Swoole\Client::sendfile(string $filename, [int $offset]): bool
```php

Esto es una envoltura de la llamada al sistema sendfile de Linux.

## Parámetros

`filename`  
La ruta del fichero a enviar.

`offset`  
El desplazamiento del fichero a enviar.

## Valores devueltos
