"""Convert docs/speech_script.md into Beamer speaker notes: slides/notes/sN.tex (N = slide number).

main.tex puts \\slidenote{N} in every frame; \\slidenote inputs slides/notes/sN.tex inside \\note{}.
Build the clean deck with `latexmk -pdf main.tex`, and the rehearsal deck (a notes page after every
slide) with `latexmk -pdf main_notes.tex`.

Usage (repo root): python code/make_notes.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'docs' / 'speech_script.md'
OUT = ROOT / 'slides' / 'notes'


def esc(t):
    for a, b in [('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('_', r'\_'),
                 ('{', r'\{'), ('}', r'\}'), ('~', r'\textasciitilde{}'), ('^', r'\textasciicircum{}')]:
        t = t.replace(a, b)
    return t


def inline(t):
    t = esc(t)
    t = t.replace('⟨def⟩', r'\textcolor{navy}{\textbf{[def]}}')
    t = t.replace('▶ HAND-OVER:', r'\textcolor{nlred}{\textbf{HAND-OVER:}}')
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t)
    t = re.sub(r'\*(.+?)\*', r'\\emph{\1}', t)
    return t


def convert(body):
    out, in_list = [], False
    for line in body.strip().split('\n'):
        if line.startswith('- '):
            if not in_list:
                out.append(r'\begin{itemize}\setlength\itemsep{0pt}')
                in_list = True
            out.append(r'\item ' + inline(line[2:]))
        else:
            if in_list:
                out.append(r'\end{itemize}')
                in_list = False
            out.append(inline(line) if line.strip() else r'\par\smallskip')
    if in_list:
        out.append(r'\end{itemize}')
    return '\n'.join(out)


def main():
    OUT.mkdir(exist_ok=True)
    text = SRC.read_text().split('\n---\n', 1)[1]
    n = 0
    for sec in re.split(r'\n### ', '\n' + text)[1:]:
        head, body = sec.split('\n', 1)
        m = re.match(r'Slide (\d+) · (.*)', head)
        if not m:
            continue
        num, rest = int(m.group(1)), m.group(2)
        (OUT / f's{num}.tex').write_text(r'{\small\textbf{' + inline(rest) + '}}\\par\\smallskip\n' + convert(body) + '\n')
        n += 1
    print(f'wrote {n} note files to {OUT}')


if __name__ == '__main__':
    main()
