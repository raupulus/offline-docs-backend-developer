---
title: Clonación de objetos
source_url: https://www.php.net/manual/es/language.oop5.cloning.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/cloning.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 28529d353
order: 2430
---

## Clonación de objetos

La creación de una copia de un objeto con exactamente las mismas propiedades no siempre es el comportamiento deseado. Un buen ejemplo para ilustrar la necesidad de un constructor de copia: si se tiene un objeto que representa una ventana GTK y el objeto contiene el recurso que representa esa ventana GTK, al crear una copia, se puede desear crear una nueva ventana con las mismas propiedades, pero que el nuevo objeto contenga un recurso que represente la nueva ventana.

Una copia de objeto se crea utilizando la palabra clave `clone` (que invoca al método [\_\_clone()](#object.clone) del objeto, si ha sido definido).

    $copy_of_object = clone $object;

Cuando un objeto es clonado, PHP realiza una copia superficial de todas las propiedades del objeto. Todas las propiedades que son referencias a otras variables permanecerán como referencias.

```php
__clone(): void
```php

Una vez realizada la clonación, si se ha definido un método [\_\_clone()](#object.clone), el método [\_\_clone()](#object.clone) del nuevo objeto será llamado, para permitir que cada propiedad que deba ser modificada lo sea.

Ejemplo de duplicación de objetos

```
<?php
class SubObject
{
  static $instances = 0;
  public $instance;

  public function __construct() {
    $this->instance = ++self::$instances;
  }

  public function __clone() {
    $this->instance = ++self::$instances;
  }
}

class MyCloneable
{
  public $object1;
  public $object2;

  function __clone()
  {
    // Fuerza la copia de this->object, de lo contrario
    // apuntará al mismo objeto.
    $this->object1 = clone $this->object1;
  }
}

$obj = new MyCloneable();

$obj->object1 = new SubObject();
$obj->object2 = new SubObject();

$obj2 = clone $obj;

print "Objeto original :\n";
print_r($obj);

print "Objeto clonado :\n";
print_r($obj2);

?>

   
```php

El ejemplo anterior mostrará:

```
Objeto original :
MyCloneable Object
(
    [object1] => SubObject Object
        (
            [instance] => 1
        )

    [object2] => SubObject Object
        (
            [instance] => 2
        )

)
Objeto clonado :
MyCloneable Object
(
    [object1] => SubObject Object
        (
            [instance] => 3
        )

    [object2] => SubObject Object
        (
            [instance] => 2
        )

)

   
```php

Es posible acceder a un miembro de un objeto recién clonado en una sola expresión:

Acceso a un miembro de un objeto recién clonado

```
<?php
$dateTime = new DateTime();
echo (clone $dateTime)->format('Y');
?>

   
```php

Resultado del ejemplo anterior es similar a:

    2016
