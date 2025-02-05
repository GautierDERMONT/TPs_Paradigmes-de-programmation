homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
homem(luc)

femme(marie).
femme(sophie).
femme(lucie).
femme(anne).


parent(jacques, luc).  
parent(luc, marie).   
parent(anne, sophie).  
parent(pierre, paul).
parent(marie, lucie).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).
parent(jacques, lucie).

parent(marc, pierre).
parent(sophie, marie).

longueur([], 0).
longueur([_ | Queue], N) :- longueur(Queue, M), N is M + 1.


membre(X, [X | _]).        
membre(X, [_ | Queue]) :- membre(X, Queue). 


oncle_ou_tante(X, Y) :- parent(Z, Y), freresoeur(X, Z). 


tante(X, Y) :- femme(X), parent(Z, Y), freresoeur(X, Z).


cousin(X, Y) :- parent(Z, X), oncle_ou_tante(Z, Y).



parents(X, Y) :- parent(X, Y).


grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

freresoeur(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

pere(X, Y) :- homme(X), parent(X, Y).
mere(X, Y) :- femme(X), parent(X, Y).

