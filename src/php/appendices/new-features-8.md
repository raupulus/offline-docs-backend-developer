---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration81.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration81/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 161dde4fe
order: 880
---

## Nuevas características

## Núcleo de PHP

### Prefijo literal octal entero

Los enteros octales ahora pueden usar un prefijo explícito `0o`/`0O` en literales enteros, de manera similar a los literales enteros binarios y hexadecimales.

```php
<?php
014;  // Literal octal sin prefijo
0o14; // Literal octal prefixed
?>

     
```

### Desempaquetado de array con claves de cadena de caracteres

Se ha añadido soporte para [el desempaquetado de array con claves de cadena de caracteres](#language.types.array.unpacking).

```php
<?php
$arr1 = [1, 'a' => 'b'];
$arr2 = [...$arr1, 'c' => 'd']; //[1, 'a' => 'b', 'c' => 'd']
?>

     
```

### Argumento nombrado después de un desempaquetado de argumento

Ahora es posible especificar argumentos nombrados después de un desempaquetado de argumento. por ejemplo: foo(...\$args, named: \$arg).

### Clave de ruta completa para subidas de archivos

Las subidas de archivos ahora proporcionan una clave `full_path` adicional, que contiene la ruta completa (en lugar de solo el nombre base) del archivo subido. Esto está destinado a ser usado en conjunción con "upload webkitdirectory".

### Enumeraciones

Se ha añadido soporte para [enumeraciones](#language.enumerations).

### Fibras

Se ha añadido soporte para [fibras](#language.fibers).

### Sintaxis de callable de primera clase

Las cierres para callables ahora pueden ser creadas usando [la sintaxis `myFunc(...)`](#functions.first_class_callable_syntax), que es idéntica a `Closure::fromCallable('myFunc')`.

> [!NOTE]
> El `...` es parte de la sintaxis, y no una omisión.

### Intersección de tipos

Se ha añadido soporte para [intersección de tipos](#language.types.type-system.composite.intersection).

> [!CAUTION]
> [ Los tipos de intersección](#language.types.type-system.composite.intersection) no pueden ser usados con [ los tipos de unión](#language.types.declarations.composite.union)

### El tipo never

Se ha añadido un nuevo tipo de retorno `never`. Esto indica que una función o bien `exit`, lanza una excepción, o no termina.

### [`new`](#language.oop5.basic.new) en los inicializadores

Ahora es posible usar expresiones `new ClassName()` como valor por defecto de un parámetro, una variable estática, inicializadores de constantes globales, y como argumentos de atributo. Los objetos también pueden ser pasados a `define` ahora.

### Propiedades de solo lectura

Se ha añadido soporte para [solo lectura](#language.oop5.properties.readonly-properties).

### Constantes de clase finales

Se ha añadido soporte para [el modificador final para constantes de clase](#language.oop5.final.example.php81). Además, las constantes de interfaz se vuelven sobrecargables por defecto.

## CURL

Se ha añadido la opción `CURLOPT_DOH_URL`.

Se han añadido opciones para certificados blob cuando libcurl \>= 7.71.0:

- `CURLOPT_ISSUERCERT_BLOB`

- `CURLOPT_PROXY_ISSUERCERT`

- `CURLOPT_PROXY_ISSUERCERT_BLOB`

- `CURLOPT_PROXY_SSLCERT_BLOB`

- `CURLOPT_PROXY_SSLKEY_BLOB`

- `CURLOPT_SSLCERT_BLOB`

- `CURLOPT_SSLKEY_BLOB`

Se ha añadido `CURLStringFile`, que puede ser usado para enviar un archivo desde una `string` en lugar de un archivo:

```php
<?php
$file = new CURLStringFile($data, 'filename.txt', 'text/plain');
curl_setopt($curl, CURLOPT_POSTFIELDS, ['file' => $file]);
?>

    
```

## FPM

Se ha añadido el formato de estado openmetrics. Puede ser usado por Prometheus para recuperar las métricas FPM.

Se ha añadido una nueva opción de pool para el gestor de procesos dinámico llamada `pm.max_spawn_rate`. Permite iniciar un número de hijos a una tasa más rápida cuando el gestor de procesos dinámico está seleccionado. El valor por defecto es `32` que era el valor anterior codificado.

## GD

El soporte Avif ahora está disponible a través de `imagecreatefromavif` y `imageavif`, si libgd ha sido compilado con soporte Avif.

## Hash

Las siguientes funciones `hash`, `hash_file`, y `hash_init` ahora soportan un nuevo argumento opcional `options`, que puede ser usado para pasar datos específicos al algoritmo.

### MurmurHash3

Se ha añadido soporte para `MurmurHash3` con soporte de streaming. Las siguientes variantes están implementadas:

- murmur3a, hash de 32-bit

- murmur3c, hash de 128-bit para x86

- murmur3f, hash de 128-bit para x64

El estado de hash inicial puede ser pasado vía la clave `seed` en el array `options`, por ejemplo:

```php
      
<?php
$h = hash("murmur3f", $data, options: ["seed" => 42]);
echo $h, "\n";
?>

     
```

Un valor de semilla válido está en el rango de `0` a la `UINT_MAX` definida por la plataforma, generalmente `4294967295`.

### xxHash

Se ha añadido soporte para `xxHash`. Las siguientes variantes están implementadas:

- xxh32, hash de 32-bit

- xxh64, hash de 64-bit

- xxh3, hash de 64-bit

- xxh128, hash de 128-bit

El estado de hash inicial puede ser pasado vía la clave `seed` en el array `options`, por ejemplo:

```php
      
<?php
$h = hash("xxh3", $data, options: ["seed" => 42]);
echo $h, "\n";
?>

     
```

El uso secreto es soportado pasando la clave `secret` en el array `options`, también:

```php
      
<?php
$h = hash("xxh3", $data, options: ["secret" => "at least 136 bytes long secret here"]);
echo $h, "\n";
?>

     
```

La calidad del secreto personalizado es crucial para la calidad del hash resultante. Se recomienda encarecidamente usar la mejor entropía posible.

## MySQLi

### Nueva directiva INI`mysqli.local_infile_directory`

Se ha añadido la directiva INI [mysqli.local_infile_directory](#ini.mysqli.local-infile-directory), que puede ser usada para especificar un directorio desde el cual los archivos están permitidos ser cargados. Solo tiene sentido si [mysqli.allow_local_infile](#ini.mysqli.allow-local-infile) no está activado, ya que todos los directorios están permitidos en ese caso.

### Enlazar parámetros en execute

Ahora es posible enlazar parámetros pasándolos como un array a mysqli_stmt::execute. Todos los valores serán enlazados como strings. Solo los arrays de lista están permitidos. Esta nueva funcionalidad no está disponible cuando MySQLi es compilado con libmysqlclient.

```php
<?php
$stmt = $mysqli->prepare('INSERT INTO users(id, name) VALUES(?,?)');
$stmt->execute([1, $username]);
?>

     
```

### Nuevo método mysqli_result::fetch_column

mysqli_result::fetch_column ha sido añadido para permitir recuperar un solo valor escalar del conjunto de resultados. El nuevo método acepta un parámetro de columna opcional `column` basado en 0 de tipo `int` especificando qué columna recuperar.

```php
<?php
$result = $mysqli->query('SELECT username FROM users WHERE id = 123');
echo $result->fetch_column();
?>

     
```

## PDO

Se ha añadido el atributo `PDO::MYSQL_ATTR_LOCAL_INFILE_DIRECTORY`, que puede ser usado para especificar un directorio desde el cual los archivos están permitidos ser cargados. Solo tiene sentido si `PDO::MYSQL_ATTR_LOCAL_INFILE` no está activado, ya que todos los directorios están permitidos en ese caso.

## PDO_SQLite

La sintaxis DSN `"file:"` de SQLite ahora es soportada, lo que permite especificar banderas adicionales. Esta funcionalidad no está disponible si open_basedir está definido.

```php
<?php
new PDO('sqlite:file:path/to/sqlite.db?mode=ro')
?>

    
```

## POSIX

Se ha añadido `POSIX_RLIMIT_KQUEUES` y `POSIX_RLIMIT_NPTS`. Estos límites soft y hard solo están disponibles en FreeBSD.

## Estándar

`fputcsv` ahora acepta un nuevo argumento `eol` que permite definir una secuencia de fin de línea personalizada, el valor por defecto sigue siendo el mismo y es `"\n"`.

## SPL

SplFileObject::fputcsv ahora acepta un nuevo argumento `eol` que permite definir una secuencia de fin de línea personalizada, el valor por defecto sigue siendo el mismo y es `"\n"`.
