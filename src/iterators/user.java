package iterators;

import places.Place;
import java.util.List;

public class user implements iterator {
    private final List<Place> places;
    private int pointer = 0;

    public user(List<Place> places) {
        this.places = places;
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
