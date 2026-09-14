---
title: Phar::setMetadata
description: Establece las metadatos del archivo phar
source_url: https://www.php.net/manual/es/phar.setmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/setMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64360
---

Phar::setMetadata

Establece las metadatos del archivo phar

## Descripción

```php
public Phar::setMetadata(mixed $metadata): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

`Phar::setMetadata` debe ser utilizada para almacenar datos personalizados que describen el archivo phar, como una entidad separada. `PharFileInfo::setMetadata` debe ser utilizada para las metadatos específicas de los ficheros. Las metadatos pueden disminuir el rendimiento de carga de un archivo phar si los datos son grandes.

Un uso posible de las metadatos es la especificación de los ficheros a utilizar dentro del archivo para ejecutarlo, o la ubicación de un fichero de manifiesto como el fichero package.xml de [PEAR](https://pear.php.net/). En general, cualquier dato útil que describa el archivo phar puede ser almacenado.

## Parámetros

`metadata`  
Cualquier variable PHP que contenga información a almacenar y que describa el archivo phar

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Un ejemplo con `Phar::setMetadata`

```
<?php
// se asegura de que el phar no exista ya
@unlink('nuevo.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/nuevo.phar', 0, 'nuevo.phar');
    $p['fichero.php'] = '<?php echo "hola"';
    $p->setMetadata(array('cargador' => 'fichero.php'));
    var_dump($p->getMetadata());
} catch (Exception $e) {
    echo 'No puede crear/modificar el phar :', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["cargador"]=>
      string(11) "fichero.php"
    }

## Véase también

`Phar::getMetadata`, `Phar::delMetadata`, `Phar::hasMetadata`
