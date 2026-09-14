---
title: goto
source_url: https://www.php.net/manual/es/control-structures.goto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/goto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 7204e2dbb
order: 2170
---

## goto

![¿Cuál es la cosa más extraña al usar goto?](en/language/figures/xkcd-goto.png)

El operador `goto` puede ser utilizado para continuar la ejecución del script en otro punto del programa. El destino es especificado por una etiqueta *sensible a mayúsculas y minúsculas*, seguida de dos puntos, y la instrucción `goto` es luego seguida de esta etiqueta. `goto` no está totalmente sin limitaciones. La etiqueta de destino debe estar en el mismo contexto y fichero, lo que significa que no es posible cambiar de método o función, ni ir a otra función. Asimismo, es imposible entrar en una estructura de bucle o un `switch`. Sin embargo, es posible salir de ellas, y el uso común es entonces utilizar `goto` como un `break`.

Ejemplo con `goto`

```php
<?php

goto a;
echo 'Foo';

a:
echo 'Bar';

?>

   
```

El ejemplo anterior mostrará:

    Bar

Ejemplo de bucle con `goto`

```php
<?php
for ($i = 0, $j = 50; $i < 100; $i++) {
    while ($j--) {
        if ($j == 17) {
            goto end;
        }
    }
}
echo "i = $i";
end:
echo 'j hit 17';

?>

   
```

El ejemplo anterior mostrará:

    j hit 17

Esto no funcionará

```php
<?php
goto loop;
for ($i = 0, $j = 50; $i < 100; $i++) {
    while ($j--) {
        loop:
    }
}
echo "$i = $i";

?>

   
```

El ejemplo anterior mostrará:

    Fatal error: 'goto' into loop or switch statement is disallowed in
    script on line 2
