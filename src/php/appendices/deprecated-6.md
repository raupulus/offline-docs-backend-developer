---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration74.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration74/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 4642b715f
order: 690
---

## Funcionalidades obsoletas

## Núcleo de PHP

### Operadores ternarios anidados sin paréntesis explícitos

Los operadores ternarios anidados deben utilizar explícitamente paréntesis para dictar el orden de las operaciones. Anteriormente, cuando se utilizaba sin paréntesis, la asociatividad a la izquierda no resultaba en el comportamiento esperado para la mayoría de los casos.

```php
<?php
1 ? 2 : 3 ? 4 : 5;   // obsoleto
(1 ? 2 : 3) ? 4 : 5; // ok
1 ? 2 : (3 ? 4 : 5); // ok
?>

     
```

Los paréntesis no son *necesarios* al anidar en el operando del medio ya que esto siempre es sin ambigüedad y no se ve afectado por la asociatividad:

```php
1 ? 2 ? 3 : 4 : 5 // ok

     
```

### Acceso a la posición de array y string utilizando llaves

La sintaxis para acceder a la posición de `array` y `string` con llaves es obsoleta. Utilizar `$var[$idx]` en lugar de `$var{$idx}`.

### El transtipado (real) y la función `is_real`

El transtipado `(real)` es obsoleto, utilizar `(float)` en su lugar.

La función `is_real` también es obsoleta, utilizar `is_float` en su lugar.

### Desligar `$this` cuando `$this` es utilizado

Desligar `$this` de una clausura no estática que utiliza `$this` es obsoleto.

### Palabra clave `parent` sin clase padre

El uso de `parent` dentro de una clase sin padre es obsoleto, y emitirá un error en la compilación en el futuro. Actualmente, solo se generará un error si/cuando un padre es accedido durante la ejecución.

### Opción INI allow_url_include

La directiva INI [allow_url_include](#ini.allow-url-include) es obsoleta. Activarla generará un aviso de obsolescencia al inicio.

### Caracteres inválidos en las funciones de conversión de base

Pasar caracteres inválidos a `base_convert`, `bindec`, `octdec` y `hexdec` generará ahora un aviso de obsolescencia. El resultado siempre se calculará como si los caracteres inválidos no existieran. Los caracteres de espaciado en blanco, así como los prefijos de tipo 0x (en función de la base) continúan siendo aceptados.

### El uso de `array_key_exists` en objetos

El uso de `array_key_exists` en objetos es obsoleto. En su lugar, `isset` o `property_exists` deberían ser utilizados.

### Funciones de comillas mágicas

Las funciones `get_magic_quotes_gpc` y `get_magic_quotes_runtime` son obsoletas. Siempre devuelven `false`.

### Función `hebrevc`

La función `hebrevc` es obsoleta. Puede ser reemplazada por `nl2br(hebrev($str))` o, preferiblemente, utilizando el soporte Unicode RTL (Derecha a Izquierda).

### Función `convert_cyr_string`

La función `convert_cyr_string` es obsoleta. Puede ser reemplazada por una de `mb_convert_string`, `iconv` o `UConverter`.

### Función `money_format`

La función `money_format` es obsoleta. Puede ser reemplazada por la funcionalidad intl `NumberFormatter`.

### Función `ezmlm_hash`

La función `ezmlm_hash` es obsoleta.

### Función `restore_include_path`

La función `restore_include_path` es obsoleta. Puede ser reemplazada por `ini_restore('include_path')`.

### Implode con el orden de parámetros histórico

Pasar los parámetros a `implode` en el orden inverso es obsoleto, utilizar `implode($glue, $parts)` en lugar de `implode($parts, $glue)`.

## COM

La importación de bibliotecas de tipo con el registro de constantes no sensibles a mayúsculas y minúsculas ha sido declarada obsoleta.

## Filtro

`FILTER_SANITIZE_MAGIC_QUOTES` es obsoleto, utilizar `FILTER_SANITIZE_ADD_SLASHES` en su lugar.

## Cadenas Multi-octetos

Pasar un patrón que no es una `string` a `mb_ereg_replace` es obsoleto. Actualmente, los patrones que no son `string` son interpretados como punto de código ASCII. En PHP 8, el patrón será interpretado como una `string` en su lugar.

Pasar la codificación como tercer parámetro a `mb_strrpos` es obsoleto. En su lugar, pasar una posición de 0, y la codificación como cuarto parámetro.

## Protocolo Ligero de Acceso a Directorios (LDAP)

`ldap_control_paged_result_response` y `ldap_control_paged_result` son obsoletos. Los controles de paginación pueden ser enviados con `ldap_search` en su lugar.

## Reflection

La llamada a ReflectionType::\_\_toString genera ahora un aviso de obsolescencia. Este método fue deprecado en favor de ReflectionNamedType::getName en la documentación a partir de PHP 7.1, pero no lanzaba un aviso de obsolescencia por razones técnicas.

Los métodos `export()` en todas las clases `Reflection` son obsoletos. Crear un objeto `Reflection` y convertirlo en `string` en su lugar:

```php
<?php
// ReflectionClass::export(Foo::class, false) es:
echo new ReflectionClass(Foo::class), "\n";

// $str = ReflectionClass::export(Foo::class, true) es:
$str = (string) new ReflectionClass(Foo::class);
?>

     
```

## Socket

Los flags `AI_IDN_ALLOW_UNASSIGNED` y `AI_IDN_USE_STD3_ASCII_RULES` para `socket_addrinfo_lookup` son obsoletos, debido a una deprecación en glibc.
