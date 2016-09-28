## TP 3 du cours programmation avancée

Dans cet exercice, nous allons construire une calculette sur le principe d’un client-serveur. Le client soumet un calcul à exécuter au serveur qui lui retourne le résultat.
Le protocole utilisé est le suivant :
  - lorsque le client se connecte au serveur, le serveur lui envoie la trame HELLO ;
  - le client lui répond alors en lui envoyant la trame HELLO également ;
  - le client peut alors envoyer ses requêtes avec les trames ADDITION, SOUSTRACTION,MULTIPLICATION et DIVISION. 
 En retour, le serveur envoie au client la trame RESULTAT ;
  - Quand le client veut mettre fin à la connexion, il envoie au serveur la trame QUITTER.
  
Les trames sont composées comme suit : 3 octets codant la commande (caractères en UTF-8), un nombre d’octets fournissant les opérandes la commande.

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column



Nom de la trame      |     Code commande sur 3 octets    |   Argument
------------- |-------------| ---------
HELLO      |        HLO        |      Aucun
QUITTER        |        QUT        |      Aucun
ADDITION      |        ADD        |      Aucun
SOUSTRACTION      |        MIN        |      Aucun
MULTIPLICATION      |        TIM        |      16 octets correspondant à deux doubles
DIVISION | DIV | 16 octets correspondant à deux doubles
