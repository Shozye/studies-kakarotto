import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *  JColorChangeFrame 
 * Class that manages frame that shows up to change
 * color of figure.
 */
public class JColorChangeFrame extends JFrame {
    /**
     * panel with Color palette
     */
    JColorChooser panel;
    /**
     * Figure we are changing color of
     */
    Figure figure;
    /**
     * Graphic panel on which frame is changing color of figure
     */
    JGraphicPanel gp;

    /**
     * creates frame
     * @param figure figure on which color should be changed
     * @param gp graphic panel where is figure
     */
    public JColorChangeFrame(Figure figure, JGraphicPanel gp) {
        this.figure = figure;
        this.gp = gp;

        this.panel = new JColorChooser(figure.color);
        this.add(panel);
        panel.getSelectionModel().addChangeListener(new changeFigureColorListener());

        this.setVisible(true);
        this.setBounds((int) gp.frame.getBounds().getMinX() - 250, (int) gp.frame.getBounds().getMinY(), 0, 0);
        this.setResizable(false);

        this.pack();
    }

    /**
     *  changeFigureColorListener 
     * Class used to change color of a figure changing color in JcolorChooser
     */
    class changeFigureColorListener implements ChangeListener {

        @Override
        public void stateChanged(ChangeEvent e) {
            Color new_color = panel.getColor();
            figure.changeColor(new_color);
            gp.repaint();
        }
    }
}
