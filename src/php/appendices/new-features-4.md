---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration72.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration72/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 6d2953348
order: 560
---

## Nuevas características

## Nuevo tipo de objeto

Se ha introducido un nuevo tipo, `object`, que puede ser usado para el tipado de parámetros (contravariante) y el tipado de retorno (covariante) de cualquier objeto.

```php
<?php

function test(object $obj) : object
{
    return new SplQueue();
}

test(new stdClass());

   
```

## Carga de extensiones por nombre

Las extensiones compartidas ya no requieren que se especifique su extensión de archivo (`.so` para Unix o `.dll` para Windows) para ser cargadas. Esto está habilitado en el archivo php.ini, así como en la función `dl`.

## Sobrescribir métodos abstractos

Ahora los métodos abstractos pueden ser sobrescritos cuando una clase abstracta extiende otra clase abstracta.

```php
<?php

abstract class A
{
    abstract function test(string $s);
}
abstract class B extends A
{
    // sobrescrito - aún manteniendo la contravarianza para los parámetros y la covarianza para el retorno
    abstract function test($s) : int;
}

   
```

## [Sodium](#book.sodium) ahora es una extensión del núcleo

La biblioteca moderna de criptografía Sodium se ha convertido en una extensión del núcleo en PHP.

Para una referencia completa de funciones, consulte el capítulo [Sodium](#book.sodium).

## Hash de contraseñas con Argon2

Argon2 se ha añadido a la API de [hash de contraseñas](#book.password), donde se han expuesto las siguientes constantes:

- `PASSWORD_ARGON2I`

- `PASSWORD_ARGON2_DEFAULT_MEMORY_COST`

- `PASSWORD_ARGON2_DEFAULT_TIME_COST`

- `PASSWORD_ARGON2_DEFAULT_THREADS`

## Tipos de cadena extendidos para [PDO](#book.pdo)

El tipo de cadena de PDO se ha extendido para soportar el tipo de carácter nacional cuando se emulan preparaciones. Esto se ha hecho con las siguientes constantes:

- `PDO::PARAM_STR_NATL`

- `PDO::PARAM_STR_CHAR`

- `PDO::ATTR_DEFAULT_STR_PARAM`

Estas constantes se utilizan mediante la combinación bit a bit `OR` con `PDO::PARAM_STR`:

```php
<?php

$db->quote('über', PDO::PARAM_STR | PDO::PARAM_STR_NATL);

   
```

## Información adicional de depuración para preparaciones emuladas en [PDO](#book.pdo)

El método `PDOStatement::debugDumpParams` ha sido actualizado para incluir el SQL que se envía a la base de datos, donde se mostrará la consulta completa y sin procesar (incluyendo los marcadores de posición reemplazados con sus valores vinculados). Esto se ha añadido para ayudar en la depuración de preparaciones emuladas (y por lo tanto solo estará disponible cuando las preparaciones emuladas estén activadas).

## Soporte para operaciones extendidas en [LDAP](#book.ldap)

Se ha añadido soporte para EXOP a la extensión LDAP. Esto se ha hecho exponiendo las siguientes funciones y constantes:

- `ldap_parse_exop`

- `ldap_exop`

- `ldap_exop_passwd`

- `ldap_exop_whoami`

- `LDAP_EXOP_START_TLS`

- `LDAP_EXOP_MODIFY_PASSWD`

- `LDAP_EXOP_REFRESH`

- `LDAP_EXOP_WHO_AM_I`

- `LDAP_EXOP_TURN`

## Adiciones de Información de Dirección a la extensión [Sockets](#book.sockets)

La extensión de sockets ahora tiene la capacidad de buscar información de direcciones, así como conectarse a ella, enlazarse a ella y explicarla. Se han añadido las siguientes cuatro funciones para esto:

- `socket_addrinfo_lookup`

- `socket_addrinfo_connect`

- `socket_addrinfo_bind`

- `socket_addrinfo_explain`

## Ampliación del tipo de parámetro

Los tipos de parámetros de métodos sobrescritos y de implementaciones de interfaces ahora pueden ser omitidos. Esto sigue siendo conforme con LSP, ya que los tipos de parámetros son contravariantes.

```php
<?php

interface A
{
    public function Test(array $input);
}

class B implements A
{
    public function Test($input){} // tipo omitido para $input
}

   
```

## Permitir una coma final para namespaces agrupados

Ahora se puede añadir una coma final a la sintaxis de uso agrupado introducida en PHP 7.0.

```php
<?php

use Foo\Bar\{
    Foo,
    Bar,
    Baz,
};

   
```

## Soporte de `proc_nice` en Windows

La función `proc_nice` ahora es soportada en Windows.

## Soporte de endian en `pack` y `unpack`

Las funciones `pack` y `unpack` ahora soportan float y double tanto en little endian como en big endian.

## Mejoras en la extensión [EXIF](#book.exif)

La extensión EXIF se ha actualizado para soportar una gama mucho más amplia de formatos. Esto significa que sus etiquetas específicas de formato ahora se traducen correctamente al analizar imágenes con la función `exif_read_data`. Los siguientes nuevos formatos ahora son soportados:

- Samsung

- DJI

- Panasonic

- Sony

- Pentax

- Minolta

- Sigma/Foveon

- AGFA

- Kyocera

- Ricoh

- Epson

Las funciones EXIF `exif_read_data` y `exif_thumbnail` ahora soportan pasar flujos como su primer argumento.

## Nuevas características en [PCRE](#book.pcre)

- Se ha añadido el modificador `J` para establecer PCRE_DUPNAMES.

## [SQLite3](#book.sqlite3) permite escribir BLOBs

SQLite3::openBlob ahora permite abrir campos BLOB en modo de escritura; anteriormente solo se soportaba el modo de lectura.

## Devoluciones de llamada de [Oracle OCI8](#book.oci8) para Falla Transparente de Aplicaciones

Se ha añadido soporte para [devoluciones de llamada de Falla Transparente de Aplicaciones (TAF) de Oracle Database](#oci8.taf). TAF permite que las aplicaciones PHP OCI8 se reconecten automáticamente a una base de datos preconfigurada cuando una conexión se rompe. El nuevo soporte de devoluciones de llamada de TAF permite que las aplicaciones PHP supervisen y controlen la reconexión durante la falla.

## Mejoras en la extensión [ZIP](#book.zip)

Se ha añadido soporte de lectura y escritura para archivos cifrados (requiere libzip 1.2.0).

La clase `ZipArchive` ahora implementa la interfaz Countable.

El flujo `zip://` ahora acepta una opción de contexto `'password'`.
