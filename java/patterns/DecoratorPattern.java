/**
 *	Pattern: Decorator Pattern
 *	Intent: Add dynamically features to a object.
 */
import javax.swing.JOptionPane;
import java.util.Date;

/**
 *	Component
 */
interface ITextViewer {

	public void viewText(String text);

}

/**
 *	ConcreteComponent
 */
class StdoutTextViewer implements ITextViewer {

	public void viewText(String text) {
		System.out.println(text);
	}
}


/**
 *	ConcreteComponent
 */
class PopupTextViewer implements ITextViewer {

	public void viewText(String text) {
		JOptionPane.showConfirmDialog(null, text);
	}
}

/**
 *	Decorator
 */
class TextDecorator implements ITextViewer {

	private ITextViewer textViewer;

	public TextDecorator(ITextViewer textViewer) {
		this.textViewer = textViewer;
	}

	public void viewText(String text) {
		textViewer.viewText(text);
	}
}

/**
 *	ConcreteDecorator
 */
class DoubleSpaceRemoverDecorator extends TextDecorator {

	public DoubleSpaceRemoverDecorator(ITextViewer textViewer) {
		super(textViewer);
	}

	public void viewText(String text) {
		super.viewText(text.replace("  ", " "));
	}
}

/**
 *	ConcreteDecorator
 */
class UppercaseDecorator extends TextDecorator {

	public UppercaseDecorator(ITextViewer textViewer) {
		super(textViewer);
	}

	public void viewText(String text) {
		super.viewText(text.toUpperCase());
	}
}

/**
 *	ConcreteDecorator
 */
class LoggerDecorator extends TextDecorator {

	public LoggerDecorator(ITextViewer textViewer) {
		super(textViewer);
	}

	public void viewText(String text) {
		System.out.println(new Date().getTime() + ": About to view: " + text);
		super.viewText(text);
	}
}

public class DecoratorPattern {
	public static void main(String[] args) {
		String text = "foo bar  baz  DECorator";
		ITextViewer viewer = new StdoutTextViewer();
		viewer.viewText(text); // output: "foo bar  baz  DECorator"
		TextDecorator spaceRemover = new DoubleSpaceRemoverDecorator(viewer);
		spaceRemover.viewText(text); // output: "foo bar baz DECorator"

		viewer = new PopupTextViewer();
		TextDecorator logger = new LoggerDecorator(viewer);
		TextDecorator uppercase = new UppercaseDecorator(logger);
		viewer.viewText(text); // popup-output: "foo bar  baz  DECorator"
		logger.viewText(text);	// stdout-output: "[current-time]: About to view: foo bar  baz DECorator"
								// popup-output: "foo bar  baz  DECorator"
		uppercase.viewText(text);	// stdout-output: "[current-time]: About to view: FOO BAR  BAZ DECORATOR"
									// popup-output: "FOO BAR  BAZ  DECORATOR"
	}
}
