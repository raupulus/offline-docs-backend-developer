---
title: Zookeeper::create
description: Crear un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109590
---

Zookeeper::create

Crear un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::create(string $path, string $value, array $acls, [int $flags]): string
```php

Este método crea un nodo en ZooKeeper. Sólo se puede crear un nodo si aún no existe. Las banderas de creación afectan a la creación de nodos. Si se establece el indicador ZOO_EPHEMERAL, el nodo se eliminará automáticamente si desaparece la sesión del cliente. Si el indicador ZOO_SEQUENCE está activado, se añade un número de secuencia ascendente único al nombre de la ruta.

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`value`  
Los datos que se almacenarán en el nodo.

`acls`  
La ACL inicial del nodo. La ACL no debe ser nula ni estar vacía.

`flags`  
Este parámetro puede establecerse en 0 para una creación normal o en una combinación OR de las banderas de creación.

## Valores devueltos

Devuelve la ruta del nuevo nodo (puede ser diferente de la ruta suministrada debido a la bandera ZOO_SEQUENCE) en caso de éxito, y false en caso de fallo.

## Errores/Excepciones

Este método emite un error/advertencia de PHP si el número de parámetros o tipos es incorrecto o si la creación del nodo ha fallado.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::create

Crea un nuevo nodo.

```
<?php
$zookeeper = new Zookeeper('localhost:2181');
$aclArray = array(
  array(
    'perms'  => Zookeeper::PERM_ALL,
    'scheme' => 'world',
    'id'     => 'anyone',
  )
);
$path = '/path/to/newnode';
$realPath = $zookeeper->create($path, null, $aclArray);
if ($realPath)
  echo $realPath;
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    /path/to/newnode

## Véase también

Zookeeper::delete

Zookeeper::getChildren

Permisos de ZooKeeper

ZookeeperException
