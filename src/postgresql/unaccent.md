---
title: unaccent — a text search dictionary which removes diacritics
source_url: https://www.postgresql.org/docs/17/unaccent.html
source_repo: https://github.com/postgres/postgres.git
source_ref: REL_17_STABLE
source_commit: 23088673d
source_path: unaccent.sgml
technology: postgresql
version: REL_17_STABLE
license: PostgreSQL
retrieved_at: '2026-09-15'
order: 3710
---

## unaccent a text search dictionary which removes diacritics

unaccent

`unaccent` is a text search dictionary that removes accents (diacritic signs) from lexemes. It's a filtering dictionary, which means its output is always passed to the next dictionary (if any), unlike the normal behavior of dictionaries. This allows accent-insensitive processing for full text search.

The current implementation of `unaccent` cannot be used as a normalizing dictionary for the `thesaurus` dictionary.

This module is considered “trusted”, that is, it can be installed by non-superusers who have `CREATE` privilege on the current database.

## Configuration

An `unaccent` dictionary accepts the following options:

- `RULES` is the base name of the file containing the list of translation rules. This file must be stored in `$SHAREDIR/tsearch_data/` (where `$SHAREDIR` means the PostgreSQL installation's shared-data directory). Its name must end in `.rules` (which is not to be included in the `RULES` parameter).

The rules file has the following format:

- Each line represents one translation rule, consisting of a character with accent followed by a character without accent. The first is translated into the second. For example,

              A
              A
              A
              A
              A
              A
              AE

  The two characters must be separated by whitespace, and any leading or trailing whitespace on a line is ignored.

- Alternatively, if only one character is given on a line, instances of that character are deleted; this is useful in languages where accents are represented by separate characters.

- Actually, each “character” can be any string not containing whitespace, so `unaccent` dictionaries could be used for other sorts of substring substitutions besides diacritic removal.

- Some characters, like numeric symbols, may require whitespaces in their translation rule. It is possible to use double quotes around the translated characters in this case. A double quote needs to be escaped with a second double quote when including one in the translated character. For example:

            " 1/4"
            " 1/2"
            " 3/4"
             """"
             """"

- As with other PostgreSQL text search configuration files, the rules file must be stored in UTF-8 encoding. The data is automatically translated into the current database's encoding when loaded. Any lines containing untranslatable characters are silently ignored, so that rules files can contain rules that are not applicable in the current encoding.

A more complete example, which is directly useful for most European languages, can be found in `unaccent.rules`, which is installed in `$SHAREDIR/tsearch_data/` when the `unaccent` module is installed. This rules file translates characters with accents to the same characters without accents, and it also expands ligatures into the equivalent series of simple characters (for example, to AE).

## Usage

Installing the `unaccent` extension creates a text search template `unaccent` and a dictionary `unaccent` based on it. The `unaccent` dictionary has the default parameter setting `RULES='unaccent'`, which makes it immediately usable with the standard `unaccent.rules` file. If you wish, you can alter the parameter, for example

    mydb=# ALTER TEXT SEARCH DICTIONARY unaccent (RULES='my_rules');

or create new dictionaries based on the template.

To test the dictionary, you can try:

    mydb=# select ts_lexize('unaccent','Htel');
     ts_lexize
    -----------
     {Hotel}
    (1 row)

Here is an example showing how to insert the `unaccent` dictionary into a text search configuration:

    mydb=# CREATE TEXT SEARCH CONFIGURATION fr ( COPY = french );
    mydb=# ALTER TEXT SEARCH CONFIGURATION fr
            ALTER MAPPING FOR hword, hword_part, word
            WITH unaccent, french_stem;
    mydb=# select to_tsvector('fr','Htels de la Mer');
        to_tsvector
    -------------------
     'hotel':1 'mer':4
    (1 row)

    mydb=# select to_tsvector('fr','Htel de la Mer') @@ to_tsquery('fr','Hotels');
     ?column?
    ----------
     t
    (1 row)

    mydb=# select ts_headline('fr','Htel de la Mer',to_tsquery('fr','Hotels'));
          ts_headline
    ------------------------
     <b>Htel</b> de la Mer
    (1 row)

## Functions

The `unaccent()` function removes accents (diacritic signs) from a given string. Basically, it's a wrapper around `unaccent`-type dictionaries, but it can be used outside normal text search contexts.

unaccent

unaccent(

dictionary

regdictionary

,

string

text

) returns

text

If the \<dictionary\> argument is omitted, the text search dictionary named `unaccent` and appearing in the same schema as the `unaccent()` function itself is used.

For example:

    SELECT unaccent('unaccent', 'Htel');
    SELECT unaccent('Htel');
