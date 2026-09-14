---
title: La interfaz IteratorAggregate
source_url: https://www.php.net/manual/es/class.iteratoraggregate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/iteratoraggregate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 4b06b2d5c
order: 3800
---

## Introducción

Interfaz para crear un iterador externo.

## Sinopsis de la interfaz

IteratorAggregate

extends

Traversable

Métodos

## Ejemplos

Ejemplo simple

```php
<?php

class myData implements IteratorAggregate
{
    public function getIterator(): Traversable
    {
        return new ArrayIterator([
            "clave uno" => "elemento uno",
            "clave dos" => "elemento dos",
            "clave tres" => "elemento tres"
        ]);
    }
}

$obj = new myData();

foreach($obj as $key => $value) {
    var_dump($key, $value);
    echo "\n";
}

    
```

Resultado del ejemplo anterior es similar a:

    string(9) "clave uno"
    string(12) "elemento uno"

    string(9) "clave dos"
    string(12) "elemento dos"

    string(10) "clave tres"
    string(13) "elemento tres"
