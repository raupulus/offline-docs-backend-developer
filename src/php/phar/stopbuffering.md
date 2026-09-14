---
title: Phar::stopBuffering
description: Detiene el almacenamiento en búfer de las escrituras Phar y provoca la
  escritura en el disco
source_url: https://www.php.net/manual/es/phar.stopbuffering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/stopBuffering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64400
---

Phar::stopBuffering

Detiene el almacenamiento en búfer de las escrituras Phar y provoca la escritura en el disco

## Descripción

```php
public Phar::stopBuffering(): void
```php

`Phar::stopBuffering` se utiliza en conjunción con el método `Phar::startBuffering`. `Phar::startBuffering` puede proporcionar un aumento de rendimiento durante la creación o modificación de un archivo Phar con un gran número de ficheros. Normalmente, cada vez que un fichero dentro del archivo Phar es creado o modificado, el archivo Phar completo se recrea incluyendo los cambios. De esta manera, el archivo estará siempre actualizado respecto a las operaciones que se le aplican.

Aunque esto puede parecer innecesario durante la creación de un archivo Phar simple, adquiere sentido al escribir el archivo Phar completo de una sola vez. Asimismo, es frecuentemente necesario realizar una serie de cambios y asegurarse de que todos son posibles antes de escribir en el disco, de manera similar a las transacciones de las bases de datos relacionales. Las funciones `Phar::startBuffering`/`Phar::stopBuffering` están disponibles con este propósito.

El almacenamiento en búfer Phar se realiza por archivo, el búfer activo para el archivo Phar `foo.phar` no afecta a los cambios realizados en el archivo Phar `bar.phar`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Se lanza una excepción `PharException` si se encuentran problemas durante la escritura de los cambios en el disco.

## Ejemplos

Un ejemplo `Phar::stopBuffering`

```
<?php
$p = new Phar(dirname(__FILE__) . '/nouveau.phar', 0, 'nouveau.phar');
$p['fichier1.txt'] = 'salut';
$p->startBuffering();
var_dump($p->getStub());
$p->setStub("<?php
function __autoload(\$class)
{
    include 'phar://nouveau.phar/' . str_replace('_', '/', \$class) . '.php';
}
Phar::mapPhar('nouveau.phar');
include 'phar://nouveau.phar/demarrage.php';
__HALT_COMPILER();");
$p->stopBuffering();
var_dump($p->getStub());
?>

    
```php

El ejemplo anterior mostrará:

    string(24) "<?php __HALT_COMPILER();"
    string(195) "<?php
    function __autoload($class)
    {
        include 'phar://' . str_replace('_', '/', $class);
    }
    Phar::mapPhar('nouveau.phar');
    include 'phar://nouveau.phar/demarrage.php';
    __HALT_COMPILER();"

## Véase también

`Phar::startBuffering`, `Phar::isBuffering`
