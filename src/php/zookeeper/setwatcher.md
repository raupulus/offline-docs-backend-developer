---
title: Zookeeper::setWatcher
description: Define una función de observación
source_url: https://www.php.net/manual/es/zookeeper.setwatcher.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/setwatcher.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109750
---

Zookeeper::setWatcher

Define una función de observación

## Descripción

```php
public Zookeeper::setWatcher(callable $watcher_cb): bool
```php

## Parámetros

`watcher_cb`  
Un observador que será llamado cada vez que el nodo cambie.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia PHP cuando el número de parámetros o los tipos son incorrectos o es imposible cambiar el observador.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Véase también

Zookeeper::exists

Zookeeper::get

ZookeeperException
