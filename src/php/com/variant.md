---
title: variant La clase variant
source_url: https://www.php.net/manual/es/class.variant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/variant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 8030
---

## Introducción

El VARIANT es el equivalente COM de zval para PHP; es una estructura que puede contener un valor con un rango de diferentes tipos posibles. La clase variant proporcionada por la extensión COM permite tener más control sobre lo que PHP envía y recibe de COM.

## Sinopsis de la clase

variant

Métodos

## Ejemplos variant

Ejemplo variant

```php
<?php
$v = new variant(42);
print "El tipo es " . variant_get_type($v) . "<br/>";
print "El valor es " . $v . "<br/>";
?>

     
```

> [!NOTE]
> Al devolver un valor o recuperar una propiedad variant, el variant se convierte en un valor PHP solo cuando hay una correspondencia directa entre los tipos que no produciría una pérdida de información. En todos los demás casos, el valor se devuelve como una instancia de la clase variant. Se puede forzar a PHP a convertir o evaluar el variant como un tipo PHP nativo utilizando los operadores de transtipado explícitamente, o implícitamente a una `string` al mostrarlo gracias a `print`. Se puede utilizar la gran variedad de funciones variant para realizar operaciones aritméticas sin forzar una conversión y arriesgarse a una pérdida de datos.

Véase también `variant_get_type`.
