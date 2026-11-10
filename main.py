from pyscript import document, display 

elements = {
        "H" : {"Hydrogen", 1, 1.008},
        "He" : {"Helium", 2, 4.0026},
        "C" : {"Carbon", 6, 12.011},
        "N" : {"Nitrogen", 7, 14.007},
        "O" : {"Oxygen", 8, 15.999},
        "F" : {"Flourine", 9, 18.998},
        "Ne" : {"Neon", 10, 20.180},
        "P" : {"Phosphorus", 15, 30.974},
        "S" : {"Sulfur", 16, 32.06},
        "Cl" : {"Chlorine", 17, 35.45},
        "Ar" : {"Argon", 18, 39.948},
        "Se" : {"Selenium", 34, 78.971},
        "Br" : {"Bromine", 35, 79.904},
        "Kr" : {"Krypton", 36, 83,798},
        "I" : {"Iodine", 53, 126.90},
        "Xe" : {"Xenon", 54, 131.29},
        "Rn" : {"Radon", 86, 222}
    }

def show_element(e):
    document.getElementById("output1").innerHTML = ""
  
    element = getElementById("elements").value 
    var2 = dict.get(element, ("Information not found.", "Atomic Number not found.", "Atomic Mass not found." ))

    document.getElementById("output1").innerHTML = f"""
    Symbol: {element} <br>
    Element: {var2[0]} <br>
    Atomic Number: {var2[1]} <br>
    Atomic Mass: {var2[2]} <br>
    """

  

