---
title: Yaf_Loader::registerNamespace
description: Registra un espacio de nombre con ruta de búsqueda
source_url: https://www.php.net/manual/es/yaf-loader.registernamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_loader/registernamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: e2f2172bf
order: 105970
---

Yaf_Loader::registerNamespace

Registra un espacio de nombre con ruta de búsqueda

## Descripción

```php
public Yaf_Loader::registerNamespace(string $namespaces, [string $path]): bool
```php

Registra un espacio de nombres con una ruta de búsqueda, `Yaf_Loader` busca clases bajo este espacio de nombres en la ruta, el uno es también podría ser configurado vía [ application.library.directory.namespace](#configuration.yaf.library.namespace)(in application.ini);

> [!NOTE]
> Yaf sigue pensando que el subrayado es un separador de carpetas.

## Parámetros

`namespace`  
un string de espacio de nombre, o un array de espacio de nombres con rutas.

`path`  
un string de ruta, es mejor usar la ruta abosoluta aquí para la ejecución.

## Valores devueltos

bool

## Ejemplos

Ejemplo de `Yaf_Loader::registerNamespace`

```
<?php
$loader = Yaf_Loader::getInstance();
$loader->registerNamespace("\Vendor\PHP", "/var/lib/php");
$loader->registerNamespace(array(
     "\Vendor\ASP" => "/var/lib/asp",
     "\Vendor\JSP" => "/usr/lib/vendor/",
));

$loader->autoload("\Vendor\PHP\Dummy");   //load '/var/lib/php/Dummy.php'
$loader->autoload("\Vendor\PHP\Foo_Bar"); //load '/var/lib/php/Foo/Bar.php'
$loader->autoload("\Vendor\JSP\Dummy");   //load '/usr/lib/vendor/Dummy.php'

?>

   
```php
