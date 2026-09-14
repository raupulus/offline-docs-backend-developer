---
title: Lista de filtros estándar
source_url: https://www.php.net/manual/es/filters.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/filters.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 3f1dbc451
order: 100
---

## Lista de filtros estándar

Esta sección contiene la lista de filtros de flujo, para usar con `stream_filter_append`. Su versión de PHP puede tener filtros adicionales, o faltantes en comparación con esta lista.

Es bueno notar una ligera diferencia entre `stream_filter_append` y `stream_filter_prepend`. Todos los flujos PHP disponen de un pequeño *buffer de lectura*, donde almacenan bloques de datos leídos en el sistema de ficheros, o en otras fuentes, para tratarlos de manera más eficiente. Tan pronto como los datos son leídos desde el recurso en el buffer interno, los datos son inmediatamente pasados al filtro, incluso si la aplicación PHP no está lista para leer estos datos. Si los datos ya están en espera en el buffer cuando un filtro se *añade al final*, estos datos serán inmediatamente pasados al filtro, para que la modificación sea transparente. Pero si un filtro se *antepone*, los datos *NO serán* filtrados. Esperarán a que el próximo bloque llegue del recurso.

Para obtener la lista completa de filtros de su versión de PHP, utilice la función `stream_get_filters`.

## Filtros de cadenas de caracteres

Cada filtro hace lo que su nombre implica, y se refiere al comportamiento de la función PHP correspondiente. Para más detalles sobre un filtro, consulte el manual de la función de referencia.

## string.rot13

El uso de este filtro es equivalente a tratar todos los datos del flujo a través de la función `str_rot13`.

string.rot13

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'string.rot13');
fwrite($fp, "Ceci est un test.\n");
/* muestra :  Prpv rfg ha grfg.   */
?>

    
```

## string.toupper

El uso de este filtro es equivalente a tratar todos los datos del flujo a través de la función `strtoupper`.

string.toupper

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'string.toupper');
fwrite($fp, "Ceci est un test.\n");
/* muestra :  CECI EST UN TEST.   */
?>

    
```

## string.tolower

El uso de este filtro es equivalente a tratar todos los datos del flujo a través de la función `strtolower`.

string.tolower

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'string.tolower');
fwrite($fp, "Ceci est un test.\n");
/* muestra :  ceci est un test.   */
?>

    
```

## string.strip_tags

El uso de este filtro es equivalente a tratar todos los datos del flujo a través de la función `strip_tags`. El filtro acepta parámetros en dos formatos: O bien como una `string` que contiene una lista de etiquetas, similar al segundo parámetro de la función `strip_tags`, o bien como un `array` de nombres de etiquetas.

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.3.0. Depender de esta funcionalidad está altamente desaconsejado.

string.strip_tags

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'string.strip_tags', STREAM_FILTER_WRITE, "<strong><em><span>");
fwrite($fp, "<strong>Ce texte en gras</strong> finit par être agrandi <h1>en un titre 1</h1>\n");
fclose($fp);
/* muestra :  Ce texte en gras finit par être agrandi en un titre 1   */

$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'string.strip_tags', STREAM_FILTER_WRITE, array('strong','em','span'));
fwrite($fp, "<strong>Ce texte en gras</strong> finit par être agrandi <h1>en un titre 1</h1>\n");
fclose($fp);
/* muestra :  Ce texte en gras finit par être agrandi en un titre 1   */
?>

    
```

## Filtros de conversión

Al igual que los filtros de `string`, los filtros de conversión hacen lo que su nombre indica. Para más información sobre un filtro dado, consulte la página del manual de la función correspondiente.

## convert.base64-encode y convert.base64-decode

El uso de este filtro es equivalente a tratar todos los datos del flujo a través de las funciones `base64_encode` y `base64_decode` respectivamente. `convert.base64-encode` soporta parámetros en forma de `array` asociativo. Si `line-length` es proporcionado, la salida base64 será separada en líneas de `line-length` caracteres. Si `line-break-chars` es proporcionado, cada bloque de caracteres será delimitado por el carácter proporcionado. Estos parámetros dan el mismo efecto que la función `base64_encode` utilizada conjuntamente con `chunk_split`.

