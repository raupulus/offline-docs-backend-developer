---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration73.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration73/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: b37727aba
order: 630
---

## Nuevas características

## Núcleo de PHP

### Sintaxis Más Flexible para Heredoc y Nowdoc

El marcador de cierre para las cadenas doc ya no es requerido de ser seguido por un punto y coma o un retorno de línea. Adicionalmente, el marcador de cierre puede ser indentado, en este caso la indentación será retirada de todas las líneas en la cadena doc.

### La Desestructuración de Arrays Soporta las Asignaciones de Referencia

La desestructuración de arrays soporta ahora las asignaciones de referencia utilizando la sintaxis `[&$a, [$b, &$c]] = $d`. Esto también es soportado para `list`.

### El Operador Instanceof Acepta los Literales

`instanceof` acepta ahora los literales como primer operando, en este caso el resultado es siempre `false`.

### Excepción CompileError en Lugar de Algunos Errores de Compilación

Se ha añadido una nueva excepción `CompileError`, de la cual `ParseError` hereda. Un pequeño número de errores de compilación lanzarán ahora `CompileError` en lugar de generar un error fatal. Actualmente esto afecta únicamente a los errores de compilación que pueden ser lanzados por `token_get_all` en el modo `TOKEN_PARSE`, pero más errores podrán ser convertidos en el futuro.

### Las Comas de Fin son Autorizadas en las Llamadas

Las comas de fin en las llamadas de funciones y métodos son ahora autorizadas.

### Soporte para Argon2id

El argumento de configuración `--with-password-argon2[=dir]` proporciona ahora el soporte para los hash Argon2i y Argon2id en las funciones `password_hash`, `password_verify`, `password_get_info`, y `password_needs_rehash`. Las contraseñas pueden ser hasheadas y verificadas utilizando la constante `PASSWORD_ARGON2ID`. El soporte para Argon2i y Argon2id en las funciones `password_*` requiere ahora que PHP esté ligado a la biblioteca de referencia libargon2 ≥ 20161029.

## Gestor de Procesos FastCGI

Se han añadido nuevas opciones para personalizar los registros de eventos FPM :

`log_limit`  
Esta opción global puede ser utilizada para definir el límite de registro para la línea registrada, lo que permite consignar mensajes de más de 1024 caracteres sin retorno de línea. También corrige diversos problemas de embalaje (retorno de línea).

`log_buffering`  
Esta opción global permite un registro experimental sin almacenamiento en búfer adicional.

`decorate_workers_output`  
Esta opción de pool permite desactivar la decoración de salida para las salidas de los workers cuando `catch_workers_output` está activado.

## Funciones BC Math

`bcscale` puede ahora ser utilizado como recuperador para recuperar la precisión actualmente en uso.

## Protocolo Ligero de Acceso a Directorios

Se ha añadido soporte total para los Controles LDAP a las funciones de consulta [LDAP](#book.ldap) y `ldap_parse_result` :

- Se ha añadido un parámetro `$controls` para enviar los controles al servidor en `ldap_add`, `ldap_mod_replace`, `ldap_mod_add`, `ldap_mod_del`, `ldap_rename`, `ldap_compare`, `ldap_delete`, `ldap_modify_batch`, `ldap_search`, `ldap_list` y `ldap_read`.

- Se ha añadido el parámetro de salida `$controls` para recuperar los controles desde el servidor en `ldap_parse_result`.

- Se ha corregido el soporte para `LDAP_OPT_SERVER_CONTROLS` y `LDAP_OPT_CLIENT_CONTROLS` en `ldap_get_option` y `ldap_set_option`.

## Funciones para las Cadenas Multi-Octetos

### Soporte para el Mapeo de Caja Completa y Plegado de Caja

Se ha añadido soporte para el mapeo de caja completa y plegado de caja. A diferencia del mapeo básico de caja, el mapeo de caja completa puede modificar la longitud de la cadena. Por ejemplo :

```php
<?php
mb_strtoupper("Straße");
// Produce STRAßE en PHP 7.2
// Produce STRASSE en PHP 7.3
?>

     
```

Los diferentes modos de mapeo y plegado de caja están disponibles a través de `mb_convert_case` :

- `MB_CASE_LOWER` (utilizado por `mb_strtolower`)

- `MB_CASE_UPPER` (utilizado por `mb_strtoupper`)

- `MB_CASE_TITLE`

- `MB_CASE_FOLD`

- `MB_CASE_LOWER_SIMPLE`

- `MB_CASE_UPPER_SIMPLE`

- `MB_CASE_TITLE_SIMPLE`

- `MB_CASE_FOLD_SIMPLE` (utilizado por las operaciones insensibles a la caja)

Solo se realiza un mapeo completo de caja, incondicional e independiente del idioma.

### Las Operaciones de Cadenas Insensibles a la Caja Utilizan el Plegado de Caja

Las operaciones de cadenas insensibles a la caja utilizan ahora el plegado de caja en lugar del mapeo de caja durante las comparaciones. Esto significa que más caracteres serán considerados (insensibles a la caja) iguales ahora.

### MB_CASE_TITLE Ejecuta una Conversión de Caja de Título

`mb_convert_case` con `MB_CASE_TITLE` ejecuta ahora una conversión de caja de título basada en las propiedades derivadas Unicode Cased y CaseIgnorable. En particular, esto también mejora la gestión de las comillas y apóstrofes.

### Soporte para Unicode 11

Las tablas de datos para las [Cadenas Multi-octetos](#book.mbstring) han sido actualizadas para Unicode 11.

### Soporte para las Cadenas Largas

Las [Funciones de Cadenas Multi-Octetos](#ref.mbstring) soportan ahora correctamente las cadenas más grandes que 2Go.

### Mejora de las Performances

Las performances de la extensión de las [Cadenas Multi-Octetos](#book.mbstring) han sido mejoradas de manera significativa a todos los niveles. Las mayores mejoras están en las funciones de conversión de caja.

### Soporte para las Capturas Nombradas

Las funciones `mb_ereg_*` soportan ahora las capturas nombradas. Las funciones de correspondencias como `mb_ereg` devolverán ahora las capturas nombradas utilizando tanto sus números de grupo como sus nombres, similares a PCRE :

```php
<?php
mb_ereg('(?<word>\w+)', '国', $matches);
// => [0 => "国", 1 => "国", "word" => "国"];
?>

     
```

Además, `mb_ereg_replace` soporta ahora las notaciones `\k<>` y `\k''` para hacer referencia a las capturas nombradas en la cadena de reemplazo :

```php
<?php
mb_ereg_replace('\s*(?<word>\w+)\s*', "_\k<word>_\k'word'_", ' foo ');
// => "_foo_foo_"
?>

     
```

`\k<>` y `\k''` pueden también ser utilizados para las referencias numéricas, que también funcionan con números de grupo superiores a 9.

## Readline

Se ha añadido soporte para las opciones `completion_append_character` y `completion_suppress_append` a `readline_info`. Estas opciones están disponibles solo si PHP está ligado a libreadline (en lugar de libedit).
