import re

FILE_HEAD = """<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#"
     xml:base="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep"
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:ns="http://www.w3.org/2003/06/sw-vocab-status/ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:wot="http://xmlns.com/wot/0.1/"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:foaf="http://xmlns.com/foaf/0.1/"
     xmlns:obda="https://w3id.org/obda/vocabulary#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:mac0444-ep="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#">
    <owl:Ontology rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep">
        <owl:imports rdf:resource="http://xmlns.com/foaf/0.1/"/>
    </owl:Ontology>
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Object Properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#apareceNo -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#apareceNo">
        <owl:inverseOf rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#temPersonagem"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuaComo -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuaComo">
        <owl:inverseOf rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuadoPor"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuaNo -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuaNo">
        <owl:inverseOf rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#temAtores"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuadoPor -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#atuadoPor">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#dirige -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#dirige">
        <rdfs:subPropertyOf rdf:resource="http://xmlns.com/foaf/0.1/made"/>
        <owl:inverseOf rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#dirigidoPor"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#dirigidoPor -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#dirigidoPor">
        <rdfs:subPropertyOf rdf:resource="http://xmlns.com/foaf/0.1/maker"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#temAtores -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#temAtores">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
    </owl:ObjectProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#temPersonagem -->

    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#temPersonagem">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
    </owl:ObjectProperty>
    


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Data properties
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    


    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#duration">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topDataProperty"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#int"/>
    </owl:DatatypeProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#lancamento -->

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#lancamento">
        <rdfs:domain rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#int"/>
    </owl:DatatypeProperty>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#name -->

    <owl:DatatypeProperty rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#name">
        <rdfs:domain rdf:resource="http://www.w3.org/2002/07/owl#Thing"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>


    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // Classes
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Ator -->

    <owl:Class rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Ator">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
        <owl:disjointWith rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atriz"/>
    </owl:Class>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores -->

    <owl:Class rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores">
        <rdfs:subClassOf rdf:resource="http://www.w3.org/2000/10/swap/pim/contact#Person"/>
    </owl:Class>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atriz -->

    <owl:Class rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atriz">
        <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
    </owl:Class>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor -->

    <owl:Class rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor">
        <rdfs:subClassOf rdf:resource="http://www.w3.org/2000/10/swap/pim/contact#Person"/>
    </owl:Class>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme -->

    <owl:Class rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme">
        <rdfs:subClassOf rdf:resource="http://xmlns.com/foaf/0.1/Project"/>
    </owl:Class>
    


    <!-- http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem -->

    <owl:Class rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem">
        <rdfs:subClassOf rdf:resource="http://www.w3.org/2000/10/swap/pim/contact#Person"/>
    </owl:Class>
    


"""
FILE_FOOT = """
    <!-- 
    ///////////////////////////////////////////////////////////////////////////////////////
    //
    // General axioms
    //
    ///////////////////////////////////////////////////////////////////////////////////////
     -->

    <rdf:Description>
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#AllDisjointClasses"/>
        <owl:members rdf:parseType="Collection">
            <rdf:Description rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atores"/>
            <rdf:Description rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor"/>
            <rdf:Description rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
        </owl:members>
    </rdf:Description>
</rdf:RDF>


<!-- Generated by the OWL API (version 4.5.9.2019-02-01T07:24:44Z) https://github.com/owlcs/owlapi -->

"""
# ATOR = 0
# ATRIZ = 1
# DIRETOR = 2
# FILME = 3
# PERSONAGEM = 4

# ids = [{}, {}, {}, {}, {}]
# counts = [0, 0, 0, 0, 0]


treco = {}
funcoes = {}

