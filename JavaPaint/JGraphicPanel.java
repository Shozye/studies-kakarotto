import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Comparator;

/**
 *  JGraphicPanel 
 * Place where all the drawing will be done
 * tempBaseFigure is BaseFigure in creation
 * @see BaseFigure
 * Figures is list of drawn figures
 * @see Figure
 * @see Drawer
 * colorChangeFrame is shown after right clicking at drawn Figure
 * @see JColorChangeFrame
 */
public class JGraphicPanel extends JPanel {
    /**
     * Figure during creation, whose shape is changing
     */
    BaseFigure tempBaseFigure;
    /**
     * Figures is list of drawn figures
     */
    ArrayList<Figure> Figures;
    /**
     * class containing listener of mouse on this panel
     */
    Drawer drawer;
    /**
     * frame used to change color of figure after right clicking
     */
    JColorChangeFrame colorChangeFrame;
    /**
     * Frame in which this panel is
     */
    JFrame frame;

    /**
     * Constructor for JGraphicPanel
     * @param width width of panel
     * @param height height of panel
     * @param frame frame in which panel is created
     */
    public JGraphicPanel(int width, int height, JFrame frame) {
        super(new BorderLayout());
        this.frame = frame;
        setBackground(Color.white);
        this.setBorder(BorderFactory.createLineBorder(Color.PINK, 1, true));
        this.setPreferredSize(new Dimension(width, height));
        drawer = new Drawer(this);
        addMouseWheelListener(drawer);
        addMouseListener(drawer);
        addMouseMotionListener(drawer);

        colorChangeFrame = null;

        tempBaseFigure = null;
        Figures = new ArrayList<>();
    }

    /**
     * Function that is doing all the drawing
     * Figures should be sorted by priority
     * Higher priority means that figure will be
     * shown on the top of another
     * Highest priority figure gets special border
     * @see Figure
     * @param g basic Graphics
     */
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Comparator<Figure> comparator = Comparator.comparing(Figure::returnPriority);
        Figures.sort(comparator);
        for (Figure figure : Figures) {
            figure.draw(g);
        }
        if (tempBaseFigure != null) {
            tempBaseFigure.draw(g);
        } else {
            if (Figures.size() >= 1) {
                Figures.get(Figures.size() - 1).drawBounds(g);
            }
        }
    }

}

