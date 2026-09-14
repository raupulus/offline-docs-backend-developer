---
title: debug_zval_dump
description: Extrae una representación en forma de string de la estructura interna
  de una zval para su visualización
source_url: https://www.php.net/manual/es/function.debug-zval-dump.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/debug-zval-dump.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: 17ebcd2ea
order: 100450
---

debug_zval_dump

Extrae una representación en forma de string de la estructura interna de una zval para su visualización

## Descripción

```php
debug_zval_dump(mixed $value, mixed ...$values): void
```php

Extrae una representación en forma de string de una estructura interna de una zval (Zend value) para su visualización. Esto es generalmente útil para comprender o depurar los detalles de implementación del motor Zend o de extensiones PHP.

## Parámetros

`value`  
La variable o valor a extraer.

`values`  
Variables o valores adicionales a extraer.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                                                  |
|---------|--------------------------------------------------------------|
| 8.4.0   | `debug_zval_dump` ahora indica si un array está empaquetado. |

## Ejemplos

Ejemplo con `debug_zval_dump`

```
<?php
$var1 = 'Hello';
$var1 .= ' World';
$var2 = $var1;

debug_zval_dump($var1);
?>

    
```php

El ejemplo anterior mostrará:

    string(11) "Hello World" refcount(3)

> [!NOTE]
> El valor `refcount` mostrado por esta función puede resultar sorprendente sin una comprensión detallada de la implementación del motor.
>
> El motor Zend utiliza el conteo de referencias por dos razones diferentes:
>
> Optimizar el uso de memoria utilizando una técnica llamada "copy on write", donde múltiples variables que contienen el mismo valor apuntan a la misma copia en memoria. Cuando una de estas variables es modificada, apunta a una nueva copia en memoria, y el conteo de referencias del original se reduce en 1., El seguimiento de variables que han sido asignadas o pasadas por referencia (ver [Referencias explicadas](#language.references)). Este refcount se almacena en una zval de referencia separada, apuntando a la zval para el valor actual. Esta zval adicional no se muestra actualmente por `debug_zval_dump`.
>
> Como `debug_zval_dump` toma su entrada como un parámetro normal, pasado por valor, la técnica de copy on write será utilizada para el paso: en lugar de copiar los datos, el refcount será incrementado en 1 durante la vida del llamado a la función. Si la función modifica el parámetro después de haberlo recibido, entonces se realizará una copia; como no lo hace, mostrará un refcount 1 más alto que en el ámbito de llamada.
>
> El paso de parámetros también impide que `debug_zval_dump` muestre variables que han sido asignadas por referencia. Para ilustrar esto, considere una versión ligeramente modificada del ejemplo anterior:
>
> <div class="informalexample">
>
> ```
> <?php
> $var1 = 'Hello';
> $var1 .= ' World';
> // Apunta tres variables como referencia al mismo valor
> $var2 =& $var1;
> $var3 =& $var1;
>
> debug_zval_dump($var1);
> ?>
>
>      
> ```
>
> El ejemplo anterior mostrará:
>
>     string(11) "Hello World" refcount(2)
>
>          
>
> </div>
>
> Aunque `$var1`, `$var2` y `$var3` están vinculadas como referencia, solo el *valor* es pasado a `debug_zval_dump`. Este valor es utilizado una sola vez por el conjunto de referencias, y una vez dentro de `debug_zval_dump`, por lo que muestra un refcount de 2.
>
> Complicaciones adicionales emergen debido a las optimizaciones realizadas por el motor para diferentes tipos de datos. Algunos tipos como los enteros no utilizan "copy on write", y por lo tanto no muestran ningún refcount. En otros casos, el refcount muestra otras copias utilizadas internamente, como cuando una cadena literal o un array es almacenado como parte de una instrucción de código.

## Véase también

`var_dump`, `debug_backtrace`, [Explicaciones sobre referencias](#language.references), [Explicaciones sobre referencias (por Derick Rethans)](http://derickrethans.nl/php_references_article.php)
