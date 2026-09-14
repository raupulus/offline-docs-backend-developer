---
title: Zookeeper::set
description: Define los datos asociados a un nodo
source_url: https://www.php.net/manual/es/zookeeper.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109700
---

Zookeeper::set

Define los datos asociados a un nodo

## Descripción

```php
public Zookeeper::set(string $path, string $value, [int $version], [array $stat]): bool
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`value`  
Los datos que se almacenarán en el nodo.

`version`  
La versión esperada del nodo. La función fallará si la versión actual del nodo no coincide con la versión esperada. Si se utiliza -1, no se realizará la comprobación de la versión.

`stat`  
Si no es NULL, contendrá el valor de las estadísticas de la ruta devuelta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el número de parámetros o los tipos son incorrectos o cuando guardar el valor en el nodo ha fallado.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::set

Guarda un valor en un nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$path = '/path/to/node';
$value = 'nodevalue';
$r = $zookeeper->set($path, $value);
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

Zookeeper::get

ZookeeperException
