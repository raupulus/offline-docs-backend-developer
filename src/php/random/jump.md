---
title: Random\Engine\PcgOneseq128XslRr64::jump
description: Avanza el motor varios pasos
source_url: https://www.php.net/manual/es/random-engine-pcgoneseq128xslrr64.jump.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/pcgoneseq128xslrr64/jump.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: '826073522'
order: 68030
---

Random\Engine\PcgOneseq128XslRr64::jump

Avanza el motor varios pasos

## Descripción

```php
public Random\Engine\PcgOneseq128XslRr64::jump(int $advance): void
```php

Avanza el estado del algoritmo el número de pasos indicado por `advance`, como si `Random\Engine\PcgOneseq128XslRr64::generate` fuera llamado tantas veces.

## Parámetros

`advance`  
El número de pasos a avanzar; debe ser `0` o más.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

- Si `advance` es inferior a `0`, se lanzará una `ValueError`.

## Ejemplos

Ejemplo de `Random\Engine\PcgOneseq128XslRr64::jump`

```
<?php
$a = new \Random\Engine\PcgOneseq128XslRr64(0);
$b = clone $a;

for ($i = 0; $i < 1_000; $i++) {
    $a->generate();
}
$b->jump(1_000);

echo "A: ", bin2hex($a->generate()), "\n";
echo "B: ", bin2hex($b->generate()), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    A: e6d0d5813913a424
    B: e6d0d5813913a424

Los métodos de Randomizer pueden llamar al motor más de una vez

```
<?php
$a = new \Random\Randomizer(new \Random\Engine\PcgOneseq128XslRr64(42659));
$b = new \Random\Randomizer(clone $a->engine);

$a->getInt(1, 1572864); // Realiza dos llamadas a generate().
$a->getInt(1, 1572864);

$b->engine->jump(2);

// Como la primera llamada a ->getInt() llamó a ->generate() dos veces
// los motores no coinciden después de realizar un ->jump(2).
echo "A: ", bin2hex($a->engine->generate()), "\n";
echo "B: ", bin2hex($b->engine->generate()), "\n";

// Ahora el motor B coincide con el motor A.
echo "B: ", bin2hex($b->engine->generate()), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    A: 1e9f3107d56653d0
    B: a156c0086dd79d44
    B: 1e9f3107d56653d0
