---
title: continue
source_url: https://www.php.net/manual/es/control-structures.continue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/continue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16389a7b3
order: 2100
---

## continue

La instrucción `continue` se utiliza en un bucle para eludir las instrucciones de la iteración actual y continuar la ejecución en la condición de evaluación y, por lo tanto, comenzar la siguiente iteración.

> [!NOTE]
> En PHP, la estructura [switch](#control-structures.switch) se considera un bucle por `continue`. `continue` se comporta como `break` (cuando no se pasa ningún argumento) pero emitirá una advertencia, ya que es probable que esto sea un error. Si un `switch` se encuentra dentro de un bucle, `continue 2` continuará en la siguiente iteración del bucle externo.

`continue` acepta un argumento numérico opcional que indicará cuántas estructuras anidadas deben ser eludidas. El valor por omisión es `1`, lo que equivale a ir directamente al final del bucle actual.

```php
<?php
$arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six'];
foreach ($arr as $key => $value) {
    if (0 === ($key % 2)) { // elude los miembros pares
        continue;
    }
    echo $value . "\n";
}
?>

   
```

Los ejemplos anteriores mostrarán:

    one
    three
    five

       

```php
<?php
$i = 0;
while ($i++ < 5) {
    echo "Outer\n";
    while (1) {
        echo "Middle\n";
        while (1) {
            echo "Inner\n";
            continue 3;
        }
        echo "This never gets output.\n";
    }
    echo "Neither does this.\n";
}
?>

   
```

Los ejemplos anteriores mostrarán:

    Outer
    Middle
    Inner
    Outer
    Middle
    Inner
    Outer
    Middle
    Inner
    Outer
    Middle
    Inner
    Outer
    Middle
    Inner

Olvidar el punto y coma después de `continue` puede llevar a confusión. Aquí hay un ejemplo de lo que no se debe hacer:

```php
<?php
for ($i = 0; $i < 5; ++$i) {
    if ($i == 2)
        continue
    print "$i\n";
}
?>

   
```

Se puede esperar que el resultado sea:

    0
    1
    3
    4

| Versión | Descripción |
|----|----|
| 7.3.0 | `continue` dentro de un `switch` que intenta actuar como una declaración `break` para `switch` emitirá `E_WARNING`. |

Historial para `continue`
