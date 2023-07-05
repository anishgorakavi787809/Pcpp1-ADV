import java.sql.*;
import java.util.Scanner;

public class j {
    private static final String DATABASE_URL = "jdbc:sqlite:Tasks.db";

    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection(DATABASE_URL)) {
            createTable(conn);

            while (true) {
                System.out.println("1. Show list");
                System.out.println("2. Add task");
                System.out.println("3. Remove task");
                System.out.println("4. Update task priority");
                System.out.println("5. Quit");

                Scanner scanner = new Scanner(System.in);
                System.out.print("Enter option by number: ");
                int option = Integer.parseInt(scanner.nextLine());

                switch (option) {
                    case 1:
                        showTaskList(conn);
                        break;

                    case 2:
                        addTask(conn, scanner);
                        break;

                    case 3:
                        removeTask(conn, scanner);
                        break;

                    case 4:
                        updateTaskPriority(conn, scanner);
                        break;

                    case 5:
                        System.out.println("Well, it's nice seeing you");
                        return;

                    default:
                        System.out.println("Error, you entered an invalid input");
                }

                System.out.println("Press enter to go to the main menu");
                scanner.nextLine();
                clearConsole();
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private static void createTable(Connection conn) throws SQLException {
        String query = "CREATE TABLE IF NOT EXISTS task_list (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, priority INTEGER)";
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(query);
        }
    }

    private static void showTaskList(Connection conn) throws SQLException {
        String query = "SELECT * FROM task_list ORDER BY priority ASC";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            if (rs.next()) {
                System.out.println("╒══════╤═════════════════╤════════════╕");
                System.out.println("│   id │ Task Name       │   priority │");
                System.out.println("╞══════╪═════════════════╪════════════╡");
                do {
                    int id = rs.getInt("id");
                    String taskName = rs.getString("name");
                    int priority = rs.getInt("priority");
                    System.out.printf("│%6d│%-17s│%12d│%n", id, taskName, priority);
                } while (rs.next());
                System.out.println("╘══════╧═════════════════╧════════════╛");
            } else {
                System.out.println("List is empty");
            }
        }
    }

    private static void addTask(Connection conn, Scanner scanner) throws SQLException {
        System.out.println("Enter task name:");
        String taskName = scanner.nextLine();

        System.out.println("Enter task priority:");
        int taskPriority = Integer.parseInt(scanner.nextLine());

        if (taskPriority < 1) {
            System.out.println("Task priority should be >= 1");
            return;
        }

        String query = "INSERT INTO task_list (name, priority) VALUES (?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, taskName);
            stmt.setInt(2, taskPriority);
            stmt.executeUpdate();
        }

        System.out.println("Added the task to the database");
    }

    private static void removeTask(Connection conn, Scanner scanner) throws SQLException {
        System.out.println("Enter the ID of the task you want to remove:");
        int taskId = Integer.parseInt(scanner.nextLine());

        String query = "DELETE FROM task_list WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, taskId);
            int rowCount = stmt.executeUpdate();
            if (rowCount > 0) {
                System.out.println("Deleted the task");
            } else {
                System.out.println("Task not found");
            }
        }
    }

    private static void updateTaskPriority(Connection conn, Scanner scanner) throws SQLException {
        System.out.println("Enter the ID of the task you want to update:");
        int taskId = Integer.parseInt(scanner.nextLine());

        System.out.println("Enter the new task priority:");
        int taskPriority = Integer.parseInt(scanner.nextLine());

        if (taskPriority < 1) {
            System.out.println("Task priority should be >= 1");
            return;
        }

        String query = "UPDATE task_list SET priority = ? WHERE id = ?";
        try (PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setInt(1, taskPriority);
            stmt.setInt(2, taskId);
            stmt.executeUpdate();
        }

        System.out.println("Updated the task priority in the database");
    }

    private static void clearConsole() {
        try {
            if (System.getProperty("os.name").contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                Runtime.getRuntime().exec("clear");
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
