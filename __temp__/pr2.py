# -*- coding: utf-8 -*-

from docxtpl import DocxTemplate

tpl = DocxTemplate('horizontal_merge_tpl.docx')
tpl.render({})
tpl.save('horizontal_merge.docx')
