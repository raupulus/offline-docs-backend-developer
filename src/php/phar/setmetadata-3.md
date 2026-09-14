---
title: PharFileInfo::setMetadata
description: Establece las metadatos específicas de un fichero
source_url: https://www.php.net/manual/es/pharfileinfo.setmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/setMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64850
---

PharFileInfo::setMetadata

Establece las metadatos específicas de un fichero

## Descripción

```php
public PharFileInfo::setMetadata(mixed $metadata): void
```php

`PharFileInfo::setMetadata` debe ser utilizada únicamente para almacenar datos personalizados en un fichero que no pueden ser almacenados con las informaciones normalmente almacenadas con el fichero. Las metadatos pueden degradar el rendimiento de carga de un archivo phar si los datos son demasiado pesados o si hay muchos ficheros con metadatos. Es importante señalar que los permisos de ficheros son soportados nativamente en un phar; es posible fijarlos con el método `PharFileInfo::chmod`. Al igual que con todas las funcionalidades que modifican el contenido del phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar a off para tener éxito si el fichero está dentro de un archivo `Phar`. Los ficheros dentro de archivos `PharData` no tienen esta restricción.

Un uso posible de las metadatos es el paso de un usuario/grupo que debería ser utilizado cuando un fichero es extraído del phar hacia el disco. También puede especificarse un tipo MIME a devolver. En general, puede almacenarse cualquier dato útil que describa un fichero pero que no pueda ser inscrito directamente en él.

## Parámetros

`metadata`  
Cualquier variable PHP que contenga información a almacenar aparte del fichero

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Un ejemplo con `PharFileInfo::setMetadata`

```
<?php
// se asegura de que el phar no exista ya
@unlink('nouveauphar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/nouveauphar.phar', 0, 'nouveauphar.phar');
    $p['fichier.txt'] = 'salut';
    $p['fichier.txt']->setMetadata(array('utilisateur' => 'PhilDaiguille', 'mime-type' => 'text/plain'));
    var_dump($p['fichier.txt']->getMetadata());
} catch (Exception $e) {
    echo 'No puede crear/modificar el phar : ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["utilisateur"]=>
      string(7) "PhilDaiguille"
      ["mime-type"]=>
      string(10) "text/plain"
    }

## Véase también

`PharFileInfo::hasMetadata`, `PharFileInfo::getMetadata`, `PharFileInfo::delMetadata`, `Phar::setMetadata`, `Phar::hasMetadata`, `Phar::getMetadata`
