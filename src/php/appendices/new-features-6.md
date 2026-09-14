---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration74.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration74/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 720
---

## Nuevas características

## Núcleo de PHP

### Propiedades tipadas

Las propiedades de las clases ahora soportan la declaración de tipos.

```php
<?php
class User {
    public int $id;
    public string $name;
}
?>

     
```

El ejemplo anterior asegura que `$user->id` solo puede recibir valores de tipo `int` y `$user->name` solo puede recibir valores de tipo `string`.

### Funciones flecha

Las [funciones flecha](#functions.arrow) proporcionan una sintaxis corta para definir funciones que enlazan el ámbito por valor de manera implícita.

```php
<?php
$factor = 10;
$nums = array_map(fn($n) => $n * $factor, [1, 2, 3, 4]);
// $nums = array(10, 20, 30, 40);
?>

     
```

### Tipo de retorno covariante y tipo de argumento contravariante limitado

El siguiente código ahora funcionará:

```php
<?php
class A {}
class B extends A {}

class Producer {
    public function method(): A {}
}
class ChildProducer extends Producer {
    public function method(): B {}
}
?>

     
```

El soporte de varianza total solo está disponible cuando se utiliza la carga automática. En un único fichero solo son posibles referencias de tipos no cíclicos, ya que todas las clases deben estar disponibles antes de ser referenciadas.

```php
<?php

/**
 * Estas clases satisfacen los requisitos del LSP, ya que C es un subtipo de A.
 * Sin embargo, en el momento en que se declara la clase B, la clase C aún no está disponible
 */
class A
{
    public function method(): A {}
}

class B extends A
{
    // Error fatal: No se puede verificar la compatibilidad entre B::method():C y
    // A::method(): A, ya que la clase C no está disponible
    public function method(): C {}
}

class C extends B {}

?>

     
```

### Operador de asignación de fusión Null

```php
<?php
$array['key'] ??= computeDefault();
// es aproximadamente equivalente a
if (!isset($array['key'])) {
    $array['key'] = computeDefault();
}
?>

     
```

### Desempaquetado en los arrays

```php
<?php
$parts = ['apple', 'pear'];
$fruits = ['banana', 'orange', ...$parts, 'watermelon'];
// ['banana', 'orange', 'apple', 'pear', 'watermelon'];
?>

     
```

### Separador numérico literal

Los números literales pueden contener un carácter de subrayado entre los dígitos.

```php
<?php
6.674_083e-11; // float
299_792_458;   // decimal
0xCAFE_F00D;   // hexadecimal
0b0101_1111;   // binario
?>

     
```

### Referencias débiles

Las [referencias débiles](#class.weakreference) permiten al desarrollador retener una referencia a un objeto que no impide que el objeto sea destruido.

### Permitir Excepciones desde \_\_toString()

Lanzar excepciones desde [\_\_toString()](#object.tostring) ahora está permitido. Anteriormente, esto resultaba en un error fatal. Los errores fatales recuperables en las conversiones de `string` han sido convertidos en excepciones `Error`.

## CURL

`CURLFile` ahora soporta las envolturas de flujo además de los nombres de ficheros brutos, si la extensión ha sido compilada con libcurl \>= 7.56.0.

## Filtro

El filtro `FILTER_VALIDATE_FLOAT` ahora soporta las opciones `min_range` y `max_range`, con la misma sémantica que `FILTER_VALIDATE_INT`.

## FFI

FFI es una nueva extensión, que proporciona una manera sencilla de llamar a las funciones nativas, acceso nativo a las variables, y la creación/acceso a estructuras de datos definidas en bibliotecas C.

## GD

Se ha añadido el filtro de imagen `IMG_FILTER_SCATTER` para aplicar un filtro de dispersión a las imágenes.

## Hash

Se ha añadido el hash `crc32c` utilizando el polinomio de Castagnoli. Esta variante de CRC32 es utilizada por sistemas de almacenamiento, tales como iSCSI, SCTP, Btrfs y ext4.

## Cadenas multioctetos

Se ha añadido la función `mb_str_split`, que proporciona la misma funcionalidad que `str_split`, pero opera sobre puntos de código en lugar de octetos.

## OPcache

[El soporte para la precarga de código](#opcache.preloading) ha sido añadido.

## Expresiones Regulares (Compatible Perl)

Las funciones `preg_replace_callback` y `preg_replace_callback_array` ahora aceptan un argumento `flags` adicional, con soporte para los flags `PREG_OFFSET_CAPTURE` y `PREG_UNMATCHED_AS_NULL`. Esto influye en el formato del `array` de coincidencias pasado a la función de retrollamada.

## PDO

El nombre de usuario y la contraseña ahora pueden ser especificados como parte del DSN PDO para los controladores mysql, mssql, sybase, dblib, firebird y oci. Anteriormente, esto solo era soportado para el controlador pgsql. Si un nombre de usuario/contraseña es definido tanto en el constructor como en el DSN, el constructor tiene precedencia.

Ahora es posible escapar los signos de interrogación en las consultas SQL para evitar que sean interpretados como parámetro ficticio. Escribir `??` permite enviar un solo signo de interrogación a la base de datos y, por ejemplo, utilizar el operador PostgreSQL JSON para saber si una clave existe (`?`).

## PDO_OCI

PDOStatement::getColumnMeta ahora está disponible.

## PDO_SQLite

`PDOStatement::getAttribute(PDO::SQLITE_ATTR_READONLY_STATEMENT)` permite verificar si la declaración es de solo lectura, es decir, si no modifica la base de datos.

`PDO::setAttribute(PDO::SQLITE_ATTR_EXTENDED_RESULT_CODES, true)` activa el uso de códigos de resultados extendidos en `PDO::errorInfo` y `PDOStatement::errorInfo`.

## SQLite3

Se ha añadido SQLite3::lastExtendedErrorCode para recuperar el último código extendido del resultado.

Se ha añadido `SQLite3::enableExtendedResultCodes($enable = true)`, que hará que SQLite3::lastErrorCode devuelva códigos de resultados extendidos.

## Estándar

### strip_tags() con un array de nombres de tag

`strip_tags` ahora acepta un `array` de tags permitidos: en lugar de `strip_tags($str, '<a><p>')` ahora es posible escribir `strip_tags($str, ['a', 'p'])`.

### Serialización personalizada de objetos

Se ha añadido un nuevo mecanismo de serialización personalizada de objetos, que utiliza dos nuevas métodos mágicos: `__serialize` y `__unserialize`.

```php
<?php
// Devuelve un array que contiene todo el estado necesario del objeto.
public function __serialize(): array
{
}

// Restaura el estado de un objeto desde el array de datos proporcionado.
public function __unserialize(array $data): void
{
}
?>

     
```

El nuevo mecanismo de serialización sucederá a la interfaz Serializable, que será obsoleto en el futuro.

### Las funciones array merge sin argumentos

`array_merge` y `array_merge_recursive` ahora pueden ser llamadas sin argumentos, en cuyo caso devolverán un `array` vacío. Esto es útil en conjunción con el operador de descomposición, por ejemplo `array_merge(...$arrays)`.

### La función `proc_open`

`proc_open` ahora acepta un `array` en lugar de una `string` para la comanda. En este caso, el proceso se abre directamente (sin pasar a través de un shell) y PHP se encargará de escapar los argumentos cuando sea necesario.

```php
<?php
proc_open(['php', '-r', 'echo "Hello World\n";'], $descriptors, $pipes);
?>

     
```

`proc_open` ahora soporta los descriptores `redirect` y `null`.

```php
<?php
// Como 2>&1 en el shell
proc_open($cmd, [1 => ['pipe', 'w'], 2 => ['redirect', 1]], $pipes);
// Como 2>/dev/null o 2>nul en el shell
proc_open($cmd, [1 => ['pipe', 'w'], 2 => ['null']], $pipes);
?>

     
```

### argon2i(d) sin libargon

`password_hash` ahora tiene las implementaciones de argon2i y argon2id de la extensión sodium cuando PHP es compilado sin libargon.
