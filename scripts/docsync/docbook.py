"""
Conversión de DocBook XML a markdown.

Es el camino para PHP, cuya documentación se escribe en DocBook y se
publica en git (php/doc-es para español, php/doc-en para inglés).

POR QUÉ EL XML Y NO EL HTML DE php.net
──────────────────────────────────────
El tarball de HTML de php.net es un artefacto compilado: cada página
trae barra de navegación, migas de pan, pie y notas de usuario que hay
que recortar, y los ejemplos de código no van en <pre> sino en
<div class="phpcode"> con spans de color y <br />, lo que obliga a
rearmarlos a mano.

El XML no tiene nada de eso, porque es estructura y no presentación.
Pandoc además trae lector nativo de DocBook. Y al venir de git se clona
superficialmente, se registra el commit exacto y `git diff` enseña qué
cambió entre reconstrucciones.

LAS ENTIDADES
─────────────
El obstáculo aparente del XML son las entidades: &reftitle.description;
y compañía. Resultan estar definidas en cuatro ficheros .ent — tres en
el repo de traducción y uno en php/doc-base — con unas 1.500
definiciones que se resuelven por sustitución de texto. No hace falta
ni DTD ni catálogo XML.

Lo que queda sin resolver son entidades XML estándar (&gt;, &amp;) que
pandoc ya entiende, y entidades de include estructural que solo
aparecen en ficheros de armazón sin contenido propio.
"""

from __future__ import annotations

import html as html_mod
import re
import subprocess
from pathlib import Path

RE_ENTITY_DEF = re.compile(
    r"<!ENTITY\s+([\w.-]+)\s+(?:'([^']*)'|\"([^\"]*)\")\s*>", re.DOTALL
)
RE_ENTITY_USE = re.compile(r"&([\w.-]+);")
RE_XML_DECL = re.compile(r"<\?xml[^>]*\?>")
RE_TAG = re.compile(r"<[^>]+>")
RE_WS = re.compile(r"\s+")
RE_BLANK = re.compile(r"\n{3,}")

RE_METHODSYNOPSIS = re.compile(
    r"<(methodsynopsis|constructorsynopsis|destructorsynopsis)\b.*?</\1>", re.DOTALL
)
RE_TYPE = re.compile(r"<type[^>]*>(.*?)</type>", re.DOTALL)
RE_METHODNAME = re.compile(r"<methodname[^>]*>(.*?)</methodname>", re.DOTALL)
RE_METHODPARAM = re.compile(r"<methodparam([^>]*)>(.*?)</methodparam>", re.DOTALL)
RE_PARAMETER = re.compile(r"<parameter[^>]*>(.*?)</parameter>", re.DOTALL)
RE_MODIFIER = re.compile(r"<modifier[^>]*>(.*?)</modifier>", re.DOTALL)

RE_XML_ID = re.compile(r'<\w+[^>]*\bxml:id="([^"]+)"')
RE_REFNAME = re.compile(r"<refname[^>]*>(.*?)</refname>", re.DOTALL)
RE_REFPURPOSE = re.compile(r"<refpurpose[^>]*>(.*?)</refpurpose>", re.DOTALL)
RE_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.DOTALL)

# Comentario que php.net mantiene al principio de cada traducción
RE_TRANSLATION = re.compile(
    r"<!--\s*EN-Revision:\s*(\S+)\s+Maintainer:\s*(\S+)\s+Status:\s*(\S+)\s*-->"
)
RE_REVIEWED = re.compile(r"<!--\s*Reviewed:\s*(\w+)\s*-->")

# Restos de la conversión que no aportan nada en markdown
RE_BARE_DIV = re.compile(r"^\s*</?div[^>]*>\s*$", re.MULTILINE)
RE_H1 = re.compile(r"^# ", re.MULTILINE)

# Entidades de include estructural que doc-base genera al ensamblar el
# manual. Solo aparecen en ficheros de armazón sin contenido propio.
RE_LEFTOVER_ENTITY = re.compile(r"&[\w]+\.[\w.-]+;")

