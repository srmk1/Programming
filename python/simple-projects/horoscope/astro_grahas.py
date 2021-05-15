from .astro_rashis import *

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

grahas = [ surya, chandra, budha, shukra, mangala, guru, shani, rahu, ketu]

intimate_friend = 'intimate_friend'
friend = 'friend'
nuetral = 'nuetral'
enemy = 'enemy'
bitter_enemy = 'bitter_enemy'

graha_relations = [ intimate_friend, friend, nuetral, enemy, bitter_enemy]

grahas_properties = {
    surya:
        {'id':1,
         'western_name':'Sun',
         'gender':'male',
         'rank':'king',
         'owner_dir':'east',
         'varna':'kshatriya',
         'element_made_upof':'fire',
         'tridosha':'pitta',
         'movement':'sthira',
         'rules_number':1,
         'day':'ravivara/bhanuvara',
         'color':'dark-red',             #mixture of brown+red
         'stone':'ruby',
         'metal':'gold',
         #If a horoscope has favorable sun
         #they will have strong and influential personality or atma
         'controls-human-aspect':'atma/soul',
         'human-relation':'father',
         'natural-tendency':'ashubha-graha',
         'time_spent_in_one_rashi_days':30,
         },
    chandra:
        {'id':2,
         'western_name':'Moon',
         'gender':'female',
         'rank':'queen',
         'owner_dir':'north-west',
         'varna':'vaishya',
         'element_made_upof':'water',
         'tridosha':'kapha',
         'movement':'chara',
         'rules_number':2,
         'day':'somavara',
         'color':'white',
         'stone':'white-pearl',
         'metal':'silver',
         # If a horoscope has favorable moon
         # inflicted moon indicates unstable mind/flickering-mind/depression
         'controls-human-aspect':'manas/mind',
         'human-relation':'mother',
         'natural-tendency':'subha-shukla-paksha/ashubha-krishna-paksha',
         'time_spent_in_one_rashi_days':2.25,
         },
    budha:
        {'id':3,
         'western_name':'Mercury',
         'gender':'nuetral',
         'rank':'prince',
         'owner_dir':'north',
         'varna':'bhudha',
         'element_made_upof':'earth',
         'tridosha':'mixed',
         'movement':'sthira/chara/dual',
         'rules_number':5,
         'day':'bhudhavara',
         'color':'green',
         'stone':'emerald',
         'metal':'bronze',
         'controls-human-aspect':'vak/speech',
         'human-relation':'friends/relatives/maternal-uncle',
         'natural-tendency':'nuetral',      #will become shubha when placed with shubha-graha and ashubha when placed
                                            #with ashubha graha
         'time_spent_in_one_rashi_days':24,
         },
    shukra:
        {'id':4,
         'western_name':'Venus',
         'gender':'female',
         'rank':'minister',
         'owner_dir':'south-east',
         'varna':'brahmin',
         'element_made_upof':'water',
         'tridosha':'vata/kapha',
         'movement':'chara',
         'rules_number':6,
         'day':'shukravara',
         'color':'white',
         'stone':'diamond',
         'metal':'silver',
         'controls-human-body':'mind',
         'controls-human-aspect':'viryaa/semens',
         'human-relation':'spouse/life-partner/business-partner',
         'natural-tendency':'subha-graha',
         'time_spent_in_one_rashi_days':25,
         },
    mangala:
        {'id':5,
         'western_name': 'Mars',
         'gender':'male',
         'rank':'commander',
         'owner_dir':'south',
         'varna':'kshatriya',
         'element_made_upof':'fire',
         'tridosha':'pitta',
         'movement':'chara',
         'rules_number':9,
         'day':'mangalavara',
         'color':'red',
         'stone':'coral',
         'metal':'copper',
         'controls-human-aspect':'urja/strength',
         'human-relation':'younger-brothers/sisters/cousins',
         'natural-tendency':'ashubha',
         'time_spent_in_one_rashi_days':45,
         },
    guru:
        {'id':6,
         'western_name': 'Jupiter',
         'gender':'male',
         'rank':'minister',
         'owner_dir':'north-east',
         'varna':'brahmin',
         'element_made_upof':'sky',
         'tridosha':'kapha',
          'movement':'sthira',
         'rules_number':3,
         'day':'guruvara',
         'color':'yellow',
         'stone':'yellow-saphire',
         'metal':'jupiter',
         'controls-human-aspect':'gyana/knowledge',     #Spiritual or wordly
         'human-relation':'elder-brothers/sisters/cousins',
         'natural-tendency':'subha-graha',
         'time_spent_in_one_rashi_days':365,
         },
    shani:
        {'id':7,
         'western_name': 'Saturn',
         'gender':'nuetral',
         'rank':'shani',
         'owner_dir':'west',
         'varna':'shudra',
         'element_made_upof':'air',
         'tridosha':'vata',
         'movement':'sthira',
         'rules_number':8,
         'day':'shanivara',
         'color':'black',
         'stone':'blue-saphire',
         'metal':'iron',
         'controls-human-aspect':'dukha/grief',
         'human-relation':'servant',
         'natural-tendency':'asubha-graha',
         'time_spent_in_one_rashi_days':912.5,
         },
    rahu:
        {'id':8,
         'western_name': '',
         'gender':'female',
         'rank':'',
         'owner_dir':'south-west',
         'varna': '',
         'element_made_upof':'',
         'tridosha':'',
         'movement':'',
         'rules_number':4,
         'color':'blue',
         'stone':'gomedha',
         'metal':'mixed-metails',
         'human-relation':'paternal-grandfather/maternal-grandmother/old-people',
         'natural-tendency': 'nuetral',
         'time_spent_in_one_rashi_days':547.5,
         #Rahu and Ketu are always 180 degrees apart in horoscope
         },
    ketu:
        {'id':9,
         'western_name': '',
         'gender':'female',
         'rank':'',
         'owner_dir': 'south-west',
         'varna':'',
         'element_made_upof':'',
         'tridosha':'',
         'movement':'',
         'rules_number':7,
         'color':'black/smoke',
         'stone':'cats-eye',
         'metal':'mixed-metails',
         'human-relation':'paternal-grandmother/maternal-grandfather/old-people',
         'natural-tendency': 'nuetral',
         'time_spent_in_one_rashi_days':547.5,
         },
}


