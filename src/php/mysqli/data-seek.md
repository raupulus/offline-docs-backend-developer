---
title: mysqli_result::data_seek
description: Mueve el puntero interno de resultado
source_url: https://www.php.net/manual/es/mysqli-result.data-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/data-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55530
---

mysqli_result::data_seek

mysqli_data_seek

Mueve el puntero interno de resultado

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::data_seek(int $offset): bool
```php

Estilo procedimental

```php
mysqli_data_seek(mysqli_result $result, int $offset): bool
```

La función `mysqli_data_seek` mueve el puntero interno de resultado asociado al conjunto de resultados representado por `result`, haciéndolo apuntar a la fila especificada por `offset`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`offset`  
El desplazamiento de la fila. El parámetro `offset` debe estar comprendido entre cero y `mysqli_num_rows` - 1 (0..`mysqli_num_rows` - 1).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con mysqli::data_seek

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name";
$result = $mysqli->query($query);

/* Busca la fila 401 */
$result->data_seek(400);

/* Obtención de esta fila */
$row = $result->fetch_row();
printf("Ciudad: %s  Código País: %s\n", $row[0], $row[1]);
?>

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name";
$result = mysqli_query($link, $query);

/* Busca la fila 401 */
mysqli_data_seek($result, 400);

/* Obtención de esta fila */
$row = mysqli_fetch_row($result);
printf("Ciudad: %s  Código País: %s\n", $row[0], $row[1]);

   
```

Los ejemplos anteriores mostrarán:

    Ciudad: Benin City  Código País: NGA

Ajuste del puntero de resultado durante la iteración

Esta función puede ser útil durante la iteración sobre el conjunto de resultados para imponer un orden personalizado o para rebobinar el conjunto de resultados durante iteraciones múltiples.

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name LIMIT 15,4";
$result = $mysqli->query($query);

/* Consultar el conjunto de resultados en orden inverso */
for ($row_no = $result->num_rows - 1; $row_no >= 0; $row_no--) {
    $result->data_seek($row_no);

    /* Obtención de esta fila */
    $row = $result->fetch_row();
    printf("Ciudad: %s  Código País: %s\n", $row[0], $row[1]);
}

/* Restablecer el puntero al inicio del conjunto de resultados */
$result->data_seek(0);
print "\n";

/* Consultar nuevamente el mismo conjunto de resultados */
while ($row = $result->fetch_row()) {
    printf("Ciudad: %s  Código País: %s\n", $row[0], $row[1]);
}

   
```

Los ejemplos anteriores mostrarán:

    Ciudad: Acmbaro  Código País: MEX
    Ciudad: Abuja  Código País: NGA
    Ciudad: Abu Dhabi  Código País: ARE
    Ciudad: Abottabad  Código País: PAK
    Ciudad: Abottabad  Código País: PAK
    Ciudad: Abu Dhabi  Código País: ARE
    Ciudad: Abuja  Código País: NGA
    Ciudad: Acmbaro  Código País: MEX

## Notas

> [!NOTE]
> Esta función solo puede ser utilizada con resultados obtenidos con la función `mysqli_store_result`, `mysqli_query` o `mysqli_stmt_get_result`.

## Véase también

`mysqli_store_result`, `mysqli_fetch_row`, `mysqli_fetch_array`, `mysqli_fetch_assoc`, `mysqli_fetch_object`, `mysqli_query`, `mysqli_num_rows`
