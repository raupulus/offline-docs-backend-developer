---
title: La clase parallel\Future
source_url: https://www.php.net/manual/es/class.parallel-future.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel.future.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60320
---

## Futures

Un Future representa el valor de retorno o la excepción no capturada de una tarea, y expone una API para la cancelación.

Ejemplo mostrando Future como valor de retorno

```php
<?php
$runtime = new \parallel\Runtime;
$future  = $runtime->run(function(){
    return "World";
});
printf("Hello %s\n", $future->value());
?>

      
```

Resultado del ejemplo anterior es similar a:

    Hello World

El comportamiento de un Future permite también su uso como un simple punto de sincronización incluso si la tarea no devuelve explícitamente un valor.

Ejemplo mostrando Future como punto de sincronización

```php
<?php
$runtime = new \parallel\Runtime;
$future  = $runtime->run(function(){
    echo "in child ";
    for ($i = 0; $i < 500; $i++) {
        if ($i % 10 == 0) {
            echo ".";
        }
    }
    echo " leaving child";
});

$future->value();
echo "\nparent continues\n";
?>

      
```

Resultado del ejemplo anterior es similar a:

    in child .................................................. leaving child
    parent continues

## Sinopsis de la clase

parallel\Future

final

parallel\Future

Resolución

Estados

Cancelación
