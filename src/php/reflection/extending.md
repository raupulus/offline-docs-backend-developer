---
title: Extensión
source_url: https://www.php.net/manual/es/reflection.extending.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/extending.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: fa6e19697
order: 68930
---

## Extensión

Si se deseara crear versiones especializadas de las clases que vienen incorporadas (por ejemplo, para crear HTML en color cuando se exportan, parar tener variables de acceso rápido en lugar de usar métodos, o parar crear métodos auxiliares), deberá extender la clase.

Extendiendo las clases incorporadas

```php
<?php
/**
 * Mi clase Reflection_Method
 */
class My_Reflection_Method extends ReflectionMethod
{
    public $visibility = array();

    public function __construct($o, $m)
    {
        parent::__construct($o, $m);
        $this->visibility = Reflection::getModifierNames($this->getModifiers());
    }
}

/**
 * Clase demo #1
 *
 */
class T {
    protected function x() {}
}

/**
 * Clase demo #2
 *
 */
class U extends T {
    function x() {}
}

// Mostrar información
var_dump(new My_Reflection_Method('U', 'x'));
?>

  
```

Resultado del ejemplo anterior es similar a:

    object(My_Reflection_Method)#1 (3) {
      ["visibility"]=>
      array(1) {
        [0]=>
        string(6) "public"
      }
      ["name"]=>
      string(1) "x"
      ["class"]=>
      string(1) "U"
    }

> [!CAUTION]
> Si se sobrescribe el constructor, no hay que olvidar llamar en primer lugar al constructor de la clase padre. Si esto fallara, se lanzará el siguiente error: `Fatal error: Internal error: Failed to retrieve the reflection object`
