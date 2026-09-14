---
title: Callbacks
source_url: https://www.php.net/manual/es/yaml.callbacks.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/callbacks.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_reviewed: true
translation_revision: 80872147a
order: 107350
---

## Callbacks

## Análisis de callbacks

Los análisis de `callable`s son invocados por las funciones `yaml_parse`, `yaml_parse_file` o `yaml_parse_url` cuando encuentran una etiqueta YAML registrada. Al callback se le pasa el valor de la entidad de la etiqueta, la etiqueta, y los flags que indican el estilo escalar de la entidad. El callback debe devolver los datos que el convertidor YAML debe emitir para esta entidad.

Ejemplo de análisis de callback

```php
<?php
/**
 * Análisis de callback para un tag yaml.
 * @param mixed $valor Datos del archivo yaml
 * @param string $tag Etiqueta que desencadenó el callback
 * @param int $flags Estilo escalar de la entidad (ver YAML_*_SCALAR_STYLE)
 * @return mixed Valor que el convertidor YAML debería emitir para el valor dado
 */
function tag_callback ($valor, $tag, $flags) {
  var_dump(func_get_args()); // depurando
  return "Hola {$valor}";
}

$yaml = <<<YAML
saludo: !ejemplo/hola Mundo
YAML;

$resultado = yaml_parse($yaml, 0, $ndocs, array(
    '!ejemplo/hola' => 'tag_callback',
  ));

var_dump($resultado);
?>

   
```

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      string(5) "Mundo"
      [1]=>
      string(14) "!ejemplo/hola"
      [2]=>
      int(1)
    }
    array(1) {
      ["saludo"]=>
      string(11) "Hola Mundo"
    }

## Emitir callbacks

Las emisiones de callbacks son invocadas cuando una instancia de una clase registrada es emitida por la función `yaml_emit` o la función `yaml_emit_file`. El callback se pasa al objeto a ser emitido. El callback debe devolver un array que contenga dos claves: "`tag`" y "`data`". El valor asociado con la clave "`tag`" debe ser un string a ser usado como la etiqueta YAML en la salida. El valor asociado con la clave "`data`" será encodeado como YAML y será emitido en lugar del objeto interceptado.

Ejemplo de emisión de callback

```php
<?php
class EmitExample {
  public $data;    // los datos podrían ser ajustables en cualquier tipo de pecl/yaml

  public function __construct ($d) {
    $this->data = $d;
  }

  /**
   * Yaml emite la función de callback, referida a la llamada yaml_emit por el nombre de la clase.
   *
   * Se espera que devuelva un array con 2 valores:
   *   - 'tag': etiqueta personalizada para esta serialización
   *   - 'data': valor que se convierte a yaml (ya sea array, string, bool, número)
   *
   * @param object $obj Objeto a ser emitido
   * @return array Etiqueta y datos sustitutivos a emitir
   */
  public static function yamlEmit (EmitExample $obj) {
    return array(
      'tag' => '!example/emit',
      'data' => $obj->data,
    );
  }
}

$emit_callbacks = array(
  'EmitExample' => array('EmitExample', 'yamlEmit')
);

$t = new EmitExample(array('a','b','c'));
$yaml = yaml_emit(
  array(
    'example' => $t,
  ),
  YAML_ANY_ENCODING,
  YAML_ANY_BREAK,
  $emit_callbacks
);
var_dump($yaml);
?>

   
```

Resultado del ejemplo anterior es similar a:

    string(43) "---
    example: !example/emit
    - a
    - b
    - c
    ...
    "
