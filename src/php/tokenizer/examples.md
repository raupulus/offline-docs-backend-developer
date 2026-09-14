---
title: Ejemplos
source_url: https://www.php.net/manual/es/tokenizer.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 23fef04c8
order: 94340
---

## Ejemplos

Aquí hay un simple ejemplo de scripts PHP donde se usa el tokenizer para leer en un archivo PHP, quitar todo los comentarios del archivo original y mostrar solamente el código puro.

Quitar comentarios con el tokenizer

```php
<?php

$source = file_get_contents('example.php');
$tokens = token_get_all($source);

foreach ($tokens as $token) {
   if (is_string($token)) {
       // simple 1-character token
       echo $token;
   } else {
       // token array
       list($id, $text) = $token;

       switch ($id) {
           case T_COMMENT:
           case T_DOC_COMMENT:
               // ninguna acción en comentarios
               break;

           default:
               // cualquier otra cosa -> salida "tal cual"
               echo $text;
               break;
       }
   }
}
?>

  
```
