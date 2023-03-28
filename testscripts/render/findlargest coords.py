xml_file ="C:/Users/harve/Downloads/MCI Women's Files/g2312135_SecondSpectrum_tracking-produced.xml"

import xml.etree.ElementTree as ET

def get_largest_coordinates(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')

    # Iterate through all elements with a 'loc' attribute
    for element in root.iter():
        if 'loc' in element.attrib:
            loc = element.get('loc')
            try:
                x, y, z = [float(coord) for coord in loc.strip().split(',')]
                max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)
            except ValueError:
                pass

    return max_x, max_y, max_z

max_x, max_y, max_z = get_largest_coordinates(xml_file)
print(f"Largest X: {max_x}")
print(f"Largest Y: {max_y}")
print(f"Largest Z: {max_z}")
