import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Classe représentant un film de la saga Star Wars.
 */
public class Film {
    private String titre;
    private String realisateur;
    private int annee;
    private double recette;
    private double cout;
    private List<Acteur> acteurs;

    /**
     * Constructeur de la classe Film.
     * @param titre Le titre du film.
     * @param realisateur Le réalisateur du film.
     * @param annee L'année de sortie du film.
     * @param recette La recette du film.
     * @param cout Le coût de production du film.
     */
    public Film(String titre, String realisateur, int annee, double recette, double cout) {
        this.titre = titre;
        this.realisateur = realisateur;
        this.annee = annee;
        this.recette = recette;
        this.cout = cout;
        this.acteurs = new ArrayList<>();
    }

    /**
     * Méthode toString pour afficher les informations du film.
     * @return Une chaîne de caractères représentant le film.
     */
    @Override
    public String toString() {
        return "Film{" +
                "titre='" + titre + '\'' +
                ", realisateur='" + realisateur + '\'' +
                ", annee=" + annee +
                ", recette=" + recette +
                ", cout=" + cout +
                ", acteurs=" + acteurs +
                '}';
    }

    /**
     * Ajoute un acteur au film.
     * @param acteur L'acteur à ajouter.
     */
    public void ajouterActeur(Acteur acteur) {
        acteurs.add(acteur);
    }

    /**
     * Retourne le nombre d'acteurs du film.
     * @return Le nombre d'acteurs.
     */
    public int nbActeurs() {
        return acteurs.size();
    }

    /**
     * Retourne le nombre de personnages du film.
     * @return Le nombre de personnages.
     */
    public int nbPersonnages() {
        int nbPersonnages = 0;
        for (Acteur acteur : acteurs) {
            nbPersonnages += acteur.nbPersonnages();
        }
        return nbPersonnages;
    }

    /**
     * Calcule le bénéfice du film.
     * @return Un tableau contenant le bénéfice et un booléen indiquant si le film est bénéficiaire.
     */
    public Object[] calculBenefice() {
        double benefice = recette - cout;
        boolean estBeneficiaire = benefice > 0;
        return new Object[]{benefice, estBeneficiaire};
    }

    /**
     * Vérifie si le film est sorti avant une année donnée.
     * @param annee L'année à comparer.
     * @return True si le film est sorti avant l'année donnée, False sinon.
     */
    public boolean isBefore(int annee) {
        return this.annee < annee;
    }

    /**
     * Trie les acteurs par ordre alphabétique.
     */
    public void tri() {
        acteurs.sort(Comparator.comparing(Acteur::getNom));
    }

    public String getTitre() {
        return titre;
    }
}