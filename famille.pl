homme(pierre).
homme(marc).
homme(paul).
homme(jacques).
femme(marie).
femme(sophie).

parent(pierre, paul).
parent(marie, paul).
parent(marc, sophie).
parent(jacques, marc).
parent(marc, pierre).
parent(sophie, marie).

% Définir le prédicat parents/2
parents(X, Y) :- parent(X, Y).

% Définir le prédicat grandparent/2
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
)
% Règles pour définir père et mère
pere(X, Y) :- homme(X), parents(X, Y).
mere(X, Y) :- femme(X), parents(X, Y).
