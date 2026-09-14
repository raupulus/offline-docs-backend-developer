---
title: cubrid_fetch_object
description: Recupera la siguiente línea y la devuelve como un objeto
source_url: https://www.php.net/manual/es/function.cubrid-fetch-object.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-fetch-object.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8700
---

cubrid_fetch_object

Recupera la siguiente línea y la devuelve como un objeto

## Descripción

```php
cubrid_fetch_object(resource $result, [string $class_name], [array $params], [int $type]): object
```php

Esta función devuelve un objeto con los nombres de la columna del conjunto de resultados como propiedades. Los valores de estas propiedades se extraen de la línea actual del conjunto de resultados.

## Parámetros

`result`  
El parámetro `result` proviene de una llamada a la función `cubrid_execute`

`class_name`  
El nombre de la clase a instanciar, definir las propiedades y devolver. Si no se especifica, se devuelve un objeto `stdClass`.

`params`  
Un array de parámetros opcionales a pasar al constructor de la clase `class_name`.

`type`  
El tipo solo puede ser CUBRID_LOB; este parámetro solo se utilizará cuando se necesite usar un objeto lob.

## Valores devueltos

Un objeto en caso de éxito.

`false` cuando no hay más líneas, NULL si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_fetch_object`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$res = cubrid_execute($conn, "SELECT * FROM code");

var_dump(cubrid_fetch_object($res));

// if you want to operate LOB object, you can use cubrid_fetch_object($res, CUBRID_LOB)

class demodb_code {
    public $s_name = null;
    public $f_name = null;

    public function toString() {
        var_dump($this);
    }
}

var_dump(cubrid_fetch_object($res, "demodb_code"));

// Si se desea utilizar un objeto LOB, se puede usar
// cubrid_fetch_object($res, 'demodb_code_construct', array('s_name', 'f_name'), CUBRID_LOB)

class demodb_code_construct extends demodb_code {
    public function __construct($s, $f) {
        $this->s_name = $s;
        $this->f_name = $f;
    }
}

var_dump(cubrid_fetch_object($res, 'demodb_code_construct', array('s_name', 'f_name')));

// Si se desea utilizar un objeto LOB, se puede usar
// cubrid_fetch_object($res, 'demodb_code_construct', array('s_name', 'f_name'), CUBRID_LOB)

var_dump(cubrid_fetch_object($res));

cubrid_close_request($res);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    object(stdClass)#1 (2) {
      ["s_name"]=>
      string(1) "X"
      ["f_name"]=>
      string(5) "Mixed"
    }
    object(demodb_code)#1 (2) {
      ["s_name"]=>
      string(1) "W"
      ["f_name"]=>
      string(5) "Woman"
    }
    object(demodb_code_construct)#1 (2) {
      ["s_name"]=>
      string(6) "s_name"
      ["f_name"]=>
      string(6) "f_name"
    }
    object(stdClass)#1 (2) {
      ["s_name"]=>
      string(1) "B"
      ["f_name"]=>
      string(6) "Bronze"
    }

## Véase también

cubrid_execute

cubrid_fetch

cubrid_fetch_array

cubrid_fetch_assoc

cubrid_fetch_row
