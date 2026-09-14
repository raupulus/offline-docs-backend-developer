---
title: uniqid
description: Genera un identificador basado en el tiempo
source_url: https://www.php.net/manual/es/function.uniqid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/uniqid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: b65b98da1
order: 47280
---

uniqid

Genera un identificador basado en el tiempo

## Descripción

```php
uniqid([string $prefix], [bool $more_entropy]): string
```php

Genera un identificador basado en la hora actual con una precisión a la microsegundo, prefijado por el `prefix` dado y añadiendo eventualmente un valor generado aleatoriamente.

> [!CAUTION]
> Esta función no genera valores criptográficamente seguros, y *no debe* ser utilizada con fines criptográficos, o con fines que requieran que los valores devueltos sean indescifrables.
>
> Si se requiere aleatoriedad criptográficamente segura, el `Random\Randomizer` puede ser utilizado con el motor `Random\Engine\Secure`. Para casos de uso simples, las funciones `random_int` y `random_bytes` proporcionan una API práctica y segura que es soportada por el CSPRNG del sistema operativo.

> [!WARNING]
> Esta función no garantiza la unicidad del valor devuelto ya que este se basa en la hora actual en microsegundos o en la hora actual con una pequeña cantidad de datos aleatorios añadidos si `more_entropy` es `true`.

## Parámetros

`prefix`  
Puede ser útil, por ejemplo, para identificar fácilmente diferentes hosts, si se genera simultáneamente en varios hosts que pueden generar el mismo identificador en la misma microsegundo. (Esto puede ocurrir incluso en un solo host si el reloj del sistema se mueve hacia atrás, por ejemplo por un ajuste NTP.)

Sin `prefix` (prefijo vacío), la cadena devuelta tendrá 13 caracteres. Si `more_entropy` es `true`, tendrá 23 caracteres.

`more_entropy`  
Si el parámetro opcional `more_entropy` es `true`, `uniqid` añadirá una entropía `"combined LCG"` al final del valor devuelto, lo que aumenta la probabilidad de la unicidad del resultado.

## Valores devueltos

Devuelve un identificador basado en el timestamp, en forma de `string`.

> [!WARNING]
> Esta función no garantiza la unicidad del valor devuelto.

## Ejemplos

Ejemplo con `uniqid`

```
<?php
/* Un identificador único, como: 4b3403665fea6 */
printf("uniqid(): %s\r\n", uniqid());

/* También podemos prefijar el identificador único,
 * lo que equivale a:
 *
 * $uniqid = $prefix . uniqid();
 * $uniqid = uniqid($prefix);
 */
printf("uniqid('php_'): %s\r\n", uniqid('php_'));

/* También podemos activar el parámetro more_entropy,
 * requerido por algunos sistemas, como Cygwin. Esto hará que
 * uniqid() produzca un valor como: 4b340550242239.64159797
 */
printf("uniqid('', true): %s\r\n", uniqid('', true));
?>

    
```php

## Notas

> [!NOTE]
> En Cygwin, el parámetro `more_entropy` debe ser pasado a `true` para que esta función funcione.

## Véase también

random_bytes
