---
title: Los tipos
source_url: https://www.php.net/manual/es/language.types.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: e587d0655
order: 4580
---

## Los tipos

## Introducción

En PHP, cada expresión tiene uno de los siguientes tipos integrados según su valor:

- `null`

- `bool`

- `int`

- `float` (número de punto flotante)

- `string`

- `array`

- `object`

- `callable`

- `resource`

PHP es un lenguaje de tipado dinámico, lo que significa que, por omisión, no es necesario especificar el tipo de una variable, ya que esto se determinará en tiempo de ejecución. Sin embargo, es posible tipar estáticamente ciertos aspectos del lenguaje utilizando las [declaraciones de tipo](#language.types.declarations). Los diferentes tipos soportados por el sistema de tipos de PHP están disponibles en la [página del sistema de tipos](#language.types.type-system).

Los tipos limitan el tipo de operaciones que pueden realizarse sobre ellos. Sin embargo, si una expresión/variable se utiliza en una operación que su tipo no soporta, PHP intentará [manipular el tipo](#language.types.type-juggling) en un tipo compatible con la operación. Este proceso depende del contexto en el que se utiliza el valor. Para más información, consulte la sección sobre la [manipulación de tipos](#language.types.type-juggling).

> [!TIP]
> [Las tablas de comparación de tipos](#types.comparisons) pueden ser también útiles, ya que se presentan diversos ejemplos de comparación entre valores de diferentes tipos.

> [!NOTE]
> Es posible forzar la evaluación de una expresión a un cierto tipo utilizando un [type casting](#language.types.typecasting). Una variable también puede ser convertida en el lugar utilizando la función `settype`.

Para verificar el tipo y el valor de una [expresión](#language.expressions), utilice la función `var_dump`. Para recuperar el tipo de una [expresión](#language.expressions), utilice la función `get_debug_type`. Sin embargo, para verificar si una expresión es de un cierto tipo, utilice mejor las funciones `is_type`.

Tipos Diferentes

```php
<?php
$a_bool = TRUE;   // un booleano
$a_str  = "foo";  // un string
$a_str2 = 'foo';  // un string
$an_int = 12;     // un integer

echo gettype($a_bool); // muestra:  boolean
echo gettype($a_str);  // muestra:  string

// Si es un integer, incrementa en 4
if (is_int($an_int)) {
    $an_int += 4;
}

// Si $a_bool es un string, se muestra
if (is_string($a_bool)) {
    echo "String: $a_bool";
}
?>

    
```

Resultado del ejemplo anterior en PHP 8:

    bool
    string
    int(16)

> [!NOTE]
> Anterior a PHP 8.0.0, cuando la función `get_debug_type` no está disponible, la función `gettype` puede ser utilizada en su lugar. Sin embargo, no utiliza los nombres de tipo canónicos.
