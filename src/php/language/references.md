---
title: Objetos y referencias
source_url: https://www.php.net/manual/es/language.oop5.references.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/references.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: a9edd62d0
order: 2580
---

## Objetos y referencias

Uno de los pilares de la POO de PHP es el hecho de que los "objetos son pasados por referencia por omisión". Esto no es completamente cierto. Esta sección corrige esta generalización con algunos ejemplos.

Una referencia PHP es un alias, que permite a dos variables diferentes representar el mismo valor. En PHP, una variable objeto no contiene más el objeto en sí mismo como valor. Contiene solo un identificador de objeto, que permite a los métodos de acceso de objetos encontrar dicho objeto. Cuando el objeto es utilizado como argumento, devuelto por una función, o asignado a otra variable, las diferentes variables no son alias: contienen copias del identificador, que apuntan al mismo objeto.

Referencias y Objetos

```php
<?php
class A {
    public $foo = 1;
}

$a = new A;
$b = $a;     // $a y $b son copias del mismo identificador
             // ($a) = ($b) = <id>
$b->foo = 2;
echo $a->foo."\n";

$c = new A;
$d = &$c;    // $c y $d son referencias
             // ($c,$d) = <id>

$d->foo = 2;
echo $c->foo."\n";

$e = new A;

function foo($obj) {
    // ($obj) = ($e) = <id>
    $obj->foo = 2;
}

foo($e);
echo $e->foo."\n";

?>

   
```

El ejemplo anterior mostrará:

    2
    2
    2
