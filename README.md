
# 🧾 Automatic Invoice Generation with Python

This Python project reads a list of clients from a `.csv` file, customizes an invoice message for each client based on a template (`fatura.txt`), and saves the invoices as individual `.txt` files.

---

## 📌 Features

- Reads client data from a CSV file.
- Uses `string.Template` to personalize messages.
- Formats monetary values to Brazilian currency format (R$).
- Securely generates random identifiers for file names.
- Automatically saves personalized invoices in an output folder (`faturas/`).

---

## 🗂️ Project Structure

```
📁 your_project/
├── clientes.csv          # CSV file with client data
├── fatura.txt            # Message template with variables (%name, %value, etc.)
├── gerar_faturas.py      # Main script
└── faturas/              # Folder where generated invoices are saved
```

---

## 📄 Example Template (`fatura.txt`)

```
Hello %nome,

We inform you that the invoice for our services has been generated in the amount of %{valor}, due on %vencimento.

For more information, please contact %empresa at %telefone.

Best regards,
%empresa Team
```

---

## 📋 Example `clientes.csv`

```
nome,email,valor,vencimento,empresa,telefone
João Silva,joao@email.com,199.90,2025-07-10,TechSoft,+55 (11) 91234-5678
Maria Oliveira,maria@email.com,249.50,2025-07-12,InfoWeb,+55 (21) 99876-5432
```

---

## ▶️ How to Run

1. Make sure you have Python 3.10+ installed.
2. Place the `clientes.csv` and `fatura.txt` files in the same directory as the script.
3. Run the script:

```bash
python gerar_faturas.py
```

4. The invoices will be saved in the `faturas/` folder.

---

## ✅ Requirements

- Python 3.10 or higher (due to `locale.currency`)
- Files required:
  - `clientes.csv`
  - `fatura.txt`

---

## 🔐 Security

- The unique identifiers for invoice file names are generated using `SystemRandom` from the `secrets` module, ensuring stronger randomness suitable for real-world applications.

---

## 📦 Possible Improvements

- Add email sending via `smtplib`.
- Generate PDF files instead of `.txt` using `reportlab` or `fpdf`.
- Create a GUI using `tkinter` or `PyQt`.
