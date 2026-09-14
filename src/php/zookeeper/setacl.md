---
title: Zookeeper::setAcl
description: Establece la ACL asociada a un nodo de forma sincrónica
source_url: https://www.php.net/manual/es/zookeeper.setacl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zookeeper/zookeeper/setacl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zookeeper
translation_status: ready
translation_reviewed: true
translation_revision: 7cecc752c
order: 109710
---

Zookeeper::setAcl

Establece la ACL asociada a un nodo de forma sincrónica

## Descripción

```php
public Zookeeper::setAcl(string $path, int $version, array $acl): bool
```php

## Parámetros

`path`  
El nombre del nodo. Expresado como un nombre de archivo con barras separando los ancestros del nodo.

`version`  
El número de versión esperado de la ruta.

`acl`  
La ACL que debe definirse en la ruta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Este método emite un error/advertencia de PHP cuando el número de parámetros o los tipos son incorrectos o no se ha podido definir la ACL para un nodo.

> [!CAUTION]
> Desde la versión 0.3.0, este método lanza `ZookeeperException` y sus derivados.

## Ejemplos

Ejemplo de Zookeeper::setAcl

Establece la ACL para un nodo.

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
$zookeeper->setAcl($path, $aclArray);

$r = $zookeeper->getAcl($path);
if ($r)
  var_dump($r);
else
  echo 'ERR';
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      [0]=>
      array(3) {
        ["perms"]=>
        int(31)
        ["scheme"]=>
        string(5) "world"
        ["id"]=>
        string(6) "anyone"
      }
    }

## Véase también

Zookeeper::create

Zookeeper::getAcl

Permisos de ZooKeeper

ZookeeperException
