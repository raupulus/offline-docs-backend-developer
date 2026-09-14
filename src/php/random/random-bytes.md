---
title: random_bytes
description: Obtiene bytes aleatorios criptográficamente seguros
source_url: https://www.php.net/manual/es/function.random-bytes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/functions/random-bytes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: f08b9a8ae
order: 67910
---

random_bytes

Obtiene bytes aleatorios criptográficamente seguros

## Descripción

```php
random_bytes(int $length): string
```php

Genera una cadena que contiene bytes seleccionados uniformemente de manera aleatoria con el valor de `length`.

Dado que los bytes devueltos se eligen completamente al azar, la cadena resultante probablemente contendrá caracteres no imprimibles o secuencias UTF-8 inválidas. Puede ser necesario codificarlos antes de la transmisión o visualización.

La aleatorización generada por esta función es adecuada para todas las aplicaciones, incluyendo la generación de secretos a largo plazo, como claves de cifrado.

Las fuentes de aleatoriedad por orden de prioridad son las siguientes:

- Linux: [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- FreeBSD \>= 12 (PHP \>= 7.3): [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- Windows (PHP \>= 7.2): [CNG-API](https://docs.microsoft.com/en-us/windows/desktop/SecCNG/cng-portal)

  Windows: [CryptGenRandom](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379942(v=vs.85).aspx)

- macOS (PHP \>= 8.2; \>= 8.1.9; \>= 8.0.22 si CCRandomGenerateBytes está disponible en el momento de la compilación): CCRandomGenerateBytes()

  macOS (PHP \>= 8.1; \>= 8.0.2): arc4random_buf(), `/dev/urandom`

- NetBSD \>= 7 (PHP \>= 7.1; \>= 7.0.1): arc4random_buf(), `/dev/urandom`

- OpenBSD \>= 5.5 (PHP \>= 7.1; \>= 7.0.1): arc4random_buf(), `/dev/urandom`

- DragonflyBSD (PHP \>= 8.1): [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- Solaris (PHP \>= 8.1): [getrandom()](http://man7.org/linux/man-pages/man2/getrandom.2.html), `/dev/urandom`

- Cualquier combinación de un sistema operativo y una versión de PHP no mencionada anteriormente: `/dev/urandom`.

- Si ninguna de las fuentes de aleatoriedad está disponible o todas fallan al generar aleatoriedad, se lanzará una excepción de tipo `Random\RandomException` .

> [!NOTE]
> Aunque esta función fue añadida en PHP 7.0, una [implementación en espacio de usuario](https://github.com/paragonie/random_compat) está disponible para PHP 5.2 hasta 5.6, inclusive.

## Parámetros

`length`  
La longitud de la `string` aleatoria que debe ser devuelta en bytes; debe ser mayor o igual a `1`.

## Valores devueltos

Devuelve una `string` que contiene el número solicitado de bytes criptográficamente seguros.

## Errores/Excepciones

- Si no se encuentra ninguna fuente de datos aleatorios, se lanzará una `Random\RandomException`.

- Si el valor de `length` es menor que `1`, se lanzará una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | En caso de fallo CSPRNG, esta función lanzará ahora una `Random\RandomException`. Anteriormente se lanzaba una `Exception` básica. |

## Ejemplos

Ejemplo con `random_bytes`

```
<?php
$bytes = random_bytes(5);
var_dump(bin2hex($bytes));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(10) "385e33f741"

## Véase también

Random\Randomizer::getBytes

random_int

bin2hex

base64_encode
