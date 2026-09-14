---
title: ReflectionExtension::info
description: Muestra información sobre la extensión
source_url: https://www.php.net/manual/es/reflectionextension.info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: e62098163
order: 70260
---

ReflectionExtension::info

Muestra información sobre la extensión

## Descripción

```php
public ReflectionExtension::info(): void
```php

Muestra el extracto "`phpinfo`" de la extensión proporcionada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Información sobre la extensión.

## Ejemplos

Ejemplo con ReflectionExtension::info

```
<?php
$ext = new ReflectionExtension('mysqli');
$ext->info();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    mysqli

    Soporte MysqlI => activado
    Versión de la biblioteca de la API del cliente => mysqlnd 8.3.17
    Conexiones persistentes activas => 0
    Conexiones persistentes inactivas => 0
    Conexiones activas => 0
    Caché persistente => activado
    put_hits => 0
    put_misses => 0
    get_hits => 0
    get_misses => 0
    size => 2000
    free_items => 2000
    references => 2

    Directiva => Valor Local => Valor Maestro
    mysqli.max_links => Ilimitado => Ilimitado
    mysqli.max_persistent => Ilimitado => Ilimitado
    mysqli.allow_persistent => On => On
    mysqli.default_host => no value => no value
    mysqli.default_user => no value => no value
    mysqli.default_pw => no value => no value
    mysqli.default_port => 3306 => 3306
    mysqli.default_socket => no value => no value
    mysqli.reconnect => Off => Off
    mysqli.allow_local_infile => On => On
    mysqli.cache_size => 2000 => 2000

## Véase también

ReflectionExtension::getName, `phpinfo`
