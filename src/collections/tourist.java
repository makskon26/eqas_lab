package collections;

import iterators.guid;
import iterators.user;
import iterators.navigator;
import iterators.iterator;
import places.Place;

import java.util.ArrayList;
import java.util.List;

public class tourist implements touristInterface {
    private final List<Place> places = new ArrayList<>();

    public void add(Place place) {
        places.add(place);
    }

    public void get(int index) {
        places.get(index);
    }

    @Override
    public iterator getUserIterator() {
        return new user(new ArrayList<>(places));
    }

    @Override
    public iterator getNavigatorIterator() {
        return new navigator(new ArrayList<>(places));
    }

    @Override
    public iterator getGuideIterator() {
        return new guid(new ArrayList<>(places));

    }
}
