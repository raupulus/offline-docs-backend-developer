---
title: ReflectionClass::isCloneable
description: Proporciona información sobre la propiedad de duplicación de la clase
source_url: https://www.php.net/manual/es/reflectionclass.iscloneable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/iscloneable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69450
---

ReflectionClass::isCloneable

Proporciona información sobre la propiedad de duplicación de la clase

## Descripción

```php
public ReflectionClass::isCloneable(): bool
```php

Indica si esta clase es clonable.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la clase puede ser clonada, `false` en caso contrario.

## Ejemplos

Uso básico de ReflectionClass::isCloneable

```
<?php
class NotCloneable {
    public $var1;

    private function __clone() {
    }
}

class Cloneable {
    public $var1;
}

$notCloneable = new ReflectionClass('NotCloneable');
$cloneable = new ReflectionClass('Cloneable');

var_dump($notCloneable->isCloneable());
var_dump($cloneable->isCloneable());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
