# CS3C_TeamMananap_Technical-Debt-Management-Activity

### Activity Roles
  + **Project Manager** - *Jaber Sangcopan*
  + **Lead Developer** - *Carl Cañas / Jaber Sangcopan*
  + **Refactoring Specialist** - *Carl Cañas*
  + **Git Manager** - *James Darwen Bañas*
  + **Tester/Documenter** - *Ralph Rhey Lumigue*

### Key Changes and Improvements:
  + **Poor Naming Conventions** - 
  + **Lack of Modular Functions** -
  + **Hardcoded Values instead of Dynamic Inputs** -
  + **No Error Handling** -Your code does not check for invalid input. For instance, if the user enters a non-numeric value or a negative salary, the program will crash with a ValueError or produce incorrect results.
  + Solution: Implement error handling (e.g., try-except) to ensure that the input is valid and that the program doesn't crash due to bad input.
  + **Code Duplication** - While the code doesn’t have much outright repetition, the deduction logic is contained in a single function. If you wanted to add additional deductions in the future (e.g., health insurance, retirement), you’d have to modify the compute_deductions() function directly.
Solution: Make the deduction calculations modular so that adding new deductions doesn't require touching the main function every time.

## General Fixes:
  + asd
  + asd
  + asd
  + asd
