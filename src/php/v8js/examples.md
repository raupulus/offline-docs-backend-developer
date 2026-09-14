---
title: Ejemplos
source_url: https://www.php.net/manual/es/v8js.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_revision: 04ffd9be7
order: 100300
---

## Ejemplos

Uso básico

Básica ejecución Javascript

```php
<?php

$v8 = new V8Js();

/* basic.js */
$JS = <<< EOT
len = print('¡Hola' + ' ' + 'Mundo!' + "\\n");
len;
EOT;

try {
  var_dump($v8->executeString($JS, 'basic.js'));
} catch (V8JsException $e) {
  var_dump($e);
}

?>

  
```

El ejemplo anterior mostrará:

    ¡Hola Mundo!
    int(13)
