import java.awt.*;
/**
 *  Circle 
 * Class that handles circle that will be drawn on screen
 * <b>For documentation of overriden methods see</b>
 * @see Figure
 * @see BaseFigure
 * Idea is that we are working on middle and on base R and our
 * radius is calculated on the run
 */
public class Circle extends Figure {
    /**
     * Middle of circle
     */
    MyPoint S;
    /**
     * radius of circle
     */
    double r;
    /**
     * topleft of rectangle bound of circle
     */
    MyPoint topleft;
    /**
     * Point from which circle was created
     */
    MyPoint creator;
    /**
     * radius at which circle was created
     */
    double baseR;


    /**
     * Constructor to create circle that is being drawn to the screen right now
     * See public Circle(MyPoint S, double r, Color color) for more information
     * @param x x of middle
     * @param y y of middle
     * @param r radius of circle
     * @param color color of circle
     */
    public Circle(int x, int y, double r, Color color) {
        this(new MyPoint(x, y), r, color);
    }

    /**
     * Constructor to create circle that is
     * being drawn to the screen right now
     * @param S middle of circle
     * @param r radius of circle
     * @param color color of circle
     */
    public Circle(MyPoint S, double r, Color color) {
        super(color, "circle");
        this.S = S;
        this.creator = new MyPoint(S);
        this.topleft = new MyPoint(S);
        this.r = r;
        this.how_much_increased = 0;
        baseR = r;
    }

    /**
     * Constructor that should be used to create
     * circle from savefile
     * @see JSaveFrame
     * @param line string containing all data about figure
     */
    public Circle(String line) {
        super();
        String[] creator = line.split(" ");
        S = new MyPoint(Double.parseDouble(creator[1]), Double.parseDouble(creator[2]));
        topleft = new MyPoint(S);
        baseR = Double.parseDouble(creator[3]);
        color = new Color(Integer.parseInt(creator[4]));
        how_much_increased = Integer.parseInt(creator[5]);
    }

    @Override
    public String saveData() {
        return "C " +
                S.rx + " " + S.ry + " " + baseR + " " +
                color.getRGB() + " " +
                how_much_increased;
    }

    @Override
    public void draw(Graphics g) {
        if (created) {
            resize();
        }
        topleft.update(S.rx - r, S.ry - r);
        g.setColor(color);
        g.drawOval(topleft.x, topleft.y, 2 * (int) r, 2 * (int) r);
        g.fillOval(topleft.x, topleft.y, 2 * (int) r, 2 * (int) r);
        g.setColor(color.darker().darker());
        g.fillRect(S.x - 1, S.y - 1, 3, 3);
    }

    @Override
    public void created() {
        baseR = r;
        created = true;
    }

    @Override
    public void drawBounds(Graphics g) {
        g.setColor(color.darker());
        g.drawOval(topleft.x, topleft.y, 2 * (int) r, 2 * (int) r);
    }

    @Override
    public void drag(MyPoint prev, MyPoint now) {
        S.update(S.rx + now.rx - prev.rx, S.ry + now.ry - prev.ry);
    }


    @Override
    public void changeDuringCreation(MyPoint mousePos) {
        this.r = Math.max(Math.abs(mousePos.rx - creator.rx), Math.abs(mousePos.ry - creator.ry)) / 2;
        if (mousePos.rx >= creator.rx) {
            if (mousePos.ry >= creator.ry) {
                topleft.mutate_to(creator);
            } else {
                topleft.update(creator.rx, creator.ry - 2 * r);
            }
        } else {
            if (mousePos.y >= creator.y) {
                topleft.update(creator.rx - 2 * r, creator.ry);
            } else {
                topleft.update(creator.rx - 2 * r, creator.ry - 2 * r);
            }
        }
        S.update(topleft.rx + r, topleft.ry + r);
    }

    @Override
    public boolean contains(MyPoint mousePos) {
        return S.distancesq_to(mousePos) <= r * r;
    }

    @Override
    public void resize() {
        double factor = 1;
        double base_factor;
        if (how_much_increased > 0) {
            base_factor = 1.1;
        } else if (how_much_increased < 0) {
            base_factor = 0.9;
        } else {
            base_factor = 1;
        }
        for (int i = 0; i < Math.abs(how_much_increased); i++) {
            factor *= base_factor;
        }
        r = baseR * factor;

    }

    @Override
    public String toString() {
        return "Circle{" +
                "S=" + S +
                ", r=" + r +
                ", topleft=" + topleft +
                '}';
    }
}
