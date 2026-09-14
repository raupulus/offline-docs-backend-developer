---
title: PDOStatement::fetchAll
description: Recupera las líneas restantes de un conjunto de resultados
source_url: https://www.php.net/manual/es/pdostatement.fetchall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/fetchall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 44bcc82c7
order: 62110
---

PDOStatement::fetchAll

Recupera las líneas restantes de un conjunto de resultados

## Descripción

```php
public PDOStatement::fetchAll([int $mode]): array
```php

```php
public PDOStatement::fetchAll(int $mode, int $column): array
```

```php
public PDOStatement::fetchAll(int $mode, string $class, array $constructorArgs): array
```php

```php
public PDOStatement::fetchAll(int $mode, callable $callback): array
```

## Parámetros

`mode`  
Controla el contenido del array retornado como se documenta en la función PDOStatement::fetch. Valor por omisión: `PDO::ATTR_DEFAULT_FETCH_MODE` (que toma su valor por omisión de `PDO::FETCH_BOTH`).

Para retornar un array que contenga todos los valores de una sola columna desde el conjunto de resultados, se especifica `PDO::FETCH_COLUMN`. Puede especificarse qué columna se desea con el argumento `column`.

Para indexar el array resultante por el valor de una cierta columna (en lugar de por números consecutivos), se coloca el nombre de esta columna en primer lugar en la lista de columnas en SQL, y se utiliza `PDO::FETCH_UNIQUE`. Esta columna debe contener únicamente valores únicos, de lo contrario se perderán algunos datos.

Para agrupar los resultados en forma de un array de tres dimensiones indexado por los valores de una columna especificada, se coloca el nombre de esta columna en primer lugar en la lista de columnas en SQL y se utiliza `PDO::FETCH_GROUP`.

Para agrupar los resultados en forma de un array de dos dimensiones, se utiliza un OU a nivel de bits con `PDO::FETCH_GROUP` y `PDO::FETCH_COLUMN`. Los resultados serán agrupados por la primera columna, el valor del elemento del array siendo una lista de entradas correspondientes de la segunda columna.

Los argumentos siguientes son dinámicos y dependen del modo de recuperación. No pueden ser utilizados con argumentos nombrados.

`column`  
Utilizado con `PDO::FETCH_COLUMN`. Retorna la columna indicada indexada a 0.

`class`  
Utilizado con `PDO::FETCH_CLASS`. Retorna instancias de la clase especificada, haciendo corresponder las columnas de cada línea a propiedades nombradas en la clase.

`constructorArgs`  
Argumentos del constructor personalizado de la clase cuando el argumento `mode` es `PDO::FETCH_CLASS`.

`callback`  
Utilizado con `PDO::FETCH_FUNC`. Retorna los resultados de la llamada de la función especificada, utilizando las columnas de cada línea como argumentos en la llamada.

## Valores devueltos

PDOStatement::fetchAll retorna un array que contiene todas las líneas del conjunto de registros. El array representa cada línea como un array de valores de las columnas, o un objeto con propiedades correspondientes a cada nombre de columna. Un array vacío es retornado si no hay resultados.

El uso de este método para recuperar grandes conjuntos de resultados puede aumentar el uso de recursos del sistema, pero también estos recursos. En lugar de recuperar todas las datos y manipularlas con PHP, se utiliza el servidor de base de datos para manipular los conjuntos de resultados. Por ejemplo, se utilizan las cláusulas WHERE y ORDER BY en las consultas SQL para restringir los resultados antes de recuperarlos y procesarlos con PHP.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_WARNING`.

Lanza una excepción `PDOException` si el atributo `PDO::ATTR_ERRMODE` está definido a `PDO::ERRMODE_EXCEPTION`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Este método retorna ahora siempre un `array`, anteriormente `false` podía ser retornado en caso de fallo. |

## Ejemplos

Recuperación de todas las líneas de un conjunto de resultados

```php
<?php
$sth = $dbh->prepare("SELECT nom, couleur FROM fruit");
$sth->execute();

