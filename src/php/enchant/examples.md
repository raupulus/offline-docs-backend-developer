---
title: Ejemplos
source_url: https://www.php.net/manual/es/enchant.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/enchant/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: enchant
translation_status: ready
translation_revision: 96c9d88ba
order: 17320
---

## Ejemplos

Ejemplos de Uso de Enchant

```php
<?php
$etiqueta = 'en_US';
$r = enchant_broker_init();
$bprovides = enchant_broker_describe($r);
echo "El agente actual proporciona los siguientes entornos:\n";
print_r($bprovides);

$diccionarios = enchant_broker_list_dicts($r);
print_r($diccionarios);
if (enchant_broker_dict_exists($r,$etiqueta)) {
    $d = enchant_broker_request_dict($r, $etiqueta);
    $dprovides = enchant_dict_describe($d);
    echo "el diccionario $etiqueta proporciona:\n";
    $palabra_correcta = enchant_dict_check($d, "soong");
    print_r($dprovides);
    if (!$palabra_correcta) {
        $sugerencias = enchant_dict_suggest($d, "soong");
        echo "Sugerencias para 'soong':";
        print_r($sugerencias);
    }
    enchant_broker_free_dict($d);
} else {
}
enchant_broker_free($r);
?>

  
```
