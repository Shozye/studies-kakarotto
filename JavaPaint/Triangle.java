import java.awt.*;
import java.util.Objects;

/**
 *  Triangle 
 * Class that handles triangle that will be drawn on screen
 * <b>For documentation of overriden methods see</b>
 * @see Figure
 * @see BaseFigure
 * Idea is that we are working of baseA, baseB, baseC
 * and A,B,C are only representations of figure shown
 * to user and calculated on the run
 */
public class Triangle extends Figure {
    /**
     * Resized point of a figure. Also used during creation
     */
    MyPoint A;
    /**
     * Resized point of a figure. Also used during creation
     */
    MyPoint B;
    /**
     * Resized point of a figure. Also used during creation
     */
    MyPoint C; // that's not static during creation
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C are calculated from this. Changed only during dragging
     */
    MyPoint baseA;
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C are calculated from this. Changed only during dragging
     */
    MyPoint baseB;
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C are calculated from this. Changed only during dragging
     */
    MyPoint baseC;
    /**
     *  this point represents circumference middle of triangle
     */
    MyPoint S;
    /**
     * this point represents Centroid of triangle
     */
    MyPoint Centroid;

    /**
     * Constructor used during drawing figure on GUI
     * @param A First point clicked during drawing
     * @param B Second point clicked during drawing
     * @param C Third point clicked during drawing
     * @param color color of which triangle will be created
     */
    public Triangle(MyPoint A, MyPoint B, MyPoint C, Color color) {
        super(color, "triangle");
        this.C = Objects.requireNonNullElseGet(C, () -> new MyPoint(B));
        this.A = A;
        this.B = B;
        this.color = color;
        this.S = new MyPoint(0, 0);
        how_much_increased = 0;
        created = false;

        this.Centroid = new MyPoint(0, 0);
    }
    /**
     * Constructor used during creation of figure from savefile
     * @param line string containing all data about figure in specified form
     */
    public Triangle(String line) {
        super();
        String[] creator = line.split(" ");
        baseA = new MyPoint(Double.parseDouble(creator[1]), Double.parseDouble(creator[2]));
        baseB = new MyPoint(Double.parseDouble(creator[3]), Double.parseDouble(creator[4]));
        baseC = new MyPoint(Double.parseDouble(creator[5]), Double.parseDouble(creator[6]));
        color = new Color(Integer.parseInt(creator[7]));
        how_much_increased = Integer.parseInt(creator[8]);
        A = new MyPoint(baseA);
        B = new MyPoint(baseB);
        C = new MyPoint(baseC);
        S = new MyPoint(baseA);
    }

    @Override
    public String saveData() {
        return "T " +
                baseA.rx + " " + baseA.ry + " " + baseB.rx + " " + baseB.ry + " " + baseC.rx + " " + baseC.ry + " " +
                color.getRGB() + " " +
                how_much_increased;
    }

    @Override
    public void draw(Graphics g) {
        if (created) {
            resize();
        }
        int[] x = {A.x, B.x, C.x};
        int[] y = {A.y, B.y, C.y};
        int n = 3;
        g.setColor(color);
        g.drawPolygon(x, y, n);
        g.fillPolygon(x, y, n);
        g.setColor(color.darker().darker());
        if (created) {
            g.fillRect(S.x - 1, S.y - 1, 3, 3);
        }
        if (!created) {
            g.fillRect((int) (A.rx + B.rx + C.rx - 1), (int) (A.ry + B.ry + C.ry - 1), 3, 3);
        }
    }

    @Override
    public void drawBounds(Graphics g) {
        int[] x = {A.x, B.x, C.x};
        int[] y = {A.y, B.y, C.y};
        int n = 3;
        g.setColor(color.darker());
        g.drawPolygon(x, y, n);
    }

    @Override
    public void drag(MyPoint prev, MyPoint now) {
        baseA.update(baseA.rx + now.rx - prev.rx, baseA.ry + now.ry - prev.ry);
        baseB.update(baseB.rx + now.rx - prev.rx, baseB.ry + now.ry - prev.ry);
        baseC.update(baseC.rx + now.rx - prev.rx, baseC.ry + now.ry - prev.ry);
    }

    @Override
    public void created() {
        created = true;
        baseA = new MyPoint(A);
        baseB = new MyPoint(B);
        baseC = new MyPoint(C);
        find_middle();
    }

    @Override
    public void changeDuringCreation(MyPoint mousePos) {
        this.C.mutate_to(mousePos);
    }

    @Override
    public boolean contains(MyPoint mousePos) {
        int[] x = {A.x, B.x, C.x};
        int[] y = {A.y, B.y, C.y};
        int n = 3;
        Polygon temp = new Polygon(x, y, n);
        return temp.contains(new Point(mousePos.x, mousePos.y));
    }

    /**
     * Idea is to use cook-off according to middle of figure
     */
    @Override
    public void resize() {
        find_middle();
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
        A = new MyPoint(baseA);
        A.move_away_from(S, factor);
        B = new MyPoint(baseB);
        B.move_away_from(S, factor);
        C = new MyPoint(baseC);
        C.move_away_from(S, factor);
    }

    /**
     * Method to find circumference middle of triangle
     * using analytical geometry
     */
    public void find_middle() {
        double a, b, c, d, e, f;
        a = baseA.rx;
        b = baseA.ry;
        c = baseB.rx;
        d = baseB.ry;
        e = baseC.rx;
        f = baseC.ry;
        double low = 2 * (a * f - a * d + b * c - b * e - c * f + d * e);
        double newrx = (a * a * f - a * a * d + b * b * f - b * b * d + b * c * c + b * d * d - b * e * e - b * f * f - c * c * f - d * d * f + d * e * e + d * f * f) / low;
        double newry = (a * a * c - a * a * e - a * c * c - a * d * d + a * e * e + a * f * f + b * b * c - b * b * e + c * c * e - c * e * e - c * f * f + d * d * e) / low;
        S.update(newrx, newry);
    }
}
