# Jednoduchy konverter
#
#
# import xml.etree.ElementTree as Et
#
#
# def simple_xml_to_txt(xml_file, txt_file):
#     tree = Et.parse(xml_file)
#     root = tree.getroot()
#
#     with open(txt_file, 'w', encoding='utf-8') as f:
#         for element in root:
#             line = []
#             for child in element:
#                 if child.text:
#                     line.append(child.text.strip())
#             f.write(';'.join(line) + '\n')
#
#
# if __name__ == "__main__":
#     simple_xml_to_txt('invoices.xml', 'vystup.txt')
#     print("Konverzia hotová!")



# --------------------------------------------------------------
# Univerzalnejsi skript

import xml.etree.ElementTree as ET

def parse_element(element):
    """Získa texty zo všetkých children."""
    data = []
    for child in element:
        if list(child):  # ak má children, pokračujeme hlbšie
            data.extend(parse_element(child))
        else:
            if child.text:
                data.append(child.text.strip())
            else:
                data.append('')  # ak text nie je, vložíme prázdno
    return data


def xml_to_txt_universal(xml_file, txt_file, delimiter=';'):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(txt_file, 'w', encoding='utf-8') as f:
        for item in root:
            line_data = parse_element(item)
            f.write(delimiter.join(line_data) + '\n')


if __name__ == "__main__":
    xml_to_txt_universal('invoices.xml', 'vystup_univesal.txt', delimiter=';')
    print("Univerzálna konverzia xml-txt dokončená!")
