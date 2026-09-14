---
title: El atributo Deprecated
source_url: https://www.php.net/manual/es/class.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 77325b622
order: 2920
---

## Introducción

Este atributo se utiliza para marcar la funcionalidad como obsoleta. El uso de funcionalidad obsoleta hará que se emita un error `E_USER_DEPRECATED`.

## Sinopsis de la clase

\#\[\Attribute\]

final

Deprecated

Propiedades

public

readonly

string

null

message

public

readonly

string

null

since

Métodos

## Propiedades

`message`  
Un mensaje opcional que explica la razón de la deprecación y la posible funcionalidad de reemplazo. Se incluirá en el mensaje de deprecación emitido.

`since`  
Una cadena opcional que indica desde cuándo la funcionalidad está deprecada. El contenido no es validado por PHP y puede contener un número de versión, una fecha o cualquier otro valor que se considere apropiado. Se incluirá en el mensaje de deprecación emitido.

La funcionalidad que es parte de PHP utilizará Major.Minor como el valor de `since`, por ejemplo `'8.4'`.

## Ejemplos

```php
<?php

#[\Deprecated(message: "use safe_replacement() instead", since: "1.5")]
function unsafe_function()
{
   echo "This is unsafe", PHP_EOL;
}

unsafe_function();

?>

    
```

La salida del ejemplo anterior en PHP 8.4 es similar a:

    Deprecated: Function unsafe_function() is deprecated since 1.5, use safe_replacement() instead in example.php on line 9
    This is unsafe

## Véase también

Visión general de los atributos

ReflectionFunctionAbstract::isDeprecated

ReflectionClassConstant::isDeprecated

E_USER_DEPRECATED
