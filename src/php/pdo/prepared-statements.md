---
title: Consultas preparadas y procedimientos almacenados
source_url: https://www.php.net/manual/es/pdo.prepared-statements.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/prepared-statements.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 84e8f0960
order: 62220
---

## Consultas preparadas y procedimientos almacenados

La mayoría de las bases de datos soportan el concepto de consultas preparadas. ¿Qué son? Pueden verse como una especie de plantilla compilada para el SQL que se desea ejecutar, que puede ser personalizada utilizando variables como parámetros. Las consultas preparadas ofrecen dos funcionalidades esenciales:

- La consulta solo debe ser analizada (o preparada) una vez, pero puede ser ejecutada múltiples veces con parámetros idénticos o diferentes. Cuando la consulta es preparada, la base de datos analizará, compilará y optimizará su plan para ejecutar la consulta. Para consultas complejas, este proceso puede tomar bastante tiempo, lo que puede ralentizar las aplicaciones si se debe repetir la misma consulta múltiples veces con diferentes parámetros. Al utilizar consultas preparadas, se evita repetir el ciclo análisis/compilación/optimización. En resumen, las consultas preparadas utilizan menos recursos y se ejecutan más rápidamente.

- Los parámetros para preparar las consultas no necesitan estar entre comillas; el controlador gestiona esto. Si la aplicación utiliza exclusivamente consultas preparadas, se puede estar seguro de que no es posible ninguna inyección SQL (Sin embargo, si se construyen otras partes de la consulta basándose en entradas de usuario, se sigue asumiendo un riesgo).

Las consultas preparadas son tan prácticas que es la única funcionalidad que PDO emula para los controladores que no las soportan. Esto asegura poder utilizar la misma técnica para acceder a los datos, sin preocuparse por las capacidades de la base de datos.

Inserciones repetitivas utilizando consultas preparadas

Este ejemplo realiza una consulta INSERT sustituyendo un `nombre` y un `valor` para los marcadores nombrados.

```php
<?php
$stmt = $dbh->prepare("INSERT INTO REGISTRY (name, value) VALUES (:name, :value)");
$stmt->bindParam(':name', $name);
$stmt->bindParam(':value', $value);

// inserción de una fila
$name = 'one';
$value = 1;
$stmt->execute();

// inserción de otra fila con valores diferentes
$name = 'two';
$value = 2;
$stmt->execute();
?>

   
```

Inserciones repetidas utilizando consultas preparadas

Este ejemplo realiza una consulta INSERT sustituyendo un `nombre` y un `valor` para los marcadores `?`.

```php
<?php
$stmt = $dbh->prepare("INSERT INTO REGISTRY (name, value) VALUES (?, ?)");
$stmt->bindParam(1, $name);
$stmt->bindParam(2, $value);

// inserción de una fila
$name = 'one';
$value = 1;
$stmt->execute();

// inserción de otra fila con diferentes valores
$name = 'two';
$value = 2;
$stmt->execute();
?>

   
```

Recuperación de datos utilizando consultas preparadas

Este ejemplo recupera datos basados en el valor de una clave proporcionada por un formulario. La entrada del usuario es automáticamente escapada, por lo que no hay riesgo de ataque por inyección SQL.

```php
<?php
$stmt = $dbh->prepare("SELECT * FROM REGISTRY where name = ?");
$stmt->execute([$_GET['name']]);
foreach ($stmt as $row) {
  print_r($row);
}
?>

   
```

Llamada a un procedimiento almacenado con un parámetro de salida

Si el controlador de la base de datos lo soporta, también se pueden vincular parámetros tanto para entrada como para salida. Los parámetros de salida se utilizan típicamente para recuperar valores de un procedimiento almacenado. Los parámetros de salida son un poco más complejos de usar que los parámetros de entrada ya que se debe conocer la longitud que un parámetro dado podrá alcanzar cuando se vincule. Si el valor devuelto es más largo que el tamaño sugerido, se emitirá un error.

```php
<?php
$stmt = $dbh->prepare("CALL sp_returns_string(?)");
$stmt->bindParam(1, $return_value, PDO::PARAM_STR, 4000);

// Llamada al procedimiento almacenado
$stmt->execute();

print "El procedimiento ha devuelto: $return_value\n";
?>

   
```

Llamada a un procedimiento almacenado con un parámetro de entrada/salida

También se deben especificar los parámetros que gestionan valores tanto para entrada como para salida; la sintaxis es similar a los parámetros de salida. En el siguiente ejemplo, la cadena 'Hola' es pasada al procedimiento almacenado y cuando devuelve el valor, 'Hola' es reemplazada por el valor devuelto por el procedimiento.

```php
<?php
$stmt = $dbh->prepare("CALL sp_takes_string_returns_string(?)");
$value = 'hello';
$stmt->bindParam(1, $value, PDO::PARAM_STR|PDO::PARAM_INPUT_OUTPUT, 4000);

// llamada al procedimiento almacenado
$stmt->execute();

print "El procedimiento ha devuelto: $value\n";
?>

   
```

Uso inválido de marcador

```php
<?php
$stmt = $dbh->prepare("SELECT * FROM REGISTRY where name LIKE '%?%'");
$stmt->execute([$_GET['name']]);

// un marcador debe ser utilizado en lugar de un valor completo
$stmt = $dbh->prepare("SELECT * FROM REGISTRY where name LIKE ?");
$stmt->execute(["%$_GET[name]%"]);
?>

   
```
