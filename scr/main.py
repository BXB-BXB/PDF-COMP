import fitz  # PyMuPDF

def generate_diff_pdf(path_old, path_new, output_path="diff_result.pdf"):
    doc_old = fitz.open(path_old)
    doc_new = fitz.open(path_new)
    
    # We use the 'new' doc as our base to show additions/deletions
    for page_num in range(len(doc_new)):
        page_n = doc_new[page_num]
        page_o = doc_old[page_num] if page_num < len(doc_old) else None
        
        words_new = page_n.get_text("words") # (x0, y0, x1, y1, "word", ...)
        words_old = [w[4] for w in page_o.get_text("words")] if page_o else []

        for w in words_new:
            if w[4] not in words_old:
                # Highlight NEW words in Green
                annot = page_n.add_rect_annot(fitz.Rect(w[:4]))
                annot.set_colors(stroke=(0, 1, 0)) # Green
                annot.update()
                
    doc_new.save(output_path)
    print(f"Success! Saved comparison to {output_path}")

# Add a simple GUI or CLI caller here...
