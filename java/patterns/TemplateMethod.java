/**
 *	Pattern: Template Method
 *	Intent: Define the skeleton of an algorithm and let some steps implement
 *			by it's subclasses allowing variation of these steps throught different
 *			subclasses.
 */
import javax.swing.JOptionPane;

/**
 *	The abstract class
 */
abstract class Calculator {

	/**
	 *	The template method, which calls the primitive operations getInput and printResult.
	 */
	public void performSummation() {
		int numberCount = getInput("How many numbers do you want to add?");
		
		int result = 0;
		for (int i = 1; i <= numberCount; i++) {
			result += getInput(String.format("Enter your %d. number", i));
		}

		printResult(String.format("Your result is %d", result));
	}

	/**
	 *	Concrete implementation provided by subclasses.
	 */
	protected abstract int getInput(String message);

	protected abstract void printResult(String message);
}

class ConsoleCalculator extends Calculator {

	protected int getInput(String message) {
		System.out.println(message);

		int input = 0;
		try {
			java.io.BufferedReader stdin = new java.io.BufferedReader(
					new java.io.InputStreamReader(System.in));
			String line = stdin.readLine();
			input = Integer.parseInt(line);
		} catch (java.io.IOException e) { 
			System.out.println(e);
		} catch (NumberFormatException e) {
			System.out.println("You entered a invalid number, please try again");
			return getInput(message);
		}

		return input;
	}

	protected void printResult(String message) {
		System.out.println(message);
	}
}

class MessageBoxCalculator extends Calculator {

	protected int getInput(String message) {
		int input = 0;

		try {
			String dialogInput = JOptionPane.showInputDialog(message);
			input = Integer.parseInt(dialogInput);
		} catch (NumberFormatException e) {
			System.out.println("You entered a invalid number, please try again");
			return getInput(message);
		}

		return input;
	}

	protected void printResult(String message) {
		JOptionPane.showConfirmDialog(null, message);
	}
}

public class TemplateMethod {
	public static void main(String[] args) {
		Calculator calculator = new ConsoleCalculator();
		calculator.performSummation();

		calculator = new MessageBoxCalculator();
		calculator.performSummation();
	}
}
