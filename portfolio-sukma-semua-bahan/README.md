# Portfolio Source Files — I G.N.K. Sukma Kertha Dinata

> **For Claude Code:** read this file first. It explains every folder and file
> in this package so you have full context to build, modify, or extend the
> portfolio website.

## Owner

**I G.N.K. Sukma Kertha Dinata** (standard name form — use this everywhere).
D4 Applied Hospitality Management student at IPBI Denpasar, Bali, Indonesia.
Hospitality Student and Web Enthusiast.

## Folder structure

```
01-foto/                         → Source photos (originals)
  foto-formal-latar-merah.jpg      Profile photo, suit & tie, red background. Use for hero.
  site-visit-amora-kintamani.jpg   Group photo, IPBI class at Amora Kintamani hotel.
  tim-fb-hard-rock-hotel.jpg       F&B team in purple uniforms, Hard Rock Hotel Bali NYE 2025.
  plating-dessert-dapur-acara.jpg  Chocolate dessert plating in an event kitchen.
  sertifikat-ecc-kokusai-jepang.jpg  Certificate image, ECC Kokusai Japan program.

02-sertifikat-pdf/               → Certificates in PDF format
  dicoding-belajar-dasar-ai.pdf              Dicoding AI Fundamentals, 4 Oct 2025.
  safety-basic-life-support-ipbi.pdf         IPBI BLS training, 30 Sep 2025, 4 SKP.
  ketua-panitia-storytelling-2026.pdf        Committee Chairman, Story Telling Competition, 8 Feb 2026, 7 SKP.
  webinar-uhn-igb-sugriwa.pdf               Webinar Local Wisdom Global Impact, 26 Aug 2025.
  webinar-speakup-nasional.pdf               National Public Speaking webinar, 14 Oct 2025.
  airlangga-healthpreneur-2026.pdf           Airlangga Healthpreneur Competition, Mar–Apr 2026.

03-surat-dan-piagam/             → Letters, awards, and invitations
  surat-keterangan-hard-rock-hotel.jpg   Certification letter, Hard Rock Hotel Bali, 2 Jan 2026 (PROOF).
  surat-apresiasi-bali-catering.jpg      Appreciation letter, Bali Catering Co, 3 Nov 2025 (PROOF).
  sertifikat-butler-galuh-hotel.jpg      Certificate of Achievement, Galuh Hotel butler training, Apr–Jul 2025 (PROOF).
  piagam-penghargaan-10-halaman.pdf      10 scanned award certificates (Palawakya, OSSI, OPSI, GSMB, class rankings).
  undangan-idp-education-fair.pdf        Invitation to IDP Education Fair, 13 Sep 2025.
  poster-idp-education-fair.pdf          Poster for the same event.

04-tangkapan-layar/              → Screenshots
  poster-hotshot-seminar-2026.jpg        Hotshot National Seminar poster, IPBI, 10 Feb 2026.
  google-sites-homepage.jpg              Previous Google Sites portfolio — homepage.
  google-sites-categories.jpg            Previous Google Sites — Knowledge, Skill, & Experience categories.
  google-sites-projects.jpg              Previous Google Sites — project thumbnails (PRAVA, Japan, Mochi Cookies, etc.).

05-cv-dan-resume/                → CV and resume
  cv-desain-1-halaman.pdf                Designed CV, 1 page, Indonesian/English mix.
  resume-itn-j1-3-halaman.pdf            ITN resume for J-1 internship, 3 pages, English.

06-website-siap-pakai/           → Current working website (run with `python app.py`)
  app.py                                 Local Python server (Python 3.8+, no dependencies).
  index.html                             Full website: HTML + CSS + JS, English, mobile-first, glassmorphism.
  static/                                Processed images used by index.html (resized, brightened).

07-rangkuman/                    → Summary PDF
  Portfolio_Data_Summary_I_G_N_K_Sukma_Kertha_Dinata.pdf
      10-page PDF (Times font) summarizing ALL content from every file.
      Page 1 is a bio template page (maroon theme with circular photo).
      Pages 2–10 contain tables of identity, education, work experience,
      organizations, achievements, certificates, skills, visual assets,
      presentation decisions, and a content map.
```

## Key decisions already made

1. **Name format:** always `I G.N.K. Sukma Kertha Dinata`.
2. **Language:** website and PDF content in English.
3. **Experience split:** the website has two tracks under the Hospitality tab:
   - **Experience with proof** — Hard Rock Hotel Bali, Bali Catering Company, The Galuh Pekutatan Hotel. Each shows a tappable image of the original letter/certificate.
   - **Other experience (narrative)** — The Westin Nusa Dua, Hilton Bali Resort, Teruna Teruni Denpasar, Lumbung Catering, Kecak Restaurant IPBI. Text only, no attachment yet.
4. **Website structure:** four tabs under "Work and experience":
   - Hospitality (experience with proof, narrative, leadership, documentation)
   - Digital (PRAVA Marketplace, Exploring Japan, this portfolio)
   - Marketing (Four Seasons poster, Mochi Cookies poster, The Samaya Restaurant poster)
   - Certificates (certificate images slider + webinar/activity timeline)
5. **Design:** mobile-first, nature theme (SVG forest background), glassmorphism cards, Poppins font, bottom nav bar.
6. **Privacy:** WhatsApp and email are shown. Height, weight, religion, and full address are NOT on the website.

## Items still to check (see PDF section 12 for details)

- Olympiad medals: CV understates them; certificates show 4 national golds.
- Bali Catering period: CV says 2025–2026, letter says 1 day (31 Oct 2025).
- IDP Education Fair attendance: inferred from wristband photo, unconfirmed.
- New certificates not yet in the CV.
- Project thumbnails are low-resolution crops; replace with original files if available.

## How to use with Claude Code

Open this folder in your terminal, then tell Claude Code:

```
Read README.md in this folder for full context about my portfolio.
Then [your request here, e.g. "redesign the hero section" or "add a dark mode toggle"].
The working website is in 06-website-siap-pakai/.
Source photos are in 01-foto/ through 04-tangkapan-layar/.
The full data summary is in 07-rangkuman/.
```

Claude Code can read the README, open the images and PDFs, and edit
`06-website-siap-pakai/index.html` directly.
