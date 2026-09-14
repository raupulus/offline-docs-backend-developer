---
title: mysqli::get_charset
description: Devuelve un objeto que representa el juego de caracteres
source_url: https://www.php.net/manual/es/mysqli.get-charset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-charset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: aa79a143f
order: 55060
---

mysqli::get_charset

mysqli_get_charset

Devuelve un objeto que representa el juego de caracteres

## Descripción

Estilo orientado a objetos

```php
public mysqli::get_charset(): object
```php

Estilo procedimental

```php
mysqli_get_charset(mysqli $mysql): object
```

Devuelve un objeto que representa el juego de caracteres, proporcionando diferentes propiedades del juego de caracteres actual.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

La función devuelve un juego de caracteres con las siguientes propiedades:

`charset`  
Nombre del juego de caracteres

`collation`  
Nombre de la interclasificación

`dir`  
El directorio en el que se busca la descripción del juego de caracteres o "" para los juegos de caracteres internos

`min_length`  
Longitud mínima de caracteres, en bytes

`max_length`  
Longitud máxima de caracteres, en bytes

`number`  
Número del juego de caracteres interno

`state`  
A partir de PHP 8.2.0, es siempre `1`

## Ejemplos

Ejemplo con mysqli::get_charset

Estilo orientado a objetos

```php
<?php
  $db = mysqli_init();
  $db->real_connect("localhost","root","","test");
  $db->set_charset('latin1');
  var_dump($db->get_charset());
?>

   
```

Estilo procedimental

```php
<?php
  $db = mysqli_init();
  mysqli_real_connect($db, "localhost","root","","test");
  mysqli_set_charset($db, 'latin1');
  var_dump(mysqli_get_charset($db));
?>

   
```

Los ejemplos anteriores mostrarán:

    object(stdClass)#2 (7) {
      ["charset"]=>
      string(6) "latin1"
      ["collation"]=>
      string(17) "latin1_swedish_ci"
      ["dir"]=>
      string(0) ""
      ["min_length"]=>
      int(1)
      ["max_length"]=>
      int(1)
      ["number"]=>
      int(8)
      ["state"]=>
      int(1)
    }

## Véase también

`mysqli_character_set_name`, `mysqli_set_charset`
