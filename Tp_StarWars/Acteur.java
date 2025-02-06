import java.util.ArrayList;
import java.util.List;

public class Acteur {
    private String nom;
    private List<String> personnages;

    /**
     * Constructeur de la classe Acteur.
     * @param nom Le nom de l'acteur.
     */
    public Acteur(String nom) {
        this.nom = nom;
        this.personnages = new ArrayList<>();
    }

    /**
     * Ajoute un personnage à l'acteur.
     * @param personnage Le nom du personnage.
     */
    public void ajouterPersonnage(String personnage) {
        personnages.add(personnage);
    }

    /**
     * Retourne le nombre de personnages incarnés par l'acteur.
     * @return Le nombre de personnages.
     */
    public int nbPersonnages() {
        return personnages.size();
    }

    /**
     * Méthode toString pour afficher les informations de l'acteur.
     * @return Une chaîne de caractères représentant l'acteur.
     */
    @Override
    public String toString() {
        return "Acteur{" +
                "nom='" + nom + '\'' +
                ", personnages=" + personnages +
                '}';
    }

    public String getNom() {
        return nom;
    }
}