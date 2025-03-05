# CS3C_TeamMananap_Technical-Debt-Management-Activity

### Activity Roles
  + **Project Manager** - *Jaber Sangcopan*
  + **Lead Developer** - *Carl Cañas / Jaber Sangcopan*
  + **Refactoring Specialist** - *Carl Cañas*
  + **Git Manager** - *James Darwen Bañas*
  + **Tester/Documenter** - *Ralph Rhey Lumigue*

### Key Changes and Improvements:
  + **Poor Naming Conventions** - The variables sss, philhealth, pagibig, and tax are not necessarily poorly named, but they could be more descriptive. For example, instead of just tax, a name like fixed_tax or monthly_tax would provide more context.
  + **Lack of Modular Functions** - The code combines everything into a single function, compute_deductions(), which makes it difficult to maintain and extend. If any of the deduction calculations (e.g., SSS, PhilHealth, Pag-IBIG, Tax) need to change, you'd have to modify the single function, which could lead to errors.
Solution: Refactor the code to break each calculation into its own function (modular approach). This improves readability, reusability, and maintainability.
  + **Hardcoded Values instead of Dynamic Inputs** - In your original code, values like sss = 1200 and tax = 1875 are hardcoded. This is problematic because these values may change based on the user’s salary, government policies, or other dynamic factors.
Solution: Allow these values to be dynamically calculated or input based on different rules, such as a sliding scale for taxes or varying rates for SSS and PhilHealth based on the salary range.
  + **No Error Handling** -Your code does not check for invalid input. For instance, if the user enters a non-numeric value or a negative salary, the program will crash with a ValueError or produce incorrect results.
  + Solution: Implement error handling (e.g., try-except) to ensure that the input is valid and that the program doesn't crash due to bad input.
  + **Code Duplication** - While the code doesn’t have much outright repetition, the deduction logic is contained in a single function. If you wanted to add additional deductions in the future (e.g., health insurance, retirement), you’d have to modify the compute_deductions() function directly.
Solution: Make the deduction calculations modular so that adding new deductions doesn't require touching the main function every time.

## General Fixes:
Modular Functions: Each deduction calculation is now handled by its own function (calculate_sss, calculate_philhealth, etc.). This makes the code more modular and easier to update if deduction rules change.

Dynamic Input Handling: The get_salary_input() function ensures that the salary entered by the user is a positive number and is valid. It uses a try-except block to handle invalid inputs.

Error Handling: The input function now catches errors (e.g., entering a non-numeric value) and prompts the user to try again.

Improved Naming: Function names are more descriptive, and variable names are self-explanatory.

No Code Duplication: Each deduction is calculated in its own function, which reduces duplication and makes the code easier to maintain and extend.
