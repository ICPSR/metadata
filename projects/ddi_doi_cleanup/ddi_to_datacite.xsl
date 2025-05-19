<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns="http://datacite.org/schema/kernel-4"
                xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4.3/metadata.xsd">

    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="/resource">
        <resource xsi:schemaLocation="http://datacite.org/schema/kernel-4 https://schema.datacite.org/meta/kernel-4.3/metadata.xsd" xmlns="http://datacite.org/schema/kernel-4" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <identifier identifierType="DOI">
                <xsl:value-of select="doiProposal"/>
            </identifier>

            <creators>
                <xsl:for-each select="creators/creator/person">
                    <creator>
                        <creatorName nameType="Personal">
                            <xsl:value-of select="concat(normalize-space(lastName), ', ', normalize-space(firstName))"/>
                        </creatorName>
                        <givenName><xsl:value-of select="normalize-space(firstName)"/></givenName>
                        <familyName><xsl:value-of select="normalize-space(lastName)"/></familyName>
                        <xsl:if test="affiliation">
                            <affiliation><xsl:value-of select="normalize-space(affiliation/affiliationName/name)"/></affiliation>
                        </xsl:if>
                    </creator>
                </xsl:for-each>
            </creators>

            <titles>
                <title>
                    <xsl:if test="language">
                        <xsl:attribute name="xml:lang">
                            <xsl:value-of select="normalize-space(language)"/>
                        </xsl:attribute>
                    </xsl:if>
                    <xsl:value-of select="normalize-space(titles/title/titleName)"/>
                </title>
            </titles>

            <publisher xml:lang="en" publisherIdentifier="https://ror.org/015em2733" publisherIdentifierScheme="ROR" schemeURI="https://ror.org/">Data Documentation Initiative Alliance</publisher>

            <publicationYear>
                <xsl:value-of select="substring(publicationDate/date, 1, 4)"/>
            </publicationYear>

            <resourceType resourceTypeGeneral="Report">Working paper</resourceType>

            <rightsList>
                <rights xml:lang="en">
                    <xsl:value-of select="normalize-space(availability/availabilityFree/availabilityText)"/>
                </rights>
            </rightsList>
        </resource>
    </xsl:template>

</xsl:stylesheet>
