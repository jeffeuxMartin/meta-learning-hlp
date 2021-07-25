#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finished on Mon Jul 26 06:11:06 2021

@filename:    table_format_parser.py
@author:      Chien-Cheng (Jeff) Chen
@description: Parse the table Markdown file and bib YAML file into a linked table.
"""

"""TODO:
1. Comment and wrapping functions for the script.
2. `parsed_md = parser__tex_md(ref_texfile)`
3. `parsed_yaml = parser__bib_yaml(bibtex)`
4. Auto any bibtex format
"""

"""DONE:
1. Deduplicated done
2. Surname format done (hope to have automatic method...)
3. Double link done
4. `{}`s removed
"""

import yaml
# NOTE: \[[\w:-]*\]
# NOTE: '-:_' + 'A-Za-z0-9'

# FIXME: parsed_html = parser__tex_html(ref_texfile)
# FIXME: parsed_md = parser__html_md(parsed_html)
parsed_md__FILENAME = "materials/template_md.md"
with open(parsed_md__FILENAME) as f:
    parsed_md = f.read()

# FIXME: parsed_yaml = parser__bib_yaml(bibtex)
parsed_yaml__FILENAME = "materials/bib_source.yaml"
with open(parsed_yaml__FILENAME) as f:
    parsed_yaml = yaml.load(f, Loader=yaml.FullLoader)

dup_ref_list = {}
hungyi_ref_list = {}
for cite_key in parsed_yaml:
    cited_item = parsed_yaml[cite_key]
    conf       = cited_item["conf"     ].strip().replace("\n", ' ').replace("  ", ' ')
    firstauth  = cited_item["firstauth"].strip().replace("\n", ' ').replace("  ", ' ')
    fullauth   = cited_item["fullauth" ].strip().replace("\n", ' ').replace("  ", ' ')
    title      = cited_item["title"    ].strip().replace("\n", ' ').replace("  ", ' ')
    year       = cited_item["year"     ]
    link       = cited_item["link"     ]

    paper_key = \
        f"[{firstauth}, {conf}’{str(year)[2:]}]"
    paper_hungyi_ref = \
        f"<i>{fullauth}</i>, {title}, {conf}, {year}"  # TODO: any bib?
    if link == '':
        paper_hungyi_ref_extra = \
            f"<i>{fullauth}</i>, {title}, {conf}, {year}"
    else:
        paper_hungyi_ref_extra = \
            f"<i>{fullauth}</i>, {title}, {conf}, {year} [:link:]({link})"
    paper_table_form__before = f"[{cite_key}]"
    paper_list_item = (
        paper_key, 
        paper_hungyi_ref,
        paper_table_form__before,
        cite_key,
        paper_hungyi_ref_extra,
    )
    # region Assign key to papers
    # if key in dup-ref-list:
    if paper_key in dup_ref_list:
        # give a new key
        dup_ref_list[paper_key].append(paper_list_item)
        real_key = (paper_key[:-1] + 
            chr(ord('a') + len(dup_ref_list[paper_key]) - 1)) + ']'
    # elif dup:
    elif paper_key in hungyi_ref_list:
        # dup append item
        existing = hungyi_ref_list.pop(paper_key)
        dup_ref_list[paper_key] = [
            existing, paper_list_item]
        # retrieve a key from dup
        hungyi_ref_list[
            paper_key[:-1] + 'a]'] = existing
        real_key = paper_key[:-1] + 'b]'
    else:
        real_key = paper_key
    # hyref[key] = paper
    # endregion        
    hungyi_ref_list[real_key] = paper_list_item

assert len(hungyi_ref_list) == len(parsed_yaml), \
    "Length different!"

content = parsed_md[:]
for item in hungyi_ref_list:
    (
        paper_key, 
        paper_hungyi_ref,
        paper_table_form__before,
        cite_key,
        paper_hungyi_ref_extra,
    ) = hungyi_ref_list[item]
    paper_table_form__after = \
        f"([{item[1:-1]}](#{cite_key}))"
    paper_table_form__wrapped = \
        f"<span id=\"back__{cite_key}\">{paper_table_form__after}</span>"
    
    content = content.replace(
        paper_table_form__before,
        paper_table_form__wrapped)

 
with open('README.md', 'w') as f:
    f.write(content)
    f.write('\n')
    for item in sorted(hungyi_ref_list):
        (
            paper_key, 
            paper_hungyi_ref,
            paper_table_form__before,
            cite_key,
            paper_hungyi_ref_extra,
        ) = hungyi_ref_list[item]
        paper_list_form__wrapped = \
            f"- <span id=\"{cite_key}\"> [[{item[1:-1]}](#back__{cite_key})] {paper_hungyi_ref}</span>"
        f.write(paper_list_form__wrapped + '\n')

# TODO: Smart extra?
with open('README_linked.md', 'w') as f:
    f.write(content)
    f.write('\n')
    for item in sorted(hungyi_ref_list):
        (
            paper_key, 
            paper_hungyi_ref,
            paper_table_form__before,
            cite_key,
            paper_hungyi_ref_extra,
        ) = hungyi_ref_list[item]
        paper_list_form__wrapped = \
            f"- <span id=\"{cite_key}\"> [[{item[1:-1]}](#back__{cite_key})] {paper_hungyi_ref_extra}</span>"
        f.write(paper_list_form__wrapped + '\n')
