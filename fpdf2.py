from fpdf import FPDF

# 1. Create PDF object
# Page Sizing: 'P' for Portrait, 'L' for Landscape
# Unit: 'mm', 'cm', 'in'
# Format: 'A4', 'Letter', etc.
pdf = FPDF(orientation='P', unit='mm', format='A4')

# 2. Add a page
pdf.add_page()

# 3. Set font
# Fonts: 'Arial', 'Times', 'Courier', 'Symbol', 'ZapfDingbats'
# Style: '' (regular), 'B' (bold), 'I' (italic), 'U' (underline)
# Size: in points
pdf.set_font("Arial", style='B', size=16)

# 4. Add a cell (text block)
# w: width (0 = full width)
# h: height
# txt: your text
# ln: 0 (to the right), 1 (to the beginning of next line), 2 (below)
# align: 'L', 'C', 'R'
# border: 0 (no border), 1 (draw border)
pdf.cell(200, 10, txt="Hello World!", ln=1, align="C")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is a simple PDF generated with FPDF2.", ln=1, align="L")

# Add a multi-line cell
multi_line_text = (
    "This is a longer paragraph that will demonstrate "
    "the multi_cell functionality. It can span multiple "
    "lines automatically if the text is too long for the "
    "specified width."
)
pdf.set_fill_color(200, 220, 255) # Set background color for the cell
pdf.multi_cell(0, 10, txt=multi_line_text, border=1, align="J", fill=True) # 0 width = full page width, J = justify

# Add an image (make sure you have an image file e.g., 'logo.png')
# try:
#     pdf.image("logo.png", x=10, y=pdf.get_y() + 5, w=30) # x, y, width (height auto-calculated)
# except RuntimeError as e:
#     print(f"Could not add image: {e}. Make sure 'logo.png' exists or Pillow is installed if needed for the image type.")

# 5. Output the PDF
# 'F': Save to a local file.
# 'S': Return as a string.
# 'I': Send to browser (requires web server context).
# 'D': Send to browser and force download.
output_filename = "fpdf_example.pdf"
try:
    pdf.output(output_filename, "F")
    print(f"PDF '{output_filename}' created successfully!")
except Exception as e:
    print(f"Error creating PDF: {e}")
