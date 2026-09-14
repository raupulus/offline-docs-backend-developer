---
title: Yaf_Loader::getNamespacePath
description: Recupera la ruta de un espacio de nombres registrado
source_url: https://www.php.net/manual/es/yaf-loader.getnamespacepath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_loader/getnamespacepath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: cd2604567
order: 105920
---

Yaf_Loader::getNamespacePath

Recupera la ruta de un espacio de nombres registrado

## Descripción

```php
public Yaf_Loader::getNamespacePath(string $namespaces): string
```php

recupera la ruta de un espacio de nombre registrado

## Parámetros

`namespace`  
un string de espacio de nombre.

## Valores devueltos

ruta `string`, si el espacio de nombre no está registrado, entonces `null` la biblioteca por defecto será devuelta

## Ejemplos

Ejemplo de `Yaf_Loader::registerNamespace`

```
<?php
$loader = Yaf_Loader::getInstance("/var/application/lib");
$loader->registerNamespace("\Vendor\PHP", "/var/lib/php");

$loader->getNamespacePath("\Vendor\PHP"); // '/var/lib/php'
$loader->getNamespacePath("\Vendor\JSP"); // '/var/application/lib'

?>

   
```php
