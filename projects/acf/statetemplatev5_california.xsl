<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" indent="yes"/>

    <xsl:template name="render-related-header">
      <xsl:param name="context"/>

      <!-- subPart -->
      <xsl:if test="$context/part/subPart">
        <xsl:variable name="subPart" select="$context/part/subPart"/>
        <xsl:value-of select="$context/ancestor::record/subPartName"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="$subPart/number"/>
        <xsl:text> (</xsl:text>
        <a href="{$subPart/source}">
          <xsl:value-of select="$subPart/name"/>
        </a>
        <xsl:text>)</xsl:text>
      </xsl:if>

      <!-- part -->
      <xsl:if test="$context/part and not($context/part/subPart)">
        <xsl:variable name="part" select="$context/part"/>
        <xsl:variable name="label">
          <xsl:choose>
            <xsl:when test="$part/altName">
              <xsl:value-of select="$part/altName"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$context/ancestor::record/partName"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <xsl:value-of select="$label"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="$part/number"/>
        <xsl:text> (</xsl:text>
        <a href="{$part/source}">
          <xsl:value-of select="$part/name"/>
        </a>
        <xsl:text>)</xsl:text>
      </xsl:if>

      <!-- article -->
      <xsl:if test="$context/self::article and not($context/part) and not($context/subPart)">
        <xsl:variable name="label">
          <xsl:choose>
            <xsl:when test="$context/altName">
              <xsl:value-of select="$context/altName"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$context/ancestor::record/articleName"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <xsl:value-of select="$label"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="$context/number"/>
        <xsl:text> (</xsl:text>
        <a href="{$context/source}">
          <xsl:value-of select="$context/name"/>
        </a>
        <xsl:text>)</xsl:text>
      </xsl:if>

      <!-- subtitle -->
      <xsl:if test="$context/subtitle and not($context/self::article) and not($context/part) and not($context/subPart)">
        <xsl:variable name="label">
          <xsl:choose>
            <xsl:when test="$context/subtitle/altName">
              <xsl:value-of select="$context/subtitle/altName"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="$context/ancestor::record/subtitleName"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:variable>
        <xsl:value-of select="$label"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="$context/subtitle/number"/>
        <xsl:text> (</xsl:text>
        <a href="{$context/subtitle/source}">
          <xsl:value-of select="$context/subtitle/name"/>
        </a>
        <xsl:text>)</xsl:text>
      </xsl:if>

      <!-- title fallback -->
      <xsl:if test="not($context/subtitle) and not($context/self::article) and not($context/part) and not($context/subPart)">
        <xsl:value-of select="$context/ancestor::record/titleName"/>
        <xsl:text> </xsl:text>
        <xsl:value-of select="$context/ancestor::title/number"/>
        <xsl:text> (</xsl:text>
        <a href="{$context/ancestor::title/source}">
          <xsl:value-of select="$context/ancestor::title/name"/>
        </a>
        <xsl:text>)</xsl:text>
      </xsl:if>
    </xsl:template>


    <xsl:template match="/record">

        <xsl:variable name="title_name" select="titleName"/>
        <xsl:variable name="article_name" select="articleName"/>

        <html>
            <head>
                <title>
                    <xsl:value-of select="state"/>
                </title>
                <style>
                    table,
                    th,
                    td {
                        border: 1px solid black;
                        border-collapse: collapse;
                        padding-left: 10px;
                        padding-right: 10px;
                        padding-top: 10px;
                        padding-bottom: 5px;
                    }
                    .doublespace {
                        margin: 20px 0;
                    }
                    body {
                        font-family: "Times New Roman", Times, serif;
                    }
            </style>
            </head>
            <body>
                <table style="width:100%; border:1px solid black;">
                     <xsl:apply-templates select="category/title | title"/>
                </table>
            </body>
        </html>

    </xsl:template>

    <xsl:template match="title">

        <xsl:variable name="categoryName" select="ancestor::category/name"/>
        <xsl:variable name="categorySource" select="ancestor::category/source"/>
        <xsl:variable name="titleSource" select="source"/>

        <tr style="background-color: #EEECE1;">
            <th/>
            <th>

            <!-- Include category name with hyperlink if it exists -->
            <xsl:if test="$categoryName">
                <xsl:if test="$categorySource">
                    <a href="{$categorySource}">
                        <xsl:value-of select="$categoryName"/>
                    </a>
                </xsl:if>
                <xsl:if test="not($categorySource)">
                    <xsl:value-of select="$categoryName"/>
                </xsl:if>
                <br/>
                <br/>   
            </xsl:if>

            <!-- Title details with hyperlink -->
            <xsl:value-of select="ancestor-or-self::*/titleName"/>
            <xsl:text> </xsl:text>
            <xsl:value-of select="number"/>
            <br/> 
            <xsl:element name="a">
                <xsl:attribute name="href">
                    <xsl:value-of select="$titleSource"/>
                </xsl:attribute>
                <xsl:value-of select="name"/>
            </xsl:element>
            </th>
            <td>
                <br/>
                <!-- ACF offices associated, it creates a section on the bullet list for each office and sorts it alphabetically. -->
                <b><u>ACF Offices Associated</u></b>
                <br/>
                <ul>
                    <xsl:for-each select="officesAssociated/office">
                        <li>
                          <xsl:value-of select="."/>
                        </li>
                    </xsl:for-each>
                </ul>
            </td>
        </tr>

        <!-- Now that it has made a title header, it will create a row in the table for each article. -->
        <xsl:for-each select="article | titleContent">

            <!-- Set variables for later use -->
            <xsl:variable name="titleNumber">
                <xsl:value-of select="ancestor::record/titleName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="ancestor::title/number"/>
            </xsl:variable>

            <xsl:variable name="titleLink">
                <xsl:element name="a">
                    <xsl:attribute name="href">
                        <xsl:value-of select="ancestor::title/source"/>
                    </xsl:attribute>
                    <xsl:value-of select="ancestor::title/name"/>
                </xsl:element>
            </xsl:variable>

            <xsl:variable name="articleNumber">
                <xsl:value-of select="ancestor::record/articleName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="number"/>
            </xsl:variable>

            <xsl:variable name="alt_articleNumber">
                <xsl:value-of select="altName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="number"/>
            </xsl:variable>

            <xsl:variable name="articleLink">
                <xsl:element name="a">
                    <xsl:attribute name="href">
                        <xsl:value-of select="source"/>
                    </xsl:attribute>
                    <xsl:value-of select="name"/>
                </xsl:element>
            </xsl:variable>

            <xsl:variable name="subtitleNumber">
                <xsl:value-of select="ancestor::record/subtitleName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="subtitle/number"/>
            </xsl:variable>

            <xsl:variable name="alt_subtitleNumber">
                <xsl:value-of select="subtitle/altName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="subtitle/number"/>
            </xsl:variable>


            <xsl:variable name="subtitleLink">
                <xsl:element name="a">
                    <xsl:attribute name="href">
                    <xsl:value-of select="subtitle/source"/>
                    </xsl:attribute>
                    <xsl:value-of select="subtitle/name"/>
                </xsl:element>
            </xsl:variable>

            <!-- NOTE: will assign two variables to account for variation in 'part' labels -->
            <xsl:variable name="alt_partNumber">
                <xsl:value-of select="part/altName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="part/number"/>
            </xsl:variable>

            <xsl:variable name="partNumber">
                <xsl:value-of select="ancestor::record/partName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="part/number"/>
            </xsl:variable>

            <xsl:variable name="partLink">
                <xsl:element name="a">
                    <xsl:attribute name="href">
                    <xsl:value-of select="part/source"/>
                    </xsl:attribute>
                    <xsl:value-of select="part/name"/>
                </xsl:element>
            </xsl:variable>

            <xsl:variable name="subPartNumber">
                <xsl:value-of select="ancestor::record/subPartName"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="part/subPart/number"/>
            </xsl:variable>

            <xsl:variable name="subPartLink">
                <xsl:element name="a">
                    <xsl:attribute name="href">
                    <xsl:value-of select="part/subPart/source"/>
                    </xsl:attribute>
                    <xsl:value-of select="part/subPart/name"/>
                </xsl:element>
            </xsl:variable>

            <tr valign="top">
                <xsl:attribute name="style">
                    <xsl:choose>
                        <xsl:when test="domain = 'Medical Assistance'">
                            <xsl:text>background-color: #B8CCE4;</xsl:text>
                        </xsl:when>
                        <xsl:when test="domain = 'Public Records'">
                            <xsl:text>background-color: #FFC000;</xsl:text>
                        </xsl:when>
                        <xsl:when test="domain = 'Child Welfare Services'">
                            <xsl:text>background-color: #FFFFCC;</xsl:text>
                        </xsl:when>
                        <xsl:when test="domain = 'Public Assistance'">
                            <xsl:text>background-color: #FFCCFF;</xsl:text>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:text>background-color: white;</xsl:text>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:attribute>
                <td>
                    <b>Domain</b>
                    <br/>
                    <xsl:value-of select="domain"/>
                    <br/>
                    <br/>

                    <!-- Title details -->
                    <b>
                    <xsl:value-of select="$titleNumber"/>
                    </b>
                    <br/> 
                    <xsl:copy-of select="$titleLink"/>
                    <br/>
                    <br/>

                    <!-- Subtitle details, if present -->
                    <xsl:if test="subtitle/number">
                      <b>
                        <xsl:choose>
                          <xsl:when test="subtitle/altName">
                            <xsl:value-of select="$alt_subtitleNumber"/>
                          </xsl:when>
                          <xsl:otherwise>
                            <xsl:value-of select="$subtitleNumber"/>
                          </xsl:otherwise>
                        </xsl:choose>
                      </b>
                      <br/>
                      <xsl:copy-of select="$subtitleLink"/>
                      <br/>
                      <br/>
                    </xsl:if>

                    <!-- Article details, if present -->
                    <xsl:if test="number and name and source">
                      <b>
                        <xsl:choose>
                          <xsl:when test="altName">
                            <xsl:value-of select="$alt_articleNumber"/>
                          </xsl:when>
                          <xsl:otherwise>
                            <xsl:value-of select="$articleNumber"/>
                          </xsl:otherwise>
                        </xsl:choose>
                      </b>
                      <br/>
                      <xsl:copy-of select="$articleLink"/>
                      <br/>
                      <br/>
                    </xsl:if>

                    <!-- Part details, if present -->
                    <xsl:if test="part/number">
                      <b>
                        <xsl:choose>
                          <xsl:when test="part/altName">
                            <xsl:value-of select="$alt_partNumber"/>
                          </xsl:when>
                          <xsl:otherwise>
                            <xsl:value-of select="$partNumber"/>
                          </xsl:otherwise>
                        </xsl:choose>
                      </b>
                      <br/>
                      <xsl:copy-of select="$partLink"/>
                      <br/>
                      <br/>
                    </xsl:if>

                    <!-- Subpart details, if present -->
                    <xsl:if test="part/subPart/number">
                      <b>
                        <xsl:value-of select="$subPartNumber"/>
                      </b>
                      <br/>
                      <xsl:copy-of select="$subPartLink"/>
                      <br/>
                      <br/>
                    </xsl:if>

                    <!-- Bullet point list for associatedFederal -->
                    <b><u>Associated Federal Records</u></b>
                    <ul>
                        <xsl:for-each
                          select="associatedFederalRecords/federal">
                          <li>
                          <xsl:value-of select="."/>
                          </li>
                        </xsl:for-each>
                    </ul>
                </td>

                <!-- Main content of articles. -->
                <td colspan="2">

                <!-- Start by checking if there are definitions. Note that section headings will change if we are working with titleContent vs. article -->
                <xsl:if test="definitions">
                    <b>Definitions related to
                      <xsl:call-template name="render-related-header">
                        <xsl:with-param name="context" select="."/>
                      </xsl:call-template>
                    </b>
                    <!-- Now present each statute and associated defined terms -->
                    <ul>
                        <xsl:for-each select="definitions/statute">
                            <li>
                                <xsl:element name="a">
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="source"/>
                                    </xsl:attribute>
                                    <xsl:value-of select="stateCode"/>
                                </xsl:element>
                                <xsl:text> – </xsl:text>
                                <!-- All defined terms, comma separated. -->
                                <xsl:for-each select="definedTerms/definedTerm">
                                    <xsl:value-of select="."/>
                                    <xsl:if test="position() != last()">, </xsl:if>
                                </xsl:for-each>
                            </li>
                        </xsl:for-each>
                    </ul>
                </xsl:if>  

                <!-- Now check if there are requirements. -->
                <xsl:if test="requirements">
                    <b>Requirements related to
                      <xsl:call-template name="render-related-header">
                        <xsl:with-param name="context" select="."/>
                      </xsl:call-template>
                    </b>
                    <!-- For each statute, grab label, state code, description.-->
                    <ul>
                    <xsl:for-each select="requirements/statute">
                        <li class="doublespace">
                            <b>
                            <xsl:value-of select="label"/>
                            </b>
                            <xsl:if test="description">
                                <xsl:text> – </xsl:text>
                                <xsl:value-of select="description"/>
                            </xsl:if>
                            <xsl:text> (</xsl:text>
                            <xsl:element name="a">
                                <xsl:attribute name="href">
                                    <xsl:value-of select="source"/>
                                </xsl:attribute>
                                <xsl:value-of select="stateCode"/>
                            </xsl:element>
                            <!-- This checks if for some reason there is a second stateCode. This happens extremely rarely, but this allows both to be rendered in the HTML. -->
                            <xsl:if test="altCode">
                                <xsl:text>; </xsl:text>
                                <xsl:element name="a">
                                    <xsl:attribute name="href">
                                        <xsl:value-of select="altSource"/>
                                    </xsl:attribute>
                                    <xsl:value-of select="altCode"/>
                                </xsl:element>
                            </xsl:if>
                            <xsl:text>)</xsl:text>
                            <ul>
                                <!-- Who Law Applies To -->
                                <li>
                                    <b>Who Law Applies To:</b>
                                    <xsl:text> </xsl:text>
                                    <xsl:for-each select="appliesTo/entity">
                                        <xsl:value-of select="."/>
                                        <xsl:if test="position() != last()">; </xsl:if>
                                    </xsl:for-each>
                                </li>
                                <!-- Tags -->
                                <li>
                                    <b>Tag(s):</b>
                                    <xsl:text> </xsl:text>
                                    <xsl:for-each select="terms/term">
                                        <xsl:value-of select="."/>
                                        <xsl:if test="position() != last()">; </xsl:if>
                                    </xsl:for-each>
                                </li>
                            </ul>
                        </li>
                    </xsl:for-each>
                    </ul>
                </xsl:if>
                </td>
            </tr>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>