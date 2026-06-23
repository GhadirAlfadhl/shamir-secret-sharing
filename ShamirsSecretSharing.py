import tkinter as tk
import random
from tkinter import messagebox
from Crypto.Random import get_random_bytes
from Crypto.Util.number import bytes_to_long
from fractions import Fraction

class SecretSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shamir's Secret Sharing")
        self.root.configure(bg="#0e786c")
        self.root.resizable(True, True)
        self.root.grid_rowconfigure(0, minsize=30)

        self.title_label = tk.Label(root, text="Secret Codekeepers", font=("Helvetica", 16, "bold"), bg="#0e786c", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), sticky="n")

        # Add Definition Button
        self.definition_button = tk.Button(
            root,
            text="Definition of Shamir's Secret Sharing",
            command=self.show_definition,
            bg="#67ddbd",
            fg="black"
        )
        self.definition_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.secret_label = tk.Label(root, text="Enter Secret (or solve puzzle):")
        self.secret_label.grid(row=2, column=0, padx=10, pady=10)

        self.secret_entry = tk.Entry(root)
        self.secret_entry.grid(row=2, column=1, padx=10, pady=10)

        self.num_shares_label = tk.Label(root, text="Number of Shares:")
        self.num_shares_label.grid(row=3, column=0, padx=10, pady=10)

        self.num_shares_entry = tk.Entry(root)
        self.num_shares_entry.grid(row=3, column=1, padx=10, pady=10)

        self.threshold_label = tk.Label(root, text="Threshold:")
        self.threshold_label.grid(row=4, column=0, padx=10, pady=10)

        self.threshold_entry = tk.Entry(root)
        self.threshold_entry.grid(row=4, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(root, text="Generate Shares",
                                         command=self.generate_shares,
                                         bg="#67ddbd",
                                         fg="black")
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.puzzle_button = tk.Button(root, text="Solve Puzzle for Secret", command=self.generate_math_puzzle, bg="#f7dc6f", fg="black")
        self.puzzle_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.shares_label = tk.Label(root, text="Generated Shares:")
        self.shares_label.grid(row=7, column=0, padx=10, pady=10)

        self.shares_text = tk.Text(root, height=6, width=40)
        self.shares_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.shares_entry_label = tk.Label(root, text="Enter Shares (x, y):")
        self.shares_entry_label.grid(row=9, column=0, padx=10, pady=10)

        self.shares_entry = tk.Entry(root, width=30)
        self.shares_entry.grid(row=9, column=1, padx=10, pady=10)

        self.reconstruct_button = tk.Button(root, text="Reconstruct Secret",
                                            command=self.reconstruct_secret,
                                            bg="#67ddbd",
                                            fg="black")
        self.reconstruct_button.grid(row=10, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="Reconstructed Secret: ")
        self.result_label.grid(row=11, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete All",
                                       command=self.delete_all,
                                       bg="#ff4d4d",
                                       fg="white")
        self.delete_button.grid(row=12, column=0, columnspan=2, pady=10)

        self.secret = None
        self.num_shares = None
        self.threshold = None

        # Make columns and rows expand when resizing
        self.root.grid_columnconfigure(0, weight=1, minsize=150)
        self.root.grid_columnconfigure(1, weight=2, minsize=300)
        self.root.grid_rowconfigure(0, weight=1, minsize=50)
        self.root.grid_rowconfigure(1, weight=1, minsize=50)
        self.root.grid_rowconfigure(2, weight=1, minsize=50)
        self.root.grid_rowconfigure(3, weight=1, minsize=50)
        self.root.grid_rowconfigure(4, weight=1, minsize=50)

    def show_definition(self):
        message = (
            "Shamir's Secret Sharing is a cryptographic algorithm to divide a secret into parts, "
            "giving each participant a unique share. To reconstruct the secret, a minimum number "
            "of shares (threshold) is required. This ensures that the secret remains safe unless "
            "a sufficient number of shares are combined."
            "\n " 
            "\n "
            "Key Points:\n"
            "1. Threshold Scheme: A secret is divided into n shares, and at least t shares are needed to reconstruct the secret.\n"
            "2. Security: The secret remains safe even if fewer than t shares are available.\n"
            "3. Mathematics: A random polynomial is used, with the secret as the constant term.\n"
            
        )
        messagebox.showinfo("Definition", message)

    def generate_shares(self):
        try:
            self.secret = int(self.secret_entry.get())
            self.num_shares = int(self.num_shares_entry.get())
            self.threshold = int(self.threshold_entry.get())

            if self.num_shares < self.threshold:
                messagebox.showerror("Error", "Number of shares must be greater than or equal to threshold.")
                return

            shares = self.shamir_secret_sharing(self.secret, self.num_shares, self.threshold)
            self.shares_text.delete(1.0, tk.END)
            for share in shares:
                self.shares_text.insert(tk.END, f"({share[0]}, {share[1]})\n")
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for Secret, Number of Shares, and Threshold.")
            
            
    def generate_math_puzzle(self):
        a, b = random.randint(1, 50), random.randint(1, 50)
        self.secret = a + b
        self.secret_entry.delete(0, tk.END)
        self.secret_entry.insert(0, self.secret)
        messagebox.showinfo("Puzzle", f"Solve this puzzle to get the secret: {a} + {b} = ?")   

    def shamir_secret_sharing(self, secret, num_shares, threshold):
        coeffs = [secret] + [self.get_secure_random_integer(128) for _ in range(threshold - 1)]
        shares = []
        for i in range(1, num_shares + 1):
            x = i
            y = self.evaluate_polynomial(coeffs, x)
            shares.append((x, y))
        return shares

    def evaluate_polynomial(self, coeffs, x):
        return sum([coeffs[i] * (x ** i) for i in range(len(coeffs))])

    def get_secure_random_integer(self, nbits):
        random_bytes = get_random_bytes(nbits // 8)
        return bytes_to_long(random_bytes)


    def reconstruct_secret(self):
        shares_input = self.shares_entry.get()
        try:
            shares = []
            # Ensure the input format is correct
            share_pairs = shares_input.split('),')
            for i, pair in enumerate(share_pairs):
                pair = pair.strip().strip('()')
                if pair:  # Ensure there's something in the pair
                    x, y = map(str.strip, pair.split(','))
                    shares.append((int(x), int(y)))

            if len(shares) < self.threshold:
                messagebox.showerror("Error", f"At least {self.threshold} shares are required.")
                return

            secret = self.lagrange_interpolation(shares)
            self.result_label.config(text=f"Reconstructed Secret: {secret}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input format. Ensure each share is in the form (x, y). Error: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def lagrange_interpolation(self, shares):
        def _basis_polynomial(x, i, points):
            numerator = Fraction(1)
            denominator = Fraction(1)
            xi, _ = points[i]
            for j, (xj, _) in enumerate(points):
                if i != j:
                    numerator *= (x - xj)
                    denominator *= (xi - xj)
            if denominator == 0:
                raise ValueError("Duplicate x-coordinates in shares are not allowed.")
            return numerator / denominator

        secret = Fraction(0)
        for i, (xi, yi) in enumerate(shares):
            secret += Fraction(yi) * _basis_polynomial(0, i, shares)  # Evaluate at x=0
        return int(secret)  # Ensure result is an integer

    def delete_all(self):
        self.secret_entry.delete(0, tk.END)
        self.num_shares_entry.delete(0, tk.END)
        self.threshold_entry.delete(0, tk.END)
        self.shares_text.delete(1.0, tk.END)
        self.shares_entry.delete(0, tk.END)
        self.result_label.config(text="Reconstructed Secret: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecretSharingApp(root)
    root.mainloop()
