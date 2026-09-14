---
title: MultipleIterator::__construct
description: Construye un nuevo objeto MultipleIterator
source_url: https://www.php.net/manual/es/multipleiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/multipleiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 82630
---

MultipleIterator::\_\_construct

Construye un nuevo objeto MultipleIterator

## Descripción

```php
public MultipleIterator::__construct([int $flags])
```php

Construye un nuevo objeto MultipleIterator.

## Parámetros

`flags`  
La bandera a definir, según las [constantes](#multipleiterator.constants). `MultipleIterator::MIT_NEED_ALL` o `MultipleIterator::MIT_NEED_ANY`, `MultipleIterator::MIT_KEYS_NUMERIC` o `MultipleIterator::MIT_KEYS_ASSOC`

Por omisión, vale `MultipleIterator::MIT_NEED_ALL`\|`MultipleIterator::MIT_KEYS_NUMERIC`.

## Ejemplos

Iterar un MultipleIterator

```
<?php
$people = new ArrayIterator(array('John', 'Jane', 'Jack', 'Judy'));
$roles  = new ArrayIterator(array('Developer', 'Scrum Master', 'Project Owner'));

$team = new MultipleIterator($flags);
$team->attachIterator($people, 'person');
$team->attachIterator($roles, 'role');

foreach ($team as $member) {
    print_r($member);
}
?>

    
```php

Mostrado con `$flags = MIT_NEED_ALL|MIT_KEYS_NUMERIC`

    Array
    (
        [0] => John
        [1] => Developer
    )
    Array
    (
        [0] => Jane
        [1] => Scrum Master
    )
    Array
    (
        [0] => Jack
        [1] => Project Owner
    )
        

Mostrado con `$flags = MIT_NEED_ANY|MIT_KEYS_NUMERIC`

    Array
    (
        [0] => John
        [1] => Developer
    )
    Array
    (
        [0] => Jane
        [1] => Scrum Master
    )
    Array
    (
        [0] => Jack
        [1] => Project Owner
    )
    Array
    (
        [0] => Judy
        [1] =>
    )
        

Mostrado con `$flags = MIT_NEED_ALL|MIT_KEYS_ASSOC`

    Array
    (
        [person] => John
        [role] => Developer
    )
    Array
    (
        [person] => Jane
        [role] => Scrum Master
    )
    Array
    (
        [person] => Jack
        [role] => Project Owner
    )
        

Mostrado con `$flags = MIT_NEED_ANY|MIT_KEYS_ASSOC`

    Array
    (
        [person] => John
        [role] => Developer
    )
    Array
    (
        [person] => Jane
        [role] => Scrum Master
    )
    Array
    (
        [person] => Jack
        [role] => Project Owner
    )
    Array
    (
        [person] => Judy
        [role] =>
    )

## Véase también

[Las constantes](#multipleiterator.constants), MultipleIterator::valid
