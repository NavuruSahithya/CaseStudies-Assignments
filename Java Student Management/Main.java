import java.util.*;

// Book Class
class Book {
    int id;
    String title;
    String author;
    boolean isIssued;

    Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isIssued = false;
    }
}

// User Class
class User {
    int id;
    String name;

    User(int id, String name) {
        this.id = id;
        this.name = name;
    }
}

// Transaction Class
class Transaction {
    int bookId;
    int userId;
    String issueDate;
    String returnDate;

    Transaction(int bookId, int userId, String issueDate) {
        this.bookId = bookId;
        this.userId = userId;
        this.issueDate = issueDate;
        this.returnDate = null;
    }
}

public class Main {

    static ArrayList<Book> books = new ArrayList<>();
    static ArrayList<User> users = new ArrayList<>();
    static ArrayList<Transaction> transactions = new ArrayList<>();

    static Scanner sc = new Scanner(System.in);

    // Add Book
    public static void addBook() {
        System.out.println("\n📚 --- ADD NEW BOOK TO LIBRARY ---");
        System.out.print("Please enter a unique Book ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter the title of the book: ");
        String title = sc.nextLine();

        System.out.print("Enter the name of the author: ");
        String author = sc.nextLine();

        books.add(new Book(id, title, author));
        System.out.println("✅ Book has been successfully added to the library database.");
    }

    // Register User
    public static void addUser() {
        System.out.println("\n👤 --- USER REGISTRATION ---");
        System.out.print("Enter a unique User ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter full name of the user: ");
        String name = sc.nextLine();

        users.add(new User(id, name));
        System.out.println("✅ User has been successfully registered.");
    }

    // Search Book (case-insensitive)
    public static void searchBook() {
        System.out.println("\n🔍 --- SEARCH FOR A BOOK ---");
        System.out.print("Enter book title or author name to search: ");
        String key = sc.nextLine().toLowerCase();

        boolean found = false;

        for (Book b : books) {
            if (b.title.toLowerCase().contains(key) ||
                b.author.toLowerCase().contains(key)) {

                System.out.println("\n📖 Book Found:");
                System.out.println("   Book ID   : " + b.id);
                System.out.println("   Title     : " + b.title);
                System.out.println("   Author    : " + b.author);
                System.out.println("   Status    : " + (b.isIssued ? "Issued" : "Available"));
                found = true;
            }
        }

        if (!found) {
            System.out.println("❌ No matching books were found in the system.");
        }
    }

    // Issue Book
    public static void issueBook() {
        System.out.println("\n📤 --- ISSUE A BOOK ---");
        System.out.print("Enter the Book ID you want to issue: ");
        int bookId = sc.nextInt();

        System.out.print("Enter the User ID of the person issuing the book: ");
        int userId = sc.nextInt();
        sc.nextLine();

        System.out.println("Enter the Issue Date in format (DD/MM/YYYY), for example: 05/04/2026");
        String issueDate = sc.nextLine();

        for (Book b : books) {
            if (b.id == bookId && !b.isIssued) {
                b.isIssued = true;
                transactions.add(new Transaction(bookId, userId, issueDate));

                System.out.println("✅ Book has been successfully issued.");
                System.out.println("📅 Important: Please return within 7 days to avoid late fine.");
                return;
            }
        }

        System.out.println("❌ This book is either not available or already issued.");
    }

    // Return Book
    public static void returnBook() {
        System.out.println("\n📥 --- RETURN A BOOK ---");
        System.out.print("Enter the Book ID you are returning: ");
        int bookId = sc.nextInt();
        sc.nextLine();

        System.out.println("Enter the Return Date in format (DD/MM/YYYY), for example: 12/04/2026");
        String returnDate = sc.nextLine();

        for (Transaction t : transactions) {
            if (t.bookId == bookId && t.returnDate == null) {

                t.returnDate = returnDate;

                // Simple fine logic (not real date diff)
                int fine = 0;
                System.out.print("Enter number of days book was kept: ");
                int days = sc.nextInt();

                if (days > 7) {
                    fine = (days - 7) * 10;
                }

                for (Book b : books) {
                    if (b.id == bookId) {
                        b.isIssued = false;
                    }
                }

                System.out.println("✅ Book has been successfully returned.");
                System.out.println("📊 Total days used: " + days);

                if (fine > 0) {
                    System.out.println("💰 Late return fine: Rs. " + fine);
                } else {
                    System.out.println("🎉 No fine. Book returned on time.");
                }
                return;
            }
        }

        System.out.println("❌ Invalid return. Please check Book ID.");
    }

    // Remove Book
    public static void removeBook() {
        System.out.println("\n🗑️ --- REMOVE A BOOK ---");
        System.out.print("Enter the Book ID to remove from library: ");
        int id = sc.nextInt();

        books.removeIf(b -> b.id == id);
        System.out.println("✅ Book has been removed successfully.");
    }

    // Update Book
    public static void updateBook() {
        System.out.println("\n✏️ --- UPDATE BOOK DETAILS ---");
        System.out.print("Enter the Book ID to update: ");
        int id = sc.nextInt();
        sc.nextLine();

        for (Book b : books) {
            if (b.id == id) {
                System.out.print("Enter updated book title: ");
                b.title = sc.nextLine();

                System.out.print("Enter updated author name: ");
                b.author = sc.nextLine();

                System.out.println("✅ Book details updated successfully.");
                return;
            }
        }

        System.out.println("❌ Book not found in the system.");
    }

    public static void main(String[] args) {

        while (true) {
            System.out.println("\n================ LIBRARY MANAGEMENT SYSTEM ================");
            System.out.println("1. Add a New Book to Library");
            System.out.println("2. Register a New User");
            System.out.println("3. Search for Books (by Title/Author)");
            System.out.println("4. Issue a Book to a User");
            System.out.println("5. Return a Book");
            System.out.println("6. Remove a Book from Library");
            System.out.println("7. Update Book Information");
            System.out.println("8. Exit the System");

            System.out.print("\nPlease enter your choice (1-8): ");
            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1: addBook(); break;
                case 2: addUser(); break;
                case 3: searchBook(); break;
                case 4: issueBook(); break;
                case 5: returnBook(); break;
                case 6: removeBook(); break;
                case 7: updateBook(); break;
                case 8:
                    System.out.println("👋 Thank you for using the Library Management System.");
                    return;
                default:
                    System.out.println("❌ Invalid input. Please enter a valid option.");
            }
        }
    }
}