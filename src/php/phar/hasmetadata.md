---
title: Phar::hasMetadata
description: Determina si el phar contiene o no metadatos
source_url: https://www.php.net/manual/es/phar.hasmetadata.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/hasMetadata.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64180
---

Phar::hasMetadata

Determina si el phar contiene o no metadatos

## Descripción

```php
public Phar::hasMetadata(): bool
```php

Determina si el phar contiene o no metadatos.

## Parámetros

No se admiten argumentos.

## Valores devueltos

Devuelve `true` si están presentes metadatos, `false` en caso contrario.

## Ejemplos

Un ejemplo con `Phar::hasMetadata`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    var_dump($phar->hasMetadata());
    $phar->setMetadata(array('deschoses' => 'salut'));
    var_dump($phar->hasMetadata());
    $phar->delMetadata();
    var_dump($phar->hasMetadata());
} catch (Exception $e) {
    // manejo de errores
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    bool(false)

## Véase también

`Phar::getMetadata`, `Phar::setMetadata`, `Phar::delMetadata`
