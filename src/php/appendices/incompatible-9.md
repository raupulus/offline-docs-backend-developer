---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration82.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration82/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 763b31ef6
order: 940
---

## Cambios incompatibles con versiones anteriores

## Fecha

DateTime::createFromImmutable ahora tiene un tipo de retorno provisional `static`, anteriormente era `DateTime`.

DateTimeImmutable::createFromMutable ahora tiene un tipo de retorno provisional `static`, anteriormente era `DateTimeImmutable`.

Los símbolos `number` en los [formatos relativos](#datetime.formats.relative) ya no aceptan signos múltiples, por ejemplo `+-2`.

## ODBC

La extensión ODBC ahora escapa el nombre de usuario y la contraseña en el caso donde una cadena de conexión y un nombre de usuario/contraseña son pasados, y la cadena debe ser agregada. Anteriormente, los valores de usuario que contenían valores que necesitaban ser escapados podían crear una cadena de conexión malformada o inyectar valores desde datos proporcionados por el usuario. Las reglas de escape deben ser idénticas al comportamiento de DbConnectionOptions en la BCL .NET.

## PDO_ODBC

La extensión PDO_ODBC también escapa el nombre de usuario y la contraseña cuando una cadena de conexión es pasada. Ver la [modificación de la extensión ODBC](#migration82.incompatible.odbc) para más detalles.

## Estándar

`glob` ahora devuelve un `array` vacío si todos los caminos de acceso están restringidos por [open_basedir](#ini.open-basedir). Anteriormente, devolvía `false`. Además, ahora se emite una advertencia incluso si solo algunos caminos están restringidos por [open_basedir](#ini.open-basedir).

FilesystemIterator::\_\_construct: antes de PHP 8.2.0, la constante `FilesystemIterator::SKIP_DOTS` siempre estaba definida y no podía ser desactivada. Para conservar el comportamiento anterior, la constante debe ser definida explícitamente al usar el parámetro `flags`. El valor por defecto del parámetro `flags` no ha sido modificado.

`strtolower`, `strtoupper`, `stristr`, `stripos`, `strripos`, `lcfirst`, `ucfirst`, `ucwords`, y `str_ireplace` ya no son sensibles a la configuración regional. Ahora realizan una conversión ASCII de mayúsculas y minúsculas, como si la configuración regional fuera "C". Versiones localizadas de estas funciones están disponibles en la [extensión MBString](#book.mbstring). Además, `array_change_key_case` y la ordenación con `SORT_FLAG_CASE` ahora también usan la conversión ASCII.

`str_split` ahora devuelve un `array` vacío para una `string` vacía. Anteriormente, devolvía un array con una sola cadena vacía como entrada. `mb_str_split` no se ve afectada por este cambio ya que ya se comportaba de esa manera.

`ksort` y `krsort` ahora realizan comparaciones numéricas de strings bajo `SORT_REGULAR` usando las reglas estándar de PHP 8.

`var_export` ya no omite la barra invertida inicial para las clases exportadas, es decir, ahora están completamente calificadas.

## Biblioteca estándar de PHP (SPL)

Los siguientes métodos ahora refuerzan su firma : SplFileInfo::\_bad_state_ex, SplFileObject::getCsvControl, SplFileObject::fflush, SplFileObject::ftell, SplFileObject::fgetc, SplFileObject::fpassthru

SplFileObject::hasChildren ahora tiene un tipo de retorno provisional `false`, anteriormente era `bool`.

SplFileObject::getChildren ahora tiene un tipo de retorno provisional `null`, anteriormente era `RecursiveIteratornull`.

`GlobIterator` ahora devuelve un `array` vacío si todos los caminos de acceso están restringidos por [open_basedir](#ini.open-basedir). Anteriormente, devolvía `false`. Además, ahora se emite una advertencia incluso si solo algunos caminos están restringidos por [open_basedir](#ini.open-basedir).
