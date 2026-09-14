---
title: array_column
description: Devuelve los valores de una columna de un array de entrada
source_url: https://www.php.net/manual/es/function.array-column.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-column.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: 8bf3587d8
order: 5180
---

array_column

Devuelve los valores de una columna de un array de entrada

## Descripción

```php
array_column(array $array, int $column_key, [int $index_key]): array
```php

`array_column` devuelve los valores de una columna de `array`, identificada por la clave `column_key`. Opcionalmente, se puede proporcionar un argumento `index_key` para indexar los valores en el array devuelto por los valores de la columna `index_key` del array de entrada.

## Parámetros

`array`  
Un array multidimensional o un array de objetos a partir del cual se extrae una columna de valor. Si se proporciona un array de objetos, entonces las propiedades públicas pueden ser directamente extraídas. Para que las propiedades protegidas o privadas sean extraídas, la clase debe implementar las dos métodos mágicos `__get` y `__isset`.

`column_key`  
La columna de valores a devolver. Este valor puede ser la clave entera de la columna que se desea recuperar, o bien el nombre de la clave para un array asociativo o el nombre de la propiedad. También puede valer `null` para devolver el array completo o los objetos (esto puede ser útil en conjunción con el argumento `index_key` para reindexar el array).

`index_key`  
La columna a utilizar como índice/clave para el array devuelto. Este valor puede ser la clave entera de la columna, o el nombre de la clave. El valor es [cast](#language.types.array.key-casts) como de costumbre para las claves del array (sin embargo, anterior a PHP 8.0.0, los objetos que soportan una conversión en string también eran permitidos).

## Valores devueltos

Devuelve un array de valores que representan una sola columna desde el array de entrada.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Los objetos en las columnas indicadas por el argumento `index_key` ya no se convertirán en string y lanzarán ahora una `TypeError` en su lugar. |

## Ejemplos

Recupera la columna de los nombres

```
<?php

// Array que representa un conjunto de registros de una base de datos
$records = [
    [
        'id' => 2135,
        'first_name' => 'John',
        'last_name' => 'Doe',
    ],
    [
        'id' => 3245,
        'first_name' => 'Sally',
        'last_name' => 'Smith',
    ],
    [
        'id' => 5342,
        'first_name' => 'Jane',
        'last_name' => 'Jones',
    ],
    [
        'id' => 5623,
        'first_name' => 'Peter',
        'last_name' => 'Doe',
    ]
];

$first_names = array_column($records, 'first_name');
print_r($first_names);

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => John
    [1] => Sally
    [2] => Jane
    [3] => Peter
)

    
```php

Recupera la columna de los apellidos, indexada por la columna "id"

```
<?php

// Utilizando el array del ejemplo #1
$records = [
    [
        'id' => 2135,
        'first_name' => 'John',
        'last_name' => 'Doe',
    ],
    [
        'id' => 3245,
        'first_name' => 'Sally',
        'last_name' => 'Smith',
    ],
    [
        'id' => 5342,
        'first_name' => 'Jane',
        'last_name' => 'Jones',
    ],
    [
        'id' => 5623,
        'first_name' => 'Peter',
        'last_name' => 'Doe',
    ]
];

$last_names = array_column($records, 'last_name', 'id');
print_r($last_names);

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [2135] => Doe
    [3245] => Smith
    [5342] => Jones
    [5623] => Doe
)

    
```php

Recupera la columna de los nombres de usuario desde la propiedad pública "username" de un objeto

```
<?php

class User
{
    public $username;

    public function __construct(string $username)
    {
        $this->username = $username;
    }
}

$users = [
    new User('user 1'),
    new User('user 2'),
    new User('user 3'),
];

print_r(array_column($users, 'username'));

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => user 1
    [1] => user 2
    [2] => user 3
)

    
```php

Recupera la columna de nombres desde la propiedad privada "name" de un objeto utilizando los métodos mágicos `__isset` y `__get`

```
<?php

class Person
{
    private $name;

    public function __construct(string $name)
    {
        $this->name = $name;
    }

    public function __get($prop)
    {
        return $this->$prop;
    }

    public function __isset($prop) : bool
    {
        return isset($this->$prop);
    }
}

$people = [
    new Person('Fred'),
    new Person('Jane'),
    new Person('John'),
];

print_r(array_column($people, 'name'));
?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => Fred
    [1] => Jane
    [2] => John
)

    
```php

Si `__isset` no está definido, entonces se devolverá un array vacío.
