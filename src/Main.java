import collections.tourist;
import places.Place;
import iterators.iterator;
public class Main {
    public static void main(String[] args) {
        Place timesSquare = new Place("Дендропарк «Софієвка»", 93, 94);
        Place statueOfLiberty = new Place("Кінбурнська коса", 95, 83);
        Place centralPark = new Place("Шацькі озера", 87, 95);

        tourist collection = new tourist();
        collection.add(timesSquare);
        collection.add(statueOfLiberty);
        collection.add(centralPark);

        iterator userIterator = collection.getUserIterator();
        while (userIterator.hasNext()) {
            System.out.println(userIterator.getNext());
        }

        iterator navIterator = collection.getNavigatorIterator();
        while (navIterator.hasNext()) {
            System.out.println(navIterator.getNext());
        }

        iterator guideIterator = collection.getGuideIterator();
        while (guideIterator.hasNext()) {
            System.out.println(guideIterator.getNext());
        }
    }
}