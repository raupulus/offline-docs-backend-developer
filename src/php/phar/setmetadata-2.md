---
title: PharData::setMetadata
description: Fija las metadatos del archivo
source_url: https://www.php.net/manual/es/phardata.setmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/setMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64660
---

PharData::setMetadata

Fija las metadatos del archivo

## Descripción

```php
public PharData::setMetadata(mixed $metadata): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

`Phar::setMetadata` debe ser utilizado para almacenar metadatos personalizados que describen algo acerca del archivo phar como entidad completa. `PharFileInfo::setMetadata` debe ser utilizado para metadatos específicos de ficheros. Las metadatos pueden degradar el rendimiento de carga de un archivo phar si los datos son demasiado pesados.

Las metadatos pueden ser utilizadas para especificar qué fichero dentro del archivo debe ser utilizado para cargar el archivo o la ubicación de un fichero de manifiesto como el fichero package.xml de [PEAR](https://pear.php.net/). En general, cualquier dato útil que describa el archivo phar puede ser almacenado.

## Parámetros

`metadata`  
Cualquier variable PHP que contenga información a almacenar para describir el archivo phar

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Un ejemplo con `Phar::setMetadata`

```
<?php
// se asegura de que el phar no exista
@unlink('nouveauphar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/nouveauphar.phar', 0, 'nouveauphar.phar');
    $p['fichier.php'] = '<?php echo "salut"';
    $p->setMetadata(array('chargement' => 'fichier.php'));
    var_dump($p->getMetadata());
} catch (Exception $e) {
    echo 'No puede crear/modificar el phar:', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["chargement"]=>
      string(11) "fichier.php"
    }

## Véase también

`Phar::getMetadata`, `Phar::delMetadata`, `Phar::hasMetadata`
