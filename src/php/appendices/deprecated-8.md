---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration81.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration81/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 850
---

## Funcionalidades obsoletas

## Núcleo de PHP

### Implementar Serializable sin `__serialize` y `__unserialize`

Solo los nuevos métodos deben ser implementados, si no se proporciona soporte para PHP anterior a la versión 7.4, o ambos deben ser implementados.

### Pasar `null` a parámetros no nullables de funciones nativas

Los tipos escalares de las funciones nativas son nullables por defecto. Este comportamiento está depreciado para alinearse con el comportamiento de las funciones definidas por el usuario, donde los tipos escalares deben ser marcados como nullables explícitamente.

```php
<?php
var_dump(str_contains("foobar", null));
// Deprecated: Passing null to parameter #2 ($needle) of type string
//             is deprecated
?>

     
```

### Conversiones implícitas incompatibles de `float` a `int`

La conversión implícita de `float` a `int` que resulta en una pérdida de precisión ahora está depreciada. Esto afecta a las claves de `array`, las declaraciones de tipo `int` en modo coercitivo, y los operadores que trabajan con `int`s.

```php
<?php
$a = [];
$a[15.5]; // depreciado, ya que el valor de la clave pierde el componente 0.5
$a[15.0]; // ok, ya que 15.0 == 15
?>

     
```

### Llamar a un elemento static en un trait

Llamar a un método static, o acceder a una propiedad static directamente en un trait está depreciado. Los métodos y propiedades estáticas solo deben ser accedidos en una clase que use el trait.

### Devolver un no `array` desde `__sleep`

Devolver un valor que no sea un `array` desde [\_\_sleep()](#object.sleep) ahora genera un diagnóstico.

### Devolver una referencia desde una función `void`

```php
<?php
function &test(): void {}
?>

     
```

Tal función es contradictoria, y ya emite el `E_NOTICE` siguiente cuando se llama: `Only variable references should be returned by reference`.

### La autovivificación desde `false`

La autovivificación es el proceso de crear un nuevo `array` al añadir a un valor. La autovivificación está prohibida desde valores escalares, `false` sin embargo era una excepción. Esto ahora está depreciado.

```php
<?php
$arr = false;
$arr[] = 2;   // depreciado
?>

     
```

> [!NOTE]
> La autovivificación desde `null` y valores indefinidos sigue estando permitida:
>
> <div class="informalexample">
>
> ```
> <?php
> // Desde un valor indefinido
> $arr[] = 'some value';
> $arr['doesNotExist'][] = 2;
> // Desde null
> $arr = null;
> $arr[] = 2;
> ?>
>
>       
> ```
>
> </div>

## ctype

### Verificar argumentos no cadena de caracteres

Pasar un argumento no cadena de caracteres está depreciado. En el futuro, el argumento será interpretado como una cadena de caracteres en lugar de un código ASCII. Según el comportamiento deseado, el argumento debe ser convertido a `string` o se debe hacer una llamada explícita a `chr`. Todas las funciones `ctype_*()` están afectadas.

## Fecha

`date_sunrise` y `date_sunset` han sido depreciadas a favor de `date_sun_info`.

`strptime` ha sido depreciada. Usar `date_parse_from_format` en su lugar (para un análisis independiente de la configuración regional), o IntlDateFormatter::parse (para un análisis dependiente de la configuración regional).

`strftime` y `gmstrftime` han sido depreciadas. Usar `date` en su lugar (para un formateo independiente de la configuración regional), o IntlDateFormatter::format (para un formateo dependiente de la configuración regional).

## Filtro

Los filtros `FILTER_SANITIZE_STRING` y `FILTER_SANITIZE_STRIPPED` están depreciados.

La directiva INI [filter.default](#ini.filter.default) ahora está depreciada.

## GD

El parámetro `num_points` de `imagepolygon`, `imageopenpolygon` y `imagefilledpolygon` ha sido depreciado.

## Hash

Las funciones `mhash`, `mhash_keygen_s2k`, `mhash_count`, `mhash_get_block_size`, y `mhash_get_hash_name` han sido depreciadas. Usar las funciones `hash_*()` en su lugar.

## IMAP

La constante `NIL` ha sido depreciada. Usar `0` en su lugar.

## Intl

Llamar a IntlCalendar::roll con un argumento `bool` está depreciado. Usar `1` y `-1` en lugar de `true` y `false` respectivamente.

## Cadena de caracteres multibyte

Llamar a `mb_check_encoding` sin ningún argumento está depreciado.

## MySQLi

La propiedad mysqli_driver::\$report_mode ha sido depreciada. Era redundante y obsoleta, usar `PHP_VERSION_ID` en su lugar.

Llamar a mysqli::get_client_info o `mysqli_get_client_info` con el argumento `mysqli` ha sido depreciado. Llamar a `mysqli_get_client_info` sin argumentos para obtener la información de versión de la biblioteca cliente.

El método mysqli::init ha sido depreciado. Reemplazar las llamadas a parent::init por parent::\_\_construct.

## OCI8

La directiva INI [oci8.old_oci_close_semantics](#ini.oci8.old-oci-close-semantics) está depreciada.

## ODBC

`odbc_result_all` ha sido depreciada.

## PDO

El modo de recuperación `PDO::FETCH_SERIALIZE` ha sido depreciado.

## PgSQL

No pasar el argumento de conexión a todas las funciones `pgsql_*()` ha sido depreciado.

## SOAP

La opción `ssl_method` de SoapClient::\_\_construct ha sido depreciada a favor de las opciones de contexto de flujo SSL.

## Estándar

Llamar a `key`, `current`, `next`, `prev`, `reset`, o `end` en `object`s está depreciado. Convertir el `object` en `array` con `get_mangled_object_vars` primero, o usar los métodos de una clase que implemente Iterator, como `ArrayIterator`, en su lugar.

La directiva INI [auto_detect_line_endings](#ini.auto-detect-line-endings) está depreciada. Si es necesario, manejar manualmente los saltos de línea `"\r"` en su lugar.

Las constantes `FILE_BINARY` y `FILE_TEXT` han sido depreciadas. Nunca tuvieron efecto.
