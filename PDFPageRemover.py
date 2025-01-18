import PyPDF2

def remove_page(input_pdf, output_pdf, page_number):
    # Open the PDF file
    with open(input_pdf, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        # Loop through all the pages and add them to the writer, except the page to be removed
        for i in range(len(reader.pages)):
            if i != page_number:
                writer.add_page(reader.pages[i])

        # Write the output PDF
        with open(output_pdf, 'wb') as outfile:
            writer.write(outfile)

# Example usage to remove the last page
input_pdf = 'D:\\Downloads\\input.pdf'
output_pdf = 'D:\\Downloads\\input - updated.pdf'

with open(input_pdf, 'rb') as infile:
    reader = PyPDF2.PdfReader(infile)
    num_pages = len(reader.pages)

remove_page(input_pdf, output_pdf, num_pages - 1)  # This removes the last page