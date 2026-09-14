---
title: Modificaciones en el manejo de string
source_url: https://www.php.net/manual/es/migration70.incompatible.strings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/strings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 86e6094e8
order: 350
---

## Modificaciones en el manejo de `string`

### Las cadenas hexadecimales ya no se consideran numéricas

Las `string` que contienen números hexadecimales ya no se consideran numéricas. Por ejemplo:

```php
<?php
var_dump("0x123" == "291");
var_dump(is_numeric("0x123"));
var_dump("0xe" + "0x1");
var_dump(substr("foo", "0x1"));
?>

   
```

Resultado del ejemplo anterior en PHP 5:

    bool(true)
    bool(true)
    int(15)
    string(2) "oo"

       

Resultado del ejemplo anterior en PHP 7:

    bool(false)
    bool(false)
    int(0)

    Notice: A non well formed numeric value encountered in /tmp/test.php on line 5
    string(3) "foo"

`filter_var` puede ser utilizado para verificar si una `string` contiene un número hexadecimal, y también para convertir una cadena de este tipo en un `int`:

```php
<?php
$str = "0xffff";
$int = filter_var($str, FILTER_VALIDATE_INT, FILTER_FLAG_ALLOW_HEX);
if (false === $int) {
    throw new Exception("Invalid integer!");
}
var_dump($int); // int(65535)
?>

   
```

### `\u{` puede causar errores

Debido a la adición de la nueva [sintaxis de escape de punto de código Unicode](#migration70.new-features.unicode-codepoint-escape-syntax), las `string` que contienen un literal `\u{` seguido de una secuencia no válida provocarán un error fatal. Para evitar esto, la barra invertida principal debe ser escapada.