/* Recuperación de todas las líneas de un conjunto de resultados */
print "Recuperación de todas las líneas de un conjunto de resultados :\n";
$result = $sth->fetchAll();
print_r($result);
?>

    
```

Resultado del ejemplo anterior es similar a:

    Recuperación de todas las líneas de un conjunto de resultados :
    Array
    (
        [0] => Array
            (
                [nom] => apple
                [0] => apple
                [couleur] => red
                [1] => red
            )

        [1] => Array
            (
                [nom] => pear
                [0] => pear
                [couleur] => green
                [1] => green
            )

        [2] => Array
            (
                [nom] => watermelon
                [0] => watermelon
                [couleur] => pink
                [1] => pink
            )

    )

Recuperación de todos los valores de una sola columna desde un conjunto de resultados

El siguiente ejemplo muestra cómo retornar todos los valores de una sola columna desde un conjunto de resultados, incluso si la consulta SQL retorna varias columnas por líneas.

```php
<?php
$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

/* Recuperación de todos los valores de la primera columna */
$result = $sth->fetchAll(PDO::FETCH_COLUMN, 0);
var_dump($result);
?>

    
```

Resultado del ejemplo anterior es similar a:

    Array(3)
    (
        [0] =>
        string(5) => apple
        [1] =>
        string(4) => pear
        [2] =>
        string(10) => watermelon
    )

Agrupar todos los valores de una sola columna

El siguiente ejemplo muestra cómo retornar un array asociativo agrupado por los valores de la columna especificada de un conjunto de resultados. El array contiene tres claves: los valores `apple` y `pear` son retornados en forma de arrays que contienen dos colores diferentes, mientras que `watermelon` es retornado en forma de un array que contiene únicamente un solo color.

```php
<?php
$insert = $dbh->prepare("INSERT INTO fruit(name, colour) VALUES (?, ?)");
$insert->execute(array('apple', 'green'));
$insert->execute(array('pear', 'yellow'));

$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

/* Agrupar los valores de la primera columna */
var_dump($sth->fetchAll(PDO::FETCH_COLUMN|PDO::FETCH_GROUP));
?>

    
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["apple"]=>
        array(2) {
          [0]=>
            string(5) "green"
          [1]=>
            string(3) "red"
        }
      ["pear"]=>
        array(2) {
          [0]=>
            string(5) "green"
          [1]=>
            string(6) "yellow"
        }
      ["watermelon"]=>
        array(1) {
          [0]=>
            string(5) "pink"
        }
    }

Instanciar una clase para cada resultado

El siguiente ejemplo muestra el comportamiento de `PDO::FETCH_CLASS`.

```php
<?php
class fruit {
    public $name;
    public $colour;
}

$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

$result = $sth->fetchAll(PDO::FETCH_CLASS, "fruit");
var_dump($result);
?>

    
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      object(fruit)#1 (2) {
        ["name"]=>
        string(5) "apple"
        ["colour"]=>
        string(5) "green"
      }
      [1]=>
      object(fruit)#2 (2) {
        ["name"]=>
        string(4) "pear"
        ["colour"]=>
        string(6) "yellow"
      }
      [2]=>
      object(fruit)#3 (2) {
        ["name"]=>
        string(10) "watermelon"
        ["colour"]=>
        string(4) "pink"
      }
      [3]=>
      object(fruit)#4 (2) {
        ["name"]=>
        string(5) "apple"
        ["colour"]=>
        string(3) "red"
      }
      [4]=>
      object(fruit)#5 (2) {
        ["name"]=>
        string(4) "pear"
        ["colour"]=>
        string(5) "green"
      }
    }

Llamada de una función para cada resultado

El siguiente ejemplo muestra el comportamiento de `PDO::FETCH_FUNC`.

```php
<?php
function fruit($name, $colour) {
    return "{$name}: {$colour}";
}

$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

$result = $sth->fetchAll(PDO::FETCH_FUNC, "fruit");
var_dump($result);
?>

    
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      string(12) "apple: green"
      [1]=>
      string(12) "pear: yellow"
      [2]=>
      string(16) "watermelon: pink"
      [3]=>
      string(10) "apple: red"
      [4]=>
      string(11) "pear: green"
    }

## Véase también

PDO::query, PDOStatement::fetch, PDOStatement::fetchColumn, PDO::prepare, PDOStatement::setFetchMode
