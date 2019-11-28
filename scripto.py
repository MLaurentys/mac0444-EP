import re

treco = {}

name = "baseFiles/filmes.pl"
with open( name) as file :
    for line in file :
        if (line.startswith("filme(")) :
            words = line[6:]
            words = re.split( ', |\.|\n|\\)', words)
            treco[words[0]] ="""<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
    <lançamento rdf:datatype="http://www.w3.org/2001/XMLSchema#int">{}</lançamento>""".format(words[0], words[1])


        elif (line.startswith("tit_dur(")) :
            words = line[8:]
            words = re.split( ', |\.|\n|\\)', words)
            duration = """
    <duration rdf:datatype="http://www.w3.org/2001/XMLSchema#int">{}</duration>""".format(words[2])
            name = """
    <name rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{}</name>""".format(words[1])
            treco[words[0]] = treco[words[0]] + duration + name


        elif (line.startswith("diretor(")) :
            words = line[8:]
            words = re.split( ', |\.|\n|\\)', words)

            dirigidoPor = """
    <dirigidoPor rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1])
            treco[words[0]] = treco[words[0]] + dirigidoPor

            if (treco.get(words[1]) is None) :
                treco[words[1]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"> 
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor"/>
    <dirige rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1], words[0])
            else :
                dirige = """
    <dirige rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
                treco[words[1]] = treco[words[1]] + dirige


        elif (line.startswith("atriz(")) :
            words = line[6:]
            words = re.split( ', |\.|\n|\\)', words)

            if (treco.get(words[1]) is None) :
                treco[words[1]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atriz"/>
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1], words[2], words[0])
            else :
                atuaComo = """
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2])
                atuaNo = """
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
                treco[words[1]] = treco[words[1]] + atuaComo + atuaNo
            
            treco[words[2]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
    <atuadoPor rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>
    <apareceNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2], words[1], words[0])

            temAtores = """
    <temAtores rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1])
            temPersonagem = """
    <temPersonagem rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2])
            treco[words[0]] = treco[words[0]] + temAtores + temPersonagem


        elif (line.startswith("ator(")) :
            words = line[5:]
            words = re.split( ', |\.|\n|\\)', words)

            if (treco.get(words[1]) is None) :
                treco[words[1]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Ator"/>
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1], words[2], words[0])
            else :
                atuaComo = """
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2])
                atuaNo = """
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
                treco[words[1]] = treco[words[1]] + atuaComo + atuaNo
            
            treco[words[2]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
    <atuadoPor rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2], words[1])



        elif (line.startswith("nome(")) :
            words = line[5:]
            words = re.split( ', |\.|\n|\\)', words)
            firstNameLastName = """
    <foaf:firstName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{}</foaf:firstName>
    <foaf:lastName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{}</foaf:lastName>""".format(words[1], words[2])
            treco[words[0]] = treco[words[0]] + firstNameLastName


output = "BrenoJiangMatheusVictor_OntologiaMAC0444.owl"
with open( output, mode='a') as file :
    for i in treco.values() :
        i = i + """
</owl:NamedIndividual>
"""
        file.write(i)

