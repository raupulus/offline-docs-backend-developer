---
title: Los objetos
source_url: https://www.php.net/manual/es/language.types.object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: e587d0655
order: 4500
---

## Los objetos

## Inicialización de los objetos

Para crear un nuevo `object`, utilice la palabra clave `new` para instanciar una clase:

Construcción de objeto

```php
<?php
class foo
{
    function do_foo()
    {
        echo "Doing foo.";
    }
}

$bar = new foo;
$bar->do_foo();
?>

   
```

Para una discusión completa, ver el capítulo sobre [las clases y los objetos](#language.oop5).

## Conversión en un objeto

Si un `object` es convertido en un `object`, no será modificado. Si un valor de cualquier otro tipo es convertido en un `object`, se creará una nueva instancia de la clase interna `stdClass`. Si el valor es `null`, la nueva instancia estará vacía. Un `array` se convierte en `object` con las propiedades nombradas en relación con las claves con sus valores correspondientes. Note que en este caso, antes de PHP 7.2.0 las claves numéricas fueron inaccesibles a menos que fueran iteradas.

Conversión en un objeto

```php
<?php
$obj = (object) array('1' => 'foo');
var_dump(isset($obj->{'1'})); // muestra 'bool(true)'

// Deprecado desde PHP 8.1
var_dump(key($obj)); // muestra 'string(1) "1"'
?>

   
```

Para cualquier otro tipo, un miembro llamado `scalar` contendrá el valor.

Conversión `(object)`

```php
<?php
$obj = (object) 'ciao';
echo $obj->scalar;  // Muestra: 'ciao'
?>

   
```
