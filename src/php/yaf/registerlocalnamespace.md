---
title: Yaf_Loader::registerLocalNamespace
description: Registra un prefijo de clase local
source_url: https://www.php.net/manual/es/yaf-loader.registerlocalnamespace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_loader/registerlocalnamespace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: e2f2172bf
order: 105960
---

Yaf_Loader::registerLocalNamespace

Registra un prefijo de clase local

## Descripción

```php
public Yaf_Loader::registerLocalNamespace(mixed $prefix): void
```php

Registra un nombre de prefijo de clase local. `Yaf_Loader` busca clases en dos directorios de bibliotecas, uno se configura mediante [application.library.directory](#configuration.yaf.library) (en application.ini) al que se le llama directorio de bibliotecas local; el otro se configura mediante [yaf.library](#ini.yaf.library) (en php.ini) al que se llamma le directorio de bibliotecas global, ya que puede ser compartido mediante muchas apliacionies en el mismo servidor.

Al desencadenar una autocarga, `Yaf_Loader` determinará en que directorio de bibliotecas debería buscar examinando el nombre de prefijo del nombre de clase faltante. Si el nombre de prefijo está registrado como un paquete de nombres local, entonces se le buscará en el directorio de bibliotecas local, si no, se buscará en el directorio de bibliotecas global.

> [!NOTE]
> Si yaf.library no está configurado, se asume que el directorio de bibliotecas global es el directorio de bibliotecas local. En este caso, todas las auto cargas buscarán en el directorio de bibliotecas local. Aunque si se quiere que una aplicación Yaf sea fuerte, se han de registrar siempre las propias clases como clases locales.

## Parámetros

`prefix`  
Un string o un a array con el prefijo del nombre de la clase. Todas las clases con este prefijo se cargarán en la ruta de la biblioteca local.

## Valores devueltos

Devuelve un booleano.

## Ejemplos

Ejemplo de `Yaf_Loader::registerLocalNamespace`

```
<?php
$loader = Yaf_Loader::getInstance('/local/library/', '/global/library');
$loader->registerLocalNamespace("Baidu");
$loader->registerLocalNamespace(array("Sina", "Weibo"));

$loader->autoload("Baidu_Name"); // buscar en '/local/library/'
$loader->autoload("Sina");       // buscar en '/local/library/'
$loader->autoload("Global_Name");// buscar en '/global/library/'
$loader->autoload("Foo_Bar");    // buscar en '/global/library/'

?>

   
```php
