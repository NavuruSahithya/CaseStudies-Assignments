package service;

import model.Book;
import exception.BookNotFoundException;

import java.util.ArrayList;

public class LibraryService {

    private ArrayList<Book> books = new ArrayList<>();

    // Add Book
    public void addBook(Book book) {
        books.add(book);
        System.out.println("Book Added Successfully");
    }

    // View Books
    public void viewBooks() {

        if (books.isEmpty()) {
            System.out.println("No Books Available");
            return;
        }

        for (Book book : books) {
            System.out.println(book);
        }
    }

    // Search Book
    public Book searchBook(int id)
            throws BookNotFoundException {

        for (Book book : books) {

            if (book.getBookId() == id) {
                return book;
            }
        }

        throw new BookNotFoundException(
                "Book Not Found"
        );
    }

    // Issue Book
    public void issueBook(int id)
            throws BookNotFoundException {

        Book book = searchBook(id);

        if (!book.isIssued()) {
            book.setIssued(true);
            System.out.println("Book Issued");
        } else {
            System.out.println("Book Already Issued");
        }
    }

    // Return Book
    public void returnBook(int id)
            throws BookNotFoundException {

        Book book = searchBook(id);

        if (book.isIssued()) {
            book.setIssued(false);
            System.out.println("Book Returned");
        } else {
            System.out.println("Book Was Not Issued");
        }
    }

    // Remove Book
    public void removeBook(int id)
            throws BookNotFoundException {

        Book book = searchBook(id);

        books.remove(book);

        System.out.println("Book Removed");
    }
}