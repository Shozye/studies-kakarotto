import java.awt.*;
import java.util.Objects;

/**
 *  Rectangle 
 * Class that handles rectangle that will be drawn on screen
 * <b>For documentation of overriden methods see</b>
 * @see Figure
 * @see BaseFigure
 * Idea is that we are working on baseA, baseB, baseC, baseD
 * and A,B,C,D are only representations of figure shown to user and calculated
 * on the run
 */
public class Rectangle extends Figure {
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
    MyPoint C; // non static
    /**
     * Resized point of a figure. Also used during creation
     */
    MyPoint D; // non static
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C,D are calculated from this. Changed only during dragging
     */
    MyPoint baseA;
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C,D are calculated from this. Changed only during dragging
     */
    MyPoint baseB;
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C,D are calculated from this. Changed only during dragging
     */
    MyPoint baseC;
    /**
     * Point of a figure instantiated after creation. drawn points A,B,C,D are calculated from this. Changed only during dragging
     */
    MyPoint baseD;
    /**
     * Point symbolizing middle of rectangle
     */
    MyPoint S;

    /**
     * Constructor used during drawing figure on GUI
     * @param A First point clicked during drawing
     * @param B Second point clicked during drawing
     * @param C Rectangle point connected to B and D
     * @param D Rectangle point connected to A and C
     * @param color color of a rectangle
     */
    public Rectangle(MyPoint A, MyPoint B, MyPoint C, MyPoint D, Color color) {
        super(color, "rectangle");
        this.A = new MyPoint(A);
        this.B = new MyPoint(B);
        this.color = color;
        this.C = Objects.requireNonNullElseGet(C, () -> new MyPoint(B));
        this.D = Objects.requireNonNullElseGet(D, () -> new MyPoint(A));
        S = new MyPoint(0, 0);
        created = false;

    }

    /**
     * Constructor used during creation of figure from savefile
     * @param line string containing all data about figure in specified form
     */
    public Rectangle(String line) {
        super();
        String[] creator = line.split(" ");
        baseA = new MyPoint(Double.parseDouble(creator[1]), Double.parseDouble(creator[2]));
        baseB = new MyPoint(Double.parseDouble(creator[3]), Double.parseDouble(creator[4]));
        baseC = new MyPoint(Double.parseDouble(creator[5]), Double.parseDouble(creator[6]));
        baseD = new MyPoint(Double.parseDouble(creator[7]), Double.parseDouble(creator[8]));
        color = new Color(Integer.parseInt(creator[9]));
        how_much_increased = Integer.parseInt(creator[10]);
        A = new MyPoint(baseA);
        B = new MyPoint(baseB);
        C = new MyPoint(baseC);
        D = new MyPoint(baseD);

        S = new MyPoint(baseA);
    }

    @Override
    public String saveData() {
        return "R " +
                baseA.rx + " " + baseA.ry + " " + baseB.rx + " " + baseB.ry + " " + baseC.rx + " " + baseC.ry + " " + baseD.rx + " " + baseD.ry + " " +
                color.getRGB() + " " +
                how_much_increased;
    }

    @Override
    public void draw(Graphics g) {
        if (created) {
            find_middle();
            resize();
        }

        int[] x = {A.x, B.x, C.x, D.x};
        int[] y = {A.y, B.y, C.y, D.y};
        int n = 4;
        g.setColor(color);
        g.drawPolygon(x, y, n);
        g.fillPolygon(x, y, n);
        g.setColor(color.darker().darker());
        if (created) {
            g.fillRect(S.x - 1, S.y - 1, 3, 3);
        }
        if (!created) {
            g.fillRect((int) (A.rx + B.rx + C.rx + D.rx - 1), (int) (A.ry + B.ry + C.ry + D.ry - 1), 3, 3);
        }
    }

