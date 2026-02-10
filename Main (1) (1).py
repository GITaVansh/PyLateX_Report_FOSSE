import pandas as pd
import numpy as np
from pylatex import Document, Section, Subsection, Figure, Tabular, Command, Package
from pylatex.utils import NoEscape, italic
import os

def generate_beam_report():
    print("📊 Reading beam data from Excel...")
    df = pd.read_excel('beam_data.xlsx')
    
    # Using 'article' with 11pt and a clean layout
    doc = Document(documentclass='article', document_options=['a4paper', '11pt'])
    
    # --- Specialized Packages for a New Look ---
    doc.packages.append(Package('fancyhdr'))
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('tcolorbox'))  # For a specialized header box
    doc.packages.append(Package('tikz'))
    doc.packages.append(Package('pgfplots'))
    doc.packages.append(Package('geometry', options=['margin=0.7in', 'headheight=14pt']))
    
    # --- Custom Color Palette ---
    doc.preamble.append(NoEscape(r'\definecolor{darkslate}{HTML}{2C3E50}'))
    doc.preamble.append(NoEscape(r'\definecolor{emerald}{HTML}{27AE60}'))
    
    # Using a professional Serif font for this version
    doc.preamble.append(NoEscape(r'\pgfplotsset{compat=1.18}'))

    # --- Header and Footer Configuration ---
    doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
    doc.preamble.append(NoEscape(r'\fancyhf{}'))
    doc.preamble.append(NoEscape(r'\lhead{\footnotesize \textbf{Vansh Tiwari} | 23BCE10136}'))
    doc.preamble.append(NoEscape(r'\rhead{\footnotesize \textit{Beam Analysis Tech Note}}'))
    doc.preamble.append(NoEscape(r'\cfoot{\thepage}'))

    # --- Unique "Boxed" Title Design ---
    doc.append(NoEscape(r'''
    \begin{tcolorbox}[colback=darkslate, colframe=darkslate, arc=0pt, outer arc=0pt, top=10pt, bottom=10pt]
        \centering \color{white} \Large \textbf{TECHNICAL NOTE: BENDING \& SHEAR RESPONSE} \\
        \small \textit{Structural Engineering Laboratory - 2026}
    \end{tcolorbox}
    '''))
    doc.append(NoEscape(r'\vspace{0.4cm}'))

    # Section 1: Project Parameters
    with doc.create(Section('Analytical Framework')):
        doc.append('This report evaluates the internal mechanical response of a structural beam under discrete loading. The simulation aims to isolate the shear and flexural envelopes for design verification.')
        
        with doc.create(Subsection('System Geometry')):
            doc.append('Parameters: L=12.0m, Support: Pinned-Roller.')
            with doc.create(Figure(position='h!')) as beam_fig:
                if os.path.exists('beam.png'):
                    # Slightly smaller image to fit the tech-note style
                    beam_fig.add_image('beam.png', width=NoEscape(r'0.55\textwidth'))
                beam_fig.add_caption('Schematic Load Diagram')

    # Section 2: Numerical Log (Using a two-column feel)
    with doc.create(Section('Computation Matrix')):
        doc.append('The dataset below represents the calculated stress points along the span.')
        doc.append(NoEscape(r'\vspace{0.3cm}'))
        
        # Using a centered table with emerald headers
        with doc.create(Tabular('c | c | c', row_height=1.4)) as table:
            table.add_row((NoEscape(r'\color{emerald}\textbf{x (m)}'), 
                           NoEscape(r'\color{emerald}\textbf{V (kN)}'), 
                           NoEscape(r'\color{emerald}\textbf{M (kNm)}')))
            table.add_hline()
            # Sampling every 2nd row for a clean Tech Note look
            for _, row in df.iloc[::2].iterrows():
                table.add_row((f"{row['X']:.2f}", f"{row['Shear force']:.1f}", f"{row['Bending Moment']:.1f}"))

    # Section 3: Graphical Envelopes
    with doc.create(Section('Stress Envelopes')):
        
        with doc.create(Subsection('Shear Force (V) Diagram')):
            doc.append(NoEscape(generate_sfd_plot(df)))

        with doc.create(Subsection('Bending Moment (M) Diagram')):
            doc.append(NoEscape(generate_bmd_plot(df)))

    # Generate PDF
    print("📄 Generating Technical Note PDF...")
    doc.generate_pdf('Vansh_Tiwari_Beam_Analysis', clean_tex=False, compiler='pdflatex')
    print("✅ Success: Vansh_Tiwari_Beam_Analysis.pdf")

def generate_sfd_plot(df):
    coords = "".join([f"({r['X']}, {r['Shear force']}) " for _, r in df.iterrows()])
    return r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[width=10cm, height=4.5cm, axis lines=middle, 
        grid=major, grid style={dotted, darkslate!30},
        title=\textbf{\small V-Distribution}, title style={color=emerald}]
    \addplot[thick, emerald, fill=emerald, fill opacity=0.1] coordinates {""" + coords + r"""} \closedcycle;
    \end{axis}
    \end{tikzpicture}
    \end{center}
    """

def generate_bmd_plot(df):
    coords = "".join([f"({r['X']}, {r['Bending Moment']}) " for _, r in df.iterrows()])
    return r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[width=10cm, height=4.5cm, axis lines=middle, 
        grid=major, grid style={dotted, darkslate!30},
        title=\textbf{\small M-Distribution}, title style={color=darkslate}]
    \addplot[thick, darkslate, fill=darkslate, fill opacity=0.1] coordinates {""" + coords + r"""} \closedcycle;
    \end{axis}
    \end{tikzpicture}
    \end{center}
    """

if __name__ == "__main__":
    generate_beam_report()