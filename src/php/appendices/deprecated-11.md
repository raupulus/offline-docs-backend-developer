---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration84.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: ee1ce6a0e
order: 1100
---

## Funcionalidades obsoletas

## Núcleo de PHP

### Parámetro implícitamente anulable

Un parámetro se amplía implícitamente para aceptar `null` si el valor por defecto es `null`.

El siguiente código:

```php
<?php
function foo(T1 $a = null) {}

     
```

debería convertirse en:

```php
<?php
function foo(T1|null $a = null) {}

     
```

o

```php
<?php
function foo(?T1 $a = null) {}

     
```

De lo contrario, si una declaración de parámetro es seguida por un parámetro obligatorio:

```php
<?php
function foo(T1 $a, T2 $b = null, T3 $c) {}

     
```

Debe convertirse en:

```php
<?php
function foo(T1 $a, T2|null $b, T3 $c) {}

     
```

o

```php
<?php
function foo(T1 $a, ?T2 $b, T3 $c) {}

     
```

porque los parámetros opcionales antes de los parámetros obligatorios están desaprobados.

### Elevar cero a la potencia de un número negativo

Elevar un número a la potencia de un número negativo es equivalente a tomar el recíproco del número elevado al opuesto positivo de la potencia. Es decir, `10-2` es equivalente a `1 / 102`. Por lo tanto, elevar `0` a la potencia de un número negativo corresponde a una división por `0`, es decir, que `0-2` es equivalente a `1 / 02`, o `1 / 0`. Por lo tanto, este comportamiento ha sido desaprobado.

Esto afecta al operador de exponenciación `**` y a la función `pow`.

Si se desea la semántica IEEE 754, se debe usar la nueva función `fpow`.

### Uso del guion bajo `_` como nombre de clase

Llamar a una clase `_` ahora está desaprobado:

```php
<?php
class _ {}

     
```

> [!NOTE]
> Las clases cuyo nombre comienza con un guion bajo *no* están desaprobadas:
>
> <div class="informalexample">
>
> ```
> <?php
> class _MyClass {}
>
>       
> ```
>
> </div>

### Usar `trigger_error` con `E_USER_ERROR`

Llamar a `trigger_error` con `error_level` igual a `E_USER_ERROR` ahora está desaprobado.

Tal uso debería ser reemplazado por lanzar una excepción, o llamar a `exit`, según lo que sea más apropiado.

### La constante `E_STRICT`

Debido a que el nivel de error `E_STRICT` ha sido eliminado, esta constante ahora está desaprobada.

## cURL

La constante `CURLOPT_BINARYTRANSFER` ahora está desaprobada.

## Fecha

La firma `DatePeriod::__construct(string $isostr, int $options = 0)` ahora está desaprobada. Usar DatePeriod::createFromISO8601String en su lugar.

Las constantes `SUNFUNCS_RET_TIMESTAMP`, `SUNFUNCS_RET_STRING`, y `SUNFUNCS_RET_DOUBLE` ahora están desaprobadas. Esto sigue a la desaprobación de las funciones `date_sunset` y `date_sunrise` en PHP 8.1.0.

## DBA

Pasar `null` o `false` a `dba_key_split` ahora está desaprobado. Esto siempre devolvía `false` en estos casos.

## DOM

La constante `DOM_PHP_ERR` ahora está desaprobada.

Las siguientes propiedades han sido formalmente desaprobadas: DOMDocument::\$actualEncoding, DOMDocument::\$config, DOMEntity::\$actualEncoding, DOMEntity::\$encoding, DOMEntity::\$version

## Hash

Pasar opciones no válidas a las funciones de hash ahora está desaprobado.

## Intl

Llamar a `intlcal_set` o IntlCalendar::set con más de dos argumentos ahora está desaprobado. Usar IntlCalendar::setDate o IntlCalendar::setDateTime en su lugar.

Llamar a `intlgregcal_create_instance` o IntlGregorianCalendar::\_\_construct con más de dos argumentos ahora está desaprobado. Usar IntlGregorianCalendar::createFromDate o IntlGregorianCalendar::createFromDateTime en su lugar.

## LDAP

Llamar a `ldap_connect` con más de dos argumentos ahora está desaprobado. Usar `ldap_connect_wallet` en su lugar.

Llamar a `ldap_exop` con más de cuatro argumentos ahora está desaprobado. Usar `ldap_exop_sync` en su lugar.

