# CS3C_TeamMananap_Technical-Debt-Management-Activity

Key Changes and Improvements:
Modular Functions: Each deduction calculation is now handled by its own function (calculate_sss, calculate_philhealth, etc.). This makes the code more modular and easier to update if deduction rules change.

Dynamic Input Handling: The get_salary_input() function ensures that the salary entered by the user is a positive number and is valid. It uses a try-except block to handle invalid inputs.

Error Handling: The input function now catches errors (e.g., entering a non-numeric value) and prompts the user to try again.

Improved Naming: Function names are more descriptive, and variable names are self-explanatory.

No Code Duplication: Each deduction is calculated in its own function, which reduces duplication and makes the code easier to maintain and extend.

1. Poor Naming Conventions
The variables sss, philhealth, pagibig, and tax are not necessarily poorly named, but they could be more descriptive. For example, instead of just tax, a name like fixed_tax or monthly_tax would provide more context.
2. Lack of Modular Functions
The code combines everything into a single function, compute_deductions(), which makes it difficult to maintain and extend. If any of the deduction calculations (e.g., SSS, PhilHealth, Pag-IBIG, Tax) need to change, you'd have to modify the single function, which could lead to errors.
Solution: Refactor the code to break each calculation into its own function (modular approach). This improves readability, reusability, and maintainability.
3. Hardcoded Values Instead of Dynamic Inputs
In your original code, values like sss = 1200 and tax = 1875 are hardcoded. This is problematic because these values may change based on the user’s salary, government policies, or other dynamic factors.
Solution: Allow these values to be dynamically calculated or input based on different rules, such as a sliding scale for taxes or varying rates for SSS and PhilHealth based on the salary range.
4. No Error Handling
Your code does not check for invalid input. For instance, if the user enters a non-numeric value or a negative salary, the program will crash with a ValueError or produce incorrect results.
Solution: Implement error handling (e.g., try-except) to ensure that the input is valid and that the program doesn't crash due to bad input.
5. Code Duplication
While the code doesn’t have much outright repetition, the deduction logic is contained in a single function. If you wanted to add additional deductions in the future (e.g., health insurance, retirement), you’d have to modify the compute_deductions() function directly.
Solution: Make the deduction calculations modular so that adding new deductions doesn't require touching the main function every time.
Specific Problems in the Code:
Incorrect Function Call Order

In your original code, you're calling compute_deductions(salary) after asking the user for input. This means that salary is undefined before calling compute_deductions(), which would lead to an error. You need to get the user input before calling the function.
Missing Return Statements

The compute_deductions() function doesn't return anything, but you're trying to use deductions and net_salary outside of that function. This results in NameError because deductions and net_salary are not accessible outside the function unless explicitly returned.
Print Statements Inside the Function

The code prints the deductions and net salary inside the compute_deductions() function, but this may not be the best place for them. It's better to separate the logic of calculating deductions from the logic of printing results, especially if you want to reuse the calculation logic elsewhere (like in a test).
Summary of Problems in the Original Code:
Poor naming conventions (can improve clarity and consistency).
No modularization (all logic is in one function, making it harder to maintain or extend).
Hardcoded values (tax, SSS, etc., should depend on dynamic input or logic).
No error handling (no validation of user input, which can break the program).
Code duplication (the calculation logic could be repeated and made modular).
By addressing these issues, your code will become more robust, maintainable, and flexible.

How to Fix It:
Break the logic into smaller, modular functions for each deduction.
Use dynamic input rather than hardcoded values for deductions.
Implement error handling to ensure valid input.
Return values from functions and avoid printing directly inside the functions that calculate deductions.
