---
title: Random\Engine\PcgOneseq128XslRr64::__construct
description: Construye un nuevo motor PCG Oneseq 128 XSL RR 64
source_url: https://www.php.net/manual/es/random-engine-pcgoneseq128xslrr64.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/pcgoneseq128xslrr64/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 68000
---

Random\Engine\PcgOneseq128XslRr64::\_\_construct

Construye un nuevo motor PCG Oneseq 128 XSL RR 64

## Descripción

```php
public Random\Engine\PcgOneseq128XslRr64::__construct([string $seed])
```php

## Parámetros

`seed`  
La forma en que se inicializa el estado interno de 128 bits (16 bytes) que consiste en un entero sin signo de 128 bits depende del tipo utilizado como `seed`.

| Tipo | Descripción |
|----|----|
| `null` | Rellena el estado con 16 bytes aleatorios generados usando el CSPRNG. |
| `int` | Rellena el estado estableciendo el estado a `0`, avanzando el motor un paso, añadiendo el valor de `seed` interpretado como un entero sin signo de 64 bits, y avanzando el motor otro paso. |
| `string` | Rellena el estado interpretando un `string` de 16 bytes como un entero sin signo de 128 bits en orden little-endian. |

## Errores/Excepciones

- Si la longitud de un `string` `seed` no es de 16 bytes, se lanzará un `ValueError`.

## Ejemplos

Ejemplo de `Random\Engine\PcgOneseq128XslRr64::__construct`

```
<?php
// Usa una semilla aleatoria de 128 bits.
$e = new \Random\Engine\PcgOneseq128XslRr64();

$r = new \Random\Randomizer($e);
?>

   
```php

Derivar una semilla a partir de un `string`

```
<?php
$string = "Mi semilla de string";

// Aplica hash a la cadena con SHA-256 truncado usando salida binaria
// para convertir el $string en una semilla de 128 bits. Usar la misma
// cadena resultará en la misma secuencia de aleatoriedad.
$e = new \Random\Engine\PcgOneseq128XslRr64(
    substr(hash('sha256', $string, binary: true), 0, 16)
);

echo bin2hex($e->generate()), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    8333ef59315b16d8
