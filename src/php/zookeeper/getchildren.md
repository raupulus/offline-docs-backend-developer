---
title: Zookeeper::getChildren
description: Lista los hijos de un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.getchildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/getchildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109640
---

Zookeeper::getChildren

Lista los hijos de un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::getChildren(string $path, [callable $watcher_cb]): array
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`watcher_cb`  
Si es distinto de cero, se definirá un observador en el servidor para notificar al cliente si cambia el nodo.

## Valores devueltos

Devuelve un array con las rutas de los hijos en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia PHP cuando el número de parámetros o tipos son incorrectos, o cuando la lista de hijos de un nodo ha fallado.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::getChildren

Lista los hijos de un nodo.

```
<?php

$zookeeper = new Zookeeper('localhost:2181');
$path = '/zookeeper';
$r = $zookeeper->getchildren($path);

if ($r) {
    var_dump($r);
} else {
    echo 'ERR';
}

?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      string(6) "config"
    }

## Véase también

Zookeeper::create

Zookeeper::delete

ZookeeperException
