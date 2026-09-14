---
title: Ejemplos
source_url: https://www.php.net/manual/es/classobj.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 6f11457f1
order: 6720
---

## Ejemplos

En este ejemplo, se comienza por definir una clase base así como una extensión de esta clase. La clase base describe un vegetal, si puede ser consumido y cuál es su color. La subclase `Spinach` añade un método para cocinarlo, y otro para determinar si está cocido.

Definiciones de las Clases

`Vegetable`

```php
<?php
class Vegetable {
    public $edible;
    public $color;
    public function __construct($edible, $color = "green")
    {
        $this->edible = $edible;
        $this->color = $color;
    }
    public function isEdible()
    {
        return $this->edible;
    }
    public function getColor()
    {
        return $this->color;
    }
}
?>

   
```

`Spinach`

```php
<?php
class Spinach extends Vegetable {
    public $cooked = false;
    public function __construct()
    {
        parent::__construct(true, "green");
    }
    public function cook()
    {
        $this->cooked = true;
    }
    public function isCooked()
    {
        return $this->cooked;
    }
}
?>

   
```

A continuación, se crean dos objetos a partir de estas clases y se muestran información sobre ellos, incluyendo su clase padre. Asimismo, se definen funciones utilitarias, principalmente para obtener una presentación más agradable de las variables.

test_script.php

```php
<?php
// registra el autoloader para cargar las clases
spl_autoload_register();
function printProperties($obj)
{
    foreach (get_object_vars($obj) as $prop => $val) {
        echo "\t$prop = $val\n";
    }
}
function printMethods($obj)
{
    $arr = get_class_methods(get_class($obj));
    foreach ($arr as $method) {
        echo "\tfunction $method()\n";
    }
}
function objectBelongsTo($obj, $class)
{
    if (is_subclass_of($obj, $class)) {
        echo "El objeto pertenece a la clase " . get_class($obj);
        echo ", una subclase de $class\n";
    } else {
        echo "El objeto no pertenece a una subclase de $class\n";
    }
}
// instancia 2 objetos
$veggie = new Vegetable(true, "blue");
$leafy = new Spinach();
// imprime información sobre los objetos
echo "veggie: CLASS " . get_class($veggie) . "\n";
echo "leafy: CLASS " . get_class($leafy);
echo ", PARENT " . get_parent_class($leafy) . "\n";
// muestra las propiedades de veggie
echo "\nveggie: Properties\n";
printProperties($veggie);
// y los métodos de leafy
echo "\nleafy: Methods\n";
printMethods($leafy);
echo "\nParentage:\n";
objectBelongsTo($leafy, Spinach::class);
objectBelongsTo($leafy, Vegetable::class);
?>

   
```

Los ejemplos anteriores mostrarán:

    veggie: CLASS Vegetable
    leafy: CLASS Spinach, PARENT Vegetable
    veggie: Properties
            edible = 1
            color = blue
    leafy: Methods
            function __construct()
            function cook()
            function isCooked()
            function isEdible()
            function getColor()
    Parentage:
    El objeto no pertenece a una subclase de Spinach
    El objeto pertenece a la clase Spinach, una subclase de Vegetable

       

Un aspecto importante a notar en el ejemplo anterior es que el objeto `$leafy` es una instancia de la clase `Spinach` que es una subclase de `Vegetable`.
