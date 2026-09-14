---
title: db2_escape_string
description: Escapar ciertos caracteres especiales
source_url: https://www.php.net/manual/es/function.db2-escape-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-escape-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_revision: 6047c10c1
order: 30730
---

db2_escape_string

Escapar ciertos caracteres especiales

## Descripción

```php
db2_escape_string(string $string_literal): string
```php

Agrega un caracter de escape (barra invertida) antes de cada caracter especial de la cadena enviada como parámetro.

## Parámetros

`string_literal`  
La cadena que contiene los caracteres especiales y que necesita ser escapada. Los caracteres especiales a los que se les agrega el caracter de escape son `\x00`, `\n`, `\r`, `\`, `'`, `"` y `\x1a`.

## Valores devueltos

Devuelve `string_literal` con todos los caracteres especiales ya escapados.

## Ejemplos

Ejemplo de `db2_escape_string`

Resultado del uso de la función `db2_escape_string`

```
<?php

$conn = db2_connect($database, $user, $password);

if ($conn) {
    $str[0] = "Todos los caracteres: \x00 , \n , \r , \ , ' , \" , \x1a .";
    $str[1] = "Barra invertida (\). Comilla simple ('). Comilla doble (\")";
    $str[2] = "El caracter NULL \0 debe ser citado también";
    $str[3] = "Caracteres interesantes: \x1a , \x00 .";
    $str[4] = "Nada que citar";
    $str[5] = 200676;
    $str[6] = "";

    foreach( $str as $string ) {
        echo "db2_escape_string: " . db2_escape_string($string). "\n";
    }
}
?>

   
```php

El ejemplo anterior mostrará:

    db2_escape_string: Todos los caracteres: \0 , \n , \r , \\ , \' , \" , \Z .
    db2_escape_string: Barra invertida (\\). Comilla simple (\'). Comilla doble (\")
    db2_escape_string: El caracter NULL \0 debe ser citado también
    db2_escape_string: Caracteres interesantes: \Z , \0 .
    db2_escape_string: Nada que citar
    db2_escape_string: 200676
    db2_escape_string:

## Véase también

db2_prepare
