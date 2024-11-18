from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image  # For image manipulation


def generate_certificate(intern_name, program_name, start_date, end_date, organization_name, background_path=None, logo_path=None):
    """Generates a personalized certificate PDF with optional background and logo."""

    # Create a new PDF canvas
    c = canvas.Canvas("certificate.pdf", pagesize=letter)

    # Add Optional Background
    if background_path:
        background = Image.open(background_path)
        background.thumbnail((letter[0], letter[1]))  # Resize to fit the letter page
        background.save("temp_background.png")
        c.drawImage("temp_background.png", 0, 0, width=letter[0], height=letter[1])

    # Adjust x-coordinate for a more central alignment (shift left if needed)
    x_position = 2 * inch  # Adjust as needed for horizontal alignment

    # Adjust y-coordinates for a vertical certificate layout
    # Move text elements higher by increasing y-coordinates
    c.setFont("Helvetica-Bold", 24)
    c.drawString(x_position, 10 * inch, "Certificate of Completion")  # Moved up

    # Add Organization Name
    c.setFont("Helvetica", 18)
    c.drawString(x_position, 9 * inch, organization_name)  # Moved up

    # Add Intern Name
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x_position, 8 * inch, f"This certificate is awarded to {intern_name}")  # Moved up

    # Add Program Name
    c.setFont("Helvetica", 12)
    c.drawString(x_position, 7.5 * inch, f"for successfully completing the {program_name} program.")  # Moved up

    # Add Dates
    c.setFont("Helvetica", 12)
    c.drawString(x_position, 7 * inch, f"from {start_date} to {end_date}.")  # Moved up

    # Add Optional Logo
    if logo_path:
        logo = Image.open(logo_path)
        logo.thumbnail((0.5 * inch, 0.5 * inch))  # Resize logo
        logo.save("temp_logo.png")
        c.drawImage("temp_logo.png", inch, 10.5 * inch, width=0.5 * inch, height=0.5 * inch)  # Adjust logo position

    # Save the PDF
    c.save()


def main():
    """Collects user input to generate a certificate."""

    # Collecting user inputs
    intern_name = input("Enter the intern's name: ")
    program_name = input("Enter the program name: ")
    start_date = input("Enter the start date (e.g., YYYY-MM-DD): ")
    end_date = input("Enter the end date (e.g., YYYY-MM-DD): ")
    organization_name = input("Enter the organization's name: ")
    # background_path = input("Enter the background image path (or press Enter to skip): ") or None
    # logo_path = input("Enter the logo image path (or press Enter to skip): ") or None

    # Call the generate_certificate function
    generate_certificate(
        intern_name=intern_name,
        program_name=program_name,
        start_date=start_date,
        end_date=end_date,
        organization_name=organization_name,
        background_path = "C:/Users/haidar/OneDrive/Desktop/Intern/Certificate_Generator/bg.png",
        # logo_path=logo_path,
    )

    print("Certificate generated successfully as 'certificate.pdf'!")


# Run the script
if __name__ == "__main__":
    main()
