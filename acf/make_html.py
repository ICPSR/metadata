from lxml import etree

# Paths to your files
xml_file = 'C:/ACF/FINAL APPROVED STATE RECORDS/Tennessee/tennessee_20250219.xml'
xsl_file = 'C:/icpsr_github/metadata/acf/statetemplatev5_edit.xsl'
output_html = 'C:/ACF/FINAL APPROVED STATE RECORDS/Tennessee/tennessee_20250410.html'

# Parse the XML and XSL files
xml_doc = etree.parse(xml_file)
xsl_doc = etree.parse(xsl_file)

# Create an XSLT transformer
transform = etree.XSLT(xsl_doc)

# Apply the transformation
result_tree = transform(xml_doc)

# Save the result to an HTML file
with open(output_html, 'wb') as f:
    f.write(etree.tostring(result_tree, pretty_print=True, method="html"))
