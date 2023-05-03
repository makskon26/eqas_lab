package places;

public class Place {
    private final String name;
    private final int navigatorRating;
    private final int guideRating;

    public Place(String name, int navigatorRating, int guideRating) {
        this.name = name;
        this.navigatorRating = navigatorRating;
        this.guideRating = guideRating;
    }

    public String getName() {
        return name;
    }

    public int getNavigatorRating() {
        return navigatorRating;
    }

    public int getGuideRating() {
        return guideRating;
    }

    @Override
    public String toString() {
        return "Туристичне місце{" +
                "Нзва='" + name + '\'' +
                ", Рекомендації навігатора=" + navigatorRating +
                ", Рекомендації гіда=" + guideRating +
                '}';
    }
}
