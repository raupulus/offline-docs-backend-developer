---
title: Random\Engine::generate
description: Genera aleatoriedad
source_url: https://www.php.net/manual/es/random-engine.generate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/generate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 67940
---

Random\Engine::generate

Genera aleatoriedad

## Descripción

```php
public Random\Engine::generate(): string
```php

Retorna aleatoriedad y avanza el estado del algoritmo en un paso.

La aleatoriedad está representada por una cadena binaria que contiene octetos aleatorios. Esta representación permite interpretar sin ambigüedad los bits aleatorios generados por el algoritmo, por ejemplo para tener en cuenta los diferentes tamaños de salida utilizados por los distintos algoritmos.

Los algoritmos que operan nativamente sobre valores enteros deben retornar el entero con los octetos en orden little-endian, por ejemplo utilizando la función `pack` con el código de formato `P`. La interfaz de alto nivel proporcionada por el `Random\Randomizer` interpretará los octetos aleatorios retornados como enteros no signados little-endian si se requiere una representación numérica.

Se recomienda encarecidamente que cada bit de la cadena retornada sea seleccionado de manera uniforme e independiente, ya que ciertas aplicaciones requieren aleatoriedad a nivel de bits para funcionar correctamente. Por ejemplo, los generadores congruenciales lineales generan a menudo aleatoriedad de menor calidad para los bits de menor peso del valor entero retornado y por lo tanto no serían adecuados para aplicaciones que requieren aleatoriedad a nivel de bits.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una cadena no vacía que contiene octetos aleatorios.

> [!NOTE]
> El `Random\Randomizer` utiliza internamente enteros no signados de 64 bits. Si la cadena retornada contiene más de 64 bits (8 octetos) de aleatoriedad, los octetos excedentes serán ignorados. Otras aplicaciones pueden ser capaces de procesar más de 64 bits a la vez.

## Errores/Excepciones

- Si la generación de aleatoriedad falla, una `Random\RandomException` debe ser emitida. Cualquier otra `Exception` emitida durante la generación debería ser capturada y envuelta en una `Random\RandomException`.

- Si la cadena retornada está vacía, una `Random\BrokenRandomEngineError` será emitida por el `Random\Randomizer`.

- Si el algoritmo implementado está fuertemente sesgado, una `Random\BrokenRandomEngineError` puede ser emitida por el `Random\Randomizer` para evitar bucles infinitos si un muestreo por rechazo es necesario para retornar resultados no sesgados.

## Ejemplos

Ejemplo de `Random\Engine::generate`

```
<?php
/**
 * Implementa un Generador Congruencial Lineal con módulo 65536,
 * un multiplicador de 61 y un incremento de 17, retornando un entero de 8 bits.
 *
 * Nota: Este motor solo puede ser utilizado con fines de demostración.
 *       Los generadores congruenciales lineales generalmente
 *       generan aleatoriedad de baja calidad y esta implementación específica tiene
 *       un período muy corto de 16 bits que no es adecuado para
 *       casi todos los casos de uso en el mundo real.
 */
final class LinearCongruentialGenerator implements \Random\Engine
{
    private int $state;

    public function __construct(?int $seed = null)
    {
        if ($seed === null) {
            $seed = random_int(0, 0xffff);
        }

        $this->state = $seed & 0xffff;
    }

    public function generate(): string
    {
        $this->state = (61 * $this->state + 17) & 0xffff;

        return pack('C', $this->state >> 8);
    }
}

$r = new \Random\Randomizer(
    new LinearCongruentialGenerator(seed: 1)
);

echo "Número afortunado: ", $r->getInt(0, 99), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    Número afortunado: 4
