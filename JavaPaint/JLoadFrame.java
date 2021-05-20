import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
/**
 *  JLoadFrame 
 * class containing Frame that allows functionality to load figures from file
 */
public class JLoadFrame extends JFrame {
    /**
     * gui on which load frame is operating
     */
    GUI gui;
    /**
     * label with file name
     */
    JLabel filename;
    /**
     * Path of file that will be loaded
     */
    String path;
    /**
     * Button which should open FileChooser to pick directory
     */
    JButton fileChooserButton;
    /**
     * @param gui frame in which loadframe is operating
     */
    public JLoadFrame(GUI gui) {
        JLabel label;
        JButton button;
        JPanel panel;
        JLabel title;
        JScrollPane pane;
        fileChooserButton = new JButton("Wybierz");
        //this.setLayout(new BoxLayout(this, BoxLayout.X_AXIS));
        this.gui = gui;
        this.setTitle("Wczytanie z pliku");
        panel = new JPanel();
        //panel.setPreferredSize(new Dimension(150, 200));
        title = new JLabel("Wczytywanie z pliku");
        label = new JLabel("Wybierz nazwe pliku .txt");
        String[] filenames = new File("src/saves/").list();
        button = new JButton("Zatwierdz");
        button.addActionListener(new saveLoader());
        fileChooserButton.addActionListener(new fileChooserListener());
        filename = new JLabel();
        filename.setPreferredSize(new Dimension(150, 25));
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.add(title);
        panel.add(label);
        panel.add(fileChooserButton);
        panel.add(filename);
        panel.add(button);
        this.add(panel);
        this.setVisible(true);
        this.setResizable(false);
        this.pack();
    }

    /**
     *  saveLoader 
     * Class processing file that is given to input and loading all figures
     */
    class saveLoader implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            if (path != null) {
                String pathToSave = path;
                List<String> lines = null;
                try {
                    lines = Files.readAllLines(Path.of(pathToSave));
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                }
                assert lines != null;
                ArrayList<Figure> Figures = new ArrayList<>();
                for (String line : lines) {
                    if (line.charAt(0) == 'T') {
                        Triangle triangle = new Triangle(line);
                        Figures.add(triangle);
                        System.out.println("Added triangle " + triangle.saveData());
                    } else if (line.charAt(0) == 'C') {
                        Circle circle = new Circle(line);
                        Figures.add(circle);
                        System.out.println("Added circle " + circle.saveData());
                    } else if (line.charAt(0) == 'R') {
                        Rectangle rect = new Rectangle(line);
                        Figures.add(rect);
                        System.out.println("Added rectangle " + rect.saveData());
                    } else {
                        System.out.println("Save file is corrupted and contains figures that do not exist.");
                    }
                }
                gui.graphic_panel.Figures = Figures;
                gui.graphic_panel.repaint();
                dispose();
            }
        }
    }

    /**
     * Class to open file chooser on button click and choose directory to save
     */
    class fileChooserListener implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            final JFileChooser fc = new JFileChooser();
            int returnval = fc.showOpenDialog(JLoadFrame.this);
            if (returnval == JFileChooser.APPROVE_OPTION){
                path = fc.getSelectedFile().getAbsolutePath();
                filename.setText(fc.getSelectedFile().getName());
            }
        }
    }
}




