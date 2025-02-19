# qcm2022.py
# ===========

questions = [
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