## MySQLi

La función `mysqli_ping` y el método mysqli::ping ahora están desaprobados porque la funcionalidad de reconexión fue eliminada en PHP 8.2.0.

La función `mysqli_kill` y el método mysqli::kill ahora están desaprobados. Si esta funcionalidad es necesaria, se puede usar un comando SQL `KILL` en su lugar.

La función `mysqli_refresh` y el método mysqli::refresh ahora están desaprobados. Si esta funcionalidad es necesaria, se puede usar un comando SQL `FLUSH` en su lugar. Todas las constantes `MYSQLI_REFRESH_*` también han sido desaprobadas.

Pasar el parámetro `mode` a `mysqli_store_result` explícitamente ha sido desaprobado. Como la constante `MYSQLI_STORE_RESULT_COPY_DATA` solo se usaba en conjunción con esta función, también ha sido desaprobada.

## PDO_PGSQL

Usar puntos de interrogación escapados (`??`) dentro de cadenas delimitadas por dólares ahora está desaprobado. Como PDO_PGSQL ahora tiene su propio analizador SQL con soporte para cadenas delimitadas por dólares, ya no es necesario escapar los puntos de interrogación dentro de ellas.

## PGSQL

Los 2 argumentos de la firma de `pg_fetch_result`, `pg_field_prtlen`, y `pg_field_is_null` ahora están desaprobados. Usar la firma de 3 argumentos con `row` definido a `null` en su lugar.

## Random

`lcg_value` ahora está desaprobada, porque la función está rota de varias maneras. Usar Random\Randomizer::getFloat en su lugar.

## Reflection

Llamar a ReflectionProperty::setValue con un solo parámetro ahora está desaprobado. Usar ReflectionMethod::createFromMethodName

## Sesión

Llamar a `session_set_save_handler` con más de dos argumentos ahora está desaprobado. Usar la firma de dos argumentos en su lugar.

Cambiar el valor de los parámetros INI [`session.sid_length`](#ini.session.sid-length) y [`session.sid_bits_per_character`](#ini.session.sid-bits-per-character) está desaprobado. Actualizar el backend de almacenamiento de sesión para aceptar identificadores de sesión hexadecimales de 32 caracteres y dejar de cambiar estos dos parámetros INI en su lugar.

Cambiar el valor de los parámetros INI [`session.use_only_cookies`](#ini.session.use-only-cookies), [`session.use_trans_sid`](#ini.session.use-trans-sid), [`session.trans_sid_tags`](#ini.session.trans-sid-tags), [`session.trans_sid_hosts`](#ini.session.trans-sid-hosts), y [`session.referer_check`](#ini.session.referer-check) está desaprobado. La constante `SID` también está desaprobada.

## SOAP

Pasar un `int` a SoapServer::addFunction ahora está desaprobado. Si todas las funciones PHP deben ser proporcionadas, aplanar el array devuelto por `get_defined_functions`.

La constante `SOAP_FUNCTIONS_ALL` ahora está desaprobada.

## SPL

El método SplFixedArray::\_\_wakeup ahora está desaprobado, porque implementa SplFixedArray::\_\_serialize y SplFixedArray::\_\_unserialize que deben ser sobrescritos en su lugar.

Usar el valor por defecto del parámetro `escape` para SplFileObject::setCsvControl, SplFileObject::fputcsv, y SplFileObject::fgetcsv ahora está desaprobado. Su valor debe pasarse explícitamente ya sea posicionalmente o a través de argumentos nombrados. Esto no se aplica a SplFileObject::fputcsv y SplFileObject::fgetcsv si SplFileObject::setCsvControl ha sido usado para definir un nuevo valor por defecto.

## Estándar

Llamar a `stream_context_set_option` con dos argumentos ahora está desaprobado. Usar `stream_context_set_options` en su lugar.

Deserializar cadenas usando la etiqueta `S` en mayúscula con `unserialize` ahora está desaprobado.

Usar el valor por defecto del parámetro `escape` para `fputcsv`, `fgetcsv`, y `str_getcsv` ahora está desaprobado. Debe pasarse explícitamente ya sea posicionalmente o a través de argumentos nombrados.

## XML

La función `xml_set_object` ha sido desaprobada.

Pasar una cadena no-`callable` a las funciones `xml_set_*` ahora está desaprobado.
