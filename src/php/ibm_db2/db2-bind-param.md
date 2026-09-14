---
title: db2_bind_param
description: Asocia una variable PHP a un parámetro de una consulta SQL
source_url: https://www.php.net/manual/es/function.db2-bind-param.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-bind-param.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: true
translation_revision: 020edc73b
order: 30630
---

db2_bind_param

Asocia una variable PHP a un parámetro de una consulta SQL

## Descripción

```php
db2_bind_param(resource $stmt, int $parameter_number, string $variable_name, [int $parameter_type], [int $data_type], [int $precision], [int $scale]): bool
```php

Asocia una variable PHP a un parámetro en la consulta SQL devuelta por `db2_prepare`. Esta función permite mayor control sobre los tipos de los parámetros, los tipos de datos, la precisión y la escala para el parámetro que al pasarle simplemente una variable dentro del array de entrada opcional de la función `db2_execute`.

## Parámetros

`stmt`  
Una consulta preparada devuelta por `db2_prepare`.

`parameter_number`  
Especifica la posición del parámetro comenzando en el índice 1 en la consulta preparada.

`variable_name`  
Una cadena que especifica el nombre de la variable PHP a asociar al parámetro especificado por `parameter_number`.

`parameter_type`  
Una constante que especifica si la variable PHP debe ser asociada al parámetro SQL como parámetro de entrada (`DB2_PARAM_IN`), como parámetro de salida (`DB2_PARAM_OUT`) o como parámetro que acepta entradas y salidas (`DB2_PARAM_INOUT`). Para evitar un exceso de consumo de memoria, también puede especificarse `DB2_PARAM_FILE` para asociar la variable PHP al nombre del archivo que contiene los datos del objeto grande (BLOB, CLOB o DBCLOB).

`data_type`  
Una constante que especifica el tipo de datos SQL que la variable PHP debe ser asociada. El parámetro debe tomar uno de los siguientes valores: `DB2_BINARY`, `DB2_CHAR`, `DB2_DOUBLE` o `DB2_LONG`.

`precision`  
Especifica la precisión con la que la variable debe ser asociada a la base de datos. Este parámetro también puede ser utilizado para recuperar valores de salida XML para procedimientos almacenados. Un valor no negativo especifica el tamaño máximo de los datos XML que serán recuperados desde la base de datos. Si este parámetro no es utilizado, se definirá un tamaño por defecto de 1 MB para recuperar los valores de tipo XML desde el procedimiento almacenado.

`scale`  
Especifica la escala con la que la variable debe ser asociada a la base de datos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Asociación de variables PHP a una consulta preparada

La consulta SQL en el siguiente ejemplo utiliza dos parámetros de entrada en la sección WHERE. Se llama a `db2_bind_param` para asociar dos variables que no han sido declaradas o asignadas antes de la llamada a `db2_bind_param`; en este ejemplo, `$lower_limit` es asignada antes de ser llamada a `db2_bind_param`, pero `$upper_limit` es asignada después de la llamada a `db2_bind_param`. Las variables deben ser asociadas y, para los parámetros que aceptan entradas, se les debe asignar un valor antes de llamar a `db2_execute`.

```
<?php

$sql = 'SELECT nom, race, poids FROM animaux
    WHERE poids > ? AND poids < ?';
$conn = db2_connect($database, $user, $password);
$stmt = db2_prepare($conn, $sql);

// Se puede declarar la variable antes de llamar a db2_bind_param()
$lower_limit = 1;

db2_bind_param($stmt, 1, "lower_limit", DB2_PARAM_IN);
db2_bind_param($stmt, 2, "upper_limit", DB2_PARAM_IN);

// También se puede declarar la variable después de llamar a db2_bind_param()
$upper_limit = 15.0;

if (db2_execute($stmt)) {
    while ($row = db2_fetch_array($stmt)) {
        print "{$row[0]}, {$row[1]}, {$row[2]}\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    Pook, chat, 3.2
    Rickety Ride, chèvre, 9.7
    Peaches, chien, 12.3

Llamada a procedimientos de registro con parámetros IN y OUT

El procedimiento de registro concorde_animal en el siguiente ejemplo acepta tres diferentes parámetros:

1.  un parámetro de entrada (IN) que acepta el nombre del primer animal en entrada

2.  un parámetro de entrada-salida (INOUT) que acepta el nombre del segundo animal en entrada y devuelve un `string` `TRUE` si un animal en la base de datos coincide con este nombre

3.  un parámetro de salida (OUT) que devuelve la suma de los pesos de los dos animales identificados

Además, el procedimiento de registro devuelve un conjunto de resultados que contiene los animales listados en orden alfabético comenzando con el animal correspondiente al valor de entrada del primer parámetro y terminando con el animal correspondiente al valor de entrada del segundo parámetro.

```
<?php

$sql = 'CALL concorde_animal(?, ?, ?)';
$conn = db2_connect($database, $user, $password);
$stmt = db2_prepare($conn, $sql);

$nom = "Peaches";
$second_nom = "Rickety Ride";
$poids = 0;

db2_bind_param($stmt, 1, "nom", DB2_PARAM_IN);
db2_bind_param($stmt, 2, "second_nom", DB2_PARAM_INOUT);
db2_bind_param($stmt, 3, "poids", DB2_PARAM_OUT);

print "Valores de los parámetros _antes_ de CALL :\n";
print "  1: {$nom} 2: {$second_nom} 3: {$poids}\n\n";

if (db2_execute($stmt)) {
    print "Valores de los parámetros _después_ de CALL :\n";
    print "  1: {$nom} 2: {$second_nom} 3: {$poids}\n\n";

    print "Resultados :\n";
    while ($row = db2_fetch_array($stmt)) {
        print "  {$row[0]}, {$row[1]}, {$row[2]}\n";
    }
}
?>

    
```php

El ejemplo anterior mostrará:

    Valores de los parámetros _antes_ de CALL :
      1: Peaches 2: Rickety Ride 3: 0

    Valores de los parámetros _después_ de CALL :
      1: Peaches 2: TRUE 3: 22

    Resultados :
      Peaches, chien, 12.3
      Pook, chat, 3.2
      Rickety Ride, chèvre, 9.7

Inserción de un objeto grande binario (BLOB) directamente desde un archivo

Los datos para los objetos grandes normalmente se almacenan en archivos, como documentos XML o archivos de audio. En lugar de leer el archivo completo en una variable de PHP y luego asociar la variable PHP en la consulta SQL, se puede evitar cierto sobrecoste de memoria asociando el archivo directamente al parámetro de entrada de su consulta SQL. El siguiente ejemplo demuestra cómo asociar un archivo directamente en una columna BLOB.

```
<?php
$stmt = db2_prepare($conn, "INSERT INTO animal_pictures(photo) VALUES (?)");

$picture = "/opt/albums/spook/grooming.jpg";
$rc = db2_bind_param($stmt, 1, "picture", DB2_PARAM_FILE);
$rc = db2_execute($stmt);
?>

    
```php

## Véase también

db2_execute

db2_prepare