# Marcador para las firmas, que sobrevive a pandoc sin reinterpretarse
SIGNATURE_MARKER = "ZQSIGNATUREZQ{}ZQ"
RE_SIGNATURE_MARKER = re.compile(r"ZQSIGNATUREZQ(\d+)ZQ")


def _text(fragment: str) -> str:
    return RE_WS.sub(" ", html_mod.unescape(RE_TAG.sub("", fragment))).strip()


# ── Entidades ───────────────────────────────────────────────────────

def load_entities(paths: list[Path]) -> dict[str, str]:
    """Lee todas las definiciones <!ENTITY> de los ficheros dados."""
    entities: dict[str, str] = {}
    for path in paths:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for match in RE_ENTITY_DEF.finditer(content):
            entities[match.group(1)] = match.group(2) or match.group(3) or ""
    return entities


def resolve_entities(text: str, entities: dict[str, str], depth: int = 8) -> str:
    """Sustituye entidades hasta que no queden, con tope de profundidad.

    Se itera porque una entidad puede contener otras. El tope evita un
    bucle infinito si alguna se referencia a sí misma.
    """
    for _ in range(depth):
        new = RE_ENTITY_USE.sub(
            lambda m: entities.get(m.group(1), m.group(0)), text
        )
        if new == text:
            break
        text = new
    return text


# ── Firma de funciones ──────────────────────────────────────────────

def extract_synopses(xml: str) -> tuple[str, list[str]]:
    """Sustituye las firmas por marcadores y las devuelve aparte.

    Pandoc aplana <methodsynopsis> en líneas sueltas — 'int strlen
    string string' en vez de 'strlen(string $string): int' — y para una
    referencia de funciones esa es justo la línea que más se consulta.

    Se saca de la conversión en lugar de reescribirla como
    <programlisting> porque pandoc decide por su cuenta entre bloque
    vallado e indentado, y así el resultado no depende de eso.
    """
    signatures: list[str] = []

    def one(match: re.Match) -> str:
        block = match.group(0)

        modifiers = " ".join(_text(m) for m in RE_MODIFIER.findall(block))

        name_match = RE_METHODNAME.search(block)
        name = _text(name_match.group(1)) if name_match else ""

        # El primer <type> fuera de un methodparam es el de retorno
        without_params = RE_METHODPARAM.sub("", block)
        return_match = RE_TYPE.search(without_params)
        return_type = _text(return_match.group(1)) if return_match else ""

        params = []
        for raw_attrs, body in RE_METHODPARAM.findall(block):
            optional = 'choice="opt"' in raw_attrs
            variadic = 'rep="repeat"' in raw_attrs

            type_match = RE_TYPE.search(body)
            param_match = RE_PARAMETER.search(body)
            param_type = _text(type_match.group(1)) if type_match else ""
            param_name = _text(param_match.group(1)) if param_match else ""

            piece = f"{param_type} ${param_name}".strip()
            if variadic:
                piece = f"{param_type} ...${param_name}".strip()
            params.append(f"[{piece}]" if optional else piece)

        signature = f"{name}({', '.join(params)})"
        if modifiers:
            signature = f"{modifiers} {signature}"
        if return_type:
            signature = f"{signature}: {return_type}"

        marker = SIGNATURE_MARKER.format(len(signatures))
        signatures.append(signature)
        return f"<para>{marker}</para>"

    return RE_METHODSYNOPSIS.sub(one, xml), signatures


def restore_synopses(
    markdown_text: str,
    signatures: list[str],
    language: str,
) -> str:
    def swap(match: re.Match) -> str:
        index = int(match.group(1))
        if index >= len(signatures):
            return match.group(0)
        return f"```{language}\n{signatures[index]}\n```"

    return RE_SIGNATURE_MARKER.sub(swap, markdown_text)


# ── Metadatos ───────────────────────────────────────────────────────

