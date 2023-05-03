package iterators;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import places.Place;
public class navigator implements iterator {
    private final List<Place> places;
    private int pointer = 0;

    public navigator(List<Place> places) {
        // sort by navigator rating
        this.places = places.stream()
                .sorted(Comparator.comparingInt(Place::getNavigatorRating))
                .collect(Collectors.toList());
    }

    public boolean hasNext() {
        return pointer < places.size();
    }

    public Place getNext() {
        if (!hasNext()) {
            return null;
        }
        Place place = places.get(pointer);
        pointer++;
        return place;
    }
}
