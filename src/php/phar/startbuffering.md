---
title: Phar::startBuffering
description: Inicia el almacenamiento en búfer de escrituras Phar, sin modificar el
  objeto Phar en el disco
source_url: https://www.php.net/manual/es/phar.startbuffering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/startBuffering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64390
---

Phar::startBuffering

Inicia el almacenamiento en búfer de escrituras Phar, sin modificar el objeto Phar en el disco

## Descripción

```php
public Phar::startBuffering(): void
```php

Aunque técnicamente innecesario, el método `Phar::startBuffering` puede proporcionar un aumento de rendimiento durante la creación o modificación de un archivo Phar con un gran número de ficheros. Normalmente, cada vez que un fichero dentro del archivo Phar es creado o modificado, el archivo Phar completo se recrea incluyendo los cambios. De esta manera, el archivo siempre estará actualizado con respecto a las operaciones que se le aplican.

Aunque esto pueda parecer innecesario durante la creación de un archivo Phar simple, adquiere sentido al escribir el archivo Phar completo de una sola vez. Asimismo, es frecuente necesitar realizar una serie de cambios y asegurarse de que todos son posibles antes de escribir en el disco, de manera similar a las transacciones de las bases de datos relacionales. Las funciones `Phar::startBuffering`/`Phar::stopBuffering` están disponibles con este propósito.

El almacenamiento en búfer Phar se realiza por archivo, el búfer activo para el archivo Phar `foo.phar` no afecta a los cambios realizados en el archivo Phar `bar.phar`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Un ejemplo con `Phar::startBuffering`

```
<?php
// se asegura de que el phar no exista ya
@unlink('nouveau.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/nouveau.phar', 0, 'nouveau.phar');
} catch (Exception $e) {
    echo 'No puede crear el phar:', $e;
}
echo 'El nuevo phar tiene ' . $p->count() . " entradas\n";
$p->startBuffering();
$p['fichier.txt'] = 'salut';
$p['fichier2.txt'] = 'jolie';
$p['fichier2.txt']->setCompressedGZ();
$p['fichier3.txt'] = 'môme';
$p['fichier3.txt']->setMetadata(42);
$p->setStub("<?php
function __autoload($class)
{
    include 'phar://monphar.phar/' . str_replace('_', '/', $class) . '.php';
}
Phar::mapPhar('monphar.phar');
include 'phar://monphar.phar/demarrage.php';
__HALT_COMPILER();");
$p->stopBuffering();
?>

    
```php

## Véase también

`Phar::stopBuffering`, `Phar::isBuffering`
