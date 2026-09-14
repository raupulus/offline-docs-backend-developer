---
title: Funcionalidades obsoletas
source_url: https://www.php.net/manual/es/migration80.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration80/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: ca9dbbbd2
order: 780
---

## Funcionalidades obsoletas

## Núcleo PHP

- Si un parámetro con un valor predeterminado es seguido por un parámetro obligatorio, el valor predeterminado no tiene efecto. Esto está obsoleto a partir de PHP 8.0.0 y generalmente puede resolverse eliminando el valor predeterminado, sin cambiar la funcionalidad:

```php
  <?php
  function test($a = [], $b) {} // Before
  function test($a, $b) {}      // After
  ?>

       
  ```

  Una excepción a esta regla son los parámetros de la forma `Type $param = null`, donde el valor predeterminado null hace que el tipo sea implícitamente nullable. Este uso sigue estando permitido, pero se recomienda usar un tipo nullable explícito en su lugar:

```php
  <?php
  function test(A $a = null, $b) {} // Still allowed
  function test(?A $a, $b) {}       // Recommended
  ?>

       
  ```

- Llamar a `get_defined_functions` con `exclude_disabled` establecido explícitamente a `false` está obsoleto y ya no tiene efecto. `get_defined_functions` nunca incluirá funciones deshabilitadas.

## Enchant

- `enchant_broker_set_dict_path` y `enchant_broker_get_dict_path` están obsoletas, porque esa funcionalidad no está disponible ni en libenchant \< 1.5 ni en libenchant-2.

- `enchant_dict_add_to_personal` está obsoleta; use `enchant_dict_add` en su lugar.

- `enchant_dict_is_in_session` está obsoleta; use `enchant_dict_is_added` en su lugar.

- `enchant_broker_free` y `enchant_broker_free_dict` están obsoletas; use unset sobre el objeto en su lugar.

- Las constantes `ENCHANT_MYSPELL` y `ENCHANT_ISPELL` están obsoletas.

## LibXML

`libxml_disable_entity_loader` ha sido desaprobada. Como ahora se requiere libxml 2.9.0, la carga de entidades externas está garantizada como deshabilitada por defecto, y esta función ya no es necesaria para proteger contra ataques XXE, a menos que se utilice `LIBXML_NOENT`. En ese caso, se recomienda refactorizar el código usando `libxml_set_external_entity_loader` para suprimir la carga de entidades externas.

## PGSQL / PDO PGSQL

- La constante `PGSQL_LIBPQ_VERSION_STR` ahora tiene el mismo valor que `PGSQL_LIBPQ_VERSION`, y por lo tanto está obsoleta.

- Los alias de funciones en la extensión pgsql han sido desaprobados. Consulte la siguiente lista para saber qué funciones deben usarse en su lugar:

  `pg_errormessage` → `pg_last_error`, `pg_numrows` → `pg_num_rows`, `pg_numfields` → `pg_num_fields`, `pg_cmdtuples` → `pg_affected_rows`, `pg_fieldname` → `pg_field_name`, `pg_fieldsize` → `pg_field_size`, `pg_fieldtype` → `pg_field_type`, `pg_fieldnum` → `pg_field_num`, `pg_result` → `pg_fetch_result`, `pg_fieldprtlen` → `pg_field_prtlen`, `pg_fieldisnull` → `pg_field_is_null`, `pg_freeresult` → `pg_free_result`, `pg_getlastoid` → `pg_last_oid`, `pg_locreate` → `pg_lo_create`, `pg_lounlink` → `pg_lo_unlink`, `pg_loopen` → `pg_lo_open`, `pg_loclose` → `pg_lo_close`, `pg_loread` → `pg_lo_read`, `pg_lowrite` → `pg_lo_write`, `pg_loreadall` → `pg_lo_read_all`, `pg_loimport` → `pg_lo_import`, `pg_loexport` → `pg_lo_export`, `pg_setclientencoding` → `pg_set_client_encoding`, `pg_clientencoding` -\> `pg_client_encoding`

## Biblioteca estándar

- Las funciones de comparación para ordenamiento que devuelven `true` o `false` ahora emitirán una advertencia de obsolescencia, y deberían ser reemplazadas por una implementación que devuelva un entero menor, igual o mayor que cero.

```php
  <?php
  // Replace
  usort($array, fn($a, $b) => $a > $b);
  // With
  usort($array, fn($a, $b) => $a <=> $b);
  ?>

       
  ```

## Zip

- El uso de un archivo vacío como ZipArchive está obsoleto. Libzip 1.6.0 ya no acepta archivos vacíos como archivos zip válidos. La solución alternativa existente será eliminada en la próxima versión.

- La API procedural de Zip está obsoleta. Use `ZipArchive` en su lugar. La iteración sobre todas las entradas puede realizarse usando ZipArchive::statIndex y un bucle [for](#control-structures.for):

```php
  <?php
  // iterate using the procedural API
  assert(is_resource($zip));
  while ($entry = zip_read($zip)) {
      echo zip_entry_name($entry);
  }

  // iterate using the object-oriented API
  assert($zip instanceof ZipArchive);
  for ($i = 0; $entry = $zip->statIndex($i); $i++) {
      echo $entry['name'];
  }
  ?>

       
  ```

## Reflexión

- ReflectionFunction::isDisabled está obsoleto, ya que ya no es posible crear un `ReflectionFunction` para una función deshabilitada. Este método ahora siempre devuelve `false`.

- ReflectionParameter::getClass, ReflectionParameter::isArray y ReflectionParameter::isCallable están obsoletos. En su lugar deberían usarse ReflectionParameter::getType y las API de `ReflectionType`.
