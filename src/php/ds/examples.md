---
title: Ejemplos
source_url: https://www.php.net/manual/es/ds.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: 845661fc0
order: 16630
---

## Ejemplos

Vector

```php
<?php

$vector = new \Ds\Vector();

$vector->push('a');
$vector->push('b', 'c');

$vector[] = 'd';

print_r($vector);

?>

  
```

Resultado del ejemplo anterior es similar a:

    Ds\Vector Object
    (
        [0] => a
        [1] => b
        [2] => c
        [3] => d
    )

Map

```php
<?php

$map = new \Ds\Map();

$map->put('a', 1);
$map->put('b', 2);

$map['c'] = 3;

print_r($map);

?>

  
```

Resultado del ejemplo anterior es similar a:

    Ds\Map Object
    (
        [0] => Ds\Pair Object
            (
                [key] => a
                [value] => 1
            )

        [1] => Ds\Pair Object
            (
                [key] => b
                [value] => 2
            )

        [2] => Ds\Pair Object
            (
                [key] => c
                [value] => 3
            )

    )