def translation_status(xml: str) -> dict[str, str]:
    """Estado de la traducción, que php.net anota en cada fichero.

    Permite avisar en el visor de qué páginas están sin revisar o
    desactualizadas respecto al inglés.
    """
    info: dict[str, str] = {}

    match = RE_TRANSLATION.search(xml)
    if match:
        info["translation_revision"] = match.group(1)[:9]
        info["translation_status"] = match.group(3)

    reviewed = RE_REVIEWED.search(xml)
    if reviewed:
        info["translation_reviewed"] = reviewed.group(1).lower() == "yes"

    return info


def document_title(xml: str) -> str | None:
    for pattern in (RE_REFNAME, RE_TITLE):
        match = pattern.search(xml)
        if match:
            title = _text(match.group(1))
            if title:
                return title
    return None


def document_summary(xml: str) -> str | None:
    match = RE_REFPURPOSE.search(xml)
    return _text(match.group(1)) if match else None


def document_id(xml: str) -> str | None:
    """El xml:id del elemento raíz, que es el slug real de php.net.

    <refentry xml:id="function.strlen"> se publica como
    https://www.php.net/manual/es/function.strlen.php

    Merece la pena sacarlo de aquí en vez de construir la URL a partir
    del nombre del fichero: el slug no siempre coincide, y una URL
    inventada que devuelve 404 es peor que no poner ninguna.
    """
    match = RE_XML_ID.search(xml)
    return match.group(1) if match else None


# ── Conversión ──────────────────────────────────────────────────────

def to_markdown(xml: str, pandoc_to: str = "gfm") -> str:
    proc = subprocess.run(
        ["pandoc", "-f", "docbook", "-t", pandoc_to, "--wrap=none"],
        input=xml,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "pandoc falló")
    return proc.stdout


def fence_all_code(markdown_text: str, language: str) -> str:
    """Pone lenguaje a todos los bloques de código de apertura.

    Pandoc emite ``` sin lenguaje. Se alternan aperturas y cierres, así
    que basta con marcar los de índice par.
    """
    if not language:
        return markdown_text

    lines = markdown_text.split("\n")
    inside = False
    for i, line in enumerate(lines):
        if line.strip() == "```":
            if not inside:
                lines[i] = f"```{language}"
            inside = not inside
    return "\n".join(lines)


def _tidy(markdown_text: str, language: str) -> str:
    # Los encabezados de sección de DocBook llegan como H1; el visor ya
    # pinta el título del documento, así que bajan un nivel.
    text = RE_H1.sub("## ", markdown_text)
    text = RE_BARE_DIV.sub("", text)
    text = fence_all_code(text, language)
    return RE_BLANK.sub("\n\n", text).strip() + "\n"


def convert(
    xml: str,
    entities: dict[str, str],
    language: str = "php",
    pandoc_to: str = "gfm",
) -> tuple[str, str | None, dict]:
    """XML de DocBook → (markdown, título, metadatos de traducción)."""
    meta = translation_status(xml)

    resolved = resolve_entities(xml, entities)
    title = document_title(resolved)

    summary = document_summary(resolved)
    if summary:
        meta["description"] = summary

    doc_id = document_id(resolved)
    if doc_id:
        meta["doc_id"] = doc_id

    prepared = RE_XML_DECL.sub("", resolved).strip()

    # Las entidades de include estructural se quitan ANTES de pandoc.
    # doc-base las resuelve al ensamblar el manual completo, pero aquí
    # cada fichero se convierte por separado y pandoc aborta con
    # UnresolvedEntityException. Son ficheros de armazón: al quitarlas
    # el documento queda vacío y se descarta más arriba, que es lo
    # correcto. Sin esto fallaban 780 documentos de PHP.
    prepared = RE_LEFTOVER_ENTITY.sub("", prepared)

    prepared, signatures = extract_synopses(prepared)

    body = to_markdown(prepared, pandoc_to)
    body = restore_synopses(body, signatures, language)
    body = _tidy(body, language)
    body = RE_BLANK.sub("\n\n", body).strip()

    return (body + "\n" if body else ""), title, meta
