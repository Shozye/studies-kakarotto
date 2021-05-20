import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Comparator;

/**
 * JSaveFrame
 * Class that contains frame to allow functionality of saving
 * It contains field to put filename and listener to save figures to it.
 */
public class JSaveFrame extends JFrame {
    /**
     * Field where information about filename is written to
     */
    JTextField field;
    /**
     * gui on which JSaveFrame is operating
     */
    GUI gui;

    /**
     * Directory name where the file will be saved
     */
    JLabel dirname;

    /**
     * Button which should open FileChooser to pick directory
     */
    JButton dirChooseButton;

    /**
     * path to directory to which file should be saved
     */
    String path;

    /**
     * @param gui gui on which JSaveFrame is operating
     */
    public JSaveFrame(GUI gui) {
        JLabel title;
        JLabel label;
        JButton button;
        JPanel panel;
        JLabel label2;
        dirname = new JLabel();
        dirname.setPreferredSize(new Dimension(150,25));
        //this.setLayout(new BoxLayout(this, BoxLayout.X_AXIS));
        this.gui = gui;
        this.setTitle("Zapisanie do pliku");
        panel = new JPanel();
        //panel.setPreferredSize(new Dimension(150, 200));
        title = new JLabel("Zapisywanie do pliku");
        label2 = new JLabel("Wybierz folder");
        dirChooseButton = new JButton("Wybierz");
        dirChooseButton.addActionListener(new fileChooserListener());
        label = new JLabel("Wpisz nazwe pliku");
        field = new JTextField();
        field.setAlignmentX(CENTER_ALIGNMENT);
        button = new JButton("Zatwierdz");
        button.addActionListener(new fileSaver());
        field.setPreferredSize(new Dimension(150, 25));

        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.add(title);
        panel.add(label2);
        panel.add(dirChooseButton);
        panel.add(dirname);
        panel.add(label);
        panel.add(field);
        panel.add(button);

        this.add(panel);
        this.setVisible(true);
        this.setResizable(false);
        this.pack();
    }

    /**
     *  fileSaver 
     * Listener to save figures to file specified in field
     */
    class fileSaver implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            String filename = field.getText();
            if (filename.length() >= 4 && path != null) {


                String pathToSaves = path;

                try {
                    FileWriter filewriter = new FileWriter(pathToSaves +"/"+ filename);
                    PrintWriter pw = new PrintWriter(filewriter);
                    Comparator<Figure> comparator = Comparator.comparing(Figure::returnPriority);
                    gui.graphic_panel.Figures.sort(comparator);
                    for (Figure figure : gui.graphic_panel.Figures) {
                        pw.print(figure.saveData() + "\n");
                    }
                    pw.close();
                } catch (IOException ioException) {
                    ioException.printStackTrace();
                }
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
            fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
            int returnval = fc.showOpenDialog(JSaveFrame.this);
            if (returnval == JFileChooser.APPROVE_OPTION){
                path = fc.getSelectedFile().getAbsolutePath();
                dirname.setText(fc.getSelectedFile().getName());
            }
        }
    }
}

