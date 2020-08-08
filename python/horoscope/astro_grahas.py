######### Grahas #########
surya = 'Surya'
chandra = 'Chandra'
budha = 'Budha'
shukra = 'Shukra'
mangala = 'Mangala'
guru = "Guru"
shani = 'Shani'
rahu = 'Rahu'
ketu = 'Ketu'

grahas = {
    surya: {'id':1, 'name':'Surya', 'western_name':'Sun'},
    chandra: {'id':2, 'name':'Chandra', 'western_name':'Moon'},
    budha: {'id':3, 'name':'Budha', 'western_name':'Mercury'},
    shukra: {'id':4, 'name':'Shukra', 'western_name':'Venus'},
    mangala: {'id':5, 'name':'Mangala', 'western_name': 'Mars'},
    guru: {'id':6, 'name':'guru', 'western_name':'Jupiter'},
    shani: {'id':7, 'name':'Shani', 'western_name':'Saturn'},
    rahu: {'id':8, 'name':'Rahu', 'western_name':'Neptune'},
    ketu: {'id':9, 'name':'Ketu', 'western_name':'Pluto'}
}

grahas_properties = {
    surya:
        {'id':1,
         'gender':'male',
         'rank':'king',
         'owner_dir':'east',
         'varna':'kshatriya',
         'element_made_upof':'fire',
         'tridosha':'pitta',
         'time_spent_in_one_rashi_days':30,
         },
    chandra:
        {'id':2,
         'gender':'female',
         'rank':'queen',
         'owner_dir':'north-west',
         'varna':'vaishya',
         'element_made_upof':'water',
         'tridosha':'kapha',
         'time_spent_in_one_rashi_days':2.25,
         },
    budha:
        {'id':3,
         'gender':'nuetral',
         'rank':'prince',
         'owner_dir':'north',
         'varna':'bhudha',
         'element_made_upof':'earth',
         'tridosha':'mixed',
         'time_spent_in_one_rashi_days':24,
         },
    shukra:
        {'id':4,
         'gender':'female',
         'rank':'minister',
         'owner_dir':'south-east',
         'varna':'brahmin',
         'element_made_upof':'water',
         'tridosha':'vata/kapha',
         'time_spent_in_one_rashi_days':25,
         },
    mangala:
        {'id':5,
         'gender':'male',
         'rank':'commander',
         'owner_dir':'south',
         'varna':'kshatriya',
         'element_made_upof':'fire',
         'tridosha':'pitta',
         'time_spent_in_one_rashi_days':45,
         },
    guru:
        {'id':6,
         'gender':'male',
         'rank':'minister',
         'owner_dir':'north-east',
         'varna':'brahmin',
         'element_made_upof':'sky',
         'tridosha':'kapha',
         'time_spent_in_one_rashi_days':365,
         },
    shani:
        {'id':7,
         'gender':'nuetral',
         'rank':'shani',
         'owner_dir':'west',
         'varna':'shudra',
         'element_made_upof':'air',
         'tridosha':'vata',
         'time_spent_in_one_rashi_days':912.5,
         },
    rahu:
        {'id':8,
         'gender':'female',
         'rank':'',
         'owner_dir':'south-west',
         'varna': '',
         'element_made_upof':'',
         'tridosha':'',
         'time_spent_in_one_rashi_days':547.5,
         },
    ketu:
        {'id':9,
         'gender':'female',
         'rank':'',
         'owner_dir': 'south-west',
         'varna':'',
         'element_made_upof':'',
         'tridosha':'',
         'time_spent_in_one_rashi_days':547.5,
         },
}
