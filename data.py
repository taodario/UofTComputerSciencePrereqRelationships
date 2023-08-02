raw = """{
    "CSC104H1": {
        "title": "Computational Thinking",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC108H1": {
        "title": "Introduction to Computer Programming",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC110Y1": {
        "title": "Foundations of Computer Science I",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC111H1": {
        "title": "Foundations of Computer Science II",
        "raw": "CSC110Y1",
        "full": "CSC110Y1",
        "first": [
            "CSC110Y1"
        ]
    },
    "CSC148H1": {
        "title": "Introduction to Computer Science",
        "raw": "CSC108H1",
        "full": "CSC108H1",
        "first": [
            "CSC108H1"
        ]
    },
    "CSC165H1": {
        "title": "Mathematical Expression and Reasoning for Computer Science",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC196H1": {
        "title": "Great Ideas in Computing",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC197H1": {
        "title": "What, Who, How: Privacy in the Age of Big Data Collection",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC199H1": {
        "title": "Intelligence, Artificial and Human",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC207H1": {
        "title": "Software Design",
        "raw": "CSC148H1/CSC111H1",
        "full": "OR(CSC148H1,CSC111H1)",
        "first": [
            "CSC148H1"
        ]
    },
    "CSC209H1": {
        "title": "Software Tools and Systems Programming",
        "raw": "CSC207H1/  CSC207H5/  CSCB07H3",
        "full": "OR(CSC207H1,OR(CSC207H5,CSCB07H3))",
        "first": [
            "CSC207H1"
        ]
    },
    "CSC236H1": {
        "title": "Introduction to the Theory of Computation",
        "raw": "(CSC148H1, CSC165H1) / CSC111H1",
        "full": "OR(AND(CSC148H1,CSC165H1),CSC111H1)",
        "first": [
            "CSC148H1",
            "CSC165H1"
        ]
    },
    "CSC240H1": {
        "title": "Enriched Introduction to the Theory of Computation",
        "raw": "CSC110Y1 / CSC165H1",
        "full": "OR(CSC110Y1,CSC165H1)",
        "first": [
            "CSC110Y1"
        ]
    },
    "JCC250H1": {
        "title": "Computing for Science ",
        "raw": "CHM135H1/ CHM136H1/ CHM151Y1",
        "full": "OR(OR(CHM135H1,CHM136H1),CHM151Y1)",
        "first": [
            "CHM135H1"
        ]
    },
    "CSC258H1": {
        "title": "Computer Organization",
        "raw": "((CSC148H1/CSC148H5/CSCA48H3), (CSC165H1/ CSC240H1/ MAT102H5/ MATA67H3/CSCA67H3)) / CSC111H1",
        "full": "OR(AND(OR(OR(CSC148H1,CSC148H5),CSCA48H3),OR(CSC165H1,OR(OR(CSC240H1,MAT102H5),OR(MATA67H3,CSCA67H3)))),CSC111H1)",
        "first": [
            "CSC148H1",
            "CSC165H1"
        ]
    },
    "CSC263H1": {
        "title": "Data Structures and Analysis",
        "raw": "CSC236H1/  CSC240H1/  CSC236H5/  CSCB36H3/  APS105H1/  APS106H1/  ESC180H1;  STA237H1/  STA247H1/  STA255H1/  STA257H1/  STAB57H3/  STAB52H3/  ECE302H1/  STA286H1/  CHE223H1/  CME263H1/  MIE231H1/  MIE236H1/  MSE238H1/  ECE286H1",
        "full": "AND(OR(OR(CSC236H1,OR(CSC240H1,OR(OR(CSC236H5,CSCB36H3),APS105H1))),OR(APS106H1,ESC180H1)),OR(OR(STA237H1,OR(OR(OR(OR(STA247H1,OR(STA255H1,STA257H1)),STAB57H3),OR(STAB52H3,ECE302H1)),OR(STA286H1,CHE223H1))),OR(CME263H1,OR(OR(MIE231H1,MIE236H1),OR(MSE238H1,ECE286H1)))))",
        "first": [
            "CSC236H1",
            "STA237H1"
        ]
    },
    "CSC265H1": {
        "title": "Enriched Data Structures and Analysis",
        "raw": "CSC240H1/ ( CSC236H1 ,  MAT377H1/  STA237H1/  STA247H1/  STA255H1/  STA257H1)",
        "full": "OR(CSC240H1,AND(CSC236H1,OR(MAT377H1,OR(STA237H1,OR(OR(STA247H1,STA255H1),STA257H1)))))",
        "first": [
            "CSC240H1"
        ]
    },
    "JSC270H1": {
        "title": "Data Science I",
        "raw": "STA257H1,  CSC207H1",
        "full": "AND(STA257H1,CSC207H1)",
        "first": [
            "STA257H1",
            "CSC207H1"
        ]
    },
    "CSC299H1": {
        "title": "Research Opportunity Program",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC299Y1": {
        "title": "Research Opportunity Program",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC300H1": {
        "title": "Computers and Society",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC301H1": {
        "title": "Introduction to Software Engineering",
        "raw": "CSC209H1,  CSC263H1/ CSC265H1",
        "full": "AND(CSC209H1,OR(CSC263H1,CSC265H1))",
        "first": [
            "CSC209H1",
            "CSC263H1"
        ]
    },
    "CSC302H1": {
        "title": "Engineering Large Software Systems",
        "raw": "CSC301H1",
        "full": "CSC301H1",
        "first": [
            "CSC301H1"
        ]
    },
    "CSC303H1": {
        "title": "Social and Information Networks",
        "raw": "CSC263H1/  CSC265H1/  CSC263H5/  CSCB63H3,  STA247H1/  STA255H1/  STA257H1/  ECO227Y1/  STA237H1/  STAB52H3/  STAB57H3,  MAT223H1/  MAT240H1",
        "full": "AND(OR(CSC263H1,OR(CSC265H1,OR(CSC263H5,CSCB63H3))),AND(OR(OR(OR(OR(STA247H1,STA255H1),STA257H1),OR(OR(ECO227Y1,STA237H1),STAB52H3)),STAB57H3),OR(MAT223H1,MAT240H1)))",
        "first": [
            "CSC263H1",
            "STA247H1",
            "MAT223H1"
        ]
    },
    "CSC304H1": {
        "title": "Algorithmic Game Theory and Mechanism Design",
        "raw": "STA247H1/  STA255H1/  STA257H1/  STA237H1/  PSY201H1/  ECO227Y1, ( MAT135H1,  MAT136H1)/  MAT137Y1/  MAT157Y1",
        "full": "AND(OR(OR(STA247H1,OR(STA255H1,STA257H1)),OR(OR(STA237H1,PSY201H1),ECO227Y1)),OR(AND(MAT135H1,MAT136H1),OR(MAT137Y1,MAT157Y1)))",
        "first": [
            "STA247H1",
            "MAT135H1",
            "MAT136H1"
        ]
    },
    "CSC309H1": {
        "title": "Programming on the Web",
        "raw": "CSC209H1/  CSC209H5/  CSCB09H3/ ESC180H1/ ESC190H1/  CSC190H1/ (APS105H1, ECE244H1)",
        "full": "OR(OR(CSC209H1,OR(CSC209H5,CSCB09H3)),OR(OR(OR(ESC180H1,ESC190H1),CSC190H1),AND(APS105H1,ECE244H1)))",
        "first": [
            "CSC209H1"
        ]
    },
    "CSC310H1": {
        "title": "Information Theory",
        "raw": "CSC148H1,  CSC263H1/  CSC265H1,  MAT223H1/  MAT240H1",
        "full": "AND(AND(CSC148H1,OR(CSC263H1,CSC265H1)),OR(MAT223H1,MAT240H1))",
        "first": [
            "CSC148H1",
            "CSC263H1",
            "MAT223H1"
        ]
    },
    "CSC311H1": {
        "title": "Introduction to Machine Learning",
        "raw": "CSC207H1/ APS105H1/ APS106H1/ ESC180H1/  CSC180H1;  MAT235Y1/  MAT237Y1/  MAT257Y1/ (MAT137Y1)/ (MAT157Y1)/ MAT291H1/ MAT294H1/ (MAT186H1, MAT187H1)/ (MAT194H1,  MAT195H1)/ (ESC194H1, ESC195H1);  MAT223H1/  MAT240H1/ MAT185H1/ MAT188H1;  STA237H1/  STA247H1/  STA255H1/  STA257H1/  STA286H1/ CHE223H1/ CME263H1/ MIE231H1/ MIE236H1/ MSE238H1/ ECE286H1",
        "full": "AND(AND(OR(OR(OR(CSC207H1,APS105H1),OR(APS106H1,ESC180H1)),CSC180H1),OR(OR(MAT235Y1,MAT237Y1),OR(OR(OR(MAT257Y1,MAT137Y1),MAT157Y1),OR(MAT291H1,OR(OR(OR(MAT294H1,AND(MAT186H1,MAT187H1)),AND(MAT194H1,MAT195H1)),AND(ESC194H1,ESC195H1)))))),AND(OR(OR(MAT223H1,MAT240H1),OR(MAT185H1,MAT188H1)),OR(OR(OR(OR(STA237H1,OR(STA247H1,STA255H1)),OR(STA257H1,OR(STA286H1,CHE223H1))),OR(CME263H1,OR(MIE231H1,MIE236H1))),OR(MSE238H1,ECE286H1))))",
        "first": [
            "CSC207H1",
            "MAT235Y1",
            "MAT223H1",
            "STA237H1"
        ]
    },
    "CSC317H1": {
        "title": "Computer Graphics",
        "raw": "MAT235Y1/  MAT237Y1/  MAT257Y1/ MAT291H1/ MAT292H1/ MAT294H1/ ( MAT232H5/  MAT233H5,  MAT236H5)/ ( MATB41H3,  MATB42H3);  MAT223H1/  MAT240H1/  MAT223H5/  MATA22H3/ MAT185H1/ MAT188H1;  CSC209H1/  CSC209H5/  CSCB09H3/ APS105H1/ ESC180H1/  CSC180H1",
        "full": "AND(AND(OR(MAT235Y1,OR(OR(MAT237Y1,MAT257Y1),OR(OR(OR(OR(MAT291H1,MAT292H1),MAT294H1),AND(OR(MAT232H5,MAT233H5),MAT236H5)),AND(MATB41H3,MATB42H3)))),OR(OR(MAT223H1,MAT240H1),OR(OR(MAT223H5,MATA22H3),OR(MAT185H1,MAT188H1)))),OR(OR(OR(OR(CSC209H1,CSC209H5),CSCB09H3),OR(APS105H1,ESC180H1)),CSC180H1))",
        "first": [
            "MAT235Y1",
            "MAT223H1",
            "CSC209H1"
        ]
    },
    "CSC318H1": {
        "title": "The Design of Interactive Computational Media",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC320H1": {
        "title": "Introduction to Visual Computing",
        "raw": "CSC209H1/ ( CSC207H1)/  CSC209H5/  CSCB09H3/ ESC190H1/ ECE244H1;  MAT223H1/  MAT240H1/  MAT185H1/ MAT188H1, ( MAT136H1)/ ( MAT137Y1)/ (MAT157Y1)/  MAT235Y1/  MAT237Y1/  MAT257Y1/ MAT291H1/ MAT292H1",
        "full": "AND(AND(OR(OR(OR(OR(CSC209H1,CSC207H1),CSC209H5),OR(CSCB09H3,ESC190H1)),ECE244H1),OR(OR(MAT223H1,OR(MAT240H1,MAT185H1)),MAT188H1)),OR(OR(MAT136H1,OR(OR(MAT137Y1,MAT157Y1),OR(OR(MAT235Y1,MAT237Y1),MAT257Y1))),OR(MAT291H1,MAT292H1)))",
        "first": [
            "CSC209H1",
            "MAT223H1",
            "MAT136H1"
        ]
    },
    "CSC324H1": {
        "title": "Principles of Programming Languages",
        "raw": "CSC263H1/ CSC265H1",
        "full": "OR(CSC263H1,CSC265H1)",
        "first": [
            "CSC263H1"
        ]
    },
    "CSC336H1": {
        "title": "Numerical Methods",
        "raw": "CSC148H1/  CSC111H1;  MAT133Y1/ ( MAT135H1,  MAT136H1)/  MAT135Y1/  MAT137Y1/  MAT157Y1,  MAT223H1/  MAT240H1",
        "full": "AND(AND(OR(CSC148H1,CSC111H1),OR(OR(OR(MAT133Y1,OR(AND(MAT135H1,MAT136H1),MAT135Y1)),MAT137Y1),MAT157Y1)),OR(MAT223H1,MAT240H1))",
        "first": [
            "CSC148H1",
            "MAT133Y1",
            "MAT223H1"
        ]
    },
    "CSC343H1": {
        "title": "Introduction to Databases",
        "raw": "CSC111H1/  CSC165H1/  CSC240H1/ ( MAT135H1,  MAT136H1)/  MAT135Y1/  MAT137Y1/  MAT157Y1/ (MAT186H1, MAT187H1)/ ( MAT194H1,  MAT195H1)/ (ESC194H1, ESC195H1);  CSC207H1/  CSC207H5/  CSCB07H3/ ECE345H1/ ESC190H1",
        "full": "AND(OR(OR(OR(CSC111H1,OR(CSC165H1,CSC240H1)),OR(AND(MAT135H1,MAT136H1),OR(MAT135Y1,MAT137Y1))),OR(MAT157Y1,OR(OR(AND(MAT186H1,MAT187H1),AND(MAT194H1,MAT195H1)),AND(ESC194H1,ESC195H1)))),OR(OR(CSC207H1,OR(OR(CSC207H5,CSCB07H3),ECE345H1)),ESC190H1))",
        "first": [
            "CSC111H1",
            "CSC207H1"
        ]
    },
    "CSC367H1": {
        "title": "Parallel Programming",
        "raw": "CSC258H1/  CSC258H5/  CSCB58H3;  CSC209H1/  CSC209H5/  CSCB09H3",
        "full": "AND(OR(CSC258H1,OR(CSC258H5,CSCB58H3)),OR(OR(CSC209H1,CSC209H5),CSCB09H3))",
        "first": [
            "CSC258H1",
            "CSC209H1"
        ]
    },
    "CSC369H1": {
        "title": "Operating Systems",
        "raw": "CSC209H1/  CSC209H5/  CSCB09H3;  CSC258H1/  CSC258H5/  CSCB58H3",
        "full": "AND(OR(CSC209H1,OR(CSC209H5,CSCB09H3)),OR(OR(CSC258H1,CSC258H5),CSCB58H3))",
        "first": [
            "CSC209H1",
            "CSC258H1"
        ]
    },
    "JSC370H1": {
        "title": "Data Science II",
        "raw": "JSC270H1,  STA261H1,  MAT237Y1/  MAT257Y1,  CSC263H1/  CSC265H1/  CSC263H5/  CSCB63H3,  STA302H1,  CSC343H1/  CSC343H5/  CSCC43H3",
        "full": "AND(AND(JSC270H1,STA261H1),AND(OR(MAT237Y1,MAT257Y1),AND(OR(OR(OR(CSC263H1,CSC265H1),CSC263H5),CSCB63H3),AND(STA302H1,OR(OR(CSC343H1,CSC343H5),CSCC43H3)))))",
        "first": [
            "JSC270H1",
            "STA261H1",
            "MAT237Y1",
            "CSC263H1",
            "STA302H1",
            "CSC343H1"
        ]
    },
    "CSC373H1": {
        "title": "Algorithm Design, Analysis & Complexity",
        "raw": "CSC263H1/  CSC265H1 /  CSC263H5/  CSCB63H3",
        "full": "OR(OR(OR(CSC263H1,CSC265H1),CSC263H5),CSCB63H3)",
        "first": [
            "CSC263H1"
        ]
    },
    "CSC384H1": {
        "title": "Introduction to Artificial Intelligence",
        "raw": "( CSC263H1/  CSC265H1/  CSC263H5/  CSCB63H3/ ECE345H1/ ECE358H1/  MIE245H1/ ( CSC148H1, ASMAJ1446A),  STA220H1/  STA237H1/  STA247H1/  STA255H1/  STA257H1/  STAB57H3/  STAB52H3/ ECE302H1/  STA286H1/ CHE223H1/ CME263H1/ MIE231H1/ MIE236H1/ MSE238H1/ ECE286H1/  PSY201H1)",
        "full": "AND(OR(OR(OR(OR(CSC263H1,CSC265H1),CSC263H5),OR(OR(CSCB63H3,ECE345H1),ECE358H1)),OR(MIE245H1,AND(CSC148H1,ASMAJ1446A))),OR(OR(STA220H1,OR(OR(STA237H1,STA247H1),STA255H1)),OR(OR(OR(STA257H1,STAB57H3),OR(STAB52H3,ECE302H1)),OR(OR(OR(STA286H1,CHE223H1),CME263H1),OR(MIE231H1,OR(OR(MIE236H1,MSE238H1),OR(ECE286H1,PSY201H1)))))))",
        "first": [
            "CSC263H1",
            "STA220H1"
        ]
    },
    "CSC385H1": {
        "title": "Microprocessor Systems",
        "raw": "CSC258H1;  CSC209H1",
        "full": "AND(CSC258H1,CSC209H1)",
        "first": [
            "CSC258H1",
            "CSC209H1"
        ]
    },
    "CSC396Y0": {
        "title": "Designing Systems for Real World Problems",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC398H0": {
        "title": "Research Excursions",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC398Y0": {
        "title": "Research Excursions",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC399H1": {
        "title": "Research Opportunity Program",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC399Y1": {
        "title": "Research Opportunity Program",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC401H1": {
        "title": "Natural Language Computing",
        "raw": "CSC207H1/  CSC209H1/  CSC207H5/  CSCB07H3/  CSC209H5/  CSCB09H3/ APS105H1/ APS106H1/ ESC180H1/  CSC180H1;  STA237H1/  STA247H1/  STA255H1/  STA257H1/  STAB57H3/  STAB52H3/ ECE302H1/  STA286H1/ CHE223H1/ CME263H1/ MIE231H1/ MIE236H1/ MSE238H1/ ECE286H1",
        "full": "AND(OR(OR(CSC207H1,CSC209H1),OR(OR(CSC207H5,CSCB07H3),OR(OR(CSC209H5,CSCB09H3),OR(APS105H1,OR(APS106H1,OR(ESC180H1,CSC180H1)))))),OR(OR(OR(STA237H1,STA247H1),OR(OR(STA255H1,STA257H1),STAB57H3)),OR(OR(STAB52H3,OR(ECE302H1,STA286H1)),OR(OR(OR(OR(CHE223H1,CME263H1),MIE231H1),MIE236H1),OR(MSE238H1,ECE286H1)))))",
        "first": [
            "CSC207H1",
            "STA237H1"
        ]
    },
    "CSC404H1": {
        "title": "Introduction to Video Game Design",
        "raw": "CSC301H1/  CSC317H1/  CSC318H1/  CSC384H1/  CSC417H1/  CSC418H1/  CSC419H1",
        "full": "OR(OR(CSC301H1,OR(CSC317H1,OR(OR(CSC318H1,CSC384H1),CSC417H1))),OR(CSC418H1,CSC419H1))",
        "first": [
            "CSC301H1"
        ]
    },
    "CSC410H1": {
        "title": "Software Testing and Verification",
        "raw": "CSC207H1,  CSC236H1/ CSC240H1",
        "full": "AND(CSC207H1,OR(CSC236H1,CSC240H1))",
        "first": [
            "CSC207H1",
            "CSC236H1"
        ]
    },
    "CSC412H1": {
        "title": "Probabilistic Learning and Reasoning",
        "raw": "CSC311H1/  CSC411H1/  STA314H1/ ECE421H1/ ROB313H1/  CSCC11H3/  CSC311H5",
        "full": "OR(OR(CSC311H1,OR(CSC411H1,STA314H1)),OR(OR(ECE421H1,ROB313H1),OR(CSCC11H3,CSC311H5)))",
        "first": [
            "CSC311H1"
        ]
    },
    "CSC413H1": {
        "title": "Neural Networks and Deep Learning",
        "raw": "CSC311H1/  CSC311H5/  CSCC11H3/  CSC411H1/  STA314H1/ ECE421H1/ ROB313H1;  MAT235Y1/  MAT237Y1/  MAT257Y1/  MAT257Y5/  MAT291H1/  MAT294H1/ AER210H1/ ( MAT232H5,  MAT236H5)/ ( MAT233H5,  MAT236H5)/ ( MATB41H3,  MATB42H3);  MAT223H1/  MAT240H1/ MAT185H1/ MAT188H1/  MAT223H5/  MATA23H3",
        "full": "AND(AND(OR(OR(CSC311H1,OR(CSC311H5,CSCC11H3)),OR(OR(CSC411H1,STA314H1),OR(ECE421H1,ROB313H1))),OR(OR(OR(MAT235Y1,OR(MAT237Y1,MAT257Y1)),OR(MAT257Y5,OR(OR(MAT291H1,MAT294H1),AER210H1))),OR(OR(AND(MAT232H5,MAT236H5),AND(MAT233H5,MAT236H5)),AND(MATB41H3,MATB42H3)))),OR(OR(OR(MAT223H1,OR(MAT240H1,MAT185H1)),MAT188H1),OR(MAT223H5,MATA23H3)))",
        "first": [
            "CSC311H1",
            "MAT235Y1",
            "MAT223H1"
        ]
    },
    "CSC417H1": {
        "title": "Physics-Based Animation",
        "raw": "MAT235Y1/  MAT237Y1/  MAT257Y1/  MAT291H1/ MAT294H1;  MAT223H1/  MAT240H1/ MAT185H1/ MAT188H1;  CSC209H1/ APS105H1/ ESC180H1/  CSC180H1",
        "full": "AND(OR(OR(MAT235Y1,OR(MAT237Y1,MAT257Y1)),OR(MAT291H1,MAT294H1)),AND(OR(MAT223H1,OR(MAT240H1,OR(MAT185H1,MAT188H1))),OR(OR(CSC209H1,OR(APS105H1,ESC180H1)),CSC180H1)))",
        "first": [
            "MAT235Y1",
            "MAT223H1",
            "CSC209H1"
        ]
    },
    "CSC419H1": {
        "title": "Geometry Processing",
        "raw": "MAT235Y1/  MAT237Y1/  MAT257Y1/ MAT291H1/ MAT294H1;  MAT223H1/  MAT240H1/ MAT185H1/ MAT188H1;  CSC209H1/ APS105H1/ ESC180H1/  CSC180H1",
        "full": "AND(OR(MAT235Y1,OR(OR(MAT237Y1,OR(MAT257Y1,MAT291H1)),MAT294H1)),AND(OR(OR(MAT223H1,MAT240H1),OR(MAT185H1,MAT188H1)),OR(CSC209H1,OR(OR(APS105H1,ESC180H1),CSC180H1))))",
        "first": [
            "MAT235Y1",
            "MAT223H1",
            "CSC209H1"
        ]
    },
    "CSC420H1": {
        "title": "Introduction to Image Understanding",
        "raw": "CSC263H1/  CSC265H1/ ECE345H1/ ECE358H1/ MIE335H1; ( MAT135H1,  MAT136H1)/  MAT137Y1/  MAT157Y1/ (MAT186H1, MAT187H1)/ ( MAT194H1,  MAT195H1)/ (ESC194H1, ESC195H1);  MAT223H1/  MAT240H1/ MAT185H1/ MAT188H1",
        "full": "AND(AND(OR(CSC263H1,OR(CSC265H1,OR(ECE345H1,OR(ECE358H1,MIE335H1)))),OR(OR(AND(MAT135H1,MAT136H1),OR(OR(OR(MAT137Y1,MAT157Y1),AND(MAT186H1,MAT187H1)),AND(MAT194H1,MAT195H1))),AND(ESC194H1,ESC195H1))),OR(OR(MAT223H1,MAT240H1),OR(MAT185H1,MAT188H1)))",
        "first": [
            "CSC263H1",
            "MAT135H1",
            "MAT136H1",
            "MAT223H1"
        ]
    },
    "CSC428H1": {
        "title": "Human-Computer Interaction",
        "raw": "CSC318H1;  STA237H1/  STA247H1/  STA255H1/  STA257H1/ ECE302H1/  STA286H1/ CHE223H1/ CME263H1/ MIE231H1/ MIE236H1/ MSE238H1/ ECE286H1;  CSC209H1/ APS105H1/ ESC180H1/  CSC180H1",
        "full": "AND(CSC318H1,AND(OR(OR(OR(STA237H1,OR(STA247H1,STA255H1)),OR(STA257H1,OR(OR(ECE302H1,STA286H1),OR(OR(CHE223H1,CME263H1),OR(MIE231H1,MIE236H1))))),OR(MSE238H1,ECE286H1)),OR(OR(CSC209H1,APS105H1),OR(ESC180H1,CSC180H1))))",
        "first": [
            "CSC318H1",
            "STA237H1",
            "CSC209H1"
        ]
    },
    "CSC436H1": {
        "title": "Numerical Algorithms",
        "raw": "CSC336H1/ CSC350H1",
        "full": "OR(CSC336H1,CSC350H1)",
        "first": [
            "CSC336H1"
        ]
    },
    "CSC438H1": {
        "title": "Computability and Logic",
        "raw": "( CSC363H1/  CSC463H1)/  CSC365H1/  CSC373H1/  CSC375H1/  MAT247H1",
        "full": "OR(OR(OR(CSC363H1,CSC463H1),CSC365H1),OR(CSC373H1,OR(CSC375H1,MAT247H1)))",
        "first": [
            "CSC363H1"
        ]
    },
    "CSC443H1": {
        "title": "Database System Technology",
        "raw": "CSC343H1,  CSC369H1,  CSC373H1/ CSC375H1",
        "full": "AND(AND(CSC343H1,CSC369H1),OR(CSC373H1,CSC375H1))",
        "first": [
            "CSC343H1",
            "CSC369H1",
            "CSC373H1"
        ]
    },
    "CSC446H1": {
        "title": "Computational Methods for Partial Differential Equations",
        "raw": "CSC351H1/  CSC336H1;  MAT237Y1/  MAT257Y1;  APM346H1/  MAT351Y1/ (MAT244H1/  MAT267H1)",
        "full": "AND(AND(OR(CSC351H1,CSC336H1),OR(MAT237Y1,MAT257Y1)),OR(APM346H1,OR(MAT351Y1,OR(MAT244H1,MAT267H1))))",
        "first": [
            "CSC351H1",
            "MAT237Y1",
            "APM346H1"
        ]
    },
    "CSC448H1": {
        "title": "Formal Languages and Automata",
        "raw": "CSC236H1/ CSC240H1,  CSC263H1/ CSC265H1",
        "full": "AND(OR(CSC236H1,CSC240H1),OR(CSC263H1,CSC265H1))",
        "first": [
            "CSC236H1",
            "CSC263H1"
        ]
    },
    "CSC454H1": {
        "title": "The Business of Software",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC456H1": {
        "title": "High-Performance Scientific Computing",
        "raw": "CSC436H1/  CSC336H1;  CSC209H1",
        "full": "AND(OR(CSC436H1,CSC336H1),CSC209H1)",
        "first": [
            "CSC436H1",
            "CSC209H1"
        ]
    },
    "CSC457H1": {
        "title": "Principles of Computer Networks",
        "raw": "CSC373H1/  CSC373H5/  CSCC73H3,  STA247H1/  STA255H1/  STA257H1/  STA237H1",
        "full": "AND(OR(CSC373H1,OR(CSC373H5,CSCC73H3)),OR(OR(STA247H1,STA255H1),OR(STA257H1,STA237H1)))",
        "first": [
            "CSC373H1",
            "STA247H1"
        ]
    },
    "CSC458H1": {
        "title": "Computer Networking Systems",
        "raw": "CSC209H1,  CSC258H1,  CSC263H1/  CSC265H1,  STA247H1/  STA255H1/  STA257H1/  STA237H1/  ECO227Y1",
        "full": "AND(AND(CSC209H1,AND(CSC258H1,OR(CSC263H1,CSC265H1))),OR(STA247H1,OR(OR(STA255H1,STA257H1),OR(STA237H1,ECO227Y1))))",
        "first": [
            "CSC209H1",
            "CSC258H1",
            "CSC263H1",
            "STA247H1"
        ]
    },
    "CSC463H1": {
        "title": "Computational Complexity and Computability",
        "raw": "CSC236H1/  CSC240H1/  CSC236H5/  CSCB36H3",
        "full": "OR(CSC236H1,OR(CSC240H1,OR(CSC236H5,CSCB36H3)))",
        "first": [
            "CSC236H1"
        ]
    },
    "CSC465H1": {
        "title": "Formal Methods in Software Design",
        "raw": "CSC236H1/  CSC240H1/  MAT309H1/  CSC236H5/  CSCB36H3",
        "full": "OR(CSC236H1,OR(CSC240H1,OR(OR(MAT309H1,CSC236H5),CSCB36H3)))",
        "first": [
            "CSC236H1"
        ]
    },
    "CSC466H1": {
        "title": "Numerical Methods for Optimization Problems",
        "raw": "CSC336H1,  MAT223H1/  MAT240H1,  MAT235Y1/  MAT237Y1/  MAT257Y1",
        "full": "AND(AND(CSC336H1,OR(MAT223H1,MAT240H1)),OR(OR(MAT235Y1,MAT237Y1),MAT257Y1))",
        "first": [
            "CSC336H1",
            "MAT223H1",
            "MAT235Y1"
        ]
    },
    "CSC469H1": {
        "title": "Operating Systems Design and Implementation",
        "raw": "CSC369H1",
        "full": "CSC369H1",
        "first": [
            "CSC369H1"
        ]
    },
    "JSC470H1": {
        "title": "Data Science III",
        "raw": "JSC370H1,  STA314H1/ CSC411H1/ CSC311H1,  STA303H1/ STA305H1",
        "full": "AND(AND(JSC370H1,OR(OR(STA314H1,CSC411H1),CSC311H1)),OR(STA303H1,STA305H1))",
        "first": [
            "JSC370H1",
            "STA314H1",
            "STA303H1"
        ]
    },
    "CSC473H1": {
        "title": "Advanced Algorithm Design",
        "raw": "CSC373H1,  MAT223H1/  MAT240H1",
        "full": "AND(CSC373H1,OR(MAT223H1,MAT240H1))",
        "first": [
            "CSC373H1",
            "MAT223H1"
        ]
    },
    "CSC485H1": {
        "title": "Computational Linguistics",
        "raw": "CSC209H1/ APS105H1/ APS106H1/ ESC180H1/  CSC180H1;  STA237H1/  STA247H1/  STA255H1/  STA257H1/ ECE302H1/  STA286H1/ CHE223H1/ CME263H1/ MIE231H1/ MIE236H1/ MSE238H1/ ECE286H1",
        "full": "AND(OR(OR(OR(CSC209H1,APS105H1),OR(APS106H1,ESC180H1)),CSC180H1),OR(OR(OR(OR(STA237H1,STA247H1),OR(STA255H1,STA257H1)),ECE302H1),OR(OR(OR(STA286H1,CHE223H1),CME263H1),OR(OR(MIE231H1,OR(MIE236H1,MSE238H1)),ECE286H1))))",
        "first": [
            "CSC209H1",
            "STA237H1"
        ]
    },
    "CSC486H1": {
        "title": "Knowledge Representation and Reasoning",
        "raw": "CSC384H1/  CSC384H5/ ROB311H1",
        "full": "OR(OR(CSC384H1,CSC384H5),ROB311H1)",
        "first": [
            "CSC384H1"
        ]
    },
    "CSC488H1": {
        "title": "Compilers and Interpreters",
        "raw": "CSC258H1/  CSC258H5/  CSCB58H3,  CSC324H1/  CSC324H5/  CSCC24H3,  CSC263H1/  CSC265H1/  CSC263H5/  CSCB63H3",
        "full": "AND(OR(CSC258H1,OR(CSC258H5,CSCB58H3)),AND(OR(OR(CSC324H1,CSC324H5),CSCC24H3),OR(OR(CSC263H1,CSC265H1),OR(CSC263H5,CSCB63H3))))",
        "first": [
            "CSC258H1",
            "CSC324H1",
            "CSC263H1"
        ]
    },
    "CSC490H1": {
        "title": "Capstone Design Project",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC491H1": {
        "title": "Capstone Design Project",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC494H1": {
        "title": "Computer Science Project",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC494Y1": {
        "title": "Computer Science Project",
        "raw": "",
        "full": "",
        "first": []
    },
    "CSC495H1": {
        "title": "Computer Science Project",
        "raw": "CSC494H1",
        "full": "CSC494H1",
        "first": [
            "CSC494H1"
        ]
    }
}"""