convert.base64-encode & convert.base64-decode

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'convert.base64-encode');
fwrite($fp, "This is a test.\n");
fclose($fp);
/* muestra :  VGhpcyBpcyBhIHRlc3QuCg==  */

$param = array('line-length' => 8, 'line-break-chars' => "\r\n");
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'convert.base64-encode', STREAM_FILTER_WRITE, $param);
fwrite($fp, "This is a test.\n");
fclose($fp);
/* muestra :  VGhpcyBp
           :  cyBhIHRl
           :  c3QuCg==  */

$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'convert.base64-decode');
fwrite($fp, "VGhpcyBpcyBhIHRlc3QuCg==");
fclose($fp);
/* muestra :  This is a test.  */
?>

    
```

## convert.quoted-printable-encode y convert.quoted-printable-decode

El uso de la versión decode de este filtro es equivalente a tratar todos los datos del flujo a través de la función `quoted_printable_decode`. No hay equivalente funcional a `convert.quoted-printable-encode`. `convert.quoted-printable-encode` soporta parámetros en forma de `array` asociativo. Además de los parámetros soportados por `convert.base64-encode`, `convert.quoted-printable-encode` también acepta los argumentos `bool` `binary` y `force-encode-first`. `convert.base64-decode` soporta únicamente el parámetro `line-break-chars` como indicador de tipo para la extracción de la carga codificada.

convert.quoted-printable-encode & convert.quoted-printable-decode

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'convert.quoted-printable-encode');
fwrite($fp, "This is a test.\n");
/* muestra :  =This is a test.=0A  */
?>

    
```

## convert.iconv.\*

