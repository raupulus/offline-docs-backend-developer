---
title: Funcionalidades obsoletas en PHP 7.2.x
source_url: https://www.php.net/manual/es/migration72.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration72/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 549423df6
order: 540
---

## Funcionalidades obsoletas en PHP 7.2.x

## Cadenas sin entrecomillar

Las cadenas sin entrecomillar que sean constantes globales inexistentes se convierten en cadenas de ellas mismas. Este comportamiento solía emitir una `E_NOTICE`, pero a partir de ahora emitirá una `E_WARNING`. En la siguiente versión mayor de PHP, se lanzará una excepción `Error` en su lugar.

```php
<?php

var_dump(INEXISTENTE);

/* Output:
Warning: Use of undefined constant INEXISTENTE - assumed 'INEXISTENTE' (this will throw an Error in a future version of PHP) in %s on line %d
string(11) "INEXISTENTE"
*/

   
```

## `png2wbmp` y `jpeg2wbmp`

Las funciones `png2wbmp` y `jpeg2wbmp` de la extensión GD se han marcado como obsoletas y serán borradas en la siguiente versión mayor de PHP.

## Variante `INTL_IDNA_VARIANT_2003`

La extensión Intl ha marcado como obsoleta la variante `INTL_IDNA_VARIANT_2003`, que es actualmente usada como el valor por defecto de `idn_to_ascii` y `idn_to_utf8`. PHP 7.4 cambiará estos valores por defecto a `INTL_IDNA_VARIANT_UTS46`, y en la siguiente versión mayor de PHP borrará la variante `INTL_IDNA_VARIANT_2003`.

## Método `__autoload`

El método `__autoload` se ha marcado como obsoleto porque es inferior a `spl_autoload_register` (debido a que no permite encadenar autocargadores), y no existe interoperabilidad entre los dos estilos de autocarga.

## Directiva ini `track_errors` y variable `$php_errormsg`

Cuando la directiva ini `track_errors` está activada, una variable `$php_errormsg` es creada en el ámbito local cuando ocurre un error no fatal. Dado que el método preferido de obtener ese tipo de información de errores es usando `error_get_last`, esta característica ha sido marcada como obsoleta.

## Función `create_function`

Debido a los problemas de seguridad de esta función (siendo una envoltura de `eval`), esta antigua función ha sido marcada como obsoleta. La alternativa preferida es usar [funciones anónimas](#functions.anonymous).

## Directiva ini `mbstring.func_overload`

Debido a los problemas de interoperabilidad de funciones basadas en cadenas usadas en entornos con esta directiva activada, ha sido marcada como obsoleta.

## Forzado a `(unset)`

Forzar cualquier expresión a este tipo siempre resulta en `null`, por lo que este tipo de forzado superfluo ha sido marcado como obsoleto.

## `parse_str` sin segundo argumento

Sin un segundo argumento para `parse_str`, los parámetros de una cadena de consulta son establecidos en el ámbito local. Debido a los problemas de seguridad de ello, el uso de `parse_str` sin un segundo parámetro ha sido marcado como obsoleto. Esta función siempre debe ser usada con dos argumentos, ya que el segundo argumento provoca que la cadena de consulta sea interpretada a un array.

## Función `gmp_random`

Esta función genera un número aleatorio dentro de rango que es calculado por un método no expuesto y dependiente de la plataforma. Por ello, esta función ha sido ahora marcado como obsoleto. El método preferido de generar un número aleatorio usando la extensión GMP extension es usando `gmp_random_bits` y `gmp_random_range`.

## Función `each`

Esta función es mucho más lenta iterando que un `foreach` normal, y causa problemas de implementación con algunos cambios del lenguaje. Ha sido por tanto marcada como obsoleta.

## `assert` con una cadena como argumento

Usar `assert` con una cadena como argumento requería que la cadena fuera `eval`uada. Debido al potencial para ejecución remota de código, el uso de `assert` con una cadena como argumento ha sido marcado como obsoleto en favor del uso de expresiones booleanas.

## Argumento `$errcontext` de manejadores de errores

El argumento `$errcontext` contiene todas las variables locales del ámbito donde ocurrió el error. Debido a su poco uso, y los problemas que causa con optimizaciones internas, ha sido marcado como obsoleto. En su lugar, se debe usar un depurador para obtener información sobre las variables del ámbito local del lugar del error.

## Función `read_exif_data`

El alias `read_exif_data` ha sido marcado como obsoleto. La función `exif_read_data` debe ser usada en su lugar.