filmes = "baseFiles/filmes.pl"
with open(filmes) as file :
    for line in file :
        if (line.startswith("filme(")) :
            words = line[6:]
            words = re.split( ', |\.|\n|\\)', words)
            treco[words[0]] ="""<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Filme"/>
    <lancamento rdf:datatype="http://www.w3.org/2001/XMLSchema#int">{}</lancamento>""".format(words[0], words[1])


        elif (line.startswith("tit_dur(")) :
            words = line[8:]
            words = re.split( ', |\.|\n|\\)', words)
            duration = """
    <duration rdf:datatype="http://www.w3.org/2001/XMLSchema#int">{}</duration>""".format(words[2])
            name = """
    <name rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{}</name>""".format(words[1].replace("'", ""))
            treco[words[0]] = treco[words[0]] + duration + name


        elif (line.startswith("diretor(")) :
            words = line[8:]
            words = re.split( ', |\.|\n|\\)', words)
            dirigidoPor = """
    <dirigidoPor rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1])
            treco[words[0]] = treco[words[0]] + dirigidoPor
            if (treco.get(words[1]) is None) :
                funcoes[words[1]] = 2
                treco[words[1]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"> 
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor"/>
    <dirige rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1], words[0])
            else :  
                dirige = """
    <dirige rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
                if (funcoes.get(words[1]) == 1):
                    funcoes[words[1]] = 3
                    dirige += """\n   <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Diretor"/>"""
                treco[words[1]] = treco[words[1]] + dirige


        elif (line.startswith("atriz(")) :
            words = line[6:]
            words = re.split( ', |\.|\n|\\)', words)
            if(words[2] == "herself"): words[2] = words[1]
            if (treco.get(words[1]) is None) :
                funcoes[words[1]] = 1
                treco[words[1]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atriz"/>
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1], words[2] + "_p", words[0])
            else :
                atuaComo = """
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2] + "_p")
                atuaNo = """
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
                if(funcoes[words[1]] == 2):
                    funcoes[words[1]] = 3
                    atuaNo += """\n   <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Atriz"/>"""
                
                treco[words[1]] = treco[words[1]] + atuaComo + atuaNo
            
            if (treco.get(words[2] + "_p") is None):
                treco[words[2] + "_p"] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
    <atuadoPor rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>
    <apareceNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2] + "_p", words[1], words[0])
            else: treco[words[2] + "_p"] += """<apareceNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
            temAtores = """
    <temAtores rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1])
            temPersonagem = """
    <temPersonagem rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2] + "_p")
            treco[words[0]] = treco[words[0]] + temAtores + temPersonagem


        elif (line.startswith("ator(")) :
            words = line[5:]
            words = re.split( ', |\.|\n|\\)', words)
            if(words[2] == "himself"): words[2] = words[1]

            if (treco.get(words[1]) is None) :
                funcoes[words[1]] = 1
                treco[words[1]] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Ator"/>
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[1], words[2] + "_p", words[0])
            else :
                atuaComo = """
    <atuaComo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2] + "_p")
                atuaNo = """
    <atuaNo rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[0])
                if(funcoes[words[1]] == 2):
                    funcoes[words[1]] = 3
                    atuaNo += """\n   <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Ator"/>"""
                
                treco[words[1]] = treco[words[1]] + atuaComo + atuaNo
            
            treco[words[2] + "_p"] = """<owl:NamedIndividual rdf:about="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}">
    <rdf:type rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#Personagem"/>
    <atuadoPor rdf:resource="http://www.semanticweb.org/mtlaurentys/ontologies/2019/10/mac0444-ep#{}"/>""".format(words[2] + "_p", words[1])



        elif (line.startswith("nome(")) :
            words = line[5:]
            words = re.split( ', |\.|\n|\\)', words)
            firstNameLastName = """
    <foaf:firstName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{}</foaf:firstName>
    <foaf:lastName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{}</foaf:lastName>""".format(words[1].replace("'", ""), words[2].replace("'", ""))
            treco[words[0]] = treco[words[0]] + firstNameLastName


output = "treco.owl"
with open( output, mode='w+') as file :
    file.write(FILE_HEAD)
    for i in treco.values() :
        i = i + """
</owl:NamedIndividual>
"""
        file.write(i)
    file.write(FILE_FOOT)

