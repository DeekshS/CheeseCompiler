from flask import render_template, request, Blueprint
import subprocess
import html

# Define Blueprints
home = Blueprint('home', __name__)
compile = Blueprint('compile', __name__)

# Home Route
@home.route('/')
def index():
    return render_template('home.html')

# Compile Code Route
@compile.route('/compile', methods=['POST'])
def compile_code():
    if request.method == "POST":
        cheese_code = request.form["code"]
        # Escape only special characters like <, >, & but leave quotes untouched
        escaped_cheese_code = html.escape(cheese_code, quote=False)

        if is_cheese_code(cheese_code):
            code = translate_cheese_to_python(cheese_code)
            result = execute_python_code(code)
            return render_template("compile.html", result=result, escaped_cheese_code=escaped_cheese_code)
        else:
            result = "The code you provided is not valid Cheese code. Please try again with valid Cheese code."
            return render_template("compile.html", result=result, escaped_cheese_code=escaped_cheese_code)
    
    return render_template("index.html")

# Function to validate Cheese code
def is_cheese_code(code):
    CHEESE_TO_PYTHON = {
        "🧀cheddar🧀": "def",
        "🧀brie🧀": "if",
        "🧀provolone🧀": "elif",
        "🧀gouda🧀": "else",
        "🧀parmesan🧀": "print",
        "🧀mozzarella🧀": "for",
        "🧀ricotta🧀": "while",
        "🧀gruyere🧀": "import",
        "🧀feta🧀": "return",
    }
    # Check if any cheese keyword exists in the code
    for cheese_keyword in CHEESE_TO_PYTHON.keys():
        if cheese_keyword in code:
            return True
    return False

# Function to translate Cheese code to Python code
def translate_cheese_to_python(cheese_code):
    CHEESE_TO_PYTHON = {
        "🧀cheddar🧀": "def",
        "🧀brie🧀": "if",
        "🧀provolone🧀": "elif",
        "🧀gouda🧀": "else",
        "🧀parmesan🧀": "print",
        "🧀mozzarella🧀": "for",
        "🧀ricotta🧀": "while",
        "🧀gruyere🧀": "import",
        "🧀feta🧀": "return",
    }
    # Replace cheese keywords with Python equivalents
    python_code = cheese_code
    for cheese_keyword, python_keyword in CHEESE_TO_PYTHON.items():
        python_code = python_code.replace(cheese_keyword, python_keyword)
    return python_code

# Function to execute Python code
def execute_python_code(code):
    try:
        # Run the code using subprocess and capture the output
        process = subprocess.Popen(
            ["python", "-c", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()

        if stderr:
            return f"Error: {stderr}"
        return stdout
    except Exception as e:
        return f"An error occurred: {str(e)}"
