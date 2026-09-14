---
title: is_subclass_of
description: Determina si un objeto es una subclase de una clase dada o la implementa
source_url: https://www.php.net/manual/es/function.is-subclass-of.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/is-subclass-of.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: c44475e1f
order: 6890
---

is_subclass_of

Determina si un objeto es una subclase de una clase dada o la implementa

## Descripción

```php
is_subclass_of(mixed $object_or_class, string $class, [bool $allow_string]): bool
```php

Verifica si el objeto `object_or_class` tiene la clase `class` entre sus padres o la implementa.

## Parámetros

`object_or_class`  
Un nombre de clase o una instancia de un objeto. No se genera ningún error si la clase no existe.

`class`  
El nombre de la clase

`allow_string`  
Si este argumento es establecido a `false`, un nombre de clase en forma de string en el argumento `object_or_class` no es permitido. Esto permite evitar llamar al autoloader si la clase no existe.

## Valores devueltos

Esta función retorna `true` si el objeto `object_or_class` es una instancia de una clase que es una subclase de `class`, `false` en caso contrario.

## Ejemplos

Ejemplo con `is_subclass_of`

```
<?php
// Define una clase
class WidgetFactory
{
  var $oink = 'moo';
}

// Define una subclase
class WidgetFactory_Child extends WidgetFactory
{
  var $oink = 'oink';
}

// Creación de un nuevo objeto
$WF = new WidgetFactory();
$WFC = new WidgetFactory_Child();

if (is_subclass_of($WFC, 'WidgetFactory')) {
  echo "sí, \$WFC es una subclase de la clase WidgetFactory\n";
} else {
  echo "no, \$WFC no es una subclase de la clase WidgetFactory\n";
}

if (is_subclass_of($WF, 'WidgetFactory')) {
  echo "sí, \$WF es una subclase de la clase WidgetFactory\n";
} else {
  echo "no, \$WF no es una subclase de la clase WidgetFactory\n";
}

if (is_subclass_of('WidgetFactory_Child', 'WidgetFactory')) {
  echo "sí, WidgetFactory_Child es una subclase de la clase WidgetFactory\n";
} else {
  echo "no, WidgetFactory_Child no es una subclase de la clase WidgetFactory\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    sí, $WFC es una subclase de la clase WidgetFactory
    no, $WF no es una subclase de la clase WidgetFactory
    sí, WidgetFactory_Child es una subclase de la clase WidgetFactory

Ejemplo con `is_subclass_of` utilizando una interfaz

```
<?php
// Definición de la interfaz
interface MyInterface
{
  public function MyFunction();
}

// Definición de la implementación de la clase de la interfaz
class MyClass implements MyInterface
{
  public function MyFunction()
  {
    return "MyClass implementa MyInterface!";
  }
}

// Instanciación del objeto
$my_object = new MyClass;

// Funciona desde PHP 5.3.7

// Prueba utilizando el objeto de la instancia de la clase
if (is_subclass_of($my_object, 'MyInterface')) {
  echo "Sí, \$my_object es una subclase de MyInterface\n";
} else {
  echo "No, \$my_object no es una subclase de MyInterface\n";
}

// Prueba utilizando el nombre de la clase en forma de string
if (is_subclass_of('MyClass', 'MyInterface')) {
  echo "Sí, MyClass es una subclase de MyInterface\n";
} else {
  echo "No, MyClass no es una subclase de MyInterface\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Sí, $my_object es una subclase de MyInterface
    Sí, MyClass es una subclase de MyInterface

## Notas

> [!NOTE]
> El uso de esta función utilizará todos los [autoloaders](#language.oop5.autoload) registrados si la clase no es conocida aún.

## Véase también

`get_class`, `get_parent_class`, `is_a`, `class_parents`
