import streamlit as st

# Définition des QCM
# ------------------

# QCM 2022 (exemple complet avec quelques questions, complète avec tes 100 questions)
qcm2022 = [

# qcm2022.py
# ===========

    {
        "question": "1. Lors des jeux olympiques de 2024, les épreuves de surf devraient se dérouler à :",
        "options": {"A": "Lacanau", "B": "Tahiti", "C": "Hossegor", "D": "Biarritz"},
        "correct": "B"
    },
    {
        "question": "2. Dans quelle fiction rencontre-t-on des « marcheurs blancs » ?",
        "options": {"A": "Les Randonneurs", "B": "Blanche-Neige et les Sept Nains", "C": "Le Trône de fer", "D": "Star Treck"},
        "correct": "C"
    },
    {
        "question": "3. Que sont les fleurs de Bach ?",
        "options": {"A": "Des suites musicales", "B": "Des plantes typiques de la région de Leipzig", "C": "Des remèdes", "D": "Un recueil de poèmes"},
        "correct": "C"
    },
    {
        "question": "4. Qu'est-ce que le petit verdot ?",
        "options": {"A": "Un invertébré vermiforme", "B": "Une variété de raisin", "C": "Un objet hypothétique en astrophysique", "D": "Un personnage de « la guerre des boutons »"},
        "correct": "B"
    },
    {
        "question": "5. Le livre 'Le choc des civilisations' a été écrit par :",
        "options": {"A": "Samuel Huntington", "B": "Hiram Hutchinson", "C": "James Parkinson", "D": "Georges Huntington"},
        "correct": "A"
    },
    {
        "question": "6. La ville d'Hondschoote, intimement liée à l'histoire de la gendarmerie, est située :",
        "options": {"A": "en Picardie", "B": "en Artois", "C": "en Flandre maritime", "D": "en Flandre wallonne"},
        "correct": "C"
    },
    {
        "question": "7. La garbure est :",
        "options": {"A": "un ancien land d'Allemagne de l'Est", "B": "une spécialité culinaire", "C": "un élément chimique associé au tungstène", "D": "un poisson d'eau douce"},
        "correct": "B"
    },
    {
        "question": "8. Le duathlon est une combinaison de :",
        "options": {"A": "course à pied et de cyclisme", "B": "de ski de fond et de tir à la carabine", "C": "de golf et de croquet", "D": "de saut en longueur et de saut en hauteur"},
        "correct": "A"
    },
    {
        "question": "9. En 1965, l'écrivain américain Frank Herbert a écrit le roman Dune, adapté au cinéma en 1984 par David Lynch. Dans la distribution du film figurait le chanteur :",
        "options": {"A": "Bono", "B": "Sting", "C": "Freddy Mercury", "D": "The Edge"},
        "correct": "B"
    },
    {
        "question": "10. Compléter ce couplet de La Marseillaise : nous entrerons dans la carrière, quand nos aînés :",
        "options": {"A": "n'en seront pus", "B": "auront vécu", "C": "n'y seront plus", "D": "n'y verront plus"},
        "correct": "C"
    },
    {
        "question": "11. En France, les douanes sont rattachées au ministère chargé :",
        "options": {"A": "des Transports", "B": "de l'Écologie", "C": "du Budget", "D": "de l'Intérieur"},
        "correct": "C"
    },
    {
        "question": "12. Dans la formule funéraire « ci-gît », git est une forme conjuguée du verbe :",
        "options": {"A": "gîter", "B": "gésir", "C": "gémir", "D": "gêner"},
        "correct": "B"
    },
    {
        "question": "13. Lequel de ces verbes n'est pas transitif ?",
        "options": {"A": "Lire", "B": "Travailler", "C": "Éternuer", "D": "Rencontrer"},
        "correct": "C"
    },
    {
        "question": "14. Lequel de ces départements français n'est pas en Nouvelle-Aquitaine ?",
        "options": {"A": "Creuse", "B": "Cantal", "C": "Corrèze", "D": "Deux-Sèvres"},
        "correct": "B"
    },
    {
        "question": "15. Qui est à l'origine de la théorie sur l'origine des espèces ?",
        "options": {"A": "Rousseau", "B": "Darwin", "C": "Lorenz", "D": "Pavlov"},
        "correct": "B"
    },
    {
        "question": "16. Sur le terrain, quel est le nombre de joueurs d'une équipe de handball ?",
        "options": {"A": "6", "B": "7", "C": "5", "D": "8"},
        "correct": "B"
    },
    {
        "question": "17. Périclès était :",
        "options": {"A": "un roi spartiate", "B": "un homme politique athénien", "C": "un satrape perse", "D": "un célèbre marchand crétois d'eaux pétillantes"},
        "correct": "B"
    },
    {
        "question": "18. Quel fleuve français prend sa source sur le plateau de Langres ?",
        "options": {"A": "La Loire", "B": "Le Rhône", "C": "La Seine", "D": "La Garonne"},
        "correct": "C"
    },
    {
        "question": "19. Albert Uderzo est connu pour avoir dessiné :",
        "options": {"A": "Lucky Luke", "B": "Astérix", "C": "Spirou", "D": "Tintin"},
        "correct": "B"
    },
    {
        "question": "20. Un sonnet est une pièce de poésie de quatorze vers composée de :",
        "options": {"A": "deux quatrains et deux tercets", "B": "quatre quatrains et trois tercets", "C": "trois quatrains et quatre tercets", "D": "deux quatrains et un tercet"},
        "correct": "A"
    },
    {
        "question": "21. La chanson « voler de nuit » du chanteur français Calogero est consacrée à :",
        "options": {"A": "Charles Lindbergh", "B": "Antoine de Saint-Exupéry", "C": "Arsène Lupin", "D": "Amelia Earhart"},
        "correct": "B"
    },
    {
        "question": "22. Voltaire a écrit dans CANDIDE que le travail éloigne de nous trois grands maux :",
        "options": {"A": "l'ennui, le vice et le besoin", "B": "l'ennui, l'avarice et le besoin", "C": "l'ennui, le vice et la faim", "D": "l'énurésie, le vice et le besoin"},
        "correct": "A"
    },
    {
        "question": "23. David Vincent les a vus un soir où il cherchait sa route. Il s'agissait :",
        "options": {"A": "des visiteurs", "B": "des envahisseurs", "C": "des colporteurs", "D": "des passeurs"},
        "correct": "D"
    },
    {
        "question": "24. En juin 2015, quelle bataille a été reconstituée en Belgique regroupant plusieurs milliers de figurants ?",
        "options": {"A": "Courtrai", "B": "Waterloo", "C": "Malplaquet", "D": "Fontenoy"},
        "correct": "B"
    },
    {
        "question": "25. Le 22 août 2021 a été adoptée la loi dite « climat et ...",
        "options": {"A": "transition écologique", "B": "résilience", "C": "citoyenneté", "D": "finances"},
        "correct": "B"
    },
    {
        "question": "26. Lequel de ces groupes a mis en musique le film Highlander ?",
        "options": {"A": "Queen", "B": "The Who", "C": "Dire Straits", "D": "Led Zeppelin", "E": "U2"},
        "correct": "A"
    },
    {
        "question": "27. Dans lequel de ces pays se déroulent les aventures du troisième opus de la saga OSS 117 portée par Jean Dujardin ?",
        "options": {"A": "Brésil", "B": "Égypte", "C": "Russie", "D": "Kenya", "E": "Gabon"},
        "correct": "E"
    },
    {
        "question": "28. Selon la réglementation européenne, à combien doivent se monter les stocks stratégiques de produits pétroliers en France ?",
        "options": {"A": "A 15 jours de consommation de produits pétroliers de l'an passé", "B": "Au moins 120 jours des importations nettes de pétrole calculées en moyenne de la décennie écoulée", "C": "Au moins 90 jours des importations journalières moyennes nettes de pétrole", "D": "A une année de consommation intérieure moyenne", "E": "A six mois d'importation de produits pétroliers"},
        "correct": "C"
    },
    {
        "question": "29. Quand la bataille de Verdun a-t-elle débuté ?",
        "options": {"A": "Septembre 1914", "B": "Juillet 1915", "C": "Novembre 1915", "D": "Février 1916", "E": "Février 1918"},
        "correct": "D"
    },
    {
        "question": "30. Qui était le commandant en chef des forces armées alliées lors de l'armistice de 1918 ?",
        "options": {"A": "Ferdinand FOCH", "B": "Joseph JOFFRE", "C": "Philippe PETAIN", "D": "Maxime WEYGAND", "E": "John PERSHING"},
        "correct": "A"
    },
    {
        "question": "31. Quel pays possède environ la moitié des réserves mondiales de lithium ?",
        "options": {"A": "Argentine", "B": "Bolivie", "C": "Chili", "D": "Russie", "E": "Tibet"},
        "correct": "B"
    },
    {
        "question": "32. Quelle personnalité a-t-elle forgé le terme Realpolitik ?",
        "options": {"A": "Bismarck", "B": "Frédéric II", "C": "Guillaume II", "D": "Hitler", "E": "Kant"},
        "correct": "A"
    },
    {
        "question": "33. Le groupe Bilderberg est-il :",
        "options": {"A": "un groupe hôtelier néerlandais", "B": "un groupe musical belge", "C": "un conglomérat financier allemand", "D": "un rassemblement annuel et informel d'environ cent trente personnes influentes"},
        "correct": "D"
    },
    {
        "question": "34. Combien d'années Angela MERKEL a-t-elle été chancelière fédérale d'Allemagne ?",
        "options": {"A": "9 ans", "B": "11 ans", "C": "13 ans", "D": "16 ans", "E": "18 ans"},
        "correct": "D"
    },
    {
        "question": "35. Quel est le contenu du bloc de constitutionnalité en France ?",
        "options": {
            "A": "Constitution du 4 octobre 1958 (sans son préambule), déclaration des droits de l'homme et du citoyen, Préambule de la constitution de 1948, Charte de l'environnement",
            "B": "Constitution du 4 octobre 1958 (sans son préambule), déclaration des droits de l'homme et du citoyen, Préambule de la constitution de 1948",
            "C": "Constitution du 4 octobre 1958 (avec son préambule), déclaration des droits de l'homme et du citoyen, Préambule de la constitution de 1948",
            "D": "Constitution du 4 octobre 1958 (avec son préambule), déclaration des droits de l'homme et du citoyen, Charte de l'environnement",
            "E": "Constitution du 4 octobre 1958 (avec son préambule), déclaration des droits de l'homme et du citoyen, Préambule de la constitution de 1948, Charte de l'environnement"
        },
        "correct": "E"
    },
    {
        "question": "36. Quel fruit retrouve-t-on dans l'etxeko biskotxa, le gâteau basque ?",
        "options": {"A": "Des cerises noires", "B": "Des framboises", "C": "Des prunes vertes", "D": "Des oranges", "E": "Des fraises"},
        "correct": "A"
    },
    {
        "question": "37. Fin 2021, quelle était la valeur approximative du bitcoin ?",
        "options": {"A": "40 euros", "B": "400 euros", "C": "4.000 euros", "D": "40.000 euros", "E": "100.000 euros"},
        "correct": "D"
    },
    {
        "question": "38. En quelle année a-t-on découvert les peintures et gravures de la grotte de Lascaux ?",
        "options": {"A": "1899", "B": "1925", "C": "1940", "D": "1954", "E": "1968"},
        "correct": "C"
    },
    {
        "question": "39. Au rugby à 15, combien de points un essai transformé rapporte-t-il ?",
        "options": {"A": "4", "B": "5", "C": "6", "D": "7", "E": "8"},
        "correct": "D"
    },
    {
        "question": "40. Qui a déclaré « Impossible n'est pas français » ?",
        "options": {"A": "Napoléon 1er", "B": "Clémenceau", "C": "Cambronne", "D": "De Gaulle", "E": "Hugo"},
        "correct": "C"
    },
    {
        "question": "41. Dans quelle ville le premier métro a-t-il vu le jour ?",
        "options": {"A": "Paris", "B": "New-York", "C": "Londres", "D": "Washington", "E": "Berlin"},
        "correct": "A"
    },
    {
        "question": "42. En quelle année les accords d'Evian ont-ils été signés ?",
        "options": {"A": "1953", "B": "1958", "C": "1962", "D": "1968", "E": "1973"},
        "correct": "C"
    },
    {
        "question": "43. Quelle phrase célèbre le général De Gaulle a-t-il prononcé le 4 juin 1958 à Alger ?",
        "options": {"A": "Je vous ai compris", "B": "L'Algérie restera française", "C": "La France de Dunkerque à Tamanrasset", "D": "Au revoir"},
        "correct": "A"
    },
    {
        "question": "44. A quoi le pont des Soupirs de Venise doit-il son nom ?",
        "options": {"A": "Aux soupirs des couples libertins", "B": "Aux soupirs des prisonniers", "C": "Au bruit saccadé des courants d'air", "D": "Aux soupirs des touristes quand ils passent dessous"},
        "correct": "B"
    },
    {
        "question": "45. Le droit des peuples à disposer d'eux-mêmes a été proclamé par...",
        "options": {"A": "Otto von Bismarck", "B": "Jean Jaurès", "C": "Lénine", "D": "Claude Lévi-Strauss", "E": "Woodrow Wilson"},
        "correct": "E"
    },
    {
        "question": "46. Dans le « Guide du voyageur galactique », quelle est la réponse à « La grande question sur la vie, l'univers et le reste » ?",
        "options": {"A": "7", "B": "28", "C": "42", "D": "100"},
        "correct": "C"
    },
    {
        "question": "47. Que signifie « ARNm » en évoquant un vaccin ?",
        "options": {"A": "Acide ribonucléique moléculaire", "B": "Acide ribonucléique messager", "C": "Acide ribosome messager", "D": "Actine ribonucléique moléculaire", "E": "Anticorps ribosome messager"},
        "correct": "B"
    },
    {
        "question": "48. De quoi l'atmosphère terrestre n'est-elle pas composée ?",
        "options": {"A": "Diazote", "B": "Monoxyde de carbone", "C": "Dioxygène", "D": "Vapeur d'eau", "E": "Méthane"},
        "correct": "B"
    },
    {
        "question": "49. Dans la mythologie grecque, qui était le père d'Ariane ?",
        "options": {"A": "Le Minotaure", "B": "Apollon", "C": "Thésée", "D": "Minos", "E": "Zeus"},
        "correct": "D"
    },
    {
        "question": "50. Qui ne demeure pas au Panthéon ?",
        "options": {"A": "Marie Curie", "B": "Louis-Napoléon Bonaparte", "C": "Victor Hugo", "D": "Jean Jaurès", "E": "Joséphine Baker"},
        "correct": "B"
    },
    {
        "question": "51. Qu'est-ce que le nombre d'or ?",
        "options": {"A": "Un nombre entier", "B": "Un nombre d'harmonie utilisé dans les arts", "C": "3,1415... (Pi)", "D": "L'inverse du nombre d'argent"},
        "correct": "B"
    },
    {
        "question": "52. Quelle est la capitale du Canada ?",
        "options": {"A": "Ottawa", "B": "Vancouver", "C": "Toronto", "D": "Montréal"},
        "correct": "A"
    },
    {
        "question": "53. Quel cépage n'est pas utilisé pour le vin rouge ?",
        "options": {"A": "Cot", "B": "Malepère", "C": "Gamay", "D": "Chenin", "E": "Cabernet"},
        "correct": "D"
    },
    {
        "question": "54. Quelle proposition ne représente pas une étape de la transformation de l'eau ?",
        "options": {"A": "Évaporation", "B": "Fusion", "C": "Subduction", "D": "Solidification", "E": "Liquéfaction"},
        "correct": "C"
    },
    {
        "question": "55. Lequel de ces « châteaux de la Loire » se situe sur le Cher ?",
        "options": {"A": "Amboise", "B": "Chambord", "C": "Villandry", "D": "Chenonceaux"},
        "correct": "D"
    },
    {
        "question": "56. Qui a remporté le championnat du monde de Formule 1 en 2021 ?",
        "options": {"A": "Max Verstappen", "B": "Pierre Gasly", "C": "Lewis Hamilton", "D": "Valtteri Bottas"},
        "correct": "A"
    },
    {
        "question": "57. Quelle compétence ne relève pas de la Région ?",
        "options": {"A": "Les transports", "B": "Le développement économique", "C": "Les lycées", "D": "Les déchets", "E": "La formation professionnelle"},
        "correct": "C"
    },
    {
        "question": "58. En quelle année le droit de vote a-t-il été reconnu au profit des militaires ?",
        "options": {"A": "1789", "B": "1870", "C": "1918", "D": "1945", "E": "Les militaires n'ont pas le droit de vote"},
        "correct": "C"
    },
    {
        "question": "59. En quelle année la reine Elizabeth II a-t-elle été couronnée ?",
        "options": {"A": "1933", "B": "1943", "C": "1953", "D": "1963"},
        "correct": "C"
    },
    {
        "question": "60. Qui a écrit « Cyrano de Bergerac » ?",
        "options": {"A": "Alexandre Dumas père", "B": "Alexandre Dumas fils", "C": "Théophile Gautier", "D": "Edmond Rostand"},
        "correct": "D"
    },
    {
        "question": "61. En quelle année l'esclavage a-t-il été définitivement aboli en France ?",
        "options": {"A": "1789", "B": "1793", "C": "1814", "D": "1848", "E": "1870"},
        "correct": "D"
    },
    {
        "question": "62. Quelle ville accueille le festival international du film fantastique ?",
        "options": {"A": "Deauville", "B": "Annecy", "C": "Gérardmer", "D": "Alpe d'Huez", "E": "Cannes"},
        "correct": "C"
    },
    {
        "question": "63. De combien d'os se compose le corps humain ?",
        "options": {"A": "206", "B": "621", "C": "1351", "D": "96"},
        "correct": "A"
    },
    {
        "question": "64. Qui a composé La Lettre à Élise ?",
        "options": {"A": "Chopin", "B": "Liszt", "C": "Schubert", "D": "Schumann", "E": "Beethoven"},
        "correct": "E"
    },
    {
        "question": "65. De combien de députés est composée l'Assemblée nationale ?",
        "options": {"A": "577", "B": "467", "C": "348", "D": "848"},
        "correct": "A"
    },
    {
        "question": "66. Combien de points vaut la lettre Z au Scrabble (version française) ?",
        "options": {"A": "4", "B": "8", "C": "10", "D": "12", "E": "Aucune de ces propositions"},
        "correct": "C"
    },
    {
        "question": "67. Que signifie les lettres « QR » dans QR code ?",
        "options": {"A": "Question Réponse", "B": "Qualified Request", "C": "Quick Response", "D": "Questionning Reaction"},
        "correct": "C"
    },
    {
        "question": "68. A la latitude 23° 27' Nord se trouve :",
        "options": {"A": "le Tropique du Cancer", "B": "le Tropique du Capricorne", "C": "le Méridien de Greenwich", "D": "le Cercle polaire", "E": "l'Équateur"},
        "correct": "A"
    },
    {
        "question": "69. Lequel de ces archipels ne se situe pas en Polynésie ?",
        "options": {"A": "Les îles Australes", "B": "Les îles sous le vent", "C": "Les îles Marquises", "D": "Les îles Loyauté", "E": "Les îles Tuamotu"},
        "correct": "D"
    },
    {
        "question": "70. Quelle est la forme juridique de la République française ?",
        "options": {"A": "État unitaire décentralisé", "B": "État unitaire régionalisé", "C": "État unitaire concentré", "D": "État fédéral"},
        "correct": "A"
    },
    {
        "question": "71. Sainte Geneviève, patronne de la Gendarmerie, était également patronne :",
        "options": {"A": "de la ville de Paris", "B": "du 13ème régiment de dragons parachutistes", "C": "des diplomates", "D": "des grenadiers-voltigeurs", "E": "des causes perdues"},
        "correct": "A"
    },
    {
        "question": "72. Parmi les bouteilles suivantes, laquelle détient la plus grande capacité ?",
        "options": {"A": "Le Balthazar", "B": "Le Jéroboam", "C": "Le Salmanazar", "D": "Le Nabuchodonosor", "E": "Le Mathusalem"},
        "correct": "D"
    },
    {
        "question": "73. Joséphine Baker est entrée au Panthéon le 30 novembre 2021. Combien de femmes y reposent ?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "5", "E": "6"},
        "correct": "C"
    },
    {
        "question": "74. Qui est l'auteur de la célèbre citation « L'important c'est de participer » ?",
        "options": {"A": "Baden-Powell", "B": "Philippe Chatrier", "C": "Pierre de Coubertin", "D": "Roland Garros", "E": "Diego Armando Maradona Franco"},
        "correct": "C"
    },
    {
        "question": "75. Quel océan borde l'île Maurice ?",
        "options": {"A": "Océan Indien", "B": "Océan Pacifique", "C": "Océan Atlantique", "D": "Océan Arctique", "E": "Océan Austral"},
        "correct": "A"
    },
    {
        "question": "76. Le BCG est un vaccin contre :",
        "options": {"A": "le tétanos", "B": "la grippe", "C": "la COVID 19", "D": "la rage", "E": "la tuberculose"},
        "correct": "E"
    },
    {
        "question": "77. Les perturbateurs endocriniens sont :",
        "options": {"A": "des enzymes", "B": "des virus particuliers", "C": "des hormones synthétiques", "D": "des molécules chimiques synthétiques"},
        "correct": "D"
    },
    {
        "question": "78. Comment s'appelle la réunion plénière et ponctuelle des membres de l'Assemblée nationale et du Sénat, destinée à faire voter une révision de la constitution ou la ratification d'un traité, ou encore à écouter une proclamation du Président de la République ?",
        "options": {"A": "la Chambre Haute", "B": "le Congrès", "C": "le Parlement", "D": "le Conseil Supérieur", "E": "le Concile"},
        "correct": "B"
    },
    {
        "question": "79. En 2022, de quel célèbre artiste sont commémorés les 400 ans de la naissance ?",
        "options": {"A": "Arthur Schopenhauer", "B": "Jean-Baptiste Poquelin dit Molière", "C": "Wolfgang Amadeus Mozart", "D": "Pablo Ruiz Picasso", "E": "Marcel Proust"},
        "correct": "B"
    },
    {
        "question": "80. Elon Musk, patron de Tesla et de SpaceX, prévoit avec son entreprise Neuralink :",
        "options": {
            "A": "d'implanter des puces dans le cerveau d'humains (destinées aux personnes handicapées)",
            "B": "d'apporter un accès à haut débit Internet au monde entier grâce à la mise sur orbite de satellites",
            "C": "de développer un cinquième mode de transport supersonique",
            "D": "de construire des véhicules de lancement spatiaux, avec pour objectif de baisser les coûts et de rendre à l'avenir possible une colonisation sur Mars",
            "E": "de rendre les voitures électriques plus accessibles"
        },
        "correct": "A"
    },
    {
        "question": "81. En quelle année a été votée l'abolition de la peine de mort en France ?",
        "options": {"A": "1981", "B": "1968", "C": "1989", "D": "1980", "E": "1990"},
        "correct": "A"
    },
    {
        "question": "82. Claude Monet est un peintre français connu pour sa série de toiles intitulée Les Nymphéas, représentant le jardin de fleurs de sa maison de Giverny. A quel mouvement pictural appartient-il ?",
        "options": {"A": "Le surréalisme", "B": "L'impressionnisme", "C": "Le cubisme", "D": "L'Art Nouveau", "E": "Le symbolisme"},
        "correct": "B"
    },
    {
        "question": "83. Quel événement tragique, survenu en 1897 et faisant plus de 100 victimes, est à l'origine des premières réglementations modernes de prévention contre le risque incendie dans les établissements recevant du public ?",
        "options": {"A": "L'attaque du Bon Marché", "B": "L'incendie du théâtre de la Comédie française", "C": "Le séisme de Lambesc", "D": "L'incendie du Bazar de la Charité"},
        "correct": "D"
    },
    {
        "question": "84. Dans quelle ville est située le siège du Parlement européen ?",
        "options": {"A": "Genève", "B": "Bruxelles", "C": "Strasbourg", "D": "Luxembourg", "E": "Zurich"},
        "correct": "C"
    },
    {
        "question": "85. Qui a peint 'Le jugement dernier' de la chapelle Sixtine à Rome ?",
        "options": {"A": "Léonard de Vinci", "B": "Raphaël", "C": "Michel-Ange", "D": "Botticelli", "E": "Arcimboldo"},
        "correct": "C"
    },
    {
        "question": "86. Dans quelle ville un film peut-il recevoir un Lion d'Or ?",
        "options": {"A": "Deauville", "B": "Venise", "C": "Berlin", "D": "Paris", "E": "Gérardmer"},
        "correct": "B"
    },
    {
        "question": "87. Lequel de ces pays n'a aucune façade maritime ?",
        "options": {"A": "Pologne", "B": "Bulgarie", "C": "Hongrie", "D": "Roumanie", "E": "Italie"},
        "correct": "C"
    },
    {
        "question": "88. Quel pays ne fait pas partie du Maghreb ?",
        "options": {"A": "Tunisie", "B": "Algérie", "C": "Égypte", "D": "Maroc"},
        "correct": "C"
    },
    {
        "question": "89. Quelle est la capitale du Sénégal ?",
        "options": {"A": "Dakar", "B": "Abidjan", "C": "Bamako", "D": "Ouagadougou", "E": "Kinshasa"},
        "correct": "A"
    },
    {
        "question": "90. En France, la plus grande partie de l'électricité d'origine renouvelable provient :",
        "options": {"A": "de l'énergie photovoltaïque", "B": "de l'énergie hydraulique", "C": "de l'énergie éolienne", "D": "de l'énergie géothermique"},
        "correct": "B"
    },
    {
        "question": "91. En vertu de l'article 15 de la Constitution du 4 octobre 1958, qui est le chef des armées ?",
        "options": {"A": "Le Président de la République", "B": "Le Chef d'état-major des armées", "C": "Le Premier Ministre", "D": "Le Président de l'Assemblée nationale", "E": "Le Président du Sénat"},
        "correct": "A"
    },
    {
        "question": "92. La gendarmerie nationale a été créée le :",
        "options": {"A": "14 juillet 1789", "B": "16 février 1791", "C": "1er janvier 1800", "D": "17 avril 1798", "E": "23 octobre 1812"},
        "correct": "B"
    },
    {
        "question": "93. Quelle région autonome chinoise est majoritairement peuplée d'Ouïghours, peuple turcophone et musulman sunnite ?",
        "options": {"A": "Tibet", "B": "Xinjiang", "C": "Mongolie intérieure", "D": "Guangxi"},
        "correct": "B"
    },
    {
        "question": "94. L'hygrométrie caractérise :",
        "options": {"A": "la quantité d'eau sous forme liquide", "B": "la quantité d'eau sous forme gazeuse dans l'air", "C": "la quantité d'eau sous forme solide (glace)", "D": "la mesure du débit des cours d'eaux"},
        "correct": "B"
    },
    {
        "question": "95. L'idée que les atomes puissent exister a été émise pour la première fois par :",
        "options": {"A": "Démocrite (IVe siècle avant Jésus-Christ)", "B": "Léonard de Vinci", "C": "Henri Becquerel", "D": "Marie Curie", "E": "Darwin"},
        "correct": "A"
    },
    {
        "question": "96. Le 5 juin 1883 a lieu le premier départ de 'L'Orient-Express'. Quelles étaient les gares de départ et de destination ?",
        "options": {"A": "Paris - Constantinople", "B": "Venise - Moscou", "C": "Rome - Ankara", "D": "Bruges - Budapest", "E": "Calais - Vienne"},
        "correct": "A"
    },
    {
        "question": "97. Dans quelle ville le siège de l'Organisation des Nations Unies pour l'éducation, la science et la culture (UNESCO) est-il situé ?",
        "options": {"A": "New-York", "B": "Paris", "C": "Varsovie", "D": "Bruxelles", "E": "Genève"},
        "correct": "B"
    },
    {
        "question": "98. Lequel de ces champignons est reconnu comme vénéneux ou mortel ?",
        "options": {"A": "La trompette de la mort", "B": "L'amanite printanière", "C": "L'oreille de Judas", "D": "Le lactaire délicieux", "E": "La morille"},
        "correct": "B"
    },
    {
        "question": "99. Que signifie l'acronyme CNIL ?",
        "options": {"A": "Coordination Nationale de l'Information et des Libertés", "B": "Conseil National sur l'Information et les Libertés", "C": "Centre National Informatique et Liberté", "D": "Commission Nationale de l'Informatique et des Libertés"},
        "correct": "D"
    },
    {
        "question": "100. A quel personnage célèbre de l'Histoire est associé l'événement du passage du Rubicon ?",
        "options": {"A": "Napoléon Bonaparte", "B": "Jules César", "C": "Erwin Rommel", "D": "Alexandre le Grand", "E": "Christophe Colomb"},
        "correct": "B"
    }

]




