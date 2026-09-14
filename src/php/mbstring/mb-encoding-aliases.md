---
title: mb_encoding_aliases
description: Obtiene los alias de un tipo de codificación conocido
source_url: https://www.php.net/manual/es/function.mb-encoding-aliases.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-encoding-aliases.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 96bc00858
order: 45080
---

mb_encoding_aliases

Obtiene los alias de un tipo de codificación conocido

## Descripción

```php
mb_encoding_aliases(string $encoding): array
```php

Devuelve un array de alias para un tipo conocido de codificación.

## Parámetros

`encoding`  
El tipo de codificación a verificar, para los alias.

## Valores devueltos

Devuelve un array indexado numéricamente de alias de codificación. o `false` si ocurre un error

## Errores/Excepciones

Genera un `ValueError` si `encoding` es desconocido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si el argumento `encoding` es desconocido, ahora se genera un `ValueError`; previamente, se emitía un `E_WARNING` y la función devolvía `false`. |

## Ejemplos

Ejemplo con `mb_encoding_aliases`

```
<?php
$encoding        = 'ASCII';
$known_encodings = mb_list_encodings();

if (in_array($encoding, $known_encodings)) {

    $aliases = mb_encoding_aliases($encoding);
    print_r($aliases);

} else {

    echo "Codificación ($encoding) desconocida.\n";

}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => ANSI_X3.4-1968
        [1] => iso-ir-6
        [2] => ANSI_X3.4-1986
        [3] => ISO_646.irv:1991
        [4] => US-ASCII
        [5] => ISO646-US
        [6] => us
        [7] => IBM367
        [8] => cp367
        [9] => csASCII
    )

## Véase también

`mb_list_encodings`
