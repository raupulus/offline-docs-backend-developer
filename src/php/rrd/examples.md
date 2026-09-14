---
title: Ejemplos
source_url: https://www.php.net/manual/es/rrd.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 37e7d0557
order: 72540
---

## Ejemplos

## Ejemplo procedural PECL/rrd

Procedimiento de utilización de rrd

```php
<?php
$rrdFile = dirname(__FILE__) . "/speed.rrd";

//crear el archivo rrd
rrd_create($rrdFile,
 array(
  "--start",920804400,
  "DS:speed:COUNTER:600:U:U",
  "RRA:AVERAGE:0.5:1:24",
  "RRA:AVERAGE:0.5:6:10"
  )
);

//actualizar el archivo rrd
rrd_update($rrdFile,
 array(
  "920804700:12345",
  "920805000:12357"
  )
);

//gráfico de salida
rrd_graph(dirname(__FILE__) . "/speed.png",
 array(
  "--start", "920804400",
  "--end", "920808000",
  "--vertical-label", "m/s",
  "DEF:myspeed=$rrdFile:speed:AVERAGE",
  "CDEF:realspeed=myspeed,1000,*",
  "LINE2:realspeed#FF0000"
 )
);
?>

   
```

## Ejemplo OOP PECL/rrd

Procedimiento de utilización de OOP rrd

```php
<?php
$rrdFile = dirname(__FILE__) . "/speed.rrd";
$outputPngFile = dirname(__FILE__) . "/speed.png";

$creator = new RRDCreator($rrdFile, "now -10d", 500);
$creator->addDataSource("speed:COUNTER:600:U:U");
$creator->addArchive("AVERAGE:0.5:1:24");
$creator->addArchive("AVERAGE:0.5:6:10");
$creator->save();

$updater = new RRDUpdater($rrdFile);
$updater->update(array("speed" => "12345"), "920804700");
$updater->update(array("speed" => "12357"), "920805000");

$graphObj = new RRDGraph($outputPngFile);
$graphObj->setOptions(
    array(
        "--start" => "920804400",
        "--end" => 920808000,
        "--vertical-label" => "m/s",
        "DEF:myspeed=$rrdFile:speed:AVERAGE",
        "CDEF:realspeed=myspeed,1000,*",
        "LINE2:realspeed#FF0000"
    )
);
$graphObj->save();
?>

   
```
