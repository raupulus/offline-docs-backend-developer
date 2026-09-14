---
title: Ejemplos
source_url: https://www.php.net/manual/es/xhprof.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xhprof/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xhprof
translation_status: ready
translation_revision: 991e1abe0
order: 102300
---

## Ejemplos

Ejemplo Xhprof con interfaz gráfica de usuario opcional

En este ejemplo se inicia y detiene el perfilador, a continuación, utiliza interfaz gráfica de usuario para guardar y analizar los resultados. En otras palabras, el código de la extensión se termina en la llamada a `xhprof_disable` .

```php
<?php
xhprof_enable(XHPROF_FLAGS_CPU + XHPROF_FLAGS_MEMORY);

for ($i = 0; $i <= 1000; $i++) {
    $a = $i * $i;
}

$xhprof_data = xhprof_disable();

$XHPROF_ROOT = "/tools/xhprof/";
include_once $XHPROF_ROOT . "/xhprof_lib/utils/xhprof_lib.php";
include_once $XHPROF_ROOT . "/xhprof_lib/utils/xhprof_runs.php";

$xhprof_runs = new XHProfRuns_Default();
$run_id = $xhprof_runs->save_run($xhprof_data, "xhprof_testing");

echo "http://localhost/xhprof/xhprof_html/index.php?run={$run_id}&source=xhprof_testing\n";

?>

  
```

Resultado del ejemplo anterior es similar a:

    http://localhost/xhprof/xhprof_html/index.php?run=t11_4bdf44d21121f&source=xhprof_testing
