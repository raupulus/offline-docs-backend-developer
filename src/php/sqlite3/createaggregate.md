---
title: SQLite3::createAggregate
description: Registra una función PHP para ser utilizada como función de agregación
  SQLite
source_url: https://www.php.net/manual/es/sqlite3.createaggregate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/sqlite3/createaggregate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: true
translation_revision: 855bfee2f
order: 85670
---

SQLite3::createAggregate

Registra una función PHP para ser utilizada como función de agregación SQLite

## Descripción

```php
public SQLite3::createAggregate(string $name, callable $stepCallback, callable $finalCallback, [int $argCount]): bool
```php

Registra una función PHP o una función definida por el usuario para ser utilizada como función de agregación SQL, que será utilizada en las consultas SQL.

## Parámetros

`name`  
Nombre de la función de agregación SQL a crear o redefinir.

`stepCallback`  
Función de retrollamada llamada para cada fila en el conjunto de resultados. Su función PHP debería acumular el resultado y almacenar su contexto de agregación.

Esta función debe ser definida como:

```php
step(mixed $context, int $rownumber, mixed $value, mixed ...$values): mixed
```

`context`  
`null` para la primera fila; en las filas siguientes esto tendrá el valor que previamente fue retornado por la función step; debería utilizarse esto para mantener el estado de agregación.

`rownumber`  
El número de fila actual.

`value`  
El primer argumento a pasar al agregador.

`values`  
Argumentos adicionales a pasar al agregador.

El valor retornado por esta función será utilizado como argumento `context` durante la próxima llamada a una función de paso o final.

`finalCallback`  
Función de retrollamada para agregar los "pasos" de datos de cada fila. Una vez que todas las filas han sido procesadas, la función será llamada, tomará los datos del contexto de agregación y retornará el resultado. La función de retrollamada debe retornar un tipo comprendido por SQLite (i.e. un [tipo escalar](#language.types.intro)).

Esta función debe ser definida como:

```php
fini(mixed $context, int $rownumber): mixed
```php

`context`  
Contiene el valor de retorno de la última llamada a la función step.

`rownumber`  
Siempre `0`.

El valor de retorno de esta función será utilizado como valor de retorno para la agregación.

`argCount`  
El número de argumentos tomados por la función de agregación SQL. Si este número es negativo, entonces la función de agregación SQL podrá tomar un número no definido de argumentos.

## Valores devueltos

Retorna `true` si la creación del agregado ha tenido éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de una función de agregación con max_length

```
<?php
$data = array(
   'one',
   'two',
   'three',
   'four',
   'five',
   'six',
   'seven',
   'eight',
   'nine',
   'ten',
   );
$db = new SQLite3(':memory:');
$db->exec("CREATE TABLE strings(a)");
$insert = $db->prepare('INSERT INTO strings VALUES (?)');
foreach ($data as $str) {
    $insert->bindValue(1, $str);
    $insert->execute();
}
$insert = null;

function max_len_step($context, $rownumber, $string)
{
    if (strlen($string) > $context) {
        $context = strlen($string);
    }
    return $context;
}

function max_len_finalize($context, $rownumber)
{
    return $context === null ? 0 : $context;
}

$db->createAggregate('max_len', 'max_len_step', 'max_len_finalize');

var_dump($db->querySingle('SELECT max_len(a) from strings'));
?>

    
```php

El ejemplo anterior mostrará:

```
int(5)

    
```php

En este ejemplo, se crea una función agregativa que calculará la longitud de la cadena de caracteres más larga en una de las columnas de la tabla. Para cada fila, la función `max_len_step` es llamada y el parámetro `$context` es pasado. El parámetro de contexto es como cualquier otra variable PHP y debe ser fijado para contener un array o incluso, un objeto. En este ejemplo, se utiliza para contener la longitud máxima que se ha visto hasta el momento; si el parámetro `$string` tiene una longitud mayor que la actual, se actualiza el contexto para contener esta nueva longitud máxima.

Una vez que todas las filas han sido procesadas, SQLite llama a la función `max_len_finalize` para determinar el resultado agregativo. Aquí, se podrían realizar cálculos basados en los datos encontrados en `$context`. En nuestro ejemplo simple, hemos calculado el resultado como si la consulta estuviera progresando, aunque simplemente necesitamos retornar el valor de contexto.

> [!TIP]
> No se RECOMIENDA registrar una copia de los valores en el contexto para finalmente procesarlos. En este caso, SQLite utilizaría mucha memoria para procesar la consulta - imagine la cantidad de memoria necesaria si un millón de filas fueran registradas en memoria, sabiendo que cada fila contiene una cadena de caracteres (32 bytes por cadena).

> [!TIP]
> Puede utilizarse SQLite3::createAggregate para sobrescribir las funciones nativas de SQLite.
