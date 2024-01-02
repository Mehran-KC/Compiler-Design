// Class definition for the main program
public class ss1 {
    public static void main(String[] args) {
        // Create an object of the second class
        ss2 mySecondClass = new ss2(); // Corrected class instantiation

        // Call a method from the second class
        mySecondClass.displayMessage();
    }
}

// Class definition for a second class
class ss2 {
    // Method to display a message
    public void displayMessage() {
        System.out.println("Hello from ss2!");
    }
}
