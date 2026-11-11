# 📄 The Appleseed Letter

> *A physical replica of Apple's TextEdit icon — the same words, the same type, the same sheet, with a real rolled corner.*

![print-ready](https://img.shields.io/badge/print--ready-100%25-brightgreen)
![page-card](https://img.shields.io/badge/card-5%C3%97%206in-blue)
![page-letter](https://img.shields.io/badge/letter-8.5%C3%97%2011in-lightgrey)
![type-Times](https://img.shields.io/badge/type-Times_New_Roman-black)
![license-personal-use](https://img.shields.io/badge/use-personal_only-orange)

---

## 📖 Contents

- [✨ What this is](#-what-this-is)
- [⬇️ Print me](#️-print-me)
- [🖼️ Gallery](#️-gallery)
- [🔤 The text, exactly](#-the-text-exactly)
- [✒️ Typography](#️-typography)
- [🧻 Paper & printing](#-paper--printing)
- [🌀 The curl](#-the-curl)
- [🖼️ Display it](#️-display-it)
- [✅ Build order](#-build-order)
- [🛠️ Rebuild from source](#️-rebuild-from-source)
- [🗂️ Files](#️-files)
- [⚖️ Notes & limits](#️-notes--limits)

---

## ✨ What this is

This is **not** a photograph of a document. It is **Apple's TextEdit application icon** —
the version that shipped from **Mac OS X 10.5 Leopard (2007)** through **10.9 Mavericks**.
Maximize the icon in Finder and the "paper" turns out to have a letter printed on it.[^1]

| Fact | Detail |
|:-----|:-------|
| 📝 Text | The **"Think Different" manifesto** — Rob Siltanen & Ken Segall, TBWA\Chiat\Day, 1997, voiced by Richard Dreyfuss |
| ✂️ Icon edit | Condensed to **two paragraphs**; *"They push the human race forward"* moved up to open ¶2 |
| 🙋 `John Appleseed` | Apple's stand-in demo user — same reason every sample contact is John Appleseed |
| 💌 `Kate` | Generally read as the KDE text editor *Kate* — an editor writing to another editor |
| 🕰️ Window | Letter only exists **2007–2014**; replaced by a blank sheet + pen in Yosemite |

<details>
<summary><b>Why three sizes? There's no single "correct" one — click to see why</b></summary>

1. **It is not a real document.** The icon is 5:6 (1.20), not Letter (1.29) or A4 (1.41), and its type is ~7 px tall.
   Scale it 1:1 to Letter and type lands at ~23 pt; keep normal 12 pt type on Letter and the text fills only the top third.
2. **The curl is load-bearing.** In the icon the rolled corner covers the ends of the first three lines.
   A faithful replica hides the same words — exactly like the original.

So: `card` = icon proportions, `sheet` = same composition at life size, `letter`/`a4` = a normal letter you could hand someone.

</details>

> [!IMPORTANT]
> Print at **100% / Actual size** with **no scaling** and **no header/footer** — or the geometry below won't hold.

---

## ⬇️ Print me

| Pick one | Size | Use it for | File |
|:---------|:-----|:-----------|:-----|
| 🏆 **Replica** | 5 × 6 in | the 1:1 icon object | [`out/appleseed-letter_card.pdf`](out/appleseed-letter_card.pdf) |
| ✂️ **Replica + cut guides** | Letter sheet, 5 × 6 card centered | print on US Letter, cut along the line | [`out/appleseed-letter_card-trim.pdf`](out/appleseed-letter_card-trim.pdf) |
| 🖼️ **Poster** | 8.5 × 11 in | same composition, life size, framable | [`out/appleseed-letter_sheet.pdf`](out/appleseed-letter_sheet.pdf) |
| ✉️ **Letter** | 8.5 × 11 in | a normal letter (14 pt), human scale | [`out/appleseed-letter_letter.pdf`](out/appleseed-letter_letter.pdf) |
| 🇪🇺 **A4** | 210 × 297 mm | same as letter, A4 paper | [`out/appleseed-letter_a4.pdf`](out/appleseed-letter_a4.pdf) |

```bash
# fastest path — one evening, under an hour hands-on
1. print card-trim at 100% ............ 10 min
2. check density, cut along border .....  5 min
3. curl the corner (see below) ......... 10 min
4. mount or photograph ................. 20 min
```

> [!TIP]
> Print **two copies** on the good stock — one to curl, one to keep flat as a control.

---

## 🖼️ Gallery

### The replica (`card`, 5 × 6 in)

![card proof](out/pdf-proof_card.png)

### Trim version (Letter sheet, cut along the border)

![trim proof](out/appleseed-letter_card-trim.png)

### Life size (`sheet`, 8.5 × 11 in)

![sheet proof](out/pdf-proof_sheet.png)

### Crease geometry (`card`)

![curl guide card](out/curl-guide_card.png)

---

## 🔤 The text, exactly

> Dear Kate,
>
> Here's to the crazy ones. The misfits. The rebels. The troublemakers. The round
> pegs in the square holes. The ones who see things differently. They're not fond
> of rules. And they have no respect for the status quo. You can quote them,
> disagree with them, glorify or vilify them. About the only thing you can't do is
> ignore them. Because they change things.
>
> They push the human race forward. And while some may see them as the crazy ones,
> we see genius. Because the people who are crazy enough to think they can change
> the world, are the ones who do.
>
> Take care,
> John Appleseed

<details>
<summary>Variants in the wild</summary>

| Version | Difference |
|:--------|:-----------|
| 🖥️ **Icon (this build)** | *"You can quote them…"* · two paragraphs · *"Take care,"* |
| 📺 **1997 print + TV** | *"…disagree with them, <ins>disbelieve</ins> them…"* + the *"They invent. They imagine. They heal."* paragraph |
| 👴 **Older / low-res icons** | Longer lines: *"You can praise them, disagree with them, quote them, disbelieve them…"* |

To swap text, edit `LETTER` in `build.py`.

</details>

---

## ✒️ Typography

Measured off the reference (ink bounding box as % of page):

| Property | Icon | `card` | `sheet` |
|:---------|-----:|-------:|--------:|
| Top of block | 6.5% | 7.0% | 7.0% |
| Block height | ~70% | 70.7% | 69.3% |
| Left margin | 10.6% | 10.0% | 10.1% |
| Block width | ~82% | 83.3% | 79.6% |
| Bottom margin | ~23.5% | 22.2% | 23.7% |

- [x] **Size / leading** — card 12 pt on 20 pt (1.66×); sheet 22 pt on 35.6 pt. Small but *loosely* leaded — that airiness is most of the look.
- [x] **Measure** — ~59 chars/line. Narrow, so paragraphs break in short stacks.
- [x] **Alignment** — left, ragged right, no hyphenation. Blank line between paragraphs.
- [x] **Colour** — near-black (`#1b1b1b` card / `#141414` sheet), not 100% K. Prints dark, reads soft like the icon.
- [x] **Punctuation** — proper curly apostrophes (`Here’s`, `They’re`, `can’t`). Verified in PDF text extraction.
- [ ] **Typeface** — **Times New Roman**, regular. Closest face present on every machine and print shop, so the PDF prints identically anywhere.

> [!NOTE]
> At icon resolution the glyphs are ~7 px — enough to tell serif from sans, not Times from Garamond.
> **Apple Garamond** (Apple's 1984–2003 corporate face) is the connoisseur's swap: set `font` in `VARIANTS` and rebuild.
> Free stand-in: *EB Garamond*. Check it yourself at 1024 px: compare the `a`, `e`, `t`, and the `ff` in "misfits".

---

## 🧻 Paper & printing

The icon's sheet is flat, bright white, matte, slightly warm — photocopier white, not cream. Match that.

| Layer | Spec | Why |
|:------|:-----|:----|
| 📄 Paper | **Uncoated, 100–120 gsm (24–32 lb), smooth, laser-rated**, 96–100 brightness | Holds 12 pt crisply, still takes a curl |
| 🚫 Avoid | 80 gsm office (floppy) · 270 gsm+ card (won't curl) · coated/glossy (cracks) | — |
| 🖨️ Ink | 100% K toner (laser) or pigment black (inkjet) | Toner sits on top = sharpest small type |
| 🌾 Grain | Long grain, curl *with* the grain | Rolls smoothly, holds the set |

Concrete stocks: *Mohawk Superfine Eggshell White 100 lb text* · *Neenah Classic Crest Solar White 80 lb* · *Southworth 32 lb* (home) · *HP Premium32 120 gsm* (home).

1. **Print shop** — digital laser, 1200 dpi, your own 100 lb stock. *"Black only, no scaling, 100%."* ~$1–3.
2. **Home laser** — 32 lb laser paper, driver on *best / 1200 dpi*, *fit-to-page off*.
3. **Inkjet** (e.g. HP ENVY) — *matte* paper, quality slider maxed. Fine at 12 pt; softer than laser on the big sheet.
4. **Letterpress** — polymer plate from the PDF, 1–2 pt impression. Beautiful. Most expensive way to do it.

> [!WARNING]
> Do **not** print a paper texture or fake shadow into the artwork. The object supplies both.
> And never put inkjet glossy/photo paper in a laser printer — the coating melts.

---

## 🌀 The curl

The part that makes it read as the icon. Measured: crease runs from **49% of the width** (top edge) to **37% of the height** (right edge).

- 📐 Card: starts **2.45 in** in from top-left → ends **2.22 in** down the right edge
- 📐 Sheet: **4.17 in** → **4.07 in**
- 🗺️ See `out/curl-guide_card.png` / `out/curl-guide_sheet.png`, dimensioned

### Method A — dry roll *(start here, reversible)*

1. Lay the sheet **face down** on a clean, hard surface
2. Put a <kbd>1 in</kbd> dowel / rolling pin diagonally under the corner
3. Wrap the corner over the dowel, press flat with your palm — hold 10 s
4. Release, rotate 90°, roll again — 3–4 passes gives *memory*, not a crease
5. Finish tighter at the tip so it tapers like the icon's

### Method B — moisture set *(permanent, still reversible)*

Mist the **back** of the corner *very* lightly (damp sponge, not spray) → roll → clip to the dowel with a binder clip → dry 10–15 min. Test on scrap first — too much water tidemarks uncoated stock.

### Method C — steam *(crispest)*

Two seconds over a kettle spout, then roll and clip. Same physics as B, faster, easier to overdo.

> [!TIP]
> A **half-drop of PVA** under the roll's underside (invisible) or an hour under a weight stops it relaxing.
> Want it fully readable instead? Roll only a **1 in** corner — same gesture, none hidden.

---

## 🖼️ Display it

- **Mount** — float on ⅛ in foam board with two Japanese-tissue hinges (archival, removable), or a small clear acrylic easel
- **Frame** — shadow box, **minimum 1 in deep**. A standard frame flattens the curl and undoes the work.
- **Light** — one soft source, upper left, 45°, large + diffused. The icon's whole read is that soft shadow; hard light kills it.
- **Photo** — white sweep, camera slightly above center at ~15° tilt, 50 mm at f/8, expose for the paper not the shadow

---

## ✅ Build order

- [x] Reference measured, text transcribed, geometry matched
- [x] PDFs built with embedded Times, exact page boxes, curly quotes
- [x] Proofs rendered + read back, trim + curl guides drawn
- [ ] **You:** print → cut → curl → mount / photograph

---

## 🛠️ Rebuild from source

```bash
python build.py --measure      # all variants + geometry report
python build.py card           # one variant: card | card-trim | sheet | letter | a4
python curl_guide.py           # redraw crease diagrams
```

Requirements: `Python 3` + `Chrome` (used as the PDF engine so typefaces embed exactly). Pillow only for the proof renders.

---

## 🗂️ Files

```text
build.py                            HTML → PDF engine (headless Chrome, exact page boxes)
curl_guide.py                       crease diagrams
out/appleseed-letter_card.pdf       5 × 6 in — icon proportions, the replica (33K)
out/appleseed-letter_card-trim.pdf  Letter sheet with cut guides + crop marks (51K)
out/appleseed-letter_sheet.pdf      8.5 × 11 in — same composition, life size (34K)
out/appleseed-letter_letter.pdf     8.5 × 11 in — normal 14 pt letter (34K)
out/appleseed-letter_a4.pdf         A4 — same as letter (34K)
out/curl-guide_*.png                dimensioned crease geometry
out/pdf-proof_*.png                 renders of the actual PDFs
```

---

## ⚖️ Notes & limits

- **Font certainty.** Words, proportion, alignment, leading and ink are measured from the reference. The face is inferred — see [Typography](#️-typography) for the check and the swap.
- **Copyright.** The manifesto is Apple's 1997 ad copy. Personal replica, fine; don't sell it. [^2]
- **Fidelity quirk.** The icon's own text is cut off by the curl. Curl it as specified and your copy hides the same words — that's not a bug. Use the flat print to read it.

[^1]: Wikipedia: [TextEdit](https://en.wikipedia.org/wiki/TextEdit) — *"The high-resolution TextEdit 1.5 icon found in Mac OS X versions starting with 10.5 (Leopard) features an extract from Apple's 'Think different' ad campaign."*
[^2]: Text by Rob Siltanen & Ken Segall, TBWA\Chiat\Day, 1997. This project recreates the *icon's condensed arrangement* for personal/educational use.
