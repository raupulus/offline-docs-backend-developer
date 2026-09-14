---
title: Zookeeper::isRecoverable
description: Comprueba si se puede recuperar el estado actual de la conexión zookeeper
source_url: https://www.php.net/manual/es/zookeeper.isrecoverable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/isrecoverable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109690
---

Zookeeper::isRecoverable

Comprueba si se puede recuperar el estado actual de la conexión zookeeper

## Descripción

```php
public Zookeeper::isRecoverable(): bool
```php

La aplicación debería cerrar el gestor e intentar volver a conectarse.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve true/false en caso de éxito y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia PHP cuando la operación falla.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::\_\_construct

Zookeeper::connect

Zookeeper::getClientId

Estado de ZooKeeper

ZookeeperException
