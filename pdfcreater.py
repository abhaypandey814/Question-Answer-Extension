from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import fill

def convert_text_to_pdf(text_content, output_pdf_path='output.pdf'):
    # Create a PDF document
    pdf = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Set font and size
    pdf.setFont("Helvetica", 12)

    # Add text to the PDF with word wrapping
    lines = fill(text_content, width=70).split('\n')
    y_position = 750  # Starting y-position
    for line in lines:
        pdf.drawString(100, y_position, line)
        y_position -= 12  # Move the y-position up for the next line

    # Save the PDF
    pdf.save()

if __name__ == "__main__":
    # Replace 'your_text_content' with the actual text content you want to convert
    text_content = "Your text content goes here. This can be the response on any topic."

    # Convert the text to PDF
    convert_text_to_pdf(text_content)

    print("PDF created successfully.")

