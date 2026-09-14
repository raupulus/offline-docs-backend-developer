---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/mbstring.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 5e9500dda
order: 44930
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`MB_OVERLOAD_MAIL` (`int`)  
Eliminado desde PHP 8.0.0.

`MB_OVERLOAD_STRING` (`int`)  
Eliminado desde PHP 8.0.0.

`MB_OVERLOAD_REGEX` (`int`)  
Eliminado desde PHP 8.0.0.

`MB_CASE_UPPER` (`int`)  
Realiza una conversión completa a mayúsculas. Esto puede cambiar la longitud del string. Este es el modo utilizado por mb_strtoupper().

`MB_CASE_LOWER` (`int`)  
Realiza una conversión completa a minúsculas. Esto puede cambiar la longitud del string. Este es el modo utilizado por mb_strtolower().

`MB_CASE_TITLE` (`int`)  
Realiza una conversión completa a title-case basada en las propiedades derivadas de Unicode Cased y CaseIgnorable. En particular, esto mejora el manejo de las comillas y los apóstrofes. Esto puede cambiar la longitud del string.

`MB_CASE_FOLD` (`int`)  
Realiza una conversión completa que elimina las distinciones de mayúsculas y minúsculas presentes en el string. Esto se utiliza para la comparación sin distinción entre mayúsculas y minúsculas. Esto puede cambiar la longitud del string. Disponible desde PHP 7.3.

`MB_CASE_LOWER_SIMPLE` (`int`)  
Realiza una conversión simple a minúsculas. Esto no cambia la longitud del string. Disponible desde PHP 7.3.

`MB_CASE_UPPER_SIMPLE` (`int`)  
Realiza una conversión simple a mayúsculas. Esto no cambia la longitud del string. Disponible desde PHP 7.3.

`MB_CASE_TITLE_SIMPLE` (`int`)  
Realiza una conversión simple a title-case. Esto no cambia la longitud de la cadena. Disponible desde PHP 7.3.

`MB_CASE_FOLD_SIMPLE` (`int`)  
Realiza una conversión simple que elimina las distinciones de mayúsculas y minúsculas presentes en el string. Esto se utiliza para la comparación sin distinción entre mayúsculas y minúsculas. Esto no cambia la longitud del string. Utilizado internamente por las operaciones sin distinción entre mayúsculas y minúsculas de la extensión MBString. Disponible desde PHP 7.3.

`MB_ONIGURUMA_VERSION` (`string`)  
La versión de Oniguruma, p. ej. `6.9.4`. Disponible desde PHP 7.4.
