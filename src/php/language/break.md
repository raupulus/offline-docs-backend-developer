---
title: break
source_url: https://www.php.net/manual/es/control-structures.break.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/break.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 7104ee97c
order: 2090
---

## break

La instrucción `break` permite salir de una estructura `for`, `foreach`, `while`, `do-while` o `switch`.

`break` acepta un argumento numérico opcional que indicará cuántas estructuras anidadas deben ser interrumpidas. El valor por omisión es `1`, solo la estructura anidada inmediata es interrumpida.

```php
<?php
$arr = array('un', 'dos', 'tres', 'cuatro', 'stop', 'cinco');
foreach ($arr as $val) {
    if ($val == 'stop') {
        break;    /* También podría utilizarse 'break 1;' aquí. */
    }
    echo "$val<br />\n";
}

/* Uso del argumento opcional. */

$i = 0;
while (++$i) {
    switch ($i) {
        case 5:
            echo "At 5<br />\n";
            break 1;  /* Termina únicamente el switch. */
        case 10:
            echo "At 10; quitting<br />\n";
            break 2;  /* Termina el switch y el ciclo while. */
        default:
            break;
    }
}
?>

   
```
