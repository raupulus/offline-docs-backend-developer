---
title: Phar::isBuffering
description: Determina si las operaciones de escritura de Phar están en búfer o se
  escriben directamente en el disco
source_url: https://www.php.net/manual/es/phar.isbuffering.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/isBuffering.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64200
---

Phar::isBuffering

Determina si las operaciones de escritura de Phar están en búfer o se escriben directamente en el disco

## Descripción

```php
public Phar::isBuffering(): bool
```php

Este método puede ser utilizado para determinar si un Phar guardará sus cambios inmediatamente en el disco o si es necesario un llamado a la función `Phar::stopBuffering` para escribir las modificaciones.

El búfer de escritura de Phar se realiza por archivo; el búfer del archivo Phar `foo.phar` no afecta en nada los cambios realizados en el archivo Phar `bar.phar`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si las operaciones de escritura están en búfer, `false` en caso contrario.

## Ejemplos

Un ejemplo con `Phar::isBuffering`

```
<?php
$p = new Phar(dirname(__FILE__) . '/nouveauphar.phar', 0, 'nouveauphar.phar');
$p2 = new Phar('pharexistant.phar');
$p['fichier1.txt'] = 'salut';
var_dump($p->isBuffering());
var_dump($p2->isBuffering());
?>
=2=
<?php
$p->startBuffering();
var_dump($p->isBuffering());
var_dump($p2->isBuffering());
$p->stopBuffering();
?>
=3=
<?php
var_dump($p->isBuffering());
var_dump($p2->isBuffering());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    =2=
    bool(true)
    bool(false)
    =3=
    bool(false)
    bool(false)

## Véase también

`Phar::startBuffering`, `Phar::stopBuffering`
