import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

class Student {

    int id;
    String name;
    String course;

    Student(int id, String name, String course) {

        this.id = id;
        this.name = name;
        this.course = course;
    }

    public String toString() {

        return "ID: " + id +
                " | Name: " + name +
                " | Course: " + course;
    }
}

public class Main extends JFrame {

    ArrayList<Student> students = new ArrayList<>();

    JTextField idField;
    JTextField nameField;
    JTextField courseField;

    JTextArea outputArea;

    public Main() {

        setTitle("Student Course Management System");
        setSize(750, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Main Panel
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.setBackground(new Color(245, 247, 250));

        // Header
        JLabel title = new JLabel(
                "Student Course Management System",
                JLabel.CENTER
        );

        title.setFont(new Font("Arial", Font.BOLD, 26));
        title.setBorder(
                BorderFactory.createEmptyBorder(
                        20, 10, 20, 10
                )
        );

        mainPanel.add(title, BorderLayout.NORTH);

        // Form Panel
        JPanel formPanel = new JPanel();

        formPanel.setLayout(
                new GridLayout(4, 2, 15, 15)
        );

        formPanel.setBorder(
                BorderFactory.createEmptyBorder(
                        20, 40, 20, 40
                )
        );

        formPanel.setBackground(Color.WHITE);

        JLabel idLabel = new JLabel("Student ID:");
        JLabel nameLabel = new JLabel("Student Name:");
        JLabel courseLabel = new JLabel("Course:");

        idField = new JTextField();
        nameField = new JTextField();
        courseField = new JTextField();

        JButton addBtn =
                new JButton("Register Student");

        JButton viewBtn =
                new JButton("View Enrollments");

        JButton searchBtn =
                new JButton("Search Student");

        formPanel.add(idLabel);
        formPanel.add(idField);

        formPanel.add(nameLabel);
        formPanel.add(nameField);

        formPanel.add(courseLabel);
        formPanel.add(courseField);

        formPanel.add(addBtn);
        formPanel.add(viewBtn);

        // Output Area
        outputArea = new JTextArea();

        outputArea.setEditable(false);

        outputArea.setFont(
                new Font(
                        "Monospaced",
                        Font.PLAIN,
                        14
                )
        );

        JScrollPane scrollPane =
                new JScrollPane(outputArea);

        scrollPane.setBorder(
                BorderFactory.createTitledBorder(
                        "Student Records"
                )
        );

        // Bottom Panel
        JPanel bottomPanel = new JPanel();

        bottomPanel.setBackground(
                new Color(245, 247, 250)
        );

        bottomPanel.add(searchBtn);

        // Center Panel
        JPanel centerPanel =
                new JPanel(new BorderLayout());

        centerPanel.add(
                formPanel,
                BorderLayout.NORTH
        );

        centerPanel.add(
                scrollPane,
                BorderLayout.CENTER
        );

        mainPanel.add(
                centerPanel,
                BorderLayout.CENTER
        );

        mainPanel.add(
                bottomPanel,
                BorderLayout.SOUTH
        );

        add(mainPanel);

        // Register Student
        addBtn.addActionListener(e -> {

            try {

                int id = Integer.parseInt(
                        idField.getText()
                );

                String name =
                        nameField.getText();

                String course =
                        courseField.getText();

                if (name.isEmpty()
                        || course.isEmpty()) {

                    JOptionPane.showMessageDialog(
                            this,
                            "Please fill all fields"
                    );

                    return;
                }

                students.add(
                        new Student(
                                id,
                                name,
                                course
                        )
                );

                JOptionPane.showMessageDialog(
                        this,
                        "Student Registered Successfully"
                );

                idField.setText("");
                nameField.setText("");
                courseField.setText("");

            } catch (Exception ex) {

                JOptionPane.showMessageDialog(
                        this,
                        "Invalid Input"
                );
            }
        });

        // View Enrollments
        viewBtn.addActionListener(e -> {

            outputArea.setText("");

            if (students.isEmpty()) {

                outputArea.setText(
                        "No Students Available"
                );

            } else {

                for (Student s : students) {

                    outputArea.append(
                            s.toString() +
                                    "\n\n"
                    );
                }
            }
        });

        // Search Student
        searchBtn.addActionListener(e -> {

            try {

                int searchId =
                        Integer.parseInt(

                                JOptionPane.showInputDialog(
                                        "Enter Student ID"
                                )
                        );

                boolean found = false;

                outputArea.setText("");

                for (Student s : students) {

                    if (s.id == searchId) {

                        found = true;

                        outputArea.setText(
                                "Student Found\n\n"
                                        + s.toString()
                        );
                    }
                }

                if (!found) {

                    outputArea.setText(
                            "Student Not Found"
                    );
                }

            } catch (Exception ex) {

                JOptionPane.showMessageDialog(
                        this,
                        "Invalid Input"
                );
            }
        });

        setVisible(true);
    }

    public static void main(String[] args) {

        new Main();
    }
}