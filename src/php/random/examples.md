---
title: Ejemplos
source_url: https://www.php.net/manual/es/random.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 67840
---

## Ejemplos

Ejemplo de aleatoriedad

```php
<?php
$r = new \Random\Randomizer();

// Generar un nombre de dominio aleatorio
printf(
    "%s.example.com\n",
    $r->getBytesFromString('abcdefghijklmnopqrstuvwxyz0123456789', 16)
);

// Mezclar array:
$fruits = [ 'red' => '🍎', 'green' => '🥝', 'yellow' => '🍌', 'pink' => '🍑', 'purple' => '🍇' ];
echo "Ensalada: ", implode(', ', $r->shuffleArray($fruits)), "\n";

// Mezclar claves de array
$fruits = [ 'red' => '🍎', 'green' => '🥝', 'yellow' => '🍌', 'pink' => '🍑', 'purple' => '🍇' ];

$keys = $r->pickArrayKeys($fruits, 2);
// Buscar los valores para las claves seleccionadas
$selection = array_map(
    static fn ($key) => $fruits[$key],
    $keys
);

echo "Valores: ", implode(', ', $selection), "\n";
?>

  
```

Resultado del ejemplo anterior es similar a:

    j87fzv1p0daiwmlo.example.com
    Ensalada: 🥝, 🍇, 🍎, 🍌, 🍑
    Valores: 🍌, 🍑
