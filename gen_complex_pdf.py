from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_complex_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Title (Large Font, Multi-line)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height - 50, "A Complex Research Paper")
    c.drawString(50, height - 80, "With a Long Title")
    
    # Authors (Mixed formatting)
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 110, "Author One, Author Two")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, height - 125, "University of Somewhere")
    
    # Abstract (Standard Heading)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 160, "Abstract")
    
    # Abstract Content (Standard)
    c.setFont("Helvetica", 11) # Slightly different size than body?
    c.drawString(50, height - 180, "This is the abstract. It is standard.")
    
    # Introduction (Numbered Heading with space)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 220, "1. Introduction")
    
    # Introduction Content (Mixed sizes in line)
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 240, "This is the introduction.")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(200, height - 240, "Bold text") # Same line, bold
    c.setFont("Helvetica", 12)
    c.drawString(260, height - 240, " in the middle.")
    
    # Subsection (Dynamic Heading?)
    c.setFont("Helvetica-Bold", 13) # Bold, smaller than title, bigger than text
    c.drawString(50, height - 270, "Background")
    
    # Content for subsection
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 290, "Some background info.")
    
    # Methodology (Case variation)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 320, "METHODOLOGY")
    
    # Content with a "footnote" (smaller text)
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 340, "We did things.")
    c.setFont("Helvetica", 9)
    c.drawString(50, height - 355, "Note: This is a small note that should probably be skipped or included?")
    
    c.save()

if __name__ == "__main__":
    create_complex_pdf("complex_paper.pdf")
    print("Created complex_paper.pdf")
