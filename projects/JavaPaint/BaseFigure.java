import java.awt.*;

/**
 *  BaseFigure 
 * Interface connecting every drawable figure
 * It is needed to allow
 * @see Line
 * to be drawn
 */
public interface BaseFigure {
    /**
     * Method that will be executed to draw figure
     * @param g the same argument as in paintcomponent of JPanel
     */
    void draw(Graphics g);

    /**
     * Method that will change shape of figure when we are moving mouse during creation of figure
     * @param mousePos place where is our mouse now
     */
    void changeDuringCreation(MyPoint mousePos);
}