Los filtros `convert.iconv.*` están disponibles, si el soporte de [iconv](#book.iconv) está activado, y sus usos son equivalentes a tratar todos los datos del flujo con `iconv`. Estos filtros no soportan parámetros, pero se espera que el nombre del filtro contenga la codificación de los datos de entrada y salida, es decir, `convert.iconv.<input-encoding>.<output-encoding>` o `convert.iconv.<input-encoding>/<output-encoding>` (ambas notaciones son semánticamente equivalentes).

convert.iconv.\*

```php
<?php
$fp = fopen('php://output', 'w');
stream_filter_append($fp, 'convert.iconv.utf-16le.utf-8');
fwrite($fp, "T\0h\0i\0s\0 \0i\0s\0 \0a\0 \0t\0e\0s\0t\0.\0\n\0");
fclose($fp);
/* Muestra: This is a test. */
?>

    
```

## Filtros de compresión

Aunque las [envolturas de compresión](#wrappers.compression) proporcionan un medio para generar ficheros en los formatos gzip y bz2, no permiten manejar los protocolos de red comprimidos, ni comenzar con un flujo no comprimido para transformarlo en flujo comprimido. Para ello, un filtro de compresión puede ser aplicado en cualquier momento a cualquier recurso de flujo.

> [!NOTE]
> Los filtros de compresión *no generan* los encabezados y finales de ficheros, como lo hace la utilidad `gzip`. Solo comprimen y descomprimen porciones de flujo de datos.

## zlib.deflate y zlib.inflate

`zlib.deflate` (compresión) y `zlib.inflate` (descompresión) son las implementaciones de los métodos de compresión presentados en la [RFC 1951](https://datatracker.ietf.org/doc/html/rfc1951). El filtro `deflate` toma hasta tres parámetros, pasados en forma de `array` asociativo. `level` especifica el nivel de compresión deseado, de 1 a 9. Cuanto más alto sea el nivel, mejor será la compresión, y más costoso será el coste de compresión. Existen dos niveles de compresión especiales: 0, que representa la ausencia de compresión, y -1, que representa el nivel por defecto de zlib: actualmente, 6. `window` es el tamaño del buffer de memoria, en base 2. Los valores superiores, hasta 15, es decir, 32768 bytes, dan mejores compresiones, y los valores inferiores, hasta 9, es decir, 512 bytes, ocupan menos espacio en memoria. Por defecto, `window` vale actualmente `15`. `memory` es una indicación del nivel de memoria necesario. Los valores válidos van de 1, para la asignación mínima, a 9, para una asignación máxima. La asignación de memoria afecta la velocidad de ejecución, y no el coste global.

> [!NOTE]
> Como el nivel de compresión es el parámetro más común, también puede ser proporcionado como valor `int`, en lugar de un `array`.

Los filtros de compresión zlib.\* están disponibles si el soporte de [zlib](#ref.zlib) está activado.

`zlib.deflate` y `zlib.inflate`

```php
<?php
$params = array('level' => 6, 'window' => 15, 'memory' => 9);

$original_text = "This is a test.\nThis is only a test.\nThis is not an important string.\n";
echo "El texto original es largo de " . strlen($original_text) . " bytes.\n";

$fp = fopen('test.deflated', 'w');
stream_filter_append($fp, 'zlib.deflate', STREAM_FILTER_WRITE, $params);
fwrite($fp, $original_text);
fclose($fp);

echo "El fichero comprimido hace " . filesize('test.deflated') . " bytes de largo.\n";
echo "El texto original era :\n";
/* Utiliza readfile y zlib.inflate para descomprimir al vuelo */
readfile('php://filter/zlib.inflate/resource=test.deflated');

/* Muestra :

El texto original es largo de 70 bytes
El fichero comprimido hace 56 bytes de largo.
El texto original era :
This is a test.
This is only a test.
This is not an important string.

 */
?>

    
```

`zlib.deflate` simple

```php
<?php
$original_text = "This is a test.\nThis is only a test.\nThis is not an important string.\n";
echo "El texto original es largo de " . strlen($original_text) . " bytes.\n";

$fp = fopen('test.deflated', 'w');
/* Aquí, "6" indica el nivel de compresión de 6 */
stream_filter_append($fp, 'zlib.deflate', STREAM_FILTER_WRITE, 6);
fwrite($fp, $original_text);
fclose($fp);

echo "El fichero comprimido hace " . filesize('test.deflated') . " bytes de largo.\n";

/* Muestra :

El texto original es largo de 70 bytes
El fichero comprimido hace 56 bytes de largo.

 */
?>

    
```

## bzip2.compress y bzip2.decompress

`bzip2.compress` y `bzip2.decompress` funcionan de la misma manera que los filtros zlib descritos anteriormente. El filtro `bzip2.compress` acepta hasta 2 parámetros, en forma de `array` asociativo: `blocks` es un valor `int`, de 1 a 9, especificando el número de bloques de 100 kb de memoria a asignar al espacio de trabajo. `work` es también un `int` cuyo valor va de 0 a 250, e indica el nivel de esfuerzo proporcionado con un método de compresión antes de pasar a otro método, más lento. Modificar este parámetro solo tiene efecto en la velocidad de compresión. La ganancia de espacio o la memoria utilizada permanecen iguales. Un nivel de 0 indica que la biblioteca debe utilizar su configuración por defecto. El filtro `bzip2.decompress` acepta únicamente un parámetro, que puede ser pasado en forma de `bool`, o como el elemento `small` de un `array` asociativo. `small`, cuando se define a `true`, indica a la biblioteca bzip que debe realizar una descompresión utilizando la menor cantidad de memoria posible, a expensas de la velocidad.

Los filtros bzip2.\* están disponibles si el soporte de [bz2](#ref.bzip2) está activado.

`bzip2.compress` y `bzip2.decompress`

```php
<?php
$param = array('blocks' => 9, 'work' => 0);

echo "El fichero original hace " . strlen(LICENSE) . " bytes de largo.\n";

$fp = fopen('LICENSE.compressed', 'w');
stream_filter_append($fp, 'bzip2.compress', STREAM_FILTER_WRITE, $param);
fwrite($fp, file_get_contents('LICENSE'));
fclose($fp);

echo "El fichero comprimido hace " . filesize('LICENSE.compressed') . " bytes de largo.\n";

/* Muestra :

El fichero original hace 3288 bytes de largo.
El fichero comprimido hace 1488 bytes de largo.

 */
?>

    
```

## Filtros de cifrado

Los filtros de cifrado son particularmente útiles para el cifrado de ficheros/flujos.

## mcrypt.\* y mdecrypt.\*

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.1.0. Depender de esta funcionalidad está altamente desaconsejado.

`mcrypt.*` y `mdecrypt.*` proporcionan un sistema de cifrado simétrico utilizando libmcrypt. Ambos conjuntos de filtros soportan los mismos algoritmos disponibles en la [extensión mcrypt](#ref.mcrypt) en forma `mcrypt.ciphername` donde `ciphername` es el nombre del cifrado que será transmitido a `mcrypt_module_open`. Los cinco parámetros siguientes también están disponibles:

| Parámetro | Obligatorio ? | Por omisión | Valores posibles |
|----|----|----|----|
| mode | Opcional | cbc | cbc, cfb, ecb, nofb, ofb, stream |
| algorithms_dir | Opcional | ini_get('mcrypt.algorithms_dir') | Ruta hacia los algoritmos de módulos |
| modes_dir | Opcional | ini_get('mcrypt.modes_dir') | Ruta hacia los modos de módulos |
| iv | Obligatorio | N/A | Generalmente 8, 16 o 32 bytes de datos binarios. Depende del cifrado |
| key | Obligatorio | N/A | Generalmente 8, 16 o 32 bytes de datos binarios. Depende del cifrado |

Parámetros de los filtros mcrypt

Cifrado / Descifrado con Blowfish

```php
<?php
//$key se supone que fue generado previamente
$iv_size = mcrypt_get_iv_size(MCRYPT_BLOWFISH, MCRYPT_MODE_CBC);
$iv = mcrypt_create_iv($iv_size, MCRYPT_DEV_URANDOM);
$fp = fopen('encrypted-file.enc', 'wb');
fwrite($fp, $iv);
$opts = array('mode'=>'cbc','iv'=>$iv, 'key'=>$key);
stream_filter_append($fp, 'mcrypt.blowfish', STREAM_FILTER_WRITE, $opts);
fwrite($fp, 'message to encrypt');
fclose($fp);

//descifrado...
$fp = fopen('encrypted-file.enc', 'rb');
$iv = fread($fp, $iv_size = mcrypt_get_iv_size(MCRYPT_BLOWFISH, MCRYPT_MODE_CBC));
$opts = array('mode'=>'cbc','iv'=>$iv, 'key'=>$key);
stream_filter_append($fp, 'mdecrypt.blowfish', STREAM_FILTER_READ, $opts);
$data = rtrim(stream_get_contents($fp));//elimina el relleno nulo
fclose($fp);
echo $data;
?>

    
```

Cifrar un fichero utilizando AES-128 CBC con SHA256 HMAC

```php
<?php
AES_CBC::encryptFile($password, "plaintext.txt", "encrypted.enc");
AES_CBC::decryptFile($password, "encrypted.enc", "decrypted.txt");

class AES_CBC
{
   protected static $KEY_SIZES = array('AES-128'=>16,'AES-192'=>24,'AES-256'=>32);
   protected static function key_size() { return self::$KEY_SIZES['AES-128']; } //por defecto AES-128
   public static function encryptFile($password, $input_stream, $aes_filename){
      $iv_size = mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);
      $fin = fopen($input_stream, "rb");
      $fc = fopen($aes_filename, "wb+");
      if (!empty($fin) && !empty($fc)) {
         fwrite($fc, str_repeat("_", 32) );//marcador de posición, SHA256 HMAC irá aquí más tarde
         fwrite($fc, $hmac_salt = mcrypt_create_iv($iv_size, MCRYPT_DEV_URANDOM));
         fwrite($fc, $esalt = mcrypt_create_iv($iv_size, MCRYPT_DEV_URANDOM));
         fwrite($fc, $iv = mcrypt_create_iv($iv_size, MCRYPT_DEV_URANDOM));
         $ekey = hash_pbkdf2("sha256", $password, $esalt, $it=1000, self::key_size(), $raw=true);
         $opts = array('mode'=>'cbc', 'iv'=>$iv, 'key'=>$ekey);
         stream_filter_append($fc, 'mcrypt.rijndael-128', STREAM_FILTER_WRITE, $opts);
         $infilesize = 0;
         while (!feof($fin)) {
            $block = fread($fin, 8192);
            $infilesize+=strlen($block);
            fwrite($fc, $block);
         }
         $block_size = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);
         $padding = $block_size - ($infilesize % $block_size);//$padding es un número de 1-16
         fwrite($fc, str_repeat(chr($padding), $padding) );//realiza PKCS7 padding
         fclose($fin);
         fclose($fc);
         $hmac_raw = self::calculate_hmac_after_32bytes($password, $hmac_salt, $aes_filename);
         $fc = fopen($aes_filename, "rb+");
         fwrite($fc, $hmac_raw);//sobrescribe el marcador de posición
         fclose($fc);
      }
   }
   public static function decryptFile($password, $aes_filename, $out_stream) {
      $iv_size = mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);
      $hmac_raw = file_get_contents($aes_filename, false, NULL,  0, 32);
      $hmac_salt = file_get_contents($aes_filename, false, NULL, 32, $iv_size);
      $hmac_calc = self::calculate_hmac_after_32bytes($password, $hmac_salt, $aes_filename);
      $fc = fopen($aes_filename, "rb");
      $fout = fopen($out_stream, 'wb');
      if (!empty($fout) && !empty($fc) && self::hash_equals($hmac_raw,$hmac_calc)) {
         fread($fc, 32+$iv_size);//saltar sha256 hmac y salt
         $esalt = fread($fc, $iv_size);
         $iv    = fread($fc, $iv_size);
         $ekey = hash_pbkdf2("sha256", $password, $esalt, $it=1000, self::key_size(), $raw=true);
         $opts = array('mode'=>'cbc', 'iv'=>$iv, 'key'=>$ekey);
         stream_filter_append($fc, 'mdecrypt.rijndael-128', STREAM_FILTER_READ, $opts);
         while (!feof($fc)) {
            $block = fread($fc, 8192);
            if (feof($fc)) {
               $padding = ord($block[strlen($block) - 1]);//supone PKCS7 padding
               $block = substr($block, 0, 0-$padding);
            }
            fwrite($fout, $block);
         }
         fclose($fout);
         fclose($fc);
      }
   }
   private static function hash_equals($str1, $str2) {
      if(strlen($str1) == strlen($str2)) {
         $res = $str1 ^ $str2;
         for($ret=0,$i = strlen($res) - 1; $i >= 0; $i--) $ret |= ord($res[$i]);
         return !$ret;
      }
      return false;
   }
   private static function calculate_hmac_after_32bytes($password, $hsalt, $filename) {
      static $init=0;
      $init or $init = stream_filter_register("user-filter.skipfirst32bytes", "FileSkip32Bytes");
      $stream = 'php://filter/read=user-filter.skipfirst32bytes/resource=' . $filename;
      $hkey = hash_pbkdf2("sha256", $password, $hsalt, $iterations=1000, 24, $raw=true);
      return hash_hmac_file('sha256', $stream, $hkey, $raw=true);
   }
}
class FileSkip32Bytes extends php_user_filter
{
   private $skipped=0;
   function filter($in, $out, &$consumed, $closing)  {
      while ($bucket = stream_bucket_make_writeable($in)) {
         $outlen = $bucket->datalen;
         if ($this->skipped<32){
            $outlen = min($bucket->datalen,32-$this->skipped);
            $bucket->data = substr($bucket->data, $outlen);
            $bucket->datalen = $bucket->datalen-$outlen;
            $this->skipped+=$outlen;
         }
         $consumed += $outlen;
         stream_bucket_append($out, $bucket);
      }
      return PSFS_PASS_ON;
   }
}
class AES_128_CBC extends AES_CBC {
   protected static function key_size() { return self::$KEY_SIZES['AES-128']; }
}
class AES_192_CBC extends AES_CBC {
   protected static function key_size() { return self::$KEY_SIZES['AES-192']; }
}
class AES_256_CBC extends AES_CBC {
   protected static function key_size() { return self::$KEY_SIZES['AES-256']; }
}

    
```
