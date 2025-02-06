import java.util.*;

public class Main {
    public static void main(String[] args) {
      
        Film film1 = new Film("Star Wars, épisode IV : Un nouvel espoir", "George Lucas", 1977, 775398007, 11000000);
        Film film2 = creerFilmInteractif();

        
        Acteur acteur1 = new Acteur("Mark Hamill");
        acteur1.ajouterPersonnage("Luke Skywalker");

        Acteur acteur2 = new Acteur("Harrison Ford");
        acteur2.ajouterPersonnage("Han Solo");

        Acteur acteur3 = new Acteur("Carrie Fisher");
        acteur3.ajouterPersonnage("Princesse Leia");

       
        film1.ajouterActeur(acteur1);
        film1.ajouterActeur(acteur2);
        film1.ajouterActeur(acteur3);

       
        System.out.println(film1);
        System.out.println(film2);

       
        System.out.println("Nombre d'acteurs dans le film 1 : " + film1.nbActeurs());
        System.out.println("Nombre de personnages dans le film 1 : " + film1.nbPersonnages());

        Object[] beneficeInfo = film1.calculBenefice();
        System.out.println("Bénéfice du film 1 : " + beneficeInfo[0] + " (Bénéficiaire : " + beneficeInfo[1] + ")");

       
        film1.tri();
        System.out.println("Acteurs triés : " + film1);

        
        Map<Integer, Film> films = new HashMap<>();
        films.put(1977, film1);
        films.put(1980, new Film("Star Wars, épisode V : L'Empire contre-attaque", "Irvin Kershner", 1980, 538375067, 18000000));

        
        makeBackUp(films);
    }

    /**
     * Crée un film interactivement en demandant les informations à l'utilisateur.
     * @return Le film créé.
     */
    public static Film creerFilmInteractif() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Entrez le titre du film :");
        String titre = scanner.nextLine();
        System.out.println("Entrez le réalisateur du film :");
        String realisateur = scanner.nextLine();
        System.out.println("Entrez l'année de sortie du film :");
        int annee = scanner.nextInt();
        System.out.println("Entrez la recette du film :");
        double recette = scanner.nextDouble();
        System.out.println("Entrez le coût de production du film :");
        double cout = scanner.nextDouble();

        return new Film(titre, realisateur, annee, recette, cout);
    }

    /**
     * Sauvegarde les films dans un format spécifique.
     * @param films Le dictionnaire de films à sauvegarder.
     */
    public static void makeBackUp(Map<Integer, Film> films) {
        for (Map.Entry<Integer, Film> entry : films.entrySet()) {
            int annee = entry.getKey();
            Film film = entry.getValue();
            Object[] beneficeInfo = film.calculBenefice();
            double benefice = (double) beneficeInfo[0];
            System.out.println(annee + " - " + film.getTitre() + " - " + benefice);
        }
    }
}