    @Override
    public void drawBounds(Graphics g) {
        int[] x = {A.x, B.x, C.x, D.x};
        int[] y = {A.y, B.y, C.y, D.y};
        int n = 4;
        g.setColor(color.darker());
        g.drawPolygon(x, y, n);
    }

    @Override
    public void drag(MyPoint prev, MyPoint now) {
        baseA.update(baseA.rx + now.rx - prev.rx, baseA.ry + now.ry - prev.ry);
        baseB.update(baseB.rx + now.rx - prev.rx, baseB.ry + now.ry - prev.ry);
        baseC.update(baseC.rx + now.rx - prev.rx, baseC.ry + now.ry - prev.ry);
        baseD.update(baseD.rx + now.rx - prev.rx, baseD.ry + now.ry - prev.ry);
    }

    @Override
    public void created() {
        created = true;
        baseA = new MyPoint(A);
        baseB = new MyPoint(B);
        baseC = new MyPoint(C);
        baseD = new MyPoint(D);
    }

    @Override
    public void changeDuringCreation(MyPoint mousePos) {
        if (A.x == B.x) {
            C.update(mousePos.x, C.ry);
            D.update(mousePos.x, D.ry);
        } else if (A.y == B.y) {
            C.update(C.rx, mousePos.ry);
            D.update(D.rx, mousePos.ry);
        } else {
            double a, b, c, d, e, f;
            a = A.x;
            b = A.y;
            c = B.x;
            d = B.y;
            e = mousePos.x;
            f = mousePos.y;
            double low = (a - c) * (a - c) + (b - d) * (b - d);
            double tempdx = ((a * a * a - 2 * a * a * c + a * b * b - a * b * d - a * b * f + a * c * c + a * d * f - b * b * c + b * b * e + b * c * d + b * c * f - 2 * b * d * e - c * d * f + d * d * e) / low);
            double tempdy = ((a * a * b - a * a * d + a * a * f - a * b * c - a * b * e + a * c * d - 2 * a * c * f + a * d * e + b * b * b - 2 * b * b * d + b * c * e + b * d * d + c * c * f - c * d * e) / low);
            double tempcx = ((a * a * c + a * b * d - a * b * f - 2 * a * c * c - a * d * d + a * d * f + b * b * e - b * c * d + b * c * f - 2 * b * d * e + c * c * c + c * d * d - c * d * f + d * d * e) / low);
            double tempcy = ((a * a * f + a * b * c - a * b * e - a * c * d - 2 * a * c * f + a * d * e + b * b * d - b * c * c + b * c * e - 2 * b * d * d + c * c * d + c * c * f - c * d * e + d * d * d) / low);
            D.update(tempdx, tempdy);
            C.update(tempcx, tempcy);
        }
    }

    @Override
    public boolean contains(MyPoint mousePos) {
        int[] x = {A.x, B.x, C.x, D.x};
        int[] y = {A.y, B.y, C.y, D.y};
        int n = 4;
        Polygon temp = new Polygon(x, y, n);
        return temp.contains(new Point(mousePos.x, mousePos.y));
    }

    /**
     * Idea is to use cook-off according to middle of figure
     */
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
        A = new MyPoint(baseA);
        A.move_away_from(S, factor);
        B = new MyPoint(baseB);
        B.move_away_from(S, factor);
        C = new MyPoint(baseC);
        C.move_away_from(S, factor);
        D = new MyPoint(baseD);
        D.move_away_from(S, factor);
    }

    /**
     * Method used to find middle of a rectangle
     * It is the same as centroid.
     */
    public void find_middle() {
        S.update((baseA.rx + baseB.rx + baseC.rx + baseD.rx) / 4, (baseA.ry + baseB.ry + baseC.ry + baseD.ry) / 4);
    }

    @Override
    public String toString() {
        return "ABCD:" + A + " " + B + " " + C + " " + D + " " + how_much_increased + " bABCD " + baseA + " " + baseB + " " + baseC + " " + baseD;
    }
}
