---
title: Pdo\Sqlite::createAggregate
description: Registra una función de agregación definida por el usuario para su uso
  en instrucciones SQL
source_url: https://www.php.net/manual/es/pdo-sqlite.createaggregate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlite/pdo/sqlite/createaggregate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlite
translation_status: ready
translation_reviewed: true
translation_revision: 51610360d
order: 62710
---

Pdo\Sqlite::createAggregate

Registra una función de agregación definida por el usuario para su uso en instrucciones SQL

## Descripción

```php
public Pdo\Sqlite::createAggregate(string $name, callable $step, callable $finalize, [int $numArgs]): bool
```php

Este método es similar a Pdo\Sqlite::createFunction excepto que registra funciones que pueden ser utilizadas para calcular un resultado agregado sobre el conjunto de filas de una consulta.

La principal diferencia entre este método y Pdo\Sqlite::createFunction es que se necesitan dos funciones para manejar la agregación.

> [!TIP]
> Utilizando este método, es posible reemplazar las funciones SQL nativas.

## Parámetros

`name`  
El nombre de la función utilizado en las instrucciones SQL.

`step`  
La función de retrollamada llamada para cada fila del conjunto de resultados. La función de retrollamada debe acumular el resultado y almacenarlo en el contexto de agregación.

Esta función debe ser definida como sigue:

```php
step(mixed $context, int $rownumber, mixed $value, mixed ...$values): mixed
```

`context`  
`null` para la primera fila; en las filas siguientes, tendrá el valor que fue previamente retornado por la función de retrollamada; debe utilizarse esto para mantener el estado de la agregación.

`rownumber`  
El número de la fila actual.

`value`  
El primer argumento pasado a la agregación.

`values`  
Los argumentos adicionales pasados a la agregación.

El valor de retorno de esta función será utilizado como argumento `context` en la siguiente llamada a la función de retrollamada o de finalización.

`finalize`  
La función de retrollamada para agregar los datos "step" de cada fila. Una vez que todas las filas han sido procesadas, esta función será llamada, y debería entonces tomar los datos del contexto de agregación y retornar el resultado. Esta función de retrollamada debe retornar un tipo comprendido por SQLite (es decir, un [tipo escalar](#language.types.intro)).

Esta función debe ser definida como sigue:

```php
fini(mixed $context, int $rowcount): mixed
```php

`context`  
Contiene el valor de retorno de la última llamada a la función de retrollamada.

`rowcount`  
Contiene el número de filas sobre las cuales se realizó la agregación.

El valor de retorno de esta función será utilizado como valor de retorno para la agregación.

`numArgs`  
Indicación al analizador SQLite si la función de retrollamada acepta un número predeterminado de argumentos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de Pdo\Sqlite::createAggregate

En este ejemplo, se creará una función de agregación personalizada llamada `max_length` que puede ser utilizada en las consultas SQL.

En este ejemplo, se creará una función de agregación llamada `max_length` que calculará la longitud del string más largo en una de las columnas de la tabla. Para cada fila, la función `max_len_step` es llamada y pasa un parámetro `$context`. El parámetro de contexto es como cualquier otra variable PHP y puede ser definido para contener un `array` o incluso un `object`. En este ejemplo, se utiliza para contener la longitud máxima que se ha visto hasta el momento; si el `$string` tiene una longitud mayor que la longitud máxima actual, se actualiza el contexto para contener esta nueva longitud máxima.

Después de que todas las filas han sido procesadas, SQLite llama a la función `max_len_finalize` para determinar el resultado agregado. Es posible realizar algún tipo de cálculo basado en los datos en `$context`. En este ejemplo básico, el resultado fue calculado a medida que la consulta progresaba, por lo que el valor de contexto puede ser retornado directamente.

```
<?php
$data = [
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
];
$db = new Pdo\Sqlite('sqlite::memory:');
$db->exec("CREATE TABLE strings(a)");
$insert = $db->prepare('INSERT INTO strings VALUES (?)');
foreach ($data as $str) {
    $insert->execute(array($str));
}
$insert = null;

function max_len_step($context, $row_number, $string)
{
    if (strlen($string) > $context) {
        $context = strlen($string);
    }
    return $context;
}

function max_len_finalize($context, $row_count)
{
    return $context === null ? 0 : $context;
}

$db->createAggregate('max_len', 'max_len_step', 'max_len_finalize');

var_dump($db->query('SELECT max_len(a) from strings')->fetchAll());

?>

   
```php

> [!TIP]
> NO se recomienda almacenar una copia de los valores en el contexto y procesarlos al final, ya que se obligaría a SQLite a utilizar mucha memoria para procesar la consulta - imagine cuánta memoria se necesitaría si un millón de filas fueran almacenadas en memoria, cada una conteniendo un string de 32 bytes de longitud.

## Véase también

Pdo\Sqlite::createFunction

Pdo\Sqlite::createCollation

sqlite_create_function

sqlite_create_aggregate