# QCM 2023 et QCM 2024 (exemples minimaux, à compléter)
qcm2023 = [
    {
        "question": "1. Exemple QCM 2023 – Question 1",
        "options": {"A": "Option 1", "B": "Option 2", "C": "Option 3", "D": "Option 4"},
        "correct": "A"
    },
    {
        "question": "2. Exemple QCM 2023 – Question 2",
        "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
        "correct": "B"
    }
    # ... Ajoutez ici les autres questions pour QCM 2023
]

qcm2024 = [
    {
        "question": "1. On trouve le canal carpien :",
        "options": {
            "A": "à la frontière de la Hongrie et de la Roumanie",
            "B": "au niveau du poignet de l'être humain",
            "C": "sur la face cachée de la lune",
            "D": "en entrée de certaines nasses utilisées par des pêcheurs en eaux douces"
        },
        "correct": "B"
    },
    {
        "question": "2. Une sensibilisation particulière au cancer du sein a lieu chaque année en :",
        "options": {
            "A": "novembre",
            "B": "janvier",
            "C": "octobre",
            "D": "mai"
        },
        "correct": "C"
    },
    {
        "question": "3. Le prix Goncourt 2023 a été décerné à :",
        "options": {
            "A": "Jean-Baptiste Andrea",
            "B": "Jean-Baptiste Poquelin",
            "C": "Camille Andrea",
            "D": "Jean-Louis Fournier"
        },
        "correct": "A"
    },
    {
        "question": "4. Lequel de ces pays n'a pas de frontière commune avec l'Arménie ?",
        "options": {
            "A": "La Géorgie",
            "B": "L'Azerbaïdjan",
            "C": "L'Iran",
            "D": "Le Turkménistan"
        },
        "correct": "D"
    },
    {
        "question": "5. Le film \"Imitation Game\", sorti en 2014, retrace la vie du scientifique :",
        "options": {
            "A": "Robert Oppenheimer",
            "B": "John Charles Fields",
            "C": "Alan Turing",
            "D": "Leonhard Euler"
        },
        "correct": "C"
    },
    {
        "question": "6. La droséra est :",
        "options": {
            "A": "une plante carnivore",
            "B": "une variété de mouche",
            "C": "une danse sud-américaine",
            "D": "un manteau"
        },
        "correct": "A"
    },
    {
        "question": "7. Le mouvement Movember, Mouvembre ou novembre bleu au profit de la recherche sur les maladies masculines voit chaque année des hommes :",
        "options": {
            "A": "se laisser pousser la moustache",
            "B": "défiler déguisés",
            "C": "s'épiler",
            "D": "porter uniquement des boxers en guise de sous-vêtement"
        },
        "correct": "A"
    },
    {
        "question": "8. Porté à l'écran en 2023 par Ridley Scott, l'empereur Napoléon Ier est décédé à :",
        "options": {
            "A": "Sainte-Soline",
            "B": "Sainte-Hélène",
            "C": "Saintes-Maries-de-la-Mer",
            "D": "Sainte-Sophie"
        },
        "correct": "B"
    },
    {
        "question": "9. La capitale de la Turquie est :",
        "options": {
            "A": "Istanbul",
            "B": "Ankara",
            "C": "Constantinople",
            "D": "Byzance"
        },
        "correct": "B"
    },
    {
        "question": "10. Laquelle de ces appellations de vin n'est pas située en Gironde :",
        "options": {
            "A": "Pomerol",
            "B": "Gigondas",
            "C": "Pauillac",
            "D": "Entre-deux-Mer"
        },
        "correct": "B"
    },
    {
        "question": "11. De quelle région française est originaire le tourteau fromagé ?",
        "options": {
            "A": "La Bourgogne",
            "B": "L'Auvergne",
            "C": "Le Poitou",
            "D": "La Touraine",
            "E": "La Normandie"
        },
        "correct": "C"
    },
    {
        "question": "12. Laquelle de ces villes est implantée dans la bande de Gaza ?",
        "options": {
            "A": "Khan Younes",
            "B": "Djenin",
            "C": "Hébron",
            "D": "Ramallah"
        },
        "correct": "A"
    },
    {
        "question": "13. La commune d'Hondschoote est :",
        "options": {
            "A": "belge",
            "B": "française",
            "C": "néerlandaise",
            "D": "luxembourgeoise"
        },
        "correct": "C"
    },
    {
        "question": "14. En 2023, le ministre des Affaires étrangères de la fédération de Russie se nomme :",
        "options": {
            "A": "Alexandre Gortchakov",
            "B": "Sergueï Lavrov",
            "C": "Evgueni Zinitchev",
            "D": "Dimitri Medvedev",
            "E": "Vladimir Ilitch Oulianov"
        },
        "correct": "B"
    },
    {
        "question": "15. Une équipe de beach handball est composée de :",
        "options": {
            "A": "7 joueurs",
            "B": "11 joueurs",
            "C": "4 joueurs",
            "D": "5 joueurs",
            "E": "3 joueurs"
        },
        "correct": "C"
    },
    {
        "question": "16. La valeur de Pi commence par :",
        "options": {
            "A": "3,141",
            "B": "3,529",
            "C": "3,314",
            "D": "3,014",
            "E": "3,151"
        },
        "correct": "A"
    },
    {
        "question": "17. Laquelle de ces plantes n'est pas une graminée :",
        "options": {
            "A": "le roseau",
            "B": "le bambou",
            "C": "l'orge",
            "D": "le ginkgo"
        },
        "correct": "D"
    },
    {
        "question": "18. Qui a écrit « La véritable école du commandement est la culture générale. Au fond des victoires d'Alexandre, on retrouve toujours Aristote. » ?",
        "options": {
            "A": "Charles De Gaulle",
            "B": "Blaise Pascal",
            "C": "Honoré de Balzac",
            "D": "Napoléon Ier"
        },
        "correct": "D"
    },
    {
        "question": "19. Le nouveau véhicule blindé de la gendarmerie est baptisé :",
        "options": {
            "A": "la dracène",
            "B": "le centaure",
            "C": "le pangolin",
            "D": "la limule",
            "E": "le minotaure"
        },
        "correct": "C"
    },
    {
        "question": "20. Qui a peint le tableau « L'origine du monde » ?",
        "options": {
            "A": "Gustave Courbet",
            "B": "Julien Courbet",
            "C": "Julien Courbey",
            "D": "Gustave Boulanger",
            "E": "Louis Boulanger"
        },
        "correct": "A"
    },
    {
        "question": "21. Que veut dire RSE pour une entreprise ?",
        "options": {
            "A": "Responsabilité Sociétale des Entreprises",
            "B": "Ressource Spécialisée d'Emplois",
            "C": "Revenu Spécifique Équitable"
        },
        "correct": "A"
    },
    {
        "question": "22. Quelle est la date du premier choc pétrolier ?",
        "options": {
            "A": "Mai à juin 1968",
            "B": "Mars à mai 1971",
            "C": "Octobre 1973 à mars 1974"
        },
        "correct": "C"
    },
    {
        "question": "23. À qui doit-on l'expression « les Trente glorieuses » ?",
        "options": {
            "A": "Jacques Attali",
            "B": "Jean Fourastié",
            "C": "John Rawls",
            "D": "Thomas Malthus"
        },
        "correct": "B"
    },
    {
        "question": "24. Quel auteur a écrit en 1992 « La fin de l'histoire », théorisant que la démocratie libérale comme idéologie dominante, annonçait la forme finale de tout gouvernement humain ?",
        "options": {
            "A": "Samuel Huntington",
            "B": "Francis Fukuyama",
            "C": "John Mearsheimer",
            "D": "James Oscar Mc Kinsey"
        },
        "correct": "B"
    },
    {
        "question": "25. Jusqu'au début de l'ère du Jurassique, les terres émergées ne formaient qu'un seul bloc, un supercontinent nommé :",
        "options": {
            "A": "Le Laurasia",
            "B": "Le Gondwana",
            "C": "La Pangée",
            "D": "L'Atlantide"
        },
        "correct": "C"
    },
    {
        "question": "26. Aux États-Unis, le premier président fut :",
        "options": {
            "A": "George Washington",
            "B": "Thomas Jefferson",
            "C": "John Adams",
            "D": "James Madison"
        },
        "correct": "A"
    },
    {
        "question": "27. Les Bourbons constituent la dernière des cinq dynasties de monarques français. Quelle était la première ?",
        "options": {
            "A": "Carolingienne",
            "B": "Mérovingienne",
            "C": "Capétienne",
            "D": "Valois"
        },
        "correct": "B"
    },
    {
        "question": "28. Parmi les cinq propositions suivantes, se trouvent quatre institutions et une agence. Quelle est l'agence ?",
        "options": {
            "A": "Le Parlement Européen",
            "B": "Europol",
            "C": "Le Conseil Européen",
            "D": "Le Conseil de l'Union Européenne",
            "E": "La Commission Européenne"
        },
        "correct": "B"
    },
    {
        "question": "29. Parmi ces bandes dessinées à succès mondial, quelle est celle la plus vendue au monde toutes périodes confondues ?",
        "options": {
            "A": "Tintin",
            "B": "One Piece",
            "C": "Astérix",
            "D": "Dragon Ball"
        },
        "correct": "B"
    },
    {
        "question": "30. Quel grand mathématicien a établi en 1900 la liste des 23 problèmes majeurs, dont un tiers ne sont toujours pas résolus ?",
        "options": {
            "A": "David Hilbert",
            "B": "Henri Poincaré",
            "C": "Carl Friedrich Gauss",
            "D": "Kurt Gödel"
        },
        "correct": "A"
    },
    {
        "question": "31. En quelle année a été assassiné John Fitzgerald Kennedy ?",
        "options": {
            "A": "1962",
            "B": "1964",
            "C": "1963",
            "D": "1965"
        },
        "correct": "C"
    },
    {
        "question": "32. Qui a éliminé la France en quart de finale de la coupe du monde de Rugby en 2023 ?",
        "options": {
            "A": "L'Irlande",
            "B": "La Nouvelle-Zélande",
            "C": "L'Angleterre",
            "D": "L'Afrique du Sud"
        },
        "correct": "B"
    },
    {
        "question": "33. Parmi les mots suivants, lequel n'est pas un palindrome ?",
        "options": {
            "A": "comme",
            "B": "Anna",
            "C": "ici",
            "D": "ressasser"
        },
        "correct": "A"
    },
    {
        "question": "34. Parmi ces zones de défense, laquelle comprend une seule région ?",
        "options": {
            "A": "Sud",
            "B": "Sud-ouest",
            "C": "Ouest"
        },
        "correct": "B"
    },
    {
        "question": "35. Une feuille format A4 correspond à :",
        "options": {
            "A": "deux feuilles de format A3",
            "B": "deux feuilles de format A6",
            "C": "le quart d'une feuille de format A2",
            "D": "le quart d'une feuille de format A1"
        },
        "correct": "C"
    },
    {
        "question": "36. Quel supplice est imposé à Tantale ?",
        "options": {
            "A": "Pousser indéfiniment une roche au sommet d'une montagne",
            "B": "Être dévoré sans cesse par un vautour",
            "C": "Vivre enfermé dans le labyrinthe",
            "D": "Subir la faim et la soif éternellement, incapable de saisir le moindre vivre"
        },
        "correct": "D"
    },
    {
        "question": "37. Quel bâtiment officiel a été pris d'assaut par des militants républicains américains en janvier 2021 ?",
        "options": {
            "A": "Le Lincoln Memorial",
            "B": "Le Pentagone",
            "C": "La Maison Blanche",
            "D": "Le Capitole"
        },
        "correct": "D"
    },
    {
        "question": "38. Au cours de la première guerre mondiale, quels pays constituent la Triple Entente ?",
        "options": {
            "A": "France / États-Unis / Royaume-Uni",
            "B": "France / Russie / Royaume-Uni",
            "C": "Autriche-Hongrie / Allemagne / Italie",
            "D": "France / Royaume-Uni / Italie",
            "E": "Allemagne / Autriche-Hongrie / Empire ottoman"
        },
        "correct": "B"
    },
    {
        "question": "39. Parmi les propositions suivantes, laquelle ne fait pas référence à l'un des douze travaux d'Hercule ?",
        "options": {
            "A": "Les écuries d'Augias",
            "B": "La ceinture de la reine des Amazones",
            "C": "Le chien Cerbère des Enfers",
            "D": "Le labyrinthe du Minotaure",
            "E": "Le lion de Némée"
        },
        "correct": "D"
    },
    {
        "question": "40. Dans quel département métropolitain se déroule tous les ans en juillet, depuis 30 ans, le festival des Vieilles Charrues ?",
        "options": {
            "A": "Le Morbihan",
            "B": "La Vendée",
            "C": "Les Côtes d'Armor",
            "D": "Le Finistère",
            "E": "Les Pays de la Loire"
        },
        "correct": "D"
    },
    {
        "question": "41. Où s'est déroulée la 28e conférence mondiale sur le climat (COP28), du 30 novembre au 12 décembre 2023 ?",
        "options": {
            "A": "Riyad",
            "B": "Doha",
            "C": "Abu Dhabi",
            "D": "Dubaï"
        },
        "correct": "D"
    },
    {
        "question": "42. Quelle a été la dernière personnalité à entrer au Panthéon, le 30 novembre 2021 ?",
        "options": {
            "A": "Joséphine Baker",
            "B": "Simone Veil",
            "C": "Alexandre Dumas",
            "D": "André Malraux"
        },
        "correct": "B"
    },
    {
        "question": "43. Comment se nomme la dernière mission de l'astronaute français Thomas Pesquet ?",
        "options": {
            "A": "Bêta",
            "B": "Proxima",
            "C": "Alpha",
            "D": "Omega",
            "E": "Crew-2 Endeavour"
        },
        "correct": "C"
    },
    {
        "question": "44. Quel club de football féminin a été sacré champion d'Europe le 3 juin 2023 ?",
        "options": {
            "A": "Équipe féminine de l'Olympique Lyonnais",
            "B": "Fútbol Club Barcelona Femenino",
            "C": "VfL Wolsburg",
            "D": "Chelsea Football Club Women"
        },
        "correct": "B"
    },
    {
        "question": "45. Le 10 septembre 1960, à Nantes, le Général de Gaulle qualifie une organisation internationale de \"machin\". De quelle organisation parlait-il ?",
        "options": {
            "A": "L'ONU",
            "B": "L'OTAN",
            "C": "L'OCDE",
            "D": "L'OMS"
        },
        "correct": "B"
    },
    {
        "question": "46. Dans quel domaine les Français Pierre Agostini et Anne L'Huillier ont-ils reçu un prix Nobel en 2023 ?",
        "options": {
            "A": "Physique",
            "B": "Chimie",
            "C": "Économie",
            "D": "Médecine"
        },
        "correct": "A"
    },
    {
        "question": "47. Depuis sa création en 1993, quel port a toujours accueilli le départ de la Transat Jacques Vabre, également appelée Route du café ?",
        "options": {
            "A": "La Rochelle",
            "B": "Nantes",
            "C": "Saint-Nazaire",
            "D": "Le Havre"
        },
        "correct": "D"
    },
    {
        "question": "48. Dans quel pays actuel était située la cité antique de Troie ?",
        "options": {
            "A": "Grèce",
            "B": "Italie",
            "C": "Turquie",
            "D": "Macédoine du Nord"
        },
        "correct": "C"
    },
    {
        "question": "49. À quelle date la flamme du Soldat Inconnu a-t-elle été allumée pour la première fois ?",
        "options": {
            "A": "31 décembre 1918",
            "B": "11 novembre 1923",
            "C": "31 décembre 1936",
            "D": "11 novembre 1945"
        },
        "correct": "B"
    },
    {
        "question": "50. Quel pharaon est surnommé le « roi des rois » ?",
        "options": {
            "A": "Ramsès II",
            "B": "Khéops",
            "C": "Toutânkhamon",
            "D": "Aménophis IV"
        },
        "correct": "A"
    },
    {
        "question": "51. À quelle ville fait référence le peintre espagnol Pablo Picasso dans son célèbre tableau \"Les Demoiselles d'Avignon\" ?",
        "options": {
            "A": "Avignon",
            "B": "Barcelone",
            "C": "Marseille",
            "D": "Saragosse"
        },
        "correct": "A"
    },
    {
        "question": "52. Où se déroule l'histoire de Roméo et Juliette, tragédie écrite par William Shakespeare entre 1591 et 1595 ?",
        "options": {
            "A": "Naples",
            "B": "Venise",
            "C": "Bergame",
            "D": "Vérone"
        },
        "correct": "D"
    },
    {
        "question": "53. Laquelle de ces civilisations avait sa capitale dans l'actuel Pérou ?",
        "options": {
            "A": "Les Incas",
            "B": "Les Mayas",
            "C": "Les Aztèques",
            "D": "Les Olmèques"
        },
        "correct": "A"
    },
    {
        "question": "54. À quel texte appartient l'article 11 suivant : \"La libre communication des pensées et des opinions est un des droits les plus précieux de l'homme : tout citoyen peut donc parler, écrire, imprimer librement, sauf à répondre de l'abus de cette liberté dans les cas déterminés par la loi.\"",
        "options": {
            "A": "La déclaration universelle des droits de l'Homme (1948)",
            "B": "La déclaration des Droits de l'Homme et du Citoyen (1789)",
            "C": "Les quatre Conventions de Genève (1949)",
            "D": "Les deux protocoles additionnels aux Conventions de Genève (1977)"
        },
        "correct": "B"
    },
    {
        "question": "55. En quelle année sont programmées les prochaines élections législatives en France ?",
        "options": {
            "A": "2025",
            "B": "2026",
            "C": "2027",
            "D": "2028"
        },
        "correct": "C"
    },
    {
        "question": "56. En quelle année a été commercialisée pour la première fois la poupée Barbie ?",
        "options": {
            "A": "1953",
            "B": "1959",
            "C": "1963",
            "D": "1969"
        },
        "correct": "B"
    },
    {
        "question": "57. Dans quel pays est né le physicien Julius Robert Oppenheimer le 22 avril 1904 et surnommé le \"père de la bombe atomique\" ?",
        "options": {
            "A": "Allemagne",
            "B": "Autriche",
            "C": "États-Unis",
            "D": "Pays-Bas"
        },
        "correct": "C"
    },
    {
        "question": "58. Laquelle de ces batailles napoléoniennes est communément appelée la \"bataille des trois Empereurs\" ?",
        "options": {
            "A": "Wagram",
            "B": "Friedland",
            "C": "Austerlitz",
            "D": "Iéna"
        },
        "correct": "C"
    },
    {
        "question": "59. Laquelle de ces œuvres n'est pas de Jean Racine (1639 - 1699) ?",
        "options": {
            "A": "Andromaque",
            "B": "Britannicus",
            "C": "Phèdre",
            "D": "Horace"
        },
        "correct": "D"
    },
    {
        "question": "60. Lequel de ces rois de France épousa Catherine de Médicis le 28 octobre 1533 puis succéda à son père François Ier sur le trône en 1547 ?",
        "options": {
            "A": "Louis XII",
            "B": "François II",
            "C": "Charles IX",
            "D": "Henri II"
        },
        "correct": "D"
    },
    {
        "question": "61. Le Conseil constitutionnel français est composé de neuf membres. Pour combien d'années sont-ils nommés ?",
        "options": {
            "A": "4 ans",
            "B": "5 ans",
            "C": "7 ans",
            "D": "9 ans"
        },
        "correct": "D"
    },
    {
        "question": "62. Qui est l'auteur du roman \"La Guerre des mondes\", adapté au cinéma par Steven Spielberg ?",
        "options": {
            "A": "Aldous Huxley",
            "B": "Herbert George Wells",
            "C": "Jack London",
            "D": "Jules Verne",
            "E": "Bernard Werber"
        },
        "correct": "B"
    },
    {
        "question": "63. Quelle est l'auteure de l'heptalogie Harry Potter ?",
        "options": {
            "A": "Cressida Cowell",
            "B": "J. K. Rowling",
            "C": "Babette Cole",
            "D": "Karen Traviss",
            "E": "P. D. James"
        },
        "correct": "B"
    },
    {
        "question": "64. Dans quelle ville allemande ont été jugés 24 des principaux responsables du IIIe Reich accusés de complot, crimes contre la paix, crimes de guerre et crimes contre l'humanité ?",
        "options": {
            "A": "Munich",
            "B": "Weimar",
            "C": "Berlin",
            "D": "Nuremberg",
            "E": "Aix-la-Chapelle"
        },
        "correct": "D"
    },
    {
        "question": "65. Dans quelle ville métropolitaine le festival international de la bande dessinée a-t-il lieu tous les ans ?",
        "options": {
            "A": "Poitiers",
            "B": "Nantes",
            "C": "Angoulême",
            "D": "La Rochelle",
            "E": "Bourges"
        },
        "correct": "C"
    },
    {
        "question": "66. Parmi ces peintres, lequel n'a pas fait partie de l'impressionnisme ?",
        "options": {
            "A": "Edgar Degas",
            "B": "Claude Monet",
            "C": "Auguste Renoir",
            "D": "Henri Matisse",
            "E": "Camille Pissaro"
        },
        "correct": "D"
    },
    {
        "question": "67. Qui a peint « Les Noces de Cana » ?",
        "options": {
            "A": "Jacopo Robusti, dit Le Tintoret",
            "B": "Paulo Caliari, dit Véronèse",
            "C": "Antonio Allegri da Corregio, dit Le Corrège",
            "D": "Tiziano Vecellio, dit Le Titien",
            "E": "Dominikos Theotokopoulos, dit Le Greco"
        },
        "correct": "B"
    },
    {
        "question": "68. Laquelle de ces planètes est la plus éloignée du soleil ?",
        "options": {
            "A": "Vénus",
            "B": "Neptune",
            "C": "Saturne",
            "D": "Uranus",
            "E": "Jupiter"
        },
        "correct": "B"
    },
    {
        "question": "69. Aux États-Unis, quelles villes la mythique « route 66 » reliait-elle entre les années 1926 et 1985 ?",
        "options": {
            "A": "New York (New York) à Santa Barbara (Californie)",
            "B": "Boston (Massachusetts) à Los Angeles (Californie)",
            "C": "Chicago (Illinois) à Santa Monica (Californie)",
            "D": "Détroit (Michigan) à Long Beach (Californie)",
            "E": "Miami (Floride) à San Diego (Californie)"
        },
        "correct": "C"
    },
    {
        "question": "70. Combien d'années la guerre de Cent ans a-t-elle duré ?",
        "options": {
            "A": "94 ans",
            "B": "101 ans",
            "C": "107 ans",
            "D": "116 ans",
            "E": "123 ans"
        },
        "correct": "D"
    },
    {
        "question": "71. Quelle est la première femme à avoir été inhumée au Panthéon ?",
        "options": {
            "A": "Joséphine Baker",
            "B": "Geneviève de Gaulle-Anthonioz",
            "C": "Simone Veil",
            "D": "Marie Curie"
        },
        "correct": "D"
    },
    {
        "question": "72. Dans le film « Les Visiteurs » de Jean-Marie Poiré, sorti en 1993, de quel roi français le comte Godefroy de Montmirail est-il le capitaine ?",
        "options": {
            "A": "Philippe II",
            "B": "Hugues",
            "C": "Jean Ier",
            "D": "Robert II",
            "E": "Louis VI"
        },
        "correct": "A"
    },
    {
        "question": "73. Lequel de ces réseaux sociaux n'appartient pas à l'entreprise Meta ?",
        "options": {
            "A": "Instagram",
            "B": "Facebook",
            "C": "Snapchat",
            "D": "WhatsApp"
        },
        "correct": "C"
    },
    {
        "question": "74. La CEE est considérée comme l'ancêtre de l'Union européenne. Que signifient ses initiales ?",
        "options": {
            "A": "Le conseil européen élargi",
            "B": "La communauté économique européenne",
            "C": "La confédération économique européenne",
            "D": "La commission d'entraide européenne"
        },
        "correct": "B"
    },
    {
        "question": "75. Qui a été le premier Premier ministre de la Ve République ?",
        "options": {
            "A": "Georges Pompidou",
            "B": "Charles de Gaulle",
            "C": "Michel Poniatowski",
            "D": "Michel Debré"
        },
        "correct": "D"
    },
    {
        "question": "76. Parmi les propositions suivantes, laquelle ne fait pas partie du tableau des éléments périodiques ?",
        "options": {
            "A": "Le bronze",
            "B": "Le zinc",
            "C": "Le platine",
            "D": "L'étain"
        },
        "correct": "A"
    },
    {
        "question": "77. Hélène Carrère d'Encausse est décédée en août 2023. De quelle institution occupait-elle le poste de secrétaire perpétuelle ?",
        "options": {
            "A": "L'Institut de France",
            "B": "Le Conseil constitutionnel",
            "C": "L'Académie française",
            "D": "L'Académie des beaux-arts"
        },
        "correct": "C"
    },
    {
        "question": "78. Que représente « La Cène », célèbre tableau de Léonard de Vinci ?",
        "options": {
            "A": "La trahison de Judas",
            "B": "Le dernier repas du Christ",
            "C": "La crucifixion de Jésus",
            "D": "La rupture du jeûne du Ramadan"
        },
        "correct": "B"
    },
    {
        "question": "79. Lequel de ces navires est responsable d'une importante marée noire sur les côtes françaises ?",
        "options": {
            "A": "Baraka",
            "B": "Monika",
            "C": "Erika",
            "D": "Annika",
            "E": "Jessika"
        },
        "correct": "C"
    },
    {
        "question": "80. L'école des officiers de la gendarmerie nationale se situe à :",
        "options": {
            "A": "Paris",
            "B": "Libourne",
            "C": "Melun",
            "D": "Cannes-Écluse",
            "E": "Saint-Cyr-l'École"
        },
        "correct": "C"
    },
    {
        "question": "81. Complétez cette citation de Charles de Gaulle : « La France ne peut être la France sans... » :",
        "options": {
            "A": "Ses colonies",
            "B": "L'Alsace et la Lorraine",
            "C": "La grandeur",
            "D": "La gloire de ses armées"
        },
        "correct": "C"
    },
    {
        "question": "82. Maurice Druon est l'auteur de la suite romanesque :",
        "options": {
            "A": "Le trône de fer",
            "B": "Les rois maudits",
            "C": "Les piliers de la Terre",
            "D": "Les Rougon Macquart"
        },
        "correct": "B"
    },
    {
        "question": "83. Quel physicien a donné son nom au principe d'indétermination (également dit principe d'incertitude) en mécanique quantique ?",
        "options": {
            "A": "Eisenstein",
            "B": "Eisenhower",
            "C": "Heisenberg",
            "D": "Einstein"
        },
        "correct": "C"
    },
    {
        "question": "84. Quel est l'autre nom de la Birmanie ?",
        "options": {
            "A": "Ceylan",
            "B": "Myanmar",
            "C": "Sri Lanka",
            "D": "Bangladesh"
        },
        "correct": "B"
    },
    {
        "question": "85. Que signifie l'acronyme TAAF ?",
        "options": {
            "A": "Terres australes et arctiques françaises",
            "B": "Terres arctiques et antarctiques françaises",
            "C": "Terres australes et antarctiques françaises",
            "D": "Territoires arctiques et ancestrales françaises"
        },
        "correct": "C"
    },
    {
        "question": "86. Qui a fondé le scoutisme ?",
        "options": {
            "A": "Baden-Powell",
            "B": "Philippe Chatrier",
            "C": "Pierre de Coubertin",
            "D": "Sœur Emmanuel",
            "E": "L'Abbé Pierre"
        },
        "correct": "A"
    },
    {
        "question": "87. Quels besoins apparaissent au sommet de la pyramide de Maslow ?",
        "options": {
            "A": "Les besoins d'appartenance et d'amour",
            "B": "Les besoins d'accomplissement de soi",
            "C": "Les besoins d'estime",
            "D": "Les besoins physiologiques",
            "E": "Les besoins de sécurité"
        },
        "correct": "B"
    },
    {
        "question": "88. En quelle année a été votée l'abolition de la peine de mort en France ?",
        "options": {
            "A": "1981",
            "B": "1968",
            "C": "1989",
            "D": "1980",
            "E": "1990"
        },
        "correct": "A"
    },
    {
        "question": "89. Claude Monet est un peintre français connu pour sa série de toiles intitulée « Les Nymphéas », représentant le jardin de fleurs de sa maison de Giverny. À quel mouvement pictural appartient-il ?",
        "options": {
            "A": "Le surréalisme",
            "B": "L'impressionnisme",
            "C": "Le cubisme",
            "D": "L'Art Nouveau",
            "E": "Le symbolisme"
        },
        "correct": "B"
    },
    {
        "question": "90. Quel événement tragique, survenu en 1897 et faisant plus de 100 victimes, est à l'origine des premières réglementations modernes de prévention contre le risque incendie dans les établissements recevant du public ?",
        "options": {
            "A": "L'attaque du Bon Marché",
            "B": "L'incendie du théâtre de la Comédie française",
            "C": "Le séisme de Lambesc",
            "D": "L'incendie du Bazar de la Charité"
        },
        "correct": "D"
    },
    {
        "question": "91. Dans quelle ville est située le siège du Parlement européen ?",
        "options": {
            "A": "Genève",
            "B": "Bruxelles",
            "C": "Strasbourg",
            "D": "Luxembourg",
            "E": "Zurich"
        },
        "correct": "C"
    },
    {
        "question": "92. Qui a écrit « L'art de la guerre » ?",
        "options": {
            "A": "Sun Tzu",
            "B": "Mao Zedong",
            "C": "Genghis Khan",
            "D": "Xi Jinping",
            "E": "Liu Xiaobo"
        },
        "correct": "A"
    },
    {
        "question": "93. Qui a peint \"Le jugement dernier\" de la chapelle Sixtine à Rome ?",
        "options": {
            "A": "Léonard de Vinci",
            "B": "Raphaël",
            "C": "Michel-Ange",
            "D": "Botticelli",
            "E": "Arcimboldo"
        },
        "correct": "C"
    },
    {
        "question": "94. En vertu de l'article 15 de la Constitution du 4 octobre 1958, qui est le chef des armées ?",
        "options": {
            "A": "Le président de la République",
            "B": "Le chef d'état-major des armées",
            "C": "Le Premier ministre",
            "D": "Le président de l'Assemblée nationale",
            "E": "Le président du Sénat"
        },
        "correct": "A"
    },
    {
        "question": "95. La gendarmerie nationale a été créée le :",
        "options": {
            "A": "14 juillet 1789",
            "B": "16 février 1791",
            "C": "1er janvier 1800",
            "D": "17 avril 1798",
            "E": "23 octobre 1812"
        },
        "correct": "B"
    },
    {
        "question": "96. La gendarmerie est placée sous le patronage de :",
        "options": {
            "A": "Sainte Geneviève",
            "B": "Saint Michel",
            "C": "Sainte Odile",
            "D": "Sainte Cécile",
            "E": "Saint Georges"
        },
        "correct": "B"
    },
    {
        "question": "97. L'Amour est un fleuve qui traverse deux pays :",
        "options": {
            "A": "L'Espagne et le Portugal",
            "B": "La Russie et la Pologne",
            "C": "La Russie et la Chine",
            "D": "La Russie et le Kazakhstan"
        },
        "correct": "C"
    },
    {
        "question": "98. Quelle région autonome chinoise est majoritairement peuplée d'Ouïghours, peuple turcophone et musulman sunnite ?",
        "options": {
            "A": "Tibet",
            "B": "Xinjiang",
            "C": "Mongolie intérieure",
            "D": "Guangxi"
        },
        "correct": "B"
    },
    {
        "question": "99. Quelle est la préfecture la moins peuplée de France ?",
        "options": {
            "A": "Foix",
            "B": "Guéret",
            "C": "Mende",
            "D": "Privas"
        },
        "correct": "A"
    },
    {
        "question": "100. Sous quel nom connaît-on le palais impérial de Pékin ?",
        "options": {
            "A": "La Maison Rouge",
            "B": "Le Fort de Baoji",
            "C": "La Cité interdite",
            "D": "Le Temple Suprême"
        },
        "correct": "C"
    }


]

