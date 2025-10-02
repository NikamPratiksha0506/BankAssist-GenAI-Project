import os
from fpdf import FPDF

# Ensure folder exists
folder = "sample_documents"
os.makedirs(folder, exist_ok=True)

# Create KYC PDF
pdf_path = os.path.join(folder, "kyc_report.pdf")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf_content = """KYC Compliance Report - Sample Document

Customer Name: John Doe
Account Number: 12345678
Date of Account Opening: 01-Jan-2020
Risk Profile: High

Summary of Compliance Checks:
1. Identity Verification Completed
2. Address Verified
3. Politically Exposed Person (PEP) Check: Passed
4. Source of Funds Verified
5. Risk Assessment Completed

Remarks:
All required compliance checks have been successfully completed. Customer is eligible for high-value transactions.

End of Report
"""

for line in pdf_content.split("\n"):
    pdf.cell(200, 10, txt=line, ln=True)

pdf.output(pdf_path)

# Create Credit Risk Text File
text_path = os.path.join(folder, "credit_risk.txt")
text_content = """Credit Risk Analysis - Sample Document

Loan Account: 987654321
Customer: Jane Smith
Loan Amount: 500,000
Interest Rate: 8.5%
Loan Tenure: 5 years

Risk Assessment:
- Payment History: Excellent
- Outstanding Loans: None
- Credit Score: 780

Conclusion:
The customer poses low credit risk. Recommended for loan approval.
"""

with open(text_path, "w", encoding="utf-8") as f:
    f.write(text_content)

print("✅ Sample documents created inside 'sample_documents/' folder:")
print(f"- PDF: {pdf_path}")
print(f"- Text: {text_path}")
