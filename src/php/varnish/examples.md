---
title: Ejemplos
source_url: https://www.php.net/manual/es/varnish.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/varnish/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: varnish
translation_status: ready
translation_reviewed: false
translation_revision: 73fae4ee5
order: 100880
---

## Ejemplos

## Uso Básico de VarnishAdmin

El ejemplo muestra un uso sencillo de la funcionalidad de prohibición

Prohibición de una URL

```php
<?php

$args = array(
    VARNISH_CONFIG_HOST    => "::1",
    VARNISH_CONFIG_PORT    => 6082,
    VARNISH_CONFIG_SECRET  => "5174826b-8595-4958-aa7a-0609632ad7ca",
    VARNISH_CONFIG_TIMEOUT => 300,
);

$va = new VarnishAdmin($args);

try {
    if(!$va->connect()) {
        throw new VarnishException("Conexión fallida\n");
    }
} catch (VarnishException $e) {
    echo $e->getMessage();
    exit(3);
}

try {
    if(!$va->auth()) {
        throw new VarnishException("Autorización fallida\n");
    }
} catch (VarnishException $e) {
    echo $e->getMessage();
    exit(3);
}

try {
    $estado = $va->ban('req.url ~ "^/$"');
    if (VARNISH_STATUS_OK != $estado) {
        throw new VarnishException("El método ban devolvió el estado $estado\n");
    }
} catch (VarnishException $e) {
    echo $e->getMessage();
    exit(3);
}

exit(0);

?>

   
```

## Uso básico de VarnishStat

El ejemplo muestra la obtención de una instantánea de las estadísticas de varnish de memoria compartida

Obtención de una instantánea de las estadísticas

```php
<?php

$vs = new VarnishStat;

try {
    $data = $vs->getSnapshot();
} catch (VarnishException $e) {
    echo $e->getMessage();
    exit(3);
}

exit(0);
?>

   
```

## Uso básico de VarnishLog

El ejemplo muestra la lectura de líneas del registro de varnish de memoria compartida

Lectura del log de varnish en la memoria compartida

```php
<?php

$vl = new VarnishLog;
while(1) {
    $line = $vl->getLine();
    printf("%s %d %s", VarnishLog::getTagName($line['tag']), $line['id'],
    $line['data']);
}

exit(0);
?>

   
```
