from lxml import etree

# Load your bespoke XML
xml_path = "C:/icpsr_github/metadata/ddi/input/DDIWorkingPaper05.xml"  # Path to your XML file
xsl_path = "C:/icpsr_github/metadata/ddi/ddi_to_datacite.xsl"  # Path to your XSLT file
output_path = "C:/icpsr_github/metadata/ddi/output/DDIWorkingPaper05.xml"

try:
    # Parse the XML and XSLT
    xml_tree = etree.parse(xml_path)
    xslt_tree = etree.parse(xsl_path)

    # Create an XSLT transformer
    transform = etree.XSLT(xslt_tree)

    # Apply transformation
    datacite_xml = transform(xml_tree)

    # Save the transformed DataCite XML
    with open(output_path, "wb") as f:
        f.write(etree.tostring(datacite_xml, pretty_print=True, xml_declaration=True, encoding="UTF-8"))

    print(f"Transformed DataCite XML saved to: {output_path}")

except:
    print('Check paths in variables -- may need adjusting...')