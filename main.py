#coding utf-8

import sqlite3
from lxml import etree
def add_from_xml_to_sql(xml, nom_bdd, table) :
    """Parse le XML et rajoute les données à la table"""


def export_from_sql_to_xml(nom_bdd, table, nom_xml) :
    """exporte la table en xml"""
    # Création du fichier xml

    #
    bdd = sqlite3.connect(nom_bdd)
    cursor = bdd.cursor()
    cursor.execute("""SELECT * FROM friends""")
    ListeLignes = cursor.fetchall()
    print(ListeLignes)
    xml_nom_table = etree.Element(table)

    for Ligne in ListeLignes :
        friend = etree.SubElement(xml_nom_table, "friend")
        firstname = etree.SubElement(friend, "firstName")
        firstname.text = "{}".format(Ligne[0])
        surname = etree.SubElement(friend,"surname")
        surname.text = "{}".format(Ligne[1])
        age = etree.SubElement(friend, "age")
        age.text = "{}".format(Ligne[2])

    with open(nom_xml, 'w') as f :
        f.write('{}'.format(etree.tostring(xml_nom_table, encoding="unicode", pretty_print=True)))

    print(etree.tostring(xml_nom_table, encoding="unicode", pretty_print = True))

export_from_sql_to_xml('tables.db', 'friendList', 'output.xml')