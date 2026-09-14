---
title: Zookeeper::delete
description: Elimina un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109600
---

Zookeeper::delete

Elimina un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::delete(string $path, [int $version]): bool
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`version`  
La versión esperada del nodo. La función fallará si la versión actual del nodo no coincide con la versión esperada. Si se utiliza -1, la comprobación de la versión no tendrá lugar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia de PHP si el número de parámetros o los tipos son incorrectos o si la eliminación del nodo ha fallado.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::delete

Elimina un nodo existente.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$path = '/path/to/node';
$r = $zookeeper->delete($path);
if ($r)
  echo 'SUCCESS';
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    SUCCESS

## Véase también

Zookeeper::create

Zookeeper::getChildren

ZookeeperException
