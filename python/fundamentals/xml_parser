import xml.etree.ElementTree

#Place the config.xml in the same directory
def execute_test_case():
    xml_root = xml.etree.ElementTree.parse('config.xml').getroot()
    for sw in xml_root.findall('switch_info'):
        switch = Switch(sw.get('ipaddr'),
                        sw.get('console'),
                        sw.get('switch_type'),
                        6)
                        
execute_test_case()
