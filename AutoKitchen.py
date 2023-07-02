print("\033[94m" + "    __")
print("\033[94m" + "   /")
print("\033[0m" + ".-" + "\033[94m" + "/" + "\033[0m" + "-." + "\033[38;2;194;154;107m" + "   .-````-.")
print("\033[0m" + "|'-'|" + "\033[38;2;194;154;107m" + "  /' .  '. \ " + "\033[33m" + "  \|/\//")
print("\033[0m" + "|" + "\033[48;2;68;40;28m" + "   " + "\033[0m" + "|" + "\033[38;2;210;105;90m" + " (`-..:...-')" + "\033[91m" + "  |`^^`|")
print("\033[0m" + "|" + "\033[48;2;68;40;28m" + "   " + "\033[0m" + "|" + "\033[38;2;194;154;107m" + "  ;" + "\033[38;2;210;105;90m" + "-......-" + "\033[38;2;194;154;107m" + ";" + "\033[91m" + "   |    |")
print("\033[0m" + "\___/" + "\033[38;2;194;154;107m" + "   '------'" + "\033[91m" + "    \____/" + "\033[0m")

import mysql.connector

#setup of the python-myql connection
connection = mysql.connector.connect(
    user='root',
    password='patata',
    host='localhost',
    database='autokitchen',
    port='3306')
cursor = connection.cursor()

print("\033[1m" + "\033[92m" + "     1. Show recipes")
print("     2. Create a recipe")
print("     3. Drop a recipe")
print("     4. Consult a recipe" + "\033[0m")
option = str(input("Select an option: "))

if option == "1":
    cursor.execute("SELECT recipe FROM recipes")
    for value in cursor:
        print("\033[94m" + value[0] + "\033[0m")
    connection.close()

elif option == "3":
    recipe_name = str(input("\033[31m" + "Enter the recipe name to drop: " + "\033[0m"))
    cursor.execute("DELETE FROM recipes WHERE recipe = %s", (recipe_name,))
    connection.commit()
    print("\033[31m" + "Recipe dropped successfully." + "\033[0m")
    connection.close()

elif option == "4":
    recipe_name = str(input("Enter the recipe name to consult: "))
    cursor.execute("SELECT food FROM recipes WHERE recipe = %s", (recipe_name,))
    result = cursor.fetchone()
    if result:
        print(result[0])
    else:
        print("Recipe not found.")
    connection.close()