grahas_permanent_relations = {
    surya: {'id':1,
            'name':'Surya',
            'friend': [chandra, mangala, guru],
            'nuetral': [budha],
            'enemy': [shukra, shani],
            },
    chandra: {'id':2,
              'name':'Chandra',
              'friend': [surya, budha],
              'nuetral':[mangala, guru, shani, shukra],
              'enemy':[]},
    budha: {'id':3,
            'name':'Budha',
            'friend': [surya, shukra],
            'nuetral': [shani, mangala, guru],
            'enemy': [chandra]
            },
    shukra: {'id':4,
             'name':'Shukra',
             'friend': [budha, shani],
              'nuetral':[mangala],
              'enemy':[surya, chandra, guru]},
    mangala: {'id':5,
              'name':'Mangala',
              'friend': [guru, surya, chandra],
              'nuetral': [shukra, shani],
              'enemy': [budha]
              },
    guru: {'id':6,
           'name':'guru',
           'friend': [surya, chandra, mangala],
           'nuetral': [shani],
           'enemy': [budha, shukra]
           },
    shani: {'id':7,
            'name':'Shani',
            'friend': [shukra, budha],
            'nuetral': [guru],
            'enemy': [surya, chandra, mangala]
            },
    rahu: {'id':8,
           'name':'Rahu',
           'friend': [],
           'nuetral': [],
           'enemy': []
           },
    ketu: {'id':9,
           'name':'Ketu',
           'friend': [],
           'nuetral': [],
           'enemy': []
           }
}

grahas_temporary_relations = {
    2: 'friend',
    3: 'friend',
    4: 'friend',
    5: 'enemy',
    6: 'enemy',
    7: 'enemy',
    8: 'enemy',
    9: 'enemy',
    10: 'friend',
    11: 'friend',
    12: 'friend',
}

graha_rashi_ownership = {
    surya: [simha],
    chandra: [karka],
    budha: [mithuna, kanya],
    shukra: [vrishabha, tula],
    mangala: [mesha, vrishchika],
    guru: [dhanu, meena],
    shani: [makara, kumbha],
    rahu: [],
    ketu: []
}

graha_exaltation_properties = {
    surya: { 'exaltation_rashi': mesha,
             'deep-exaltation-degree': 10,
             'exaltation-results': ['learned', 'religious', 'strong', 'placid', 'charitable'],
             },
    chandra: {'exaltation_rashi': vrishabha,
             'deep-exaltation-degree': 3,
             'exaltation-results': ['rich', 'sedulous', 'a man of letters'],
            },
    budha: {'exaltation_rashi': kanya,
             'deep-exaltation-degree': 15,
             'exaltation-results': ['learned', 'cheerful', 'fortunate', 'respected'],
            },
    shukra: {'exaltation_rashi': meena,
             'deep-exaltation-degree': 27,
             'exaltation-results': ['charitable', 'lives to a good old age', 'many qualities']
            },
    mangala: {'exaltation_rashi': makara,
             'deep-exaltation-degree': 28,
             'exaltation-results': ['possesing great fervour', 'educated', 'famous', 'princely'],
            },
    guru: {'exaltation_rashi': karka,
             'deep-exaltation-degree': 5,
             'exaltation-results': ['cheif of men', 'strong', 'respected', 'given to anger', 'supporting a large number of men']
            },
    shani: {'exaltation_rashi': tula,
             'deep-exaltation-degree': 20,
             'exaltation-results': ['skillful', 'charitable', 'opluence', 'long life', 'lovind hushband']
            },
    rahu: {'exaltation_rashi': vrishabha,
             'deep-exaltation-degree': 20,
             'exaltation-results': ['wealthy']
            },
    ketu: {'exaltation_rashi': vrishchika,
             'deep-exaltation-degree': 20,
             'exaltation-results': ['wealthy']
            }
}


