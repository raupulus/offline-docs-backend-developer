---
title: El atributo AllowDynamicProperties
source_url: https://www.php.net/manual/es/class.allowdynamicproperties.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/allowdynamicproperties.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: be3574f52
order: 2890
---

## Introducción

Este atributo se utiliza para marcar clases que permiten [propiedades dinámicas](#language.oop5.properties.dynamic-properties).

> [!NOTE]
> Aunque los atributos en sí no se heredan, el efecto del atributo `AllowDynamicProperties` *sí* se hereda. Las clases hijas de una clase marcada con este atributo también permitirán propiedades dinámicas, incluso si no declaran el atributo explícitamente.

## Sinopsis de la clase

\#\[\Attribute\]

final

AllowDynamicProperties

Métodos

## Ejemplos

Las propiedades dinámicas están deprecadas a partir de PHP 8.2.0, por lo que usarlas sin marcar la clase con este atributo emitirá un aviso de deprecación.

AllowDynamicProperties con propiedad inexistente

```php
<?php
class DefaultBehaviour { }

#[\AllowDynamicProperties]
class ClassAllowsDynamicProperties { }

$o1 = new DefaultBehaviour();
$o2 = new ClassAllowsDynamicProperties();

$o1->nonExistingProp = true;
$o2->nonExistingProp = true;
?>

    
```

Resultado del ejemplo anterior en PHP 8.2:

    Deprecated: Creation of dynamic property DefaultBehaviour::$nonExistingProp is deprecated in file on line 10

AllowDynamicProperties con propiedad inexistente en clase heredada

```php
     
<?php
class DefaultBehaviour { }

#[\AllowDynamicProperties]
class ClassAllowsDynamicProperties { }

class InheritedClassAllowsDynamicProperties extends ClassAllowsDynamicProperties { }

$o1 = new DefaultBehaviour();
$o2 = new InheritedClassAllowsDynamicProperties();

$o1->nonExistingProp = true;
$o2->nonExistingProp = true;
?>

    
```

Resultado del ejemplo anterior en PHP 8.2:

         
    Deprecated: Creation of dynamic property DefaultBehaviour::$nonExistingProp is deprecated in file on line 12

## Véase también

[Visión general de los atributos](#language.attributes)
