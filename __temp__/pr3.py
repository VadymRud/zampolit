(InteractiveConsole)
>>> from osoba.models import MilitaryRank, Platoon, ServiseID, Unit
>>> image_path = 'D:\downloads\photo_2021-02-13_10-45-02.jpg'
>>> with open(image_path,'rb') as image_file:
...     image_string = image_file.read()
...

 sid = ServiseID.objects.create(image3x4=image_string, name='proba', sename = 'prob', third_name = 'thn', birth_date='2000-03-23', military_ranks = MilitaryRank.objects.get(id=1), unit = Unit.objects.get(id=1), platoon=Platoon.objects.get(id=1))
