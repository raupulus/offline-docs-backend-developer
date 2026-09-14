---
title: Comparación de objetos
source_url: https://www.php.net/manual/es/language.oop5.object-comparison.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/object-comparison.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: a9edd62d0
order: 2530
---

## Comparación de objetos

Al utilizar el operador de comparación (`==`), los objetos se comparan de manera simple, es decir: dos objetos son iguales si tienen los mismos atributos y valores (los valores se comparan con el operador `==`), y si son instancias de la misma clase.

Al utilizar el operador de identidad (`===`), los objetos son idénticos únicamente si hacen referencia a la misma instancia de la misma clase.

Un ejemplo ilustrará estas reglas.

Ejemplo de comparación de objetos en PHP

```php
<?php
function bool2str($bool)
{
    if ($bool === false) {
            return 'FALSE';
    } else {
            return 'TRUE';
    }
}

function compareObjects(&$o1, &$o2)
{
    echo 'o1 == o2 : '.bool2str($o1 == $o2)."\n";
    echo 'o1 != o2 : '.bool2str($o1 != $o2)."\n";
    echo 'o1 === o2 : '.bool2str($o1 === $o2)."\n";
    echo 'o1 !== o2 : '.bool2str($o1 !== $o2)."\n";
}

class Flag
{
    public $flag;

    function __construct($flag = true) {
        $this->flag = $flag;
    }
}

class OtherFlag
{
    public $flag;

    function __construct($flag = true) {
        $this->flag = $flag;
    }
}

$o = new Flag();
$p = new Flag();
$q = $o;
$r = new OtherFlag();

echo "Dos instancias de la misma clase\n";
compareObjects($o, $p);

echo "\nDos referencias al mismo objeto\n";
compareObjects($o, $q);

echo "\nInstancias de clases diferentes\n";
compareObjects($o, $r);
?>

     
```

El ejemplo anterior mostrará:

    Dos instancias de la misma clase
    o1 == o2 : TRUE
    o1 != o2 : FALSE
    o1 === o2 : FALSE
    o1 !== o2 : TRUE

    Dos referencias al mismo objeto
    o1 == o2 : TRUE
    o1 != o2 : FALSE
    o1 === o2 : TRUE
    o1 !== o2 : FALSE

    Instancias de clases diferentes
    o1 == o2 : FALSE
    o1 != o2 : TRUE
    o1 === o2 : FALSE
    o1 !== o2 : TRUE

> [!NOTE]
> Las extensiones pueden definir sus propias reglas para sus comparaciones de objetos (`==`).
