import json
import streamlit as st
# Définition des QCM
# ------------------
qcm2021 = [
  {
    "question": "1. En quelle année a été légalisé le recours à l'IVG ?",
    "options": {
      "A": "1975",
      "B": "1981",
      "C": "1969",
      "D": "1970"
    },
    "correct": "A"
  },
  {
    "question": "2. Qui ne fait pas partie du GAFAM ?",
    "options": {
      "A": "Amazon",
      "B": "Microsoft",
      "C": "Google",
      "D": "Mozilla",
      "E": "Facebook"
    },
    "correct": "D"
  },
  {
    "question": "3. Quelle école, fondée en 2013 à l'initiative de Xavier Niel, constitue la première formation en informatique entièrement gratuite, ouverte à tous sans condition de diplôme et accessible dès 18 ans ?",
    "options": {
      "A": "Open Office School",
      "B": "École 42",
      "C": "École informatique opensource",
      "D": "Free e-learning"
    },
    "correct": "B"
  },
  {
    "question": "4. Qui fut officier de cavalerie de l'armée française, explorateur et géographe, puis religieux catholique, prêtre, ermite et linguiste ?",
    "options": {
      "A": "Charles de Foucauld",
      "B": "Michel Foucault",
      "C": "Jean-Pierre Foucault",
      "D": "Charles de la Rochefoucauld"
    },
    "correct": "A"
  },
  {
    "question": "5. Combien dénombre-t-on d'océans ?",
    "options": {
      "A": "3",
      "B": "4",
      "C": "5",
      "D": "6",
      "E": "7"
    },
    "correct": "C"
  },
  {
    "question": "6. En quelle année la gendarmerie a-t-elle été rattachée au ministère de l'intérieur ?",
    "options": {
      "A": "2007",
      "B": "2009",
      "C": "2011",
      "D": "2013",
      "E": "2015"
    },
    "correct": "B"
  },
  {
    "question": "7. Après Lens, quelle ville a accueilli une antenne du Louvre ?",
    "options": {
      "A": "Abou Dabi",
      "B": "Doha",
      "C": "Beauvais",
      "D": "Marseille",
      "E": "Lyon"
    },
    "correct": "A"
  },
  {
    "question": "8. Quelle centrale nucléaire a fermé le 29 juin 2020 ?",
    "options": {
      "A": "Cattenom",
      "B": "Flamanville",
      "C": "Chinon",
      "D": "Fessenheim",
      "E": "Golfech"
    },
    "correct": "D"
  },
  {
    "question": "9. Le G5 Sahel se compose des 5 pays suivants :",
    "options": {
      "A": "Mauritanie, Mali, Burkina Faso, Niger et Tchad",
      "B": "Mauritanie, Mali, Burkina Faso, Soudan et Tchad",
      "C": "Nigeria, Mali, Burkina Faso, Niger et Tchad"
    },
    "correct": "A"
  },
  {
    "question": "10. Quel est le plus long fleuve de France métropolitaine ?",
    "options": {
      "A": "La Meuse",
      "B": "La Seine",
      "C": "Le Rhin",
      "D": "La Loire",
      "E": "Le Rhône"
    },
    "correct": "D"
  },
  {
    "question": "11. Depuis le 1er janvier 2016, combien de régions la France compte-t-elle (outre-mer compris) ?",
    "options": {
      "A": "22",
      "B": "15",
      "C": "18",
      "D": "13",
      "E": "20"
    },
    "correct": "C"
  },
  {
    "question": "12. Quel est le seul acteur français à avoir remporté l'Oscar du meilleur acteur ?",
    "options": {
      "A": "Jean Gabin",
      "B": "Jean Dujardin",
      "C": "Jean-Paul Belmondo",
      "D": "Alain Delon"
    },
    "correct": "B"
  },
  {
    "question": "13. La Vème République française compte actuellement combien de présidents de la République ?",
    "options": {
      "A": "6",
      "B": "7",
      "C": "8",
      "D": "9",
      "E": "10"
    },
    "correct": "C"
  },
  {
    "question": "14. Sur décision de Valéry Giscard d'Estaing, une ancienne gare de Paris a été transformée en musée dédié à l'art de la seconde moitié du XIXème siècle. De quel musée s'agit-il ?",
    "options": {
      "A": "le Musée d'Art Moderne de Paris",
      "B": "le Musée d'Orsay",
      "C": "le Musée Carnavalet",
      "D": "le Musée du Quai Branly",
      "E": "le Centre Pompidou"
    },
    "correct": "B"
  },
  {
    "question": "15. Qu'est-ce que le transhumanisme ?",
    "options": {
      "A": "Une caractéristique qui concerne les personnes dont l'identité sexuelle psychique ne correspond pas au sexe biologique",
      "B": "Une théorie, une doctrine qui place la personne humaine et son épanouissement au-dessus de toutes les autres valeurs",
      "C": "Un courant de pensée selon lequel les capacités physiques et intellectuelles de l'être humain pourraient être accrues grâce au progrès scientifique et technique",
      "D": "Un processus croissant de libre circulation des marchandises, des capitaux, des services, des personnes, des techniques et de l'information",
      "E": "L'ensemble des techniques permettant à des machines d'accomplir des actions ou de résoudre des problèmes normalement réservés à des humains"
    },
    "correct": "C"
  },
  {
    "question": "16. La difficulté, voire l'incapacité, que rencontre une personne à utiliser les appareils numériques et les outils informatiques en raison d'un manque ou d'une absence totale de connaissances à propos de leur fonctionnement se nomme :",
    "options": {
      "A": "l'illectronisme",
      "B": "l'illettrisme",
      "C": "le lectronisme",
      "D": "l'e-inclusion"
    },
    "correct": "A"
  },
  {
    "question": "17. En vertu de l'article 24 de la Constitution de la Ve République, quelle institution est la représentante des collectivités territoriales et siège au palais du Luxembourg ?",
    "options": {
      "A": "la Cour de justice de la République",
      "B": "le Conseil Économique, Social et Environnemental",
      "C": "le Conseil Constitutionnel",
      "D": "le Sénat",
      "E": "le Parlement"
    },
    "correct": "D"
  },
  {
    "question": "18. Dans la hiérarchie des normes, quel bloc normatif se situe à la base de la pyramide ?",
    "options": {
      "A": "le bloc conventionnel",
      "B": "le bloc législatif",
      "C": "le bloc réglementaire",
      "D": "le bloc constitutionnel"
    },
    "correct": "D"
  },
  {
    "question": "19. Quel État est devenu le 28ème État de l'Union européenne le 1er juillet 2013 ?",
    "options": {
      "A": "Bulgarie",
      "B": "Roumanie",
      "C": "Turquie",
      "D": "Chypre",
      "E": "Croatie"
    },
    "correct": "E"
  },
  {
    "question": "20. Créée en 1800, l'institution préfectorale a été instituée par :",
    "options": {
      "A": "Napoléon",
      "B": "Louis XIV",
      "C": "Adolphe Thiers",
      "D": "Félix Faure",
      "E": "Charles X"
    },
    "correct": "A"
  },
  {
    "question": "21. Qui est l'auteur du célèbre article « J'accuse... ! », publié dans le quotidien L'Aurore en janvier 1898, au sujet de l'affaire Dreyfus ?",
    "options": {
      "A": "Émile Zola",
      "B": "Jules Verne",
      "C": "Louis Aragon",
      "D": "Victor Hugo",
      "E": "Gustave Flaubert"
    },
    "correct": "A"
  },
  {
    "question": "22. L'acide désoxyribonucléique constitue la molécule support de l'information :",
    "options": {
      "A": "génétique héréditaire",
      "B": "neuronale",
      "C": "musculaire",
      "D": "empathique cognitive",
      "E": "nerveuse"
    },
    "correct": "A"
  },
  {
    "question": "23. Quel était le surnom de Louis IX ?",
    "options": {
      "A": "Louis le Pieux",
      "B": "Saint-Louis",
      "C": "le roi Soleil",
      "D": "Louis de Cambridge"
    },
    "correct": "B"
  },
  {
    "question": "24. À qui succède Angela Merkel en 2005 au poste de chancelière d'Allemagne fédérale ?",
    "options": {
      "A": "Helmut Kohl",
      "B": "Gerhard Schröder",
      "C": "Konrad Adenauer",
      "D": "Willy Brandt"
    },
    "correct": "B"
  },
  {
    "question": "25. Qu'est-ce que l'ypérite ?",
    "options": {
      "A": "une inflammation des bronches",
      "B": "un type de livraison à domicile",
      "C": "un composé chimique",
      "D": "une spécialité culinaire flamande"
    },
    "correct": "C"
  },
  {
    "question": "26. Qu'est-ce qu'un céphalopode ?",
    "options": {
      "A": "un mollusque carnassier",
      "B": "un nerf crânien",
      "C": "un aliment riche en lipide",
      "D": "un type de cigarette électronique"
    },
    "correct": "A"
  },
  {
    "question": "27. Qui a écrit « Les lettres de mon moulin » ?",
    "options": {
      "A": "Jean Moulin",
      "B": "Alphonse Daudet",
      "C": "Jacques Meunier",
      "D": "Jean Lassalle"
    },
    "correct": "B"
  },
  {
    "question": "28. Qui était Aimé Césaire ?",
    "options": {
      "A": "un écrivain",
      "B": "l'inventeur de l'aspirine effervescente",
      "C": "un navigateur",
      "D": "un chirurgien obstétricien"
    },
    "correct": "A"
  },
  {
    "question": "29. Les guerres médiques se sont principalement déroulées :",
    "options": {
      "A": "dans la région de Médine",
      "B": "autour de la mer Égée",
      "C": "au nord du Médoc",
      "D": "aux abords de Carthage"
    },
    "correct": "B"
  },
  {
    "question": "30. Laquelle de ces propositions ne désigne pas une ville d'Allemagne ?",
    "options": {
      "A": "Ramstein",
      "B": "Aix-la-Chapelle",
      "C": "Maastricht",
      "D": "Rostock"
    },
    "correct": "C"
  },
  {
    "question": "31. Dans l'univers politique français, les initiales VGE désignent :",
    "options": {
      "A": "Valérie Giscard d'Esteing",
      "B": "Valéry Giscard d'Estaing",
      "C": "Valéry Giscard d'Estraing",
      "D": "Valéry Giscard d'Esteing"
    },
    "correct": "B"
  },
  {
    "question": "32. Quel texte est connu pour avoir imposé le Français dans les documents officiels ?",
    "options": {
      "A": "l'édit de Nantes",
      "B": "l'ordonnance de Villers-Cotterêts",
      "C": "la Magna Carta",
      "D": "l'Anabase"
    },
    "correct": "B"
  },
  {
    "question": "33. Lequel de ces musiciens n'a jamais fait partie du groupe de rock U2 ?",
    "options": {
      "A": "Bono",
      "B": "The Edge",
      "C": "Adam Clayton",
      "D": "George Harrison"
    },
    "correct": "D"
  },
  {
    "question": "34. En construction immobilière, le commanditaire du projet est appelé :",
    "options": {
      "A": "le maître des clés",
      "B": "le maître d'œuvre",
      "C": "le maître d'ouvrage",
      "D": "le quartier-maître"
    },
    "correct": "C"
  },
  {
    "question": "35. En économie française, le RSA est :",
    "options": {
      "A": "le revenu de solidarité active",
      "B": "le revenu solidaire auto-indexé",
      "C": "le revenu social aménagé",
      "D": "le revenu solidaire anticipé"
    },
    "correct": "A"
  },
  {
    "question": "36. En France, un maire est élu pour :",
    "options": {
      "A": "7 ans",
      "B": "4 ans",
      "C": "5 ans",
      "D": "6 ans"
    },
    "correct": "D"
  },
  {
    "question": "37. Les maisons de retraite médicalisées sont également connues sous l'acronyme :",
    "options": {
      "A": "HEPAD",
      "B": "EHPAD",
      "C": "EPAHD",
      "D": "EPADH"
    },
    "correct": "B"
  },
  {
    "question": "38. Lequel de ces spationautes français fut le dernier à partir dans l'espace ?",
    "options": {
      "A": "Patrick Baudry",
      "B": "Jean-Loup Chrétien",
      "C": "Jean-Pierre Haigneré",
      "D": "Thomas Pesquet",
      "E": "Michel Tognini"
    },
    "correct": "D"
  },
  {
    "question": "39. Daniel CORDIER était-il :",
    "options": {
      "A": "l'avant-dernier survivant des compagnons de la Libération",
      "B": "le dernier survivant des compagnons de la Libération",
      "C": "le dernier poilu survivant de la Grande Guerre",
      "D": "membre des Francs-Tireurs et Partisans (FTP)",
      "E": "membre du réseau Saint-Jacques"
    },
    "correct": "B"
  },
  {
    "question": "40. Samuel Huntington a écrit :",
    "options": {
      "A": "Le choc des civilisations",
      "B": "La fin de l'histoire ?",
      "C": "Théorie de la justice",
      "D": "L'idée de justice",
      "E": "Logique et métaphysique"
    },
    "correct": "A"
  },
  {
    "question": "41. La Cour Pénale Internationale (CPI) siège à :",
    "options": {
      "A": "Genève",
      "B": "Montevideo",
      "C": "Strasbourg",
      "D": "Bruxelles",
      "E": "La Haye"
    },
    "correct": "E"
  },
  {
    "question": "42. Quelle est la valeur d'un euro en francs français ?",
    "options": {
      "A": "6,5",
      "B": "6,5595",
      "C": "6,55959",
      "D": "6,55957",
      "E": "0,15244"
    },
    "correct": "D"
  },
  {
    "question": "43. Quelle est la nationalité du secrétaire général de l'ONU actuellement ?",
    "options": {
      "A": "coréenne",
      "B": "sud-coréenne",
      "C": "portugaise",
      "D": "égyptienne",
      "E": "ghanéenne"
    },
    "correct": "C"
  },
  {
    "question": "44. Parmi ces rayonnements, lesquels sont les moins pénétrants ?",
    "options": {
      "A": "Rayonnements alpha",
      "B": "Rayonnements bêta",
      "C": "Rayonnements gamma",
      "D": "Rayonnements X",
      "E": "Rayonnements neutroniques"
    },
    "correct": "A"
  },
  {
    "question": "45. Quelle part du globe terrestre est-elle recouverte par les océans ?",
    "options": {
      "A": "65,3 %",
      "B": "58,7 %",
      "C": "91,2 %",
      "D": "70,8 %",
      "E": "87,6 %"
    },
    "correct": "D"
  },
  {
    "question": "46. Où siège la Cour de justice de l'Union Européenne ?",
    "options": {
      "A": "La Haye",
      "B": "Strasbourg",
      "C": "Bruxelles",
      "D": "Luxembourg",
      "E": "Maastricht"
    },
    "correct": "D"
  },
  {
    "question": "47. Quelle équipe de football joue dans l'enceinte du stade Santiago Bernabeu ?",
    "options": {
      "A": "FC Barcelone",
      "B": "Real Madrid",
      "C": "Malaga CF",
      "D": "FC Porto",
      "E": "Atlético de Madrid"
    },
    "correct": "B"
  },
  {
    "question": "48. Quelle période est qualifiée de « Trente glorieuses » ?",
    "options": {
      "A": "1900 - 1930",
      "B": "1915 - 1945",
      "C": "1927 - 1960",
      "D": "1945 - 1973",
      "E": "1980 - 2008"
    },
    "correct": "D"
  },
  {
    "question": "49. Pour quel établissement bancaire travaillait le trader Jérôme Kerviel quand l'affaire éclata ?",
    "options": {
      "A": "Crédit Lyonnais",
      "B": "Société Générale",
      "C": "Banque Populaire",
      "D": "BNP Paribas",
      "E": "Crédit Agricole"
    },
    "correct": "B"
  },
  {
    "question": "50. Quand la pyramide de Khéops a-t-elle été construite ?",
    "options": {
      "A": "Vers 4000 avant J-C",
      "B": "Vers 2560 avant J-C",
      "C": "Vers 1200 avant J-C",
      "D": "Vers 50 avant J-C"
    },
    "correct": "B"
  },
  {
    "question": "51. Quel homme politique français instaure les congés payés en 1936 ?",
    "options": {
      "A": "Gaston Doumergue",
      "B": "René Coty",
      "C": "Léon Blum",
      "D": "Pierre Laval"
    },
    "correct": "C"
  },
  {
    "question": "52. Edson Arantes do Nascimento est une des personnalités sportives les plus célèbres au monde. De qui s'agit-il ?",
    "options": {
      "A": "Maradona",
      "B": "Ronaldo",
      "C": "Fangio",
      "D": "Pelé"
    },
    "correct": "D"
  },
  {
    "question": "53. La découverte du vaccin antirabique vaudra à Pasteur sa consécration dans le monde entier et lui offrira de nombreuses distinctions. En quelle année a-t-il découvert ce vaccin ?",
    "options": {
      "A": "En 1853",
      "B": "En 1885",
      "C": "En 1921",
      "D": "En 1937",
      "E": "En 1946"
    },
    "correct": "B"
  },
  {
    "question": "54. En informatique, le HyperText Markup Language (HTML) est :",
    "options": {
      "A": "Un protocole de cryptage et décryptage de données",
      "B": "Une norme de codage d'adresses d'ordinateurs",
      "C": "Un langage de balisage pour présenter des pages web",
      "D": "Une adresse de serveur internet"
    },
    "correct": "C"
  },
  {
    "question": "55. Joseph Robinette Biden a remporté les dernières élections américaines. Il est investi président des États-Unis d'Amérique en janvier 2021. Combien de prédécesseurs a-t-il eu ?",
    "options": {
      "A": "42",
      "B": "44",
      "C": "51",
      "D": "45"
    },
    "correct": "D"
  },
  {
    "question": "56. Les opérateurs de téléphonie mobile déploient progressivement la 5G en France métropolitaine. Cette technologie permet des évolutions significatives par rapport à la 4G. Parmi les affirmations suivantes, laquelle est fausse ?",
    "options": {
      "A": "La 5G sera 100 fois plus rapide que la 4G",
      "B": "La 5G présentera un temps de latence 10 fois moins important que la 4G",
      "C": "La 5G permettra de supprimer les zones blanches non couvertes par la 4G",
      "D": "Il sera possible de visionner des vidéos 4K sans que la mémoire tampon ne se charge",
      "E": "La 5G sera la technologie des objets connectés"
    },
    "correct": "C"
  },
  {
    "question": "57. Le Système International est un système comportant des unités destinées à mesurer des grandeurs physiques indépendantes et possédant chacune un symbole. Parmi celles citées ci-dessous, l'une est fausse, laquelle ?",
    "options": {
      "A": "Masse - Kilogramme",
      "B": "Temps - Seconde",
      "C": "Longueur - Mètre",
      "D": "Température - Degré",
      "E": "Intensité électrique - Ampère"
    },
    "correct": "D"
  },
  {
    "question": "58. Quel état a la plus grande densité de population ?",
    "options": {
      "A": "Inde",
      "B": "Monaco",
      "C": "Le Vatican",
      "D": "Japon",
      "E": "Singapour"
    },
    "correct": "B"
  },
  {
    "question": "59. En informatique, le Hypertext Transfer Protocol (HTTP) est :",
    "options": {
      "A": "Une clé de résolution de mot de passe",
      "B": "Une adresse de serveur internet",
      "C": "Un hyperlien permettant l'accès direct à un site web",
      "D": "Un protocole de communication client - serveur"
    },
    "correct": "D"
  },
  {
    "question": "60. Parmi les religions ci-dessous, laquelle n'est pas monothéiste ?",
    "options": {
      "A": "Le bouddhisme",
      "B": "Le judaïsme",
      "C": "L'Islam",
      "D": "Le christianisme",
      "E": "Le sikhisme"
    },
    "correct": "A"
  },
  {
    "question": "61. Parmi les courants de pensée généraux cités ci-dessous, lequel n'est pas un courant philosophique ?",
    "options": {
      "A": "Le stoïcisme",
      "B": "Le rationalisme",
      "C": "L'obscurantisme",
      "D": "Le positivisme",
      "E": "Le cynisme"
    },
    "correct": "C"
  },
  {
    "question": "62. La profondeur moyenne des océans est de l'ordre de 3700 à 3800 mètres. Quel est l'endroit le plus profond au monde ?",
    "options": {
      "A": "Le détroit de Fram",
      "B": "La fosse des Sandwich Sud",
      "C": "La fosse de Porto Rico",
      "D": "La fosse de Java",
      "E": "La fosse des Mariannes"
    },
    "correct": "E"
  },
  {
    "question": "63. Quel est le statut politique de l'Espagne ?",
    "options": {
      "A": "Monarchie absolue",
      "B": "Monarchie parlementaire",
      "C": "République",
      "D": "République fédérale"
    },
    "correct": "B"
  },
  {
    "question": "64. Comment est appelée la loi du 18 septembre 1981 relative à l'abolition de la peine de mort ?",
    "options": {
      "A": "Loi Badinter",
      "B": "Loi Hernu",
      "C": "Loi Joxe",
      "D": "Loi Mauroy",
      "E": "Loi Rocard"
    },
    "correct": "A"
  },
  {
    "question": "65. Quel fleuve traverse Bagdad ?",
    "options": {
      "A": "Le Nil",
      "B": "Le Tibre",
      "C": "Le Tigre",
      "D": "L'Euphrate"
    },
    "correct": "C"
  },
  {
    "question": "66. Comment est classifié le « super-éthanol » ?",
    "options": {
      "A": "E5",
      "B": "E10",
      "C": "E85",
      "D": "B7",
      "E": "B10"
    },
    "correct": "C"
  },
  {
    "question": "67. À quelle distance de la Terre se situe l'orbite géostationnaire ?",
    "options": {
      "A": "à 23.000 km",
      "B": "à 36.000 km",
      "C": "à 40.000 km",
      "D": "à 43.000 km",
      "E": "à 51.000 km"
    },
    "correct": "B"
  },
  {
    "question": "68. Quel pilote a franchi le mur du son pour la première fois ?",
    "options": {
      "A": "Chuck Yeager",
      "B": "Daniel Rastel",
      "C": "John Derry",
      "D": "H. J. Wilson"
    },
    "correct": "A"
  },
  {
    "question": "69. À quoi correspond la température de -273,15°C ?",
    "options": {
      "A": "L'azote liquide",
      "B": "Le zéro absolu",
      "C": "La température de la face cachée de la lune",
      "D": "La température à la surface de la planète Pluton"
    },
    "correct": "B"
  },
  {
    "question": "70. Quelle unité mesure la fréquence du courant alternatif ?",
    "options": {
      "A": "l'ampère",
      "B": "le hertz",
      "C": "l'ohm",
      "D": "le volt",
      "E": "le watt"
    },
    "correct": "B"
  },
  {
    "question": "71. Comment s'appelle la maladie infectieuse provoquée par le bacille de Koch ?",
    "options": {
      "A": "La peste",
      "B": "La tuberculose",
      "C": "La poliomyélite",
      "D": "La gale"
    },
    "correct": "B"
  },
  {
    "question": "72. Qui a créé l'Académie Française ?",
    "options": {
      "A": "Louis IV",
      "B": "Henry IV",
      "C": "Le cardinal de Richelieu",
      "D": "Le cardinal Mazarin"
    },
    "correct": "C"
  },
  {
    "question": "73. Où se trouve le siège de l'UNESCO ?",
    "options": {
      "A": "Londres",
      "B": "Paris",
      "C": "New York",
      "D": "Genève"
    },
    "correct": "B"
  },
  {
    "question": "74. Qui fut la première présidente du Parlement européen ?",
    "options": {
      "A": "Edith CRESSON",
      "B": "Margaret THATCHER",
      "C": "Simone VEIL",
      "D": "Aucune femme n'a occupé ce poste"
    },
    "correct": "C"
  },
  {
    "question": "75. Parmi ces sources d'énergie, laquelle n'est pas renouvelable ?",
    "options": {
      "A": "L'énergie hydraulique",
      "B": "L'énergie éolienne",
      "C": "Le bois",
      "D": "Le charbon"
    },
    "correct": "D"
  },
  {
    "question": "76. Quelle est la principale réalisation d'Alan Turing durant la Seconde Guerre Mondiale ?",
    "options": {
      "A": "Décrypter la machine Enigma",
      "B": "Diriger la contre-offensive des Ardennes",
      "C": "Négocier les accords de Yalta",
      "D": "Diriger le principal réseau d'espionnage américain sur le sol allemand"
    },
    "correct": "A"
  },
  {
    "question": "77. Le premier satellite artificiel de la terre se nomme :",
    "options": {
      "A": "Galileo",
      "B": "Apollo",
      "C": "Spoutnik",
      "D": "Vostok"
    },
    "correct": "C"
  },
  {
    "question": "78. Qui appelle-t-on « les malgré nous » ?",
    "options": {
      "A": "un groupe de résistants particulièrement violents",
      "B": "un parti politique",
      "C": "un groupe d'hommes et de femmes voué à la religion",
      "D": "les alsaciens et les mosellans incorporés de force lors de la Deuxième Guerre Mondiale",
      "E": "les politiciens déchus"
    },
    "correct": "D"
  },
  {
    "question": "79. Pendant les événements d'Algérie, une organisation politico-militaire clandestine française dénommée O.A.S s'oppose au processus d'indépendance. Que signifie ce sigle ?",
    "options": {
      "A": "organe de l'armée du sud",
      "B": "organisation de l'armée secrète",
      "C": "organisation d'attaques et de soulèvements",
      "D": "opposition algérienne de Sidi Bou Said"
    },
    "correct": "B"
  },
  {
    "question": "80. Quelle ville de France a vu le sacre de 35 rois ?",
    "options": {
      "A": "Avignon",
      "B": "Reims",
      "C": "Marseille",
      "D": "Bordeaux",
      "E": "Strasbourg"
    },
    "correct": "B"
  },
  {
    "question": "81. Qu'est-ce que le catharisme ?",
    "options": {
      "A": "une pathologie concernant la cataracte",
      "B": "un parti politique espagnol proche de Franco",
      "C": "un mouvement religieux médiéval dissident de l'Église catholique",
      "D": "un groupe de partisans italiens s'opposant au Vatican",
      "E": "une région portugaise"
    },
    "correct": "C"
  },
  {
    "question": "82. L'expression « œil pour œil, dent pour dent » symbolise une loi ancienne consistant en la réciprocité du crime et de la peine. Quelle est l'appellation de cette loi ?",
    "options": {
      "A": "La loi de la réciprocité",
      "B": "La loi équitable",
      "C": "La loi du Juste",
      "D": "La loi du Talion",
      "E": "La loi Vercingétorix"
    },
    "correct": "D"
  },
  {
    "question": "83. Le 10 novembre 1920, André Maginot préside la cérémonie du choix du soldat inconnu, dont le corps sera inhumé dans une tombe installée sous l'Arc de Triomphe à Paris. Dans quel lieu et dans quelle ville s'est déroulée cette cérémonie ?",
    "options": {
      "A": "Fort de Vincennes",
      "B": "Citadelle de Verdun",
      "C": "Citadelle de Namur",
      "D": "Citadelle de Lille",
      "E": "Fort de Rosny sous Bois"
    },
    "correct": "B"
  },
  {
    "question": "84. Le tableau intitulé « Guernica » date de 1937. Il est l'œuvre de :",
    "options": {
      "A": "Salvador Dali",
      "B": "Pablo Picasso",
      "C": "Joan Miro",
      "D": "Oscar Dominguez"
    },
    "correct": "B"
  },
  {
    "question": "85. Quel a été le dernier Maréchal de France nommé de son vivant ?",
    "options": {
      "A": "Alphonse Juin",
      "B": "Hubert Liautey",
      "C": "Joseph Joffre"
    },
    "correct": "A"
  },
  {
    "question": "86. Quel est le nom du président de la République populaire de Chine ?",
    "options": {
      "A": "Jiang Zemin",
      "B": "Xi Jinping",
      "C": "Hu Jintao",
      "D": "Li Keqiang"
    },
    "correct": "B"
  },
  {
    "question": "87. Parmi ces affaires célèbres, laquelle n'est pas un scandale financier ?",
    "options": {
      "A": "La bataille d'Hernani (1830)",
      "B": "Le scandale de Panama (1892)",
      "C": "La pyramide de Ponzi (1920)",
      "D": "L'affaire Stavisky (1933)",
      "E": "L'affaire Enron (2001)"
    },
    "correct": "A"
  },
  {
    "question": "88. La pyramide de Maslow est :",
    "options": {
      "A": "la schématisation proposée par Maslow des besoins humains autour de 5 niveaux",
      "B": "le nom donné pour désigner un système financier frauduleux",
      "C": "la hiérarchisation des normes juridiques",
      "D": "l'une des pyramides de Gizeh",
      "E": "la hiérarchisation de six familles d'aliments selon la place qu'ils doivent occuper dans une alimentation équilibrée"
    },
    "correct": "A"
  },
  {
    "question": "89. Quel leader britannique a été le fer de lance de l'hostilité au maintien du Royaume-Uni dans l'Union européenne en 2016 ?",
    "options": {
      "A": "David Cameron",
      "B": "Boris Johnson",
      "C": "Theresa May",
      "D": "Gerry Adams",
      "E": "Tony Blair"
    },
    "correct": "B"
  },
  {
    "question": "90. Quel est le nom du président turc depuis 2014 ?",
    "options": {
      "A": "Hassan Rohani",
      "B": "Mohammed Ben Salman",
      "C": "Recep Tayyip Erdogan",
      "D": "Abdel Fattah Al-Sissi",
      "E": "Bachar El-Assad"
    },
    "correct": "C"
  },
  {
    "question": "91. Qui est le vainqueur du Vendée Globe 2020/2021 ?",
    "options": {
      "A": "Michel Desjoyeaux",
      "B": "Yannick Bestaven",
      "C": "Armel Le Cléac'h",
      "D": "Jean Le Cam"
    },
    "correct": "B"
  },
  {
    "question": "92. Quelle est la seule figure historique féminine à être représentée par un buste à l'Assemblée Nationale ?",
    "options": {
      "A": "Marie Curie",
      "B": "Olympe de Gouges",
      "C": "Simone Veil",
      "D": "La Duchesse de Bourbon"
    },
    "correct": "B"
  },
  {
    "question": "93. Le Congrès peut adopter une réforme constitutionnelle, à quelle majorité ?",
    "options": {
      "A": "51 %",
      "B": "60 %",
      "C": "66 %"
    },
    "correct": "B"
  },
  {
    "question": "94. Qu'appelle-t-on Station F ?",
    "options": {
      "A": "Le plus grand campus de start-ups au monde installé à Paris",
      "B": "La station spatiale Force 1",
      "C": "Le centre de recherche de Facebook en Californie"
    },
    "correct": "A"
  },
  {
    "question": "95. En 2020, a été célébré le 250ème anniversaire de la naissance d'un musicien. Il s'agit de :",
    "options": {
      "A": "Verdi",
      "B": "Debussy",
      "C": "Wagner",
      "D": "Prokofiev",
      "E": "Beethoven"
    },
    "correct": "E"
  },
  {
    "question": "96. Une plateforme de signalement sur internet a été ouverte en novembre 2018 ; quel type de violences vise-t-elle ?",
    "options": {
      "A": "Les violences racistes et antisémites",
      "B": "Les violences homophobes",
      "C": "Les violences sexuelles et sexistes",
      "D": "Les violences en milieu scolaire"
    },
    "correct": "C"
  },
  {
    "question": "97. Combien de degrés comporte l'échelle de Richter ?",
    "options": {
      "A": "6",
      "B": "8",
      "C": "10",
      "D": "12",
      "E": "Illimité"
    },
    "correct": "E"
  },
  {
    "question": "98. Qui a été nommé négociateur en chef du « Brexit » pour l'Union Européenne en juillet 2016 ?",
    "options": {
      "A": "Theresa May",
      "B": "Jean-Claude Juncker",
      "C": "Michel Barnier",
      "D": "Jean-Yves Le Drian"
    },
    "correct": "C"
  },
  {
    "question": "99. Quel prix Nobel n'existe pas ?",
    "options": {
      "A": "le prix Nobel de physique",
      "B": "le prix Nobel de mathématiques",
      "C": "le prix Nobel de littérature",
      "D": "le prix Nobel de sciences économiques"
    },
    "correct": "B"
  },
  {
    "question": "100. Quels sont les six pays fondateurs de l'Union Européenne ?",
    "options": {
      "A": "Allemagne, France, Espagne, Luxembourg, Pays-Bas, Pologne",
      "B": "France, Espagne, Italie, Portugal, Danemark, Pays-Bas",
      "C": "Allemagne, Belgique, France, Italie, Luxembourg, Pays-Bas",
      "D": "Espagne, Portugal, France, Italie, Norvège, Belgique",
      "E": "Belgique, Danemark, Pays-Bas, France, Italie, Autriche"
    },
    "correct": "C"
  }
]


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
    "question": "1. En musique, la double croche vaut :",
    "options": {
      "A": "une croche pointée",
      "B": "un quart de noire",
      "C": "la moitié d'une ronde",
      "D": "la moitié d'une blanche"
    },
    "correct": "B"
  },
  {
    "question": "2. Jacques Brel repose :",
    "options": {
      "A": "aux Antilles",
      "B": "aux Marquises",
      "C": "aux îles Féroé",
      "D": "à Miquelon"
    },
    "correct": "B"
  },
  {
    "question": "3. La circulaire du ministère de l'Éducation nationale du 5 mai 2021 interdit, dans l'enseignement et les actes administratifs, l'usage de l'écriture :",
    "options": {
      "A": "cursive",
      "B": "inclusive",
      "C": "révulsive",
      "D": "déconstructive"
    },
    "correct": "B"
  },
  {
    "question": "4. La bataille \"des éperons d'or\" a opposé en 1302 l'armée du roi de France Philippe le Bel à des miliciens :",
    "options": {
      "A": "bourguignons",
      "B": "flamands",
      "C": "cathares",
      "D": "bretons"
    },
    "correct": "B"
  },
  {
    "question": "5. En 2022, parmi les unités ukrainiennes combattant à Marioupol figure le bataillon :",
    "options": {
      "A": "Popov",
      "B": "Azov",
      "C": "Koutouzov",
      "D": "Asimov"
    },
    "correct": "B"
  },
  {
    "question": "6. En janvier 2022, on a fêté les 400 ans de la naissance de :",
    "options": {
      "A": "Jean-Baptiste Poquelin",
      "B": "François-Marie Arouet",
      "C": "Sébastien Le Prestre"
    },
    "correct": "A"
  },
  {
    "question": "7. Le 8 septembre 2022, décède la reine Élisabeth II. Une série télévisée raconte son histoire, il s'agit de :",
    "options": {
      "A": "Downton Abbey",
      "B": "The Crown",
      "C": "Braveheart",
      "D": "Young Royals"
    },
    "correct": "B"
  },
  {
    "question": "8. Le père Daniel Brottier est :",
    "options": {
      "A": "cofondateur d'une entreprise de chaussure pour les soldats de 1914",
      "B": "cofondateur de l'union nationale des combattants",
      "C": "cofondateur d'une entreprise de cinéma",
      "D": "un hermite à Dakar"
    },
    "correct": "B"
  },
  {
    "question": "9. En matière budgétaire, la LOLF répartit les crédits du budget général de l'État par missions, programmes et :",
    "options": {
      "A": "activités",
      "B": "actions",
      "C": "autorisations",
      "D": "allocations"
    },
    "correct": "B"
  },
  {
    "question": "10. Laquelle de ces appellations de vin n'est pas située en Gironde :",
    "options": {
      "A": "Entre deux mers",
      "B": "Bonnezeaux",
      "C": "Moulis",
      "D": "Sauternes"
    },
    "correct": "B"
  },
  {
    "question": "11. En 2014 à Hong-Kong, quel objet usuel devient le symbole des manifestants pour la démocratie ?",
    "options": {
      "A": "le parapluie",
      "B": "le mouchoir",
      "C": "le chapeau melon"
    },
    "correct": "A"
  },
  {
    "question": "12. Taïwan est autrement connu sous le nom de :",
    "options": {
      "A": "Ceylan",
      "B": "Formose",
      "C": "Guam",
      "D": "Andaman-et-Nicobar"
    },
    "correct": "B"
  },
  {
    "question": "13. Quelle marque de calculatrice est associée à la logique polonaise inverse ?",
    "options": {
      "A": "Casio",
      "B": "Texas Instrument",
      "C": "Hewlett-Packard"
    },
    "correct": "C"
  },
  {
    "question": "14. Parmi ces zones de défense, laquelle comprend une seule région ?",
    "options": {
      "A": "Sud",
      "B": "Sud-ouest",
      "C": "Ouest"
    },
    "correct": "A"
  },
  {
    "question": "15. La commune d'Hondschoote est :",
    "options": {
      "A": "belge",
      "B": "française",
      "C": "néerlandaise",
      "D": "luxembourgeoise"
    },
    "correct": "C"
  },
  {
    "question": "16. S'agissant de leur position sur la carte de l'Europe, classer ces pays du Nord au Sud :",
    "options": {
      "A": "Estonie - Lituanie - Lettonie",
      "B": "Estonie - Lettonie - Lituanie",
      "C": "Lettonie - Estonie - Lituanie",
      "D": "Lituanie - Lettonie - Estonie",
      "E": "Lettonie - Lituanie - Estonie"
    },
    "correct": "B"
  },
  {
    "question": "17. La capitale de la Biélorussie est :",
    "options": {
      "A": "Riga",
      "B": "Tallinn",
      "C": "Minsk",
      "D": "Vilnius",
      "E": "Chisinau"
    },
    "correct": "C"
  },
  {
    "question": "18. En gastronomie, le thymus du veau s'appelle aussi :",
    "options": {
      "A": "le filet mignon",
      "B": "le rognon",
      "C": "le ris",
      "D": "le foie",
      "E": "l'araignée"
    },
    "correct": "C"
  },
  {
    "question": "19. Dans la locution « ci-gît », la seconde partie est une conjugaison du verbe :",
    "options": {
      "A": "gire",
      "B": "gîter",
      "C": "gésir",
      "D": "gigoter"
    },
    "correct": "C"
  },
  {
    "question": "20. La suspension du service national a été décidée par :",
    "options": {
      "A": "Valéry Giscard d'Estaing",
      "B": "François Mitterrand",
      "C": "Nicolas Sarkozy",
      "D": "Jacques Chirac",
      "E": "Paul Deschanel"
    },
    "correct": "D"
  },
  {
    "question": "21. Il a succédé à Louis XVIII :",
    "options": {
      "A": "Louis-Philippe 1er",
      "B": "Henri IV",
      "C": "Napoléon 1er"
    },
    "correct": "A"
  },
  {
    "question": "22. Le Myanmar est l'autre nom de :",
    "options": {
      "A": "la Birmanie",
      "B": "Formose",
      "C": "Ceylan",
      "D": "Hong Kong",
      "E": "la Mandchourie"
    },
    "correct": "A"
  },
  {
    "question": "23. Le pont d'Aquitaine enjambe :",
    "options": {
      "A": "la Dordogne",
      "B": "la Garonne",
      "C": "la Leyre",
      "D": "l'Adour"
    },
    "correct": "B"
  },
  {
    "question": "24. Combien y a-t-il de dynasties dans la monarchie française ?",
    "options": {
      "A": "3",
      "B": "4",
      "C": "5",
      "D": "6"
    },
    "correct": "C"
  },
  {
    "question": "25. Qui sont Snowball et Napoléon dans La Ferme des animaux de George ORWELL ?",
    "options": {
      "A": "Des chiens",
      "B": "Des lapins",
      "C": "Des agriculteurs",
      "D": "Des cochons",
      "E": "Des otages"
    },
    "correct": "D"
  },
  {
    "question": "26. Qu'est-ce que la loi salique ?",
    "options": {
      "A": "Une loi de nationalisation des biens du clergé",
      "B": "Une loi interdisant aux femmes d'accéder au trône de France",
      "C": "Une loi régissant la perception de l'impôt sur le sel",
      "D": "Une loi imposant la pratique du français dans les actes administratifs"
    },
    "correct": "B"
  },
  {
    "question": "27. Qui a dit « Vous n'avez pas le monopole du cœur » ?",
    "options": {
      "A": "Valéry GISCARD D'ESTAING",
      "B": "Pierre CURIE",
      "C": "François MITTERAND",
      "D": "Émile ZOLA",
      "E": "Antoine de ST EXUPERY"
    },
    "correct": "A"
  },
  {
    "question": "28. Qui a peint le tableau « La liberté guidant le peuple » ?",
    "options": {
      "A": "Paul CÉZANNE",
      "B": "Théodore GÉRICAULT",
      "C": "Auguste RENOIR",
      "D": "Eugène DELACROIX"
    },
    "correct": "D"
  },
  {
    "question": "29. Laquelle de ces directions n'appartient pas au ministère de l'Intérieur ?",
    "options": {
      "A": "La direction générale de la police nationale",
      "B": "La direction générale des douanes et des droits indirects",
      "C": "La direction générale de la sécurité intérieure",
      "D": "La direction générale des collectivités locales",
      "E": "La direction générale de la sécurité civile et de la gestion des crises"
    },
    "correct": "D"
  },
  {
    "question": "30. Que prévoit l'article 16 de la Constitution de la Vème République ?",
    "options": {
      "A": "Les conditions de mise en œuvre de l'état d'urgence",
      "B": "L'organisation de l'autorité judiciaire",
      "C": "Les pouvoirs exceptionnels accordés au président de la République en cas de menace grave et immédiate pesant sur la Nation et ses institutions",
      "D": "La responsabilité pénale des membres du gouvernement agissant dans l'exercice de leurs fonctions"
    },
    "correct": "C"
  },
  {
    "question": "31. Au début des années 1930, plusieurs millions d'Ukrainiens périssent au cours de l'Holodomor. De quoi s'agit-il ?",
    "options": {
      "A": "Une grande famine",
      "B": "Une guerre civile",
      "C": "Une campagne de tests de missiles balistiques soviétiques",
      "D": "Une pandémie"
    },
    "correct": "A"
  },
  {
    "question": "32. Laquelle de ces institutions n'appartient pas à l'Union européenne ?",
    "options": {
      "A": "Le parlement européen",
      "B": "La commission européenne",
      "C": "Le conseil de l'Union européenne",
      "D": "La cour européenne des droits de l'homme"
    },
    "correct": "D"
  },
  {
    "question": "33. « Selon que vous serez puissant ou misérable, les jugements de cour vous rendront blanc ou noir » est la morale d'une fable de Jean de la FONTAINE. Laquelle ?",
    "options": {
      "A": "Le Lion et le Rat",
      "B": "Le Lièvre et la Tortue",
      "C": "Les animaux malades de la Peste",
      "D": "Le Corbeau et le Renard"
    },
    "correct": "C"
  },
  {
    "question": "34. Quel artiste francophone évoque ses difficultés psychologiques dans sa chanson « L'enfer » ?",
    "options": {
      "A": "Orelsan",
      "B": "Stromae",
      "C": "Angèle",
      "D": "Jul"
    },
    "correct": "A"
  },
  {
    "question": "35. L'Algérie a fêté en 2022 l'anniversaire de son indépendance. Quel chiffre symbolique a été franchi à cette occasion ?",
    "options": {
      "A": "20 ans",
      "B": "40 ans",
      "C": "60 ans",
      "D": "80 ans"
    },
    "correct": "C"
  },
  {
    "question": "36. Quel lieu saint constitue la nécropole des rois de France ?",
    "options": {
      "A": "La cathédrale Notre Dame de PARIS",
      "B": "La basilique du Sacré Cœur",
      "C": "La cathédrale de REIMS",
      "D": "La basilique de SAINT DENIS"
    },
    "correct": "D"
  },
  {
    "question": "37. Lequel de ces ministères appartient au gouvernement d'Élisabeth BORNE ?",
    "options": {
      "A": "Ministère de l'Intérieur, de l'Outre-mer et des collectivités territoriales",
      "B": "Ministère de l'Intérieur et des Outre-mer",
      "C": "Ministère de l'Intérieur et de l'Immigration",
      "D": "Ministère de l'Intérieur et de l'Aménagement du territoire"
    },
    "correct": "A"
  },
  {
    "question": "38. Dans un procès hors normes, plusieurs terroristes ont été condamnés pour les attentats commis au Bataclan et au stade de France. Quand ces évènements ont-ils eu lieu ?",
    "options": {
      "A": "Mercredi 11 novembre 2015",
      "B": "Mardi 11 novembre 2016",
      "C": "Vendredi 13 novembre 2015",
      "D": "Vendredi 13 novembre 2014"
    },
    "correct": "C"
  },
  {
    "question": "39. En France, qu'est-ce que la prévôté ?",
    "options": {
      "A": "Une unité logistique",
      "B": "Une juridiction particulière en charge des contentieux religieux",
      "C": "Une unité en charge de la police militaire"
    },
    "correct": "B"
  },
  {
    "question": "40. Combien la France compte-t-elle de communes ?",
    "options": {
      "A": "Environ 4000",
      "B": "Environ 10000",
      "C": "Environ 25000",
      "D": "Environ 35000"
    },
    "correct": "D"
  },
  {
    "question": "41. Quel humoriste fondateur des « Restos du Cœur » est à l'origine d'une loi facilitant les dons aux associations caritatives ?",
    "options": {
      "A": "Jamel DEBBOUZE",
      "B": "Coluche",
      "C": "Kev ADAMS",
      "D": "Pierre DESPROGES",
      "E": "Alain CHABAT"
    },
    "correct": "B"
  },
  {
    "question": "42. Qui est l'auteur de la déclaration des droits de la femme et de la citoyenne ?",
    "options": {
      "A": "George SAND",
      "B": "Olympe de GOUGES",
      "C": "Simone de BEAUVOIR",
      "D": "Élisabeth BADINTER"
    },
    "correct": "B"
  },
  {
    "question": "43. Quel est le régime politique de la France en 1814 ?",
    "options": {
      "A": "La Monarchie de Juillet",
      "B": "La Ière République",
      "C": "Le 1er Empire",
      "D": "La IIème République"
    },
    "correct": "C"
  },
  {
    "question": "44. Combien d'étoiles compte le drapeau européen ?",
    "options": {
      "A": "27",
      "B": "12",
      "C": "15",
      "D": "21"
    },
    "correct": "B"
  },
  {
    "question": "45. Classez ces pays du Nord au Sud :",
    "options": {
      "A": "Paraguay / Bolivie / Uruguay",
      "B": "Uruguay / Bolivie / Paraguay",
      "C": "Uruguay / Paraguay / Bolivie",
      "D": "Bolivie / Paraguay / Uruguay"
    },
    "correct": "D"
  },
  {
    "question": "46. Qui a dit « ce qui se conçoit bien s'énonce clairement » ?",
    "options": {
      "A": "La Fontaine",
      "B": "Einstein",
      "C": "Boileau",
      "D": "Montesquieu"
    },
    "correct": "C"
  },
  {
    "question": "47. Quelle déclinaison du rugby n'existe pas ?",
    "options": {
      "A": "Rugby à XV",
      "B": "Rugby à XIII",
      "C": "Rugby à IX",
      "D": "Rugby à VII",
      "E": "Rugby à V"
    },
    "correct": "E"
  },
  {
    "question": "48. En quelle année le drapeau tricolore a-t-il été définitivement adopté en France ?",
    "options": {
      "A": "1789",
      "B": "1793",
      "C": "1848",
      "D": "1870"
    },
    "correct": "B"
  },
  {
    "question": "49. La Fontaine a ses Fables, Perreault ses Contes et Pascal ses Pensées ; qu'a écrit La Bruyère ?",
    "options": {
      "A": "Les Citations",
      "B": "Les Caractères",
      "C": "Les Palinodies",
      "D": "Les Parenthèses"
    },
    "correct": "B"
  },
  {
    "question": "50. Combien de Ballons d'or Lionel MESSI a-t-il obtenus ?",
    "options": {
      "A": "5",
      "B": "6",
      "C": "7",
      "D": "8"
    },
    "correct": "C"
  },
  {
    "question": "51. Quel sujet de société est abordé à la fin de la chanson « Le gorille » de Georges Brassens ?",
    "options": {
      "A": "La peine de mort",
      "B": "Le mariage pour tous",
      "C": "Le bien-être animal",
      "D": "Le vieillissement de la population",
      "E": "Le chômage"
    },
    "correct": "A"
  },
  {
    "question": "52. Dans quel pays est organisée depuis 1909 la célèbre marche militaire de Nimègue ?",
    "options": {
      "A": "France",
      "B": "Belgique",
      "C": "Pays-Bas",
      "E": "Allemagne"
    },
    "correct": "C"
  },
  {
    "question": "53. Qui était Hubert Germain, décédé le 12 octobre 2021 ?",
    "options": {
      "A": "Le premier commandant du 1er régiment de chasseurs parachutistes",
      "B": "Le dernier des 1038 compagnons de la Libération",
      "C": "Le premier directeur général de la Gendarmerie nationale",
      "D": "Le dernier des 8 millions de « poilus »"
    },
    "correct": "B"
  },
  {
    "question": "54. Qui a présidé le 75ème festival de Cannes en 2022 ?",
    "options": {
      "A": "Vincent Lindon",
      "B": "Guillaume Canet",
      "C": "Gérard Depardieu",
      "D": "François Cluzet",
      "E": "Daniel Auteuil"
    },
    "correct": "A"
  },
  {
    "question": "55. Depuis sa dernière réforme de 2020, le Conseil économique, social et environnemental (CESE) est composé de 4 pôles. Cherchez l'intrus !",
    "options": {
      "A": "Régions, départements, communes et établissements publics de coopération intercommunale",
      "B": "Salariés",
      "C": "Entreprises, exploitants agricoles, artisans, professions libérales, mutuelles et chambres consulaires",
      "D": "Cohésion sociale et territoriale et de la vie associative",
      "E": "Protection de la nature et de l'environnement"
    },
    "correct": "E"
  },
  {
    "question": "56. Que valorise l'adjectif callipyge ?",
    "options": {
      "A": "La santé",
      "B": "L'écriture",
      "C": "La silhouette",
      "D": "L'esprit"
    },
    "correct": "C"
  },
  {
    "question": "57. Cherchez l'intrus !",
    "options": {
      "A": "Paul Klee",
      "B": "Eugène Delacroix",
      "C": "Edvard Munch",
      "D": "Robert Doisneau",
      "E": "Gustav Klimt"
    },
    "correct": "D"
  },
  {
    "question": "58. Dans une partition, combien de temps dure un soupir ?",
    "options": {
      "A": "Une croche",
      "B": "Une noire",
      "C": "Une blanche",
      "D": "Une ronde",
      "E": "Aucune de ces propositions"
    },
    "correct": "E"
  },
  {
    "question": "59. Que vient fixer en 1539 l'ordonnance de Villers-Cotterêts ?",
    "options": {
      "A": "Les frontières définitives du royaume de France",
      "B": "Le Français comme langue officielle du droit et de l'administration",
      "C": "La primogéniture mâle dans la dévolution de la couronne royale",
      "D": "La départementalisation du territoire national",
      "E": "Le Franc français comme unique monnaie du royaume"
    },
    "correct": "B"
  },
  {
    "question": "60. Quel est l'auteur des Mémoires d'outre-tombe ?",
    "options": {
      "A": "Honoré de Balzac",
      "B": "Victor Hugo",
      "C": "Guy de Maupassant",
      "D": "François-René de Chateaubriand",
      "E": "Émile Zola"
    },
    "correct": "D"
  },
  {
    "question": "61. Quel château a inspiré Hergé pour dessiner le château de Moulinsart pour sa série de bande dessinée Les Aventures de Tintin ?",
    "options": {
      "A": "Le château de Blois",
      "B": "Le château de Cheverny",
      "C": "Le château de Langeais",
      "D": "Le château d'Amboise",
      "E": "Le château de Chambord"
    },
    "correct": "B"
  },
  {
    "question": "62. Qui a peint Le Radeau de la Méduse ?",
    "options": {
      "A": "Auguste Renoir",
      "B": "Paul Cézanne",
      "C": "Théodore Géricault",
      "D": "Eugène Delacroix",
      "E": "Edgar Degas"
    },
    "correct": "C"
  },
  {
    "question": "63. Le 23 avril 2021, lequel de ces astronautes n'embarque pas à bord de la capsule Crew Dragon pour rejoindre la station spatiale internationale pour une mission d'une durée de six mois ?",
    "options": {
      "A": "le Français Thomas Pesquet",
      "B": "l'Italien Luca Parmitano",
      "C": "l'Américaine Katherine Megan McArthur",
      "D": "le Japonais Akihiko Hoshide",
      "E": "l'Américain Robert Shane Kimbrough"
    },
    "correct": "B"
  },
  {
    "question": "64. Dans quel département métropolitain se situe le Mont Gerbier-de-Jonc, massif au pied duquel la Loire prend sa source ?",
    "options": {
      "A": "la Lozère",
      "B": "la Loire",
      "C": "la Drôme",
      "D": "la Haute-Loire",
      "E": "l'Ardèche"
    },
    "correct": "D"
  },
  {
    "question": "65. Quelle est la fosse sous-marine la plus profonde ?",
    "options": {
      "A": "la fosse des Philippines",
      "B": "la fosse des Mariannes",
      "C": "la fosse du Japon",
      "D": "la fosse des Tonga",
      "E": "la fosse Calypso"
    },
    "correct": "B"
  },
  {
    "question": "66. Quelle est la capitale du Kazakhstan ?",
    "options": {
      "A": "Almaty",
      "B": "Douchanbé",
      "C": "Achgabat",
      "D": "Astana",
      "E": "Bichkek"
    },
    "correct": "D"
  },
  {
    "question": "67. Quel est le principal cépage du Saint-Émilion ?",
    "options": {
      "A": "le syrah",
      "B": "le cabernet franc",
      "C": "le merlot",
      "D": "le cabernet sauvignon",
      "E": "le gamay"
    },
    "correct": "C"
  },
  {
    "question": "68. En patinage artistique, quelle figure est appelée « le Bonaly » ?",
    "options": {
      "A": "le triple boucle piqué",
      "B": "l'axel",
      "C": "le double flip",
      "D": "le salto arrière",
      "E": "le saut de biche"
    },
    "correct": "D"
  },
  {
    "question": "69. La reine Élisabeth II s'est éteinte le 8 septembre 2022 au château de Balmoral en Écosse. Combien de temps aura duré son règne sur le trône d'Angleterre ?",
    "options": {
      "A": "60 ans",
      "B": "65 ans",
      "C": "70 ans",
      "D": "75 ans",
      "E": "80 ans"
    },
    "correct": "C"
  },
  {
    "question": "70. De qui est l'expression « Les Trente Glorieuses » ?",
    "options": {
      "A": "Jean Fourastié",
      "B": "François Perroux",
      "C": "Jean Monnet",
      "D": "François Chesnais",
      "E": "Raymond Barre"
    },
    "correct": "A"
  },
  {
    "question": "71. Depuis le « Brexit » en 2020, combien d'états sont-ils membres de l'Union Européenne ?",
    "options": {
      "A": "23",
      "B": "25",
      "C": "27",
      "D": "29",
      "E": "31"
    },
    "correct": "C"
  },
  {
    "question": "72. L'ambassade de France en Italie est située à Rome. Dans quel édifice siège-t-elle ?",
    "options": {
      "A": "La villa Médicis",
      "B": "Le palais Firenze",
      "C": "La villa Giulia",
      "D": "Le palais Valentini",
      "E": "Le palais Farnèse"
    },
    "correct": "E"
  },
  {
    "question": "73. Qui est l'inventeur de la photographie ?",
    "options": {
      "A": "David Brewster",
      "B": "Nicéphore Niépce",
      "C": "Michael Faraday",
      "D": "Thomas Edison",
      "E": "Louis Lumière"
    },
    "correct": "B"
  },
  {
    "question": "74. Quel était le port d'attache du RMS Titanic lequel a sombré dans l'Atlantique Nord dans la nuit du 14 au 15 avril 1912 à la suite d'une collision avec un iceberg ?",
    "options": {
      "A": "Southampton",
      "B": "Liverpool",
      "C": "Queenstown",
      "D": "New York",
      "E": "Belfast"
    },
    "correct": "A"
  },
  {
    "question": "75. Le titre des « dix petits nègres » d'Agatha Christie a été modifié en 2020. Comment ce classique s'appelle-t-il désormais ?",
    "options": {
      "A": "Ils étaient dix",
      "B": "Les dix petits soldats",
      "C": "Ils ne sont que dix",
      "D": "Les dix petits camarades",
      "E": "Le couteau sur la nuque"
    },
    "correct": "A"
  },
  {
    "question": "76. Combien de sous-marins nucléaires lanceurs d'engins composent la flotte actuelle française ?",
    "options": {
      "A": "2",
      "B": "3",
      "C": "4",
      "D": "5",
      "E": "6"
    },
    "correct": "C"
  },
  {
    "question": "77. La tendance à parler de ce qu'on ne connaît pas est aussi appelée :",
    "options": {
      "A": "la procrastination",
      "B": "l'emphase",
      "C": "l'ultracrépidarianisme",
      "D": "l'anathème",
      "E": "l'anatidaephobie"
    },
    "correct": "C"
  },
  {
    "question": "78. Quel concept poétique désigne l'état d'un être qui ne reconnaît plus de règle à son encontre, l'être en question pouvant être une collectivité :",
    "options": {
      "A": "l'anomie",
      "B": "le hiératisme",
      "C": "l'orthodoxie",
      "D": "le panégyrique",
      "E": "la rhétorique"
    },
    "correct": "A"
  },
  {
    "question": "79. Le « Discours de la servitude volontaire », qu'Étienne de La Boétie a rédigé à 16 ans, pose une question simple : pourquoi choisit-on d'obéir ? Au cours de quel siècle a été publié cet ouvrage ?",
    "options": {
      "A": "XVIème siècle",
      "B": "XVIIème siècle",
      "C": "XVIIIème siècle",
      "D": "XIXème siècle"
    },
    "correct": "A"
  },
  {
    "question": "80. Combien de personnels composent la population totale des officiers de la gendarmerie nationale (chiffres consolidés 2021 - en position d'activité) ?",
    "options": {
      "A": "2.800",
      "B": "3.850",
      "C": "4.590",
      "D": "6.290",
      "E": "8.220"
    },
    "correct": "C"
  },
  {
    "question": "81. Dans la nuit du 22 au 23 décembre 2020, trois militaires de la compagnie d'Ambert, dans le Puy-de-Dôme, sont tués alors qu'ils intervenaient sur des violences intrafamiliales. Sur quelle commune a eu lieu ce drame ?",
    "options": {
      "A": "Saint-Just",
      "B": "Riom",
      "C": "Chevalier",
      "D": "Clermont-Ferrand",
      "E": "Montluçon"
    },
    "correct": "A"
  },
  {
    "question": "82. Qu'est-ce qu'un sous-officier CSTAGN ?",
    "options": {
      "A": "Un sous-officier du corps de soutien technique et administratif de la gendarmerie nationale",
      "B": "Un sous-officier du corps des services technologiques et de l'anticipation de la gendarmerie nationale",
      "C": "Un sous-officier du corps spécial des techniques d'acclimatation de la gendarmerie nationale",
      "D": "Un sous-officier du corps de spécialité des techniques d'aguerrissement de la gendarmerie nationale"
    },
    "correct": "A"
  },
  {
    "question": "83. Quelle est la devise de la gendarmerie ?",
    "options": {
      "A": "Honneur et Fidélité",
      "B": "Pour la Patrie, l'Honneur et le Droit",
      "C": "Honneur, Patrie, Valeur, Discipline",
      "D": "S'engager pour la vie",
      "E": "Si tu veux la paix, prépare la guerre"
    },
    "correct": "B"
  },
  {
    "question": "84. Trouvez la bonne réponse pour compléter cette affirmation. « Les députés... :",
    "options": {
      "A": "sont élus tous les six ans",
      "B": "peuvent cumuler la fonction de député avec un mandat local",
      "C": "peuvent être réélus sans limite de candidature",
      "D": "sont limités à deux mandats successifs"
    },
    "correct": "C"
  },
  {
    "question": "85. Quelle est la capitale de la Suisse ?",
    "options": {
      "A": "Bâle",
      "B": "Berne",
      "C": "Zurich",
      "D": "Bienne",
      "E": "Genève"
    },
    "correct": "B"
  },
  {
    "question": "86. Quelle miss a remporté le concours Miss France 2022 ?",
    "options": {
      "A": "Alsace",
      "B": "Île-de-France",
      "C": "Réunion",
      "D": "Normandie",
      "E": "Corse"
    },
    "correct": "B"
  },
  {
    "question": "87. Les Jeux Olympiques 2024 auront lieu à Paris. À cette occasion, le comité d'organisation a décidé que le karaté ne serait pas au programme, en revanche quelle discipline fera son apparition ?",
    "options": {
      "A": "roller sur piste",
      "B": "bowling",
      "C": "breakdance",
      "D": "twirling bâton",
      "E": "yoseikan budo"
    },
    "correct": "C"
  },
  {
    "question": "88. L'aconit est :",
    "options": {
      "A": "Une plante vénéneuse",
      "B": "Une pierre précieuse",
      "C": "Un oiseau pêcheur"
    },
    "correct": "A"
  },
  {
    "question": "89. La sécurité sociale a été créée en :",
    "options": {
      "A": "1924",
      "B": "1936",
      "C": "1945",
      "D": "1946",
      "E": "1958"
    },
    "correct": "C"
  },
  {
    "question": "90. Elle a été la base de la politique des États-Unis contre le bloc communiste durant la guerre froide. Il s'agit de la doctrine :",
    "options": {
      "A": "Monroe",
      "B": "Truman",
      "C": "Roosevelt",
      "D": "Eisenhower",
      "E": "Reagan"
    },
    "correct": "B"
  },
  {
    "question": "91. En 2017, Robert Mugabe a quitté le pouvoir. Il était président :",
    "options": {
      "A": "Du Zimbabwe",
      "B": "De l'Ouganda",
      "C": "De la Tanzanie",
      "D": "De la Sierra Leone"
    },
    "correct": "A"
  },
  {
    "question": "92. Lequel de ces personnages shakespeariens a été interprété et mis en scène à l'écran par Orson Welles ?",
    "options": {
      "A": "Richard III",
      "B": "Henri V",
      "C": "Jules César",
      "D": "Othello"
    },
    "correct": "A"
  },
  {
    "question": "93. Pour lequel de ces films le comédien Sami Bouajila a-t-il obtenu le César du meilleur acteur ?",
    "options": {
      "A": "Indigènes",
      "B": "Omar m'a tuer",
      "C": "Un fils",
      "D": "Vivre me tue"
    },
    "correct": "C"
  },
  {
    "question": "94. Comment s'appelle le grillage géométrique des fenêtres des palais arabes ?",
    "options": {
      "A": "Le pishtak",
      "B": "Le moucharabieh",
      "C": "L'iwan",
      "D": "Le hazerbaf",
      "E": "Le qasr"
    },
    "correct": "B"
  },
  {
    "question": "95. Quel sculpteur est un ancien sportif surnommé « casque d'or » ?",
    "options": {
      "A": "Eric Cantona",
      "B": "Serge Blanco",
      "C": "Serge Simon",
      "D": "Jean-Pierre Rives",
      "E": "Pierre Albaladejo"
    },
    "correct": "D"
  },
  {
    "question": "96. Le parc nucléaire civil français de production d'électricité se compose, en décembre 2021, de :",
    "options": {
      "A": "18 centres de production et 56 réacteurs",
      "B": "20 centres de production et 60 réacteurs",
      "C": "15 centres de production et 47 réacteurs",
      "D": "18 centres de production et 52 réacteurs",
      "E": "14 centres de production et 56 réacteurs"
    },
    "correct": "A"
  },
  {
    "question": "97. Qui est le dernier roi de France ?",
    "options": {
      "A": "Louis-Philippe d'Orléans",
      "B": "Charles X",
      "C": "Louis-Philippe 1er",
      "D": "Louis XVI"
    },
    "correct": "C"
  },
  {
    "question": "98. Dans quel état américain se trouve le Grand lac salé ?",
    "options": {
      "A": "Utah",
      "B": "Arizona",
      "C": "Colorado",
      "D": "Nouveau-Mexique",
      "E": "Nevada"
    },
    "correct": "A"
  },
  {
    "question": "99. Quel état du sud-est asiatique n'a-t-il pas été colonisé par les Occidentaux ?",
    "options": {
      "A": "la Birmanie",
      "B": "le Cambodge",
      "C": "l'Indonésie",
      "D": "le Laos",
      "E": "la Thaïlande"
    },
    "correct": "E"
  },
  {
    "question": "100. Qui a dit « On ne devrait lire que les livres qui vous mordent et vous piquent » ?",
    "options": {
      "A": "Dino Buzzati",
      "B": "Alfred de Musset",
      "C": "Boris Vian",
      "D": "Franz Kafka"
    },
    "correct": "C"
  }
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



