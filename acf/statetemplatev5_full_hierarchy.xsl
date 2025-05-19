<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" indent="yes"/>

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

                    <!-- NOTE: the following fields will only be present if the node is an 'article', not 'titleContent' -->
                    <xsl:if test="self::article">

                        <!-- Subtitle details, if present -->
                        <xsl:if test="subtitle">
                            <b>
                            <xsl:value-of select="$subtitleNumber"/>
                            </b>
                            <br/>
                            <xsl:copy-of select="$subtitleLink"/>
                            <br/>
                            <br/>
                        </xsl:if>

                        <!-- Article details -->
                        <b>
                        <xsl:value-of select="$articleNumber"/>
                        </b>
                        <br/>
                        <xsl:copy-of select="$articleLink"/>
                        <br/>
                        <br/>

                        <!-- Part details, if present -->
                        <xsl:if test="part">
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
                        <xsl:if test="part/subPart">
                            <b>
                            <xsl:value-of select="$subPartNumber"/>
                            </b>
                            <br/>
                            <xsl:copy-of select="$subPartLink"/>
                            <br/>
                            <br/>
                        </xsl:if>
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
                      <xsl:choose>
                        <!-- Only show Title info if we're in a titleContent context -->
                        <xsl:when test="self::titleContent">
                          <xsl:value-of select="ancestor::record/titleName"/>
                          <xsl:text> </xsl:text>
                          <xsl:value-of select="ancestor::title/number"/>
                          <xsl:if test="ancestor::title/source">
                            <xsl:text> (</xsl:text>
                            <a href="{ancestor::title/source}">
                              <xsl:value-of select="ancestor::title/name"/>
                            </a>
                            <xsl:text>)</xsl:text>
                          </xsl:if>
                        

                          <xsl:if test="subtitle/number">
                            <xsl:value-of select="ancestor::record/subtitleName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="subtitle/number"/>
                            <xsl:if test="subtitle/source">
                              <xsl:text> (</xsl:text>
                              <a href="{subtitle/source}">
                                <xsl:value-of select="subtitle/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>
                        </xsl:when>

                        <!-- Otherwise, build up Article, Part, SubPart in order -->
                        <xsl:otherwise>

                          <!-- Subtitle (optional) -->
                          <xsl:if test="subtitle/number">
                            <xsl:value-of select="ancestor::record/subtitleName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="subtitle/number"/>
                            <xsl:if test="subtitle/source">
                              <xsl:text> (</xsl:text>
                              <a href="{subtitle/source}">
                                <xsl:value-of select="subtitle/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>

                          <!-- Article -->
                          <xsl:if test="number and self::article">
                            <xsl:value-of select="ancestor::record/articleName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="number"/>
                            <xsl:if test="source">
                              <xsl:text> (</xsl:text>
                              <a href="{source}">
                                <xsl:value-of select="name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>

                          <!-- Part -->
                          <xsl:if test="part/number">
                            <xsl:choose>
                              <xsl:when test="part/altName">
                                <xsl:value-of select="part/altName"/>
                              </xsl:when>
                              <xsl:otherwise>
                                <xsl:value-of select="ancestor::record/partName"/>
                              </xsl:otherwise>
                            </xsl:choose>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="part/number"/>
                            <xsl:if test="part/source">
                              <xsl:text> (</xsl:text>
                              <a href="{part/source}">
                                <xsl:value-of select="part/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>

                          <!-- SubPart -->
                          <xsl:if test="part/subPart/number">
                            <xsl:value-of select="ancestor::record/subPartName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="part/subPart/number"/>
                            <xsl:if test="part/subPart/source">
                              <xsl:text> (</xsl:text>
                              <a href="{part/subPart/source}">
                                <xsl:value-of select="part/subPart/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                          </xsl:if>

                        </xsl:otherwise>
                      </xsl:choose>
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
                      <xsl:choose>
                        <!-- Only show Title info if we're in a titleContent context -->
                        <xsl:when test="self::titleContent">
                          <xsl:value-of select="ancestor::record/titleName"/>
                          <xsl:text> </xsl:text>
                          <xsl:value-of select="ancestor::title/number"/>
                          <xsl:if test="ancestor::title/source">
                            <xsl:text> (</xsl:text>
                            <a href="{ancestor::title/source}">
                              <xsl:value-of select="ancestor::title/name"/>
                            </a>
                            <xsl:text>)</xsl:text>
                          </xsl:if>
                        </xsl:when>
                        <xsl:if test="subtitle/number">
                            <xsl:value-of select="ancestor::record/subtitleName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="subtitle/number"/>
                            <xsl:if test="subtitle/source">
                              <xsl:text> (</xsl:text>
                              <a href="{subtitle/source}">
                                <xsl:value-of select="subtitle/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>

                        <!-- Otherwise, build up Article, Part, SubPart in order -->
                        <xsl:otherwise>

                          <!-- Subtitle (optional) -->
                          <xsl:if test="subtitle/number">
                            <xsl:value-of select="ancestor::record/subtitleName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="subtitle/number"/>
                            <xsl:if test="subtitle/source">
                              <xsl:text> (</xsl:text>
                              <a href="{subtitle/source}">
                                <xsl:value-of select="subtitle/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>  
                          
                          <!-- Article -->
                          <xsl:if test="number and self::article">
                            <xsl:value-of select="ancestor::record/articleName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="number"/>
                            <xsl:if test="source">
                              <xsl:text> (</xsl:text>
                              <a href="{source}">
                                <xsl:value-of select="name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>

                          <!-- Part -->
                          <xsl:if test="part/number">
                            <xsl:choose>
                              <xsl:when test="part/altName">
                                <xsl:value-of select="part/altName"/>
                              </xsl:when>
                              <xsl:otherwise>
                                <xsl:value-of select="ancestor::record/partName"/>
                              </xsl:otherwise>
                            </xsl:choose>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="part/number"/>
                            <xsl:if test="part/source">
                              <xsl:text> (</xsl:text>
                              <a href="{part/source}">
                                <xsl:value-of select="part/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                            <xsl:text> </xsl:text>
                          </xsl:if>

                          <!-- SubPart -->
                          <xsl:if test="part/subPart/number">
                            <xsl:value-of select="ancestor::record/subPartName"/>
                            <xsl:text> </xsl:text>
                            <xsl:value-of select="part/subPart/number"/>
                            <xsl:if test="part/subPart/source">
                              <xsl:text> (</xsl:text>
                              <a href="{part/subPart/source}">
                                <xsl:value-of select="part/subPart/name"/>
                              </a>
                              <xsl:text>)</xsl:text>
                            </xsl:if>
                          </xsl:if>

                        </xsl:otherwise>
                      </xsl:choose>
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