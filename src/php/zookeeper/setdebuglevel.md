---
title: Zookeeper::setDebugLevel
description: Define el nivel de depuración de la biblioteca
source_url: https://www.php.net/manual/es/zookeeper.setdebuglevel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/setdebuglevel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109720
---

Zookeeper::setDebugLevel

Define el nivel de depuración de la biblioteca

## Descripción

```php
public static Zookeeper::setDebugLevel(int $logLevel): bool
```php

## Parámetros

`logLevel`  
Constantes de nivel de depuración de ZooKeeper.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el número de parámetros o los tipos son incorrectos o no definen el nivel de depuración.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::setDebugLevel

Define el nivel de depuración.

```
<?php
$r = Zookeeper::setDebugLevel(Zookeeper::LOG_LEVEL_WARN);
if ($r)
  echo 'SUCCESS';
else
  echo 'ERR';
?>
?>

   
```php

El ejemplo anterior mostrará:

    SUCCESS

## Véase también

Nivel de registro ZooKeeper

ZookeeperException
