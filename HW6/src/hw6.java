public class VariableExample {

    // Java SetBy
    int initializedVar = 10;

    // Java SetBy
    void SV() {
        int setVar;
        // Java SetBy
        setVar = 20;
    }

    // Java Set Partial: Another entity setting a variable in a separate statement
    void S(int value) {
        int variableSetBy;
        variableSetBy = value;
    }

    // Java Set Partial: Another entity both setting and initializing a variable
    void P(int value) {
        int variableSetAndInitBy = value;
    }

    public static void main(String[] args) {
        VariableExample example = new VariableExample();

        // Java Set Init
        System.out.println("Initialized Variable: " + example.initializedVar);

        example.setVariable();
        example.setVariableBy(30);
        example.setAndInitVariableBy(40);
    }
}
