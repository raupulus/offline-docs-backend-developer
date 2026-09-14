---
title: Zookeeper::get
description: Devuelve los datos asociados a un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109620
---

Zookeeper::get

Devuelve los datos asociados a un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::get(string $path, [callable $watcher_cb], [array $stat], [int $max_size]): string
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`watcher_cb`  
Si es distinto de cero, se definirá un observador en el servidor para notificar al cliente si cambia el nodo.

`stat`  
Si no es NULL, contendrá el valor de las estadísticas de la ruta devuelta.

`max_size`  
El tamaño máximo de los datos. Si se utiliza 0, este método devolverá todos los datos.

## Valores devueltos

Devuelve datos en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia de PHP si el número de parámetros o los tipos son incorrectos, o si la recuperación de datos ha fallado.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::get

Recupera el valor del nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$path = '/path/to/node';
$value = 'nodevalue';
$zookeeper->set($path, $value);

$r = $zookeeper->get($path);
if ($r)
  echo $r;
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    nodevalue

Ejemplo de estadísticas de Zookeeper::get

Devuelve información estadística del nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$path = '/path/to/node';
$stat = [];
$zookeeper->get($path, null, $stat);
var_dump($stat);
?>

   
```php

El ejemplo anterior mostrará:

    array(11) {
      ["czxid"]=>
      float(0)
      ["mzxid"]=>
      float(0)
      ["ctime"]=>
      float(0)
      ["mtime"]=>
      float(0)
      ["version"]=>
      int(0)
      ["cversion"]=>
      int(-2)
      ["aversion"]=>
      int(0)
      ["ephemeralOwner"]=>
      float(0)
      ["dataLength"]=>
      int(0)
      ["numChildren"]=>
      int(2)
      ["pzxid"]=>
      float(0)
    }

## Véase también

Zookeeper::set

ZookeeperException
