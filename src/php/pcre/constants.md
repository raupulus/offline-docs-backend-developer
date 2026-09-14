---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pcre.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: e62b1e398
order: 61550
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

| Constantes | Descripción | Disponible a partir de |
|----|----|----|
| `PREG_PATTERN_ORDER` (`int`) | Ordena los resultados de forma que `$matches[0]` contenga los resultados que corresponden al patrón completo, `$matches[1]` los que corresponden a la primera paréntesis capturante y así sucesivamente. Esta constante se utiliza con `preg_match_all`. |  |
| `PREG_SET_ORDER` (`int`) | Los resultados se clasifican de tal forma que `$matches[0]` contiene la primera serie de resultados, `$matches[1]` la segunda, etc. Esta constante se utiliza con `preg_match_all`. |  |
| `PREG_OFFSET_CAPTURE` (`int`) | Si esta opción está activada, para cada coincidencia encontrada, el desplazamiento del byte correspondiente también será devuelto. Tenga en cuenta que esto modifica los valores de retorno: cada elemento del array se convierte en un array que contiene la cadena correspondiente en el offset 0 y su desplazamiento en la cadena analizada en el offset 1. |  |
| `PREG_SPLIT_NO_EMPTY` (`int`) | Si esta opción está activada, solo las sub-cadenas no vacías serán devueltas por `preg_split`. |  |
| `PREG_SPLIT_DELIM_CAPTURE` (`int`) | Esta bandera indica a `preg_split` que capture también las expresiones entre paréntesis del patrón delimitador. |  |
| `PREG_SPLIT_OFFSET_CAPTURE` (`int`) | Ver la descripción de `PREG_OFFSET_CAPTURE`. Esta bandera solo se utiliza con `preg_split`. |  |
| `PREG_UNMATCHED_AS_NULL` (`int`) | Esta constante solicita a `preg_match` y `preg_match_all` incluir los subpatrones sin coincidencia en `$matches` con un valor a `null`. Sin esta constante, los subpatrones sin coincidencia son devueltos con una cadena vacía, como si la coincidencia estuviera vacía. Definir esta constante permite distinguir estos dos casos. | 7.2.0 |
| `PREG_NO_ERROR` (`int`) | Devuelto por la función `preg_last_error` si no hay error. | 5.2.0 |
| `PREG_INTERNAL_ERROR` (`int`) | Devuelto por la función `preg_last_error` si hay un error interno de PCRE. | 5.2.0 |
| `PREG_BACKTRACK_LIMIT_ERROR` (`int`) | Devuelto por la función `preg_last_error` si [el límite de retroceso](#ini.pcre.backtrack-limit) ha sido alcanzado. | 5.2.0 |
| `PREG_RECURSION_LIMIT_ERROR` (`int`) | Devuelto por la función `preg_last_error` si [el límite de recursión](#ini.pcre.recursion-limit) ha sido alcanzado. | 5.2.0 |
| `PREG_BAD_UTF8_ERROR` (`int`) | Devuelto por la función `preg_last_error` si el último error se debe a una malformación de los datos UTF-8 (solo durante la ejecución de una expresión en [modo UTF-8](#reference.pcre.pattern.modifiers)). | 5.2.0 |
| `PREG_BAD_UTF8_OFFSET_ERROR` (`int`) | Devuelto por la función `preg_last_error` si el desplazamiento no corresponde al inicio de un punto válido UTF-8 (solo cuando se ejecuta una expresión en [modo UTF-8](#reference.pcre.pattern.modifiers)). | 5.3.0 |
| `PREG_JIT_STACKLIMIT_ERROR` (`int`) | Devuelto por `preg_last_error` si la última función PCRE falló debido al límite de la pila JIT. | 7.0.0 |
| `PCRE_VERSION` (`int`) | Versión PCRE junto con la fecha de publicación (es decir, `"7.0 18-Dec-2006"`). | 5.2.4 |
| `PCRE_VERSION_MAJOR` (`int`) | Número de versión mayor de PCRE. |  |
| `PCRE_VERSION_MINOR` (`int`) | Número de versión menor de PCRE. |  |
| `PCRE_JIT_SUPPORT` (`bool`) | Indica si el soporte JIT de PCRE está disponible. |  |
| `PREG_GREP_INVERT` (`int`) | Devuelve los elementos que no coinciden con un patrón dado. |  |

Constantes PREG