# Dictionnaire pour la sidebar
qcm_collection = {
    "QCM 2022": qcm2022,
    "QCM 2023": qcm2023,
    "QCM 2024": qcm2024
}

# --- Interface Streamlit ---

# Barre latérale pour choisir le QCM
selected_qcm = st.sidebar.selectbox("Choisissez le QCM :", list(qcm_collection.keys()))
questions = qcm_collection[selected_qcm]

st.title(f"QCM d'évaluation - {selected_qcm}")

# Score global
score = 0

# Parcours de chaque question, correction immédiate
for idx, q in enumerate(questions):
    st.markdown(f"**{q['question']}**")

    # On ajoute un placeholder pour qu'aucune option ne soit présélectionnée
    placeholder_text = "Faites un choix"
    # On concatène ce placeholder au début de la liste d'options
    all_options = [placeholder_text] + list(q["options"].keys())

    # Radio avec index=0 => placeholder sélectionné par défaut
    answer = st.radio(
        "Votre réponse :",
        all_options,
        index=0,
        key=f"q{idx}"
    )

    # Affichage du détail des options
    st.markdown(", ".join([f"**{k}** : {v}" for k, v in q["options"].items()]))

    if answer == placeholder_text:
        # L'utilisateur n'a pas encore fait de choix
        st.warning("Veuillez sélectionner une option.")
    else:
        # Vérification de la réponse
        if answer == q["correct"]:
            st.success(f"Correct ! Votre réponse : {answer} - {q['options'][answer]}")
            score += 1
        else:
            st.error(
                f"Faux. Votre réponse : {answer} - {q['options'][answer]}."
                f" La bonne réponse est : {q['correct']} - {q['options'][q['correct']]}"
            )
    st.write("---")

# Affichage de la note finale
total_questions = len(questions)
if total_questions > 0:
    percentage = (score / total_questions) * 100
    score_out_of_20 = (percentage * 20) / 100
else:
    percentage = 0
    score_out_of_20 = 0

st.subheader(f"Score final : {score} / {total_questions}")
st.subheader(f"Note en pourcentage : {percentage:.2f} %")   # Note sur 100
st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")
