import java.awt.*;

/**
 *  Line 
 * Class controlling Line that is created on the graphic panel
 * during creation of Triangle and Rectangle
 * For description of overriden methods look in
 * @see BaseFigure
 */
public class Line implements BaseFigure {
    /**
     *  start point of line
     */
    MyPoint creator;
    /**
     *  end point of line
     */
    MyPoint finisher;
    /**
     * color of line
     */
    Color color;

    /**
     * Constructor that is used during drawing of figure
     * @param creator start point of line
     * @param finisher end point of line
     * @param color color of line
     */
    public Line(MyPoint creator, MyPoint finisher, Color color) {
        if (finisher == null) {
            this.finisher = new MyPoint(creator);
        } else {
            this.finisher = new MyPoint(finisher);
        }
        this.creator = new MyPoint(creator);
        this.color = color;
    }

    @Override
    public void draw(Graphics g) {
        g.setColor(this.color);
        g.drawLine(creator.x, creator.y, finisher.x, finisher.y);
    }

    @Override
    public void changeDuringCreation(MyPoint mousePos) {
        finisher = new MyPoint(mousePos);
    }


}
