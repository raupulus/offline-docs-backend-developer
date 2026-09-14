---
title: stripslashes
description: Quita las barras de un string con comillas escapadas
source_url: https://www.php.net/manual/es/function.stripslashes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/stripslashes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 8cdc6621f
order: 89320
---

stripslashes

Quita las barras de un string con comillas escapadas

## Descripción

```php
stripslashes(string $str): string
```php

Quita las barras de un string con comillas escapadas.

`stripslashes` se puede utilizar si no está insertando estos datos en un lugar (como una base de datos) que requiere escapar. Por ejemplo, si simplemente está imprimiendo datos directamente desde un formulario HTML.

## Parámetros

`str`  
El string de entrada.

## Valores devueltos

Devuelve un string con las barras invertidas retiradas. (`\'` se convierte en `'` y así sucesivamente.) Barras invertidas dobles (`\\`) se convierten en una sencilla (`\`).

## Ejemplos

Un ejemplo de `stripslashes`

```
<?php
$str = "Is your name O\'reilly?";

// Salida: Is your name O'reilly?
echo stripslashes($str);
?>

    
```php

> [!NOTE]
> `stripslashes` no es recursiva. Si se desea aplicar esta función a un array multi-dimensional, se necesita utilizar una función recursiva.

Utilizando `stripslashes` en un array

```
<?php
function stripslashes_deep($value)
{
    $value = is_array($value) ?
                array_map('stripslashes_deep', $value) :
                stripslashes($value);

    return $value;
}

// Ejemplo
$array = array("f\\'oo", "b\\'ar", array("fo\\'o", "b\\'ar"));
$array = stripslashes_deep($array);

// Salida
print_r($array);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => f'oo
        [1] => b'ar
        [2] => Array
            (
                [0] => fo'o
                [1] => b'ar
            )

    )

## Véase también

`addslashes`, `get_magic_quotes_gpc`