# Charger les fichiers JSON externes
qcm_file_path_1 = "qcm_100_questions.json"
qcm_file_path_2 = "qcm_2_GPT_100.json"

try:
    with open(qcm_file_path_1, "r", encoding="utf-8") as file:
        qcm_100_questions = json.load(file)
except FileNotFoundError:
    qcm_100_questions = []

try:
    with open(qcm_file_path_2, "r", encoding="utf-8") as file:
        qcm2_100_questions = json.load(file)
except FileNotFoundError:
    qcm2_100_questions = []

# Définition des QCM existants
qcm_collection = {
    "QCM 2021": qcm2021,
    "QCM 2022": qcm2022,
    "QCM 2023": qcm2023,
    "QCM 2024": qcm2024,
    "QCM by gpt 1": qcm_100_questions,
    "QCM by gpt 2": qcm2_100_questions
}

# Interface Streamlit
selected_qcm = st.sidebar.selectbox("Choisissez le QCM :", list(qcm_collection.keys()))
questions = qcm_collection[selected_qcm]

st.title(f"QCM d'évaluation - {selected_qcm}")

# Initialisation du score et du résumé des erreurs
score = 0
wrong_summary = []

for idx, q in enumerate(questions):
    st.markdown(f"**{q['question']}**")
    placeholder_text = "Faites un choix"
    all_options = [placeholder_text] + list(q["options"].keys())
    
    answer = st.radio("Votre réponse :", all_options, index=0, key=f"q{idx}")
    
    st.markdown("\n".join([f"- **{k}** : {v}" for k, v in q["options"].items()]))
    
    if answer == placeholder_text:
        st.warning("Veuillez sélectionner une option.")
    else:
        if answer == q["correct"]:
            st.success(f"Correct ! Votre réponse : {answer} - {q['options'][answer]}")
            score += 1
        else:
            st.error(f"Faux. Votre réponse : {answer} - {q['options'][answer]}. La bonne réponse est : {q['correct']} - {q['options'][q['correct']]}")
            wrong_summary.append({
                "question": q["question"],
                "your_answer": answer,
                "your_answer_text": q["options"].get(answer, "Réponse invalide"),
                "correct": q["correct"],
                "correct_text": q["options"][q["correct"]]
            })
    st.write("---")

# Affichage du score final
total_questions = len(questions)
percentage = (score / total_questions) * 100 if total_questions > 0 else 0
score_out_of_20 = (percentage * 20) / 100

st.subheader(f"Score final : {score} / {total_questions}")
st.subheader(f"Note en pourcentage : {percentage:.2f} %")
st.subheader(f"Note sur 20 : {score_out_of_20:.2f} / 20")

# Affichage du récapitulatif des questions incorrectes
if wrong_summary:
    st.header("Récapitulatif des questions incorrectes")
    for item in wrong_summary:
        st.markdown(f"**{item['question']}**")
        st.write(f"Votre réponse : {item['your_answer']} - {item['your_answer_text']}")
        st.write(f"Bonne réponse : {item['correct']} - {item['correct_text']}")
        st.write("---")
