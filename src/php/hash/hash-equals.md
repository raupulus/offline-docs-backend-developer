---
title: hash_equals
description: Comparación de strings resistente a ataques temporales
source_url: https://www.php.net/manual/es/function.hash-equals.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-equals.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: 6ba84e3a5
order: 29250
---

hash_equals

Comparación de strings resistente a ataques temporales

## Descripción

```php
#[\SensitiveParameter] #[\SensitiveParameter] hash_equals(string $known_string, string $user_string): bool
```php

Verifica si dos strings son iguales sin revelar información sobre el contenido de `known_string` mediante el tiempo de ejecución.

Esta función puede ser utilizada para mitigar ataques temporales. La ejecución de una comparación regular con `===` tomará más o menos tiempo dependiendo de si las dos valores son diferentes o no y según la posición en la que la primera diferencia pueda ser encontrada, dejando así filtrar información sobre el contenido de la `known_string` secreta.

> [!CAUTION]
> Es importante pasar el string proporcionado por el usuario como segundo argumento en lugar del primero.

## Parámetros

`known_string`  
El string conocido que debe ser mantenido en secreto.

`user_string`  
El string proporcionado por el usuario a comparar.

## Valores devueltos

Retorna `true` si los dos strings son iguales, `false` en caso contrario.

## Ejemplos

Ejemplo de`hash_equals`

```
<?php
$secretKey = '8uRhAeH89naXfFXKGOEj';

// El valor y la firma son proporcionados por el usuario, p. ej. en la URL
// y recuperados mediante $_GET.
$value = 'username=rasmuslerdorf';
$signature = '8c35009d3b50caf7f5d2c1e031842e6b7823a1bb781d33c5237cd27b57b5f327';

if (hash_equals(hash_hmac('sha256', $value, $secretKey), $signature)) {
    echo "El valor está firmado correctamente.", PHP_EOL;
} else {
    echo "El valor ha sido manipulado.", PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    El valor está firmado correctamente.

## Notas

> [!NOTE]
> Ambos argumentos deben tener la misma longitud para ser comparados con éxito. Cuando se pasan argumentos de longitud diferente, `false` es retornado inmediatamente y la longitud del string conocido puede ser revelada en caso de ataque temporal.

## Véase también

`hash_hmac`
