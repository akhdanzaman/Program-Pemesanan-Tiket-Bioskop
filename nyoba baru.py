from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('background2.jpeg', 60, 40, 80)
        self.image('hihi.jpg', 135, 30, 50)
        #font
        self.set_font('helvetica', 'B', 20)
        #warna frame, background, font
        self.set_draw_color(0,80,180)
      
        # Arial bold 15
        self.set_font('helvetica', 'B', 20)
        # Move to the right
        # Title
        self.cell(0, 0, '_________________________________________', border=False, ln=1, align ='C')
        self.cell(0, 0, 'THE CINEMAKMUR PREMIERE', border=False, ln=1, align ='C')
        # Line break
        self.ln(0)

pdf = PDF('P','mm', (200, 110))
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', 'b', 12)
pdf.cell(5, 30, ' ', 0, 1)
pdf.cell(103, 7, 'DOCTOR STRANGE : MULTIVERSE OF MADNESS', border=True, ln=1)
pdf.cell(5, 7, ' ', 0, 1)
pdf.cell(5, 7, 'Date : ', 0, 1)
pdf.cell(5, 7, 'Time : ', 0, 1)
pdf.cell(5, 7, 'Seat : ', 0, 1)
pdf.cell(5, 7, 'Price : ', 0, 1)
pdf.output('tiket_bioskop.pdf', 'F')