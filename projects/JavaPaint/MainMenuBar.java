import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 *  MainMenuBar 
 * MainMenuBar is class that operates menu bar at top of GUI
 * It contains 4 JMenuItems that should give
 * save, load, help and info functionality
 */
public class MainMenuBar extends JMenuBar {
    /**
     * Object that is shown in main menu
     */
    JMenu menu;
    /**
     * found in list after clicking "File" Clicking it should open frame allowing save functionality
     */
    JMenuItem save;
    /**
     * found in list after clicking "File" Clicking it should open frame allowing load functionality
     */
    JMenuItem load;
    /**
     * found in list after clicking "File" Clicking it should open frame allowing help functionality
     */
    JMenuItem help;
    /**
     * found in list after clicking "File" Clicking it should open frame allowing info functionality
     */
    JMenuItem info;
    /**
     * gui on which menu bar is
     */
    GUI gui;

    /**
     * creator for menubar. It creates everything inside and adds action listeners to this
     * @param gui gui on which menu bar is
     */
    public MainMenuBar(GUI gui) {
        this.gui = gui;
        menu = new JMenu("File");
        this.add(menu);
        info = new JMenuItem("Info");
        help = new JMenuItem("Help");
        save = new JMenuItem("Save");
        load = new JMenuItem("Load");
        info.addActionListener(new infoListener());
        help.addActionListener(new helpListener());
        save.addActionListener(new saveListener());
        load.addActionListener(new loadListener());

        menu.add(info);
        menu.add(help);
        menu.add(save);
        menu.add(load);
    }

    /**
     * Class that gives functionality to open JInfoFrame after action
     * @see JInfoFrame
     */
    class infoListener implements ActionListener {
        /**
         * Frame with info about program
         */
        JInfoFrame frame;

        /**
         * Basic constructor for listener.
         */
        public infoListener() {
            frame = null;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (frame != null) {
                frame.dispose();
            }
            frame = new JInfoFrame();
            frame.setBounds((int) gui.frame.getBounds().getMinX() + 100, (int) gui.frame.getBounds().getMinY(), 0, 0);
            frame.pack();
        }
    }

    /**
     * Class that gives functionality to open JHelpFrame after action
     * @see JHelpFrame
     */
    class helpListener implements ActionListener {
        /**
         * Frame with help to program
         */
        JHelpFrame frame;

        /**
         * Basic constructor for listener.
         */
        public helpListener() {
            frame = null;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (frame != null) {
                frame.dispose();
            }
            frame = new JHelpFrame();
            frame.setBounds((int) gui.frame.getBounds().getMinX() + 100, (int) gui.frame.getBounds().getMinY(), 0, 0);
            frame.pack();
        }
    }
    /**
     * Class that gives functionality to open JSaveFrame after action
     * @see JSaveFrame
     */
    class saveListener implements ActionListener {
        /**
         * Frame that allows saving
         */
        JSaveFrame frame;

        /**
         * Basic constructor for listener.
         */
        public saveListener() {
            frame = null;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (frame != null) {
                frame.dispose();
            }
            frame = new JSaveFrame(gui);
            frame.setBounds((int) gui.frame.getBounds().getMinX() + 100, (int) gui.frame.getBounds().getMinY(), 0, 0);
            frame.pack();
        }
    }
    /**
     * Class that gives functionality to open JLoadFrame after action
     * @see JLoadFrame
     */
    class loadListener implements ActionListener {
        /**
         * Frame that allows loading figures from file
         */
        JLoadFrame frame;

        /**
         * Basic constructor for listener.
         */
        public loadListener() {
            frame = null;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (frame != null) {
                frame.dispose();
            }
            frame = new JLoadFrame(gui);
            frame.setBounds((int) gui.frame.getBounds().getMinX() + 100, (int) gui.frame.getBounds().getMinY(), 0, 0);
            frame.pack();
        }
    }

}
