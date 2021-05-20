import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *  GUI 
 * Class that contains main frame of application.
 * It also connects graphic panel to input panel and to menu
 * @see MainMenuBar
 * @see JInputPanel
 * @see JGraphicPanel
 */
public class GUI {
    /**
     * Main frame that contains everything
     */
    JFrame frame;
    /**
     * Graphic panel on which there is a possibility to draw
     */
    JGraphicPanel graphic_panel;
    /**
     * Panel where user can choose color and action to do
     */
    JInputPanel input_panel;
    /**
     * Menu at the top of frame that contains info, help, save and load functionality
     */
    MainMenuBar menu;

    /**
     * Initializing GUI
     * @param size width and height of frame is equal to size
     */
    public GUI(int size) {
        frame = new JFrame();
        frame.setPreferredSize(new Dimension(size, size));
        menu = new MainMenuBar(this);
        graphic_panel = new JGraphicPanel(size, size - 150 - menu.getHeight() - 10 - 1, frame);
        input_panel = new JInputPanel(size, 100);
        for (JColorButton btn : input_panel.colorPanel.buttons) {
            btn.addActionListener(new ColorListener());
        }
        for (JActionButton btn : input_panel.actionPanel.actionButtons) {
            btn.addActionListener(new pickActionListener());
        }

        frame.add(input_panel, BorderLayout.NORTH);
        frame.add(graphic_panel, BorderLayout.SOUTH);
        frame.setJMenuBar(menu);

        frame.setResizable(false);
        frame.setBounds(500, 100, 0, 0);
        frame.setVisible(true);
        frame.pack();
    }

    /**
     *  Color Listener 
     * Class that connects color buttons in input panel to drawer
     * @see Drawer
     * @see JColorPanel
     */
    class ColorListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            JColorButton temp = (JColorButton) e.getSource();
            graphic_panel.drawer.prev_color = graphic_panel.drawer.color;
            graphic_panel.drawer.color = temp.color;
            graphic_panel.drawer.resetAction();
            graphic_panel.repaint();
            System.out.println("Color on graphicPanel changed to " + graphic_panel.drawer.color);
        }
    }
    /**
     *  pickActionListener 
     * Class that connects action buttons in input panel to drawer
     * @see Drawer
     * @see JColorPanel
     */
    class pickActionListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            JActionButton temp = (JActionButton) e.getSource();
            graphic_panel.drawer.prev_action = graphic_panel.drawer.action;
            graphic_panel.drawer.action = temp.action_type;
            graphic_panel.drawer.resetAction();
            graphic_panel.repaint();

            System.out.println("Action on graphicPanel changed to " + graphic_panel.drawer.action + " and prevAction is " + graphic_panel.drawer.prev_action);
        }
    }
}
