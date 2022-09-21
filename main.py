#coding utf-8

import sqlite3
from lxml import etree
def add_from_xml_to_sql(xml) :
    """Parse le XML et rajoute les données à la table"""
    tree = etree.parse(xml)
    requete = "INSERT INTO friends (firstName, surname, age) VALUES"
    for friend in tree.xpath("/friendList/friend") :
        requete += " ('" + friend.xpath("firstName")[0].text + "', '" + friend.xpath("surname")[0].text + "', " + friend.xpath("age")[0].text + "),"

    bdd = sqlite3.connect('tables.db')
    cursor = bdd.cursor()
    cursor.execute(requete[:-1])
    bdd.commit()
    print(requete[:-1])





def export_from_sql_to_xml(nom_bdd, table, nom_xml) :
    """exporte la table en xml"""
    bdd = sqlite3.connect(nom_bdd)
    cursor = bdd.cursor()
    cursor.execute("""SELECT * FROM friends""")
    ListeLignes = cursor.fetchall()
    #print(ListeLignes)

    #Création de l'arbre
    xml_nom_table = etree.Element(table)
    #Création des branches
    for Ligne in ListeLignes :
        friend = etree.SubElement(xml_nom_table, "friend")
        firstname = etree.SubElement(friend, "firstName")
        firstname.text = "{}".format(Ligne[0])
        surname = etree.SubElement(friend,"surname")
        surname.text = "{}".format(Ligne[1])
        age = etree.SubElement(friend, "age")
        age.text = "{}".format(Ligne[2])
    #Création du fichier XML
    with open(nom_xml, 'w') as f :
        f.write('{}'.format(etree.tostring(xml_nom_table, encoding="unicode", pretty_print=True)))

        nom_bdd.close()

    print(etree.tostring(xml_nom_table, encoding="unicode", pretty_print = True))

add_from_xml_to_sql('exemple.xml')
#export_from_sql_to_xml('tables.db', 'friendList', 'output.xml')