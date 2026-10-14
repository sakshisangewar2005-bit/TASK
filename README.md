# Task 01 – Shopping Bill

These beginner-friendly Java and Python programs add GST to each category first, combine the GST-inclusive amounts, and then apply a 20% discount to the total.

## Expected output

Both programs print:

```text
Electronics after 18% GST: 236.00
Fashion after 13% GST: 226.00
Food after 7% GST: 107.00
Total after GST: 569.00
20% Discount: 113.80
Final Payable Amount: 455.20
```

## Run the Java program

1. Install a Java Development Kit (JDK) if Java is not already installed.
2. Open a terminal in this folder.
3. Compile the source file:

   ```bash
   javac ShoppingBill.java
   ```

4. Run the compiled class:

   ```bash
   java ShoppingBill
   ```

## Run the Python program

1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run the program:

   ```bash
   python3 shopping_bill.py
   ```

## Upload both programs to GitHub

1. Sign in to GitHub and create a new, empty repository. Do not initialize it with a README, license, or `.gitignore`.
2. In a terminal, change to this folder:

   ```bash
   cd shopping-bill-task
   ```

3. Initialize Git and commit the files:

   ```bash
   git init -b main
   git add ShoppingBill.java shopping_bill.py README.md
   git commit -m "Add Java and Python shopping bill programs"
   ```

4. On the new GitHub repository page, choose **Code**, copy the HTTPS repository URL, and replace the example URL below with it:

   ```bash
   git remote add origin https://github.com/USERNAME/REPOSITORY.git
   git push -u origin main
   ```

5. To submit the repository link, open the repository page on GitHub and copy its URL from the browser address bar (for example, `https://github.com/USERNAME/REPOSITORY`).
