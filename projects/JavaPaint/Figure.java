import java.awt.*;

/**
 *  Figure 
 * Class that connects every end-point figure
 * such as
 * @see Triangle
 * @see Rectangle
 * @see Circle
 * Every Figure on top of BaseFigure has got following functionalities
 * resizable, color changable, bounds drawable, draggable
 */
public abstract class Figure implements BaseFigure {
    /**
     * maximum priority that figure currently has
     */
    static int max_priority = 0;
    /**
     * Integer that tells how much have we increased size of figure. May be negative
     */
    public int how_much_increased = 0;
    /**
     * Integer saying priority of figure
     */
    int priority;
    /**
     * Name of figure. for debugging purposes only
     */
    String name;
    /**
     * Color of figure that will be shown on graphic panel
     */
    Color color;
    /**
     * If figure is created and it's shape cannot change anymore then this boolean should change to true
     */
    boolean created = false;

    /**
     * Constructor for figure that is being drawn using drawe
     * it does not assume that figure is created
     * @param color Color that figure should have
     * @param name only for debugging purposes
     */
    public Figure(Color color, String name) {
        this.color = color;
        max_priority += 1;
        this.priority = max_priority;
        this.name = name;
    }

    /**
     * Constructor for figure that should be used
     * during loading figures from file
     * @see JLoadFrame
     */
    public Figure() {
        max_priority += 1;
        this.priority = max_priority;
        created = true;
    }

    /**
     * Method used to increase size of figure
     * figure is being resized in resize method
     */
    public void resizeBigger() {
        if (how_much_increased < 100) {
            how_much_increased += 1;
        }
    }
    /**
     * Method used to decrease size of figure
     * figure is being resized in resize method
     */
    public void resizeSmaller() {
        if (how_much_increased > -50) {
            how_much_increased -= 1;
        }
    }

    /**
     * Method used to resize figure according to how many scrolls
     * have been made to increase size or decrease size
     * how_much_increased can be changed by scroll in
     * @see Drawer class
     */
    public abstract void resize();

    /**
     * Method that will return true if mousePos is in the Figure
     * Specifying what exactly means being in figure is role of
     * child classes
     * @param mousePos Point that we are checkign if it is inside of figure
     * @return true if it is inside false otherwise
     */
    public abstract boolean contains(MyPoint mousePos);

    /**
     * Method to change color of figure
     * @param color color that we will change to
     */
    public void changeColor(Color color) {
        this.color = color;
    }
    /**
     * Method executed after confirming creation of figure
     */
    public abstract void created();

    /**
     * Method that will draw bounds of figure
     * @param g graphics param of panel that we are drawing on
     */
    public abstract void drawBounds(Graphics g);

    /**
     * @return priority which figure has
     */
    public int returnPriority() {
        return priority;
    }

    /**
     * Method that will drag figure by vector from prev to now
     * Implementation in Figure should be used only for debugging purposes
     * @param prev start point of vector
     * @param now end point of vector
     */
    public void drag(MyPoint prev, MyPoint now) {
        System.out.println("prev: " + prev + " now:" + now);
    }

    /**
     * For debug purposes only
     * @return String containing basic information of figure
     */
    @Override
    public String toString() {
        return name + "{priority=" + priority + ", color=" + color + ", how_much_increased: " + how_much_increased;
    }

    /**
     * Method used for creating savefile
     * @see JSaveFrame
     * @return String that contains all save info of figure that will let recreate it
     */
    public abstract String saveData();
}
