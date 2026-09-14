---
title: Phar::getStub
description: Retorna el cargador PHP o el contenedor de carga de un archivo Phar
source_url: https://www.php.net/manual/es/phar.getstub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/getStub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 64140
---

Phar::getStub

Retorna el cargador PHP o el contenedor de carga de un archivo Phar

## Descripción

```php
public Phar::getStub(): string
```php

Los archivos phar contienen un cargador, o contenedor (`stub`), escrito en PHP que se ejecuta cuando el archivo mismo es ejecutado ya sea por inclusión:

```
    
<?php
include 'monphar.phar';
?>
    
   
```php

o por simple ejecución:

        
    php monphar.phar
        
       

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Retorna un string con el contenido del contenedor de carga (`stub`) del archivo phar actual.

## Errores/Excepciones

Levanta una excepción `RuntimeException` si no es posible leer el contenedor de carga del archivo Phar.

## Ejemplos

Ejemplo con `Phar::getStub`

```
<?php
$p = new Phar('/ruta/versus/mon.phar', 0, 'mon.phar');
echo $p->getStub();
echo "==SIGUIENTE==\n";
$p->setStub("<?php
function __autoload($class)
{
    include 'phar://' . str_replace('_', '/', $class);
}
Phar::mapPhar('monphar.phar');
include 'phar://monphar.phar/inicio.php';
__HALT_COMPILER(); ?>");
echo $p->getStub();
?>

    
```php

El ejemplo anterior mostrará:

    <?php __HALT_COMPILER(); ?>
    ==SIGUIENTE==
    <?php
    function __autoload($class)
    {
        include 'phar://' . str_replace('_', '/', $class);
    }
    Phar::mapPhar('monphar.phar');
    include 'phar://monphar.phar/inicio.php';
    __HALT_COMPILER(); ?>

## Véase también

`Phar::setStub`, `Phar::createDefaultStub`
