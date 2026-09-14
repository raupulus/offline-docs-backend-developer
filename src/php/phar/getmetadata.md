---
title: Phar::getMetadata
description: Devuelve las metadatos del archivo phar
source_url: https://www.php.net/manual/es/phar.getmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_revision: 2b232242b
order: 64100
---

Phar::getMetadata

Devuelve las metadatos del archivo phar

## Descripción

```php
public Phar::getMetadata([array $unserializeOptions]): mixed
```php

Recupera las metadatos del archivo. Estas pueden ser cualquier variable PHP que pueda ser serializada.

> [!CAUTION]
> Acceder a los metadatos activará la deserialización, lo que puede provocar la ejecución de código PHP arbitrario. No utilice esto en archivos phar no confiables ni configure `unserializeOptions` de forma segura.

## Parámetros

No se proporcionan parámetros.

## Valores devueltos

Cualquier variable PHP que pueda ser serializada y que se almacena como metadato del archivo Phar, o `null` si no se almacenan metadatos.

## Historial de cambios

| Versión | Descripción                                      |
|---------|--------------------------------------------------|
| 8.0.0   | Se ha añadido el parámetro `unserializeOptions`. |

## Ejemplos

Un ejemplo con `Phar::getMetadata`

```
<?php
// se asegura de que el phar no exista
@unlink('nouveauphar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/nouveauphar.phar', 0, 'nouveauphar.phar');
    $p['fichier.php'] = '<?php echo "salut";';
    $p->setMetadata(array('bootstrap' => 'fichier.php'));
    var_dump($p->getMetadata());
} catch (Exception $e) {
    echo 'No puede modificar el phar :', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      ["bootstrap"]=>
      string(8) "fichier.php"
    }

## Véase también

`Phar::setMetadata`, `Phar::delMetadata`, `Phar::hasMetadata`
