---
title: Zookeeper::close
description: Cierra la conexión con el servidor ZooKeeper y libera los recursos asociados
source_url: https://www.php.net/manual/es/zookeeper.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109560
---

Zookeeper::close

Cierra la conexión con el servidor ZooKeeper y libera los recursos asociados

## Descripción

```php
public Zookeeper::close(): void
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Este método lanza `ZookeeperException` y sus derivados al cerrar una instancia no inicializada.

## Véase también

Zookeeper::\_\_construct

Zookeeper::connect

ZookeeperException
