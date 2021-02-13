from docxtpl import DocxTemplate
doc = DocxTemplate("templ1.docx")
##context = { 'dick' : "И.И.Иванов"}
##doc.render(context)
##doc.save("шаблон-final.docx")

kids = [{
    
        'first': 'John',
        'last':'Williams',
        'addr1':'5555 NW 37th St',
        'addr2':'Apt 2601',
        'city':'Oklahoma City',
        'state':'OK',
        'zip':'73112'
    },
    {
        'first':'George',
        'last':'Lucas',
        'addr1':'1234 Dobbs St.',
        'addr2':'Suite 62',
        'city':'Moore',
        'state':'OK',
        'zip':'73160'
    }
]

doc = DocxTemplate("templ1.docx")
context = { 'dick' : "И.И.Иванов", 'kids' : kids}
doc.render(context)
doc.save("шаблон-final.docx")
for kid in kids:
    print(kid['first'])
    print('___________')
