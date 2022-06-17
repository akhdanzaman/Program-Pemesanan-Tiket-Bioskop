from fpdf import FPDF
def haha():
    class PDF(FPDF):
        def header(self):
            # Logo
            self.image('background2.jpeg', 60, 40, 80)
            self.image('hihi.jpg', 135, 28, 50)
            #font
            self.set_font('helvetica', 'B', 20)
            # Arial bold 15
            self.set_font('helvetica', 'B', 20)
            # Title
            self.cell(0, 0, '_________________________________________', border=False, ln=1, align ='C')
            self.cell(0, 0, 'THE CINEMAKMUR PREMIERE', border=False, ln=1, align ='C')
            # Line break
            self.ln(0)

    pdf = PDF('P','mm', (200, 110))
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.cell(5, 20, ' ', 0, 1)
    pdf.set_font('Arial', 'bu', 14)
    pdf.cell(103, 7, 'DOCTOR STRANGE : MULTIVERSE OF MADNESS', border=False, ln=1)
    pdf.set_font('Arial', 'b', 10)
    pdf.cell(5, 5, ' ', 0, 1)
    pdf.cell(5, 7, 'Date : ', 0, 1)
    pdf.cell(5, 7, 'Time : ', 0, 1)
    pdf.cell(5, 7, 'Seat : ', 0, 1)
    pdf.cell(5, 7, 'Price : ', 0, 1)
    pdf.cell(5, 7, ' ', 0, 1)
    pdf.set_font('Arial', 'b', 12)
    pdf.cell(67, 10, 'KODE BOOKING : Akj09nDB98', 1, 1, 'C')
    pdf.output('tiket_bioskop.pdf', 'F')

haha()