# Debilitation or depression points are found by adding 180 degrees
# to the maximum points exalation degrees
# While in a state of fall, planets gives results contrary to exaltation
graha_debilitation_properties = {
    surya: { 'debilitation_rashi': tula,
             'deep-debilitation-degree': 10,
             'debilitation-results': ['learned', 'religious', 'strong', 'placid', 'charitable'],
             },
    chandra: {'debilitation_rashi': vrishchika,
             'deep-debilitation-degree': 3,
             'debilitation-results': ['rich', 'sedulous', 'a man of letters'],
            },
    budha: {'debilitation_rashi': meena,
             'deep-debilitation-degree': 15,
             'debilitation-results': ['learned', 'cheerful', 'fortunate', 'respected'],
            },
    shukra: {'exaltation_rashi': kanya,
             'deep-exaltation-degree': 27,
             'debilitation-results': ['charitable', 'lives to a good old age', 'many qualities']
            },
    mangala: {'exaltation_rashi': karka,
             'deep-exaltation-degree': 28,
             'debilitation-results': ['possesing great fervour', 'educated', 'famous', 'princely'],
            },
    guru: {'exaltation_rashi': makara,
             'deep-exaltation-degree': 5,
             'debilitation-results': ['cheif of men', 'strong', 'respected', 'given to anger', 'supporting a large number of men']
            },
    shani: {'debilitation_rashi': mesha,
             'deep-debilitation-degree': 20,
             'debilitation-results': ['skillful', 'charitable', 'opluence', 'long life', 'lovind hushband']
            },
    rahu: {'debilitation_rashi': vrishchika,
             'deep-debilitation-degree': 20,
             'debilitation-results': ['wealthy']
            },
    ketu: {'debilitation_rashi': vrishabha,
             'deep-debilitation-degree': 20,
             'debilitation-results': ['wealthy']
            }
}

# Moolatrikona points are found by adding 90 degrees
# to the maximum points exalation degrees
# and has similar effects as exaltation
graha_moolatrikona_properties = {
    surya: { 'moolatrikona_rashi': mesha,
             'deep-moolatrikona-degree': 10,
             'exaltation-results': ['learned', 'religious', 'strong', 'placid', 'charitable'],
             },
    chandra: {'exaltation_rashi': vrishabha,
             'deep-exaltation-degree': 3,
             'exaltation-results': ['rich', 'sedulous', 'a man of letters'],
            },
    budha: {'exaltation_rashi': kanya,
             'deep-exaltation-degree': 15,
             'exaltation-results': ['learned', 'cheerful', 'fortunate', 'respected'],
            },
    shukra: {'exaltation_rashi': meena,
             'deep-exaltation-degree': 27,
             'exaltation-results': ['charitable', 'lives to a good old age', 'many qualities']
            },
    mangala: {'exaltation_rashi': makara,
             'deep-exaltation-degree': 28,
             'exaltation-results': ['possesing great fervour', 'educated', 'famous', 'princely'],
            },
    guru: {'exaltation_rashi': karka,
             'deep-exaltation-degree': 5,
             'exaltation-results': ['cheif of men', 'strong', 'respected', 'given to anger', 'supporting a large number of men']
            },
    shani: {'exaltation_rashi': tula,
             'deep-exaltation-degree': 20,
             'exaltation-results': ['skillful', 'charitable', 'opluence', 'long life', 'lovind hushband']
            },
    rahu: {'exaltation_rashi': vrishabha,
             'deep-exaltation-degree': 20,
             'exaltation-results': ['wealthy']
            },
    ketu: {'exaltation_rashi': vrishchika,
             'deep-exaltation-degree': 20,
             'exaltation-results': ['wealthy']
            }
}

def get_permanent_relation(src_graha, dest_graha):
    frnds = grahas_permanent_relations[src_graha]['friend']
    for frnd in frnds:
        if (frnd == dest_graha):
            return friend

    nutrls = grahas_permanent_relations[src_graha]['nuetral']
    for nutrl in nutrls:
        if (nutrl == dest_graha):
            return nuetral

    enms = grahas_permanent_relations[src_graha]['nuetral']
    for enm in enms:
        if (enm == dest_graha):
            return enemy

def get_temporary_relation(dest_graha_relative_house_no):
    return grahas_temporary_relations[dest_graha_relative_house_no]

def get_mixed_relation(perm_relation, temp_relation):
    if (perm_relation == 'friend' & temp_relation == 'friend'):
        return intimate_friend

    if (perm_relation == 'friend' & temp_relation == 'nuetral'):
        return friend

    if (perm_relation == 'friend' & temp_relation == 'enemy'):
        return nuetral

    if (perm_relation == 'nuetral' & temp_relation == 'friend'):
        return friend

    if (perm_relation == 'nuetral' & temp_relation == 'neutral'):
        return nuetral

    if (perm_relation == 'nuetral' & temp_relation == 'enemy'):
        return enemy

    if (perm_relation == 'enemy' & temp_relation == 'friend'):
        return nuetral

    if (perm_relation == 'enemy' & temp_relation == 'nuetral'):
        return enemy

    if (perm_relation == 'enemy' & temp_relation == 'enenmy'):
        return bitter_enemy









