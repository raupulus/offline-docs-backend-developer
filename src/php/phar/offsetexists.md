---
title: Phar::offsetExists
description: Determina si un fichero existe en el phar
source_url: https://www.php.net/manual/es/phar.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/offsetExists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64290
---

Phar::offsetExists

Determina si un fichero existe en el phar

## Descripción

```php
public Phar::offsetExists(string $localName): bool
```php

Es una implementación de la interfaz ArrayAccess que permite la manipulación directa del contenido de un archivo Phar utilizando los corchetes de acceso al array.

offsetExists() es llamado como `isset` es llamado.

## Parámetros

`localName`  
El nombre de fichero (en ruta relativa) a buscar en el Phar.

## Valores devueltos

Devuelve `true` si el fichero existe en el phar, `false` en caso contrario.

## Ejemplos

Un ejemplo con `Phar::offsetExists`

```
<?php
$p = new Phar(dirname(__FILE__) . '/mon.phar', 0, 'mon.phar');
$p['premierfichier.txt'] = 'premier fichier';
$p['secondfichier.txt'] = 'second fichier';
// las líneas siguientes hacen uso de offsetExists() de forma indirecta
var_dump(isset($p['premierfichier.txt']));
var_dump(isset($p['pasla.txt']));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

`Phar::offsetGet`, `Phar::offsetSet`, `Phar::offsetUnset`
