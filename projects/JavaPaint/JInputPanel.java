import javax.swing.*;
import java.awt.*;

/**
 *  JInputPanel 
 * Container for action panel and color panel
 * @see JColorPanel
 * @see JActionPanel
 */
public class JInputPanel extends JPanel {
    /**
     * Panel containing color palette
     */
    JColorPanel colorPanel;
    /**
     * Panel containing actions to pick from
     */
    JActionPanel actionPanel;

    /**
     * BaseConstructor of input panel where action panel and color panel are
     * @param width width of panel
     * @param height height of panel
     */
    public JInputPanel(int width, int height) {
        super(new BorderLayout());
        setBackground(Color.gray);
        this.setPreferredSize(new Dimension(width, height));

        actionPanel = new JActionPanel(height * 5, height);
        this.add(actionPanel, BorderLayout.EAST);

        colorPanel = new JColorPanel(height / 2 * 5, height);
        this.add(colorPanel, BorderLayout.WEST);
    }
}
