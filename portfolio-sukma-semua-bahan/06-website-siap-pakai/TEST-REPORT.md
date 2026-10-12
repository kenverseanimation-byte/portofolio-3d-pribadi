# Test Report — Portfolio I G.N.K. Sukma Kertha Dinata

Date: 12 October 2026 · Plan: `TEST-PLAN.md` · Server: `app.py` (localhost)
Browser: built-in Chromium, desktop 1600×900 and mobile 375×812.

**Result: 15 / 15 test cases passed; 1 minor defect (D1, console noise) found and fixed.**

| ID | Test case | Result | Evidence |
|----|-----------|--------|----------|
| TC01 | All assets load | PASS | 271 `static/` URLs checked: all HTTP 200; CV served as `application/pdf`; 0 broken images |
| TC02 | Loader | PASS | Title split into 24 letters; "Enter without sound" removes the loader and sets `html.entered`; hero stats count up to 3 / 4 / 6 / 12+ |
| TC03 | 3D hero | PASS | `scene-ready`; canvas 1600×900 matches the viewport; procedural character loaded |
| TC04 | Dock navigation | PASS | About, Work, Contact and Home each scroll to their section; active button and zone label follow (Zone 02 Who am I?, 03 Work, 04 Contact, 01 Home) |
| TC05 | Tabs | PASS | Order: Hospitality, Digital, Marketing, Organizations, Certificates; one panel per tab; `aria-selected` and `tabindex` correct; ArrowRight wraps from the last tab, End jumps to the last |
| TC06 | Works wheel | PASS | Cards = log items on every tab (10 / 10 / 9 / 10 / 14); choosing the 4th log item unfolds the drum to it (e.g. 04/10 "F&B team, Hard Rock Hotel Bali", 04/09 "Sukma Printing", 04/10 "Four Seasons Resort Bali") |
| TC07 | Photo stage backgrounds | PASS | `stage_hospitality`, `stage_digital`, `stage_marketing`, `stage_organizations`, `stage_certificates` each shown on their tab; turns off when the stage scrolls out (stage top 1080 px) and on as it enters (480 px); no flicker while pinned |
| TC08 | Lightbox | PASS | Proof card (1/10, Hard Rock letter); album next/prev with wrap-around (1→2→13 of 13); PRAVA document (1/5); gold medals (1/4); Escape closes and returns focus to the opener |
| TC09 | Albums | PASS | 13 albums, 107 photos (Hospitality 49, Marketing 25, Organizations 33); all thumbnails load |
| TC10 | Contact | PASS | WhatsApp `wa.me/6285142734756` (new tab), `mailto:kerthadinata16@gmail.com`, Google Maps "Denpasar, Bali", CV download `CV_Sukma_Kertha_Dinata.pdf` |
| TC11 | Content and privacy | PASS | Name appears in the exact form "I G.N.K. Sukma Kertha Dinata" (8× in the page, including the title); no other spellings; no height, weight, religion or street address. The only keyword hit, "Banjar", is part of "Banjarnegara" (olympiad venue) |
| TC12 | Mobile 375 px | PASS | No horizontal overflow; experience log hidden; tab bar scrolls; dock 343 px wide; 3D hero renders |
| TC13 | Reduced motion (`?reduced`) | PASS | 3D canvas off, wheel replaced by a static grid (10/10 images loaded), no pinned scroll, no hidden content |
| TC14 | Sound toggle | PASS | `aria-pressed` true / "Sound on", then false / "Sound off" |
| TC15 | Console and network | PASS (with defect D1) | No JavaScript errors; all page requests succeed apart from D1 |

## Defects

| ID | Severity | Description | Suggested fix |
|----|----------|-------------|---------------|
| D1 | Low — **FIXED** | Turning sound on probed for an optional music file with HEAD requests to `static/audio/bgm.mp3`, `.ogg` and `.m4a`; with no file present this logged three 404 errors in the console. Music still played (the built-in soundtrack). | Fixed: the page now reads the `static/audio/` folder listing first and only requests a file that is listed. Retest: without a file, only `GET /static/audio/` → 200 and the built-in soundtrack plays; with a `bgm.mp3` present, it is found and loaded (200). No 404s. |

## Test environment notes
- The test browser pane was hidden, so the browser throttled animation frames. To keep the page running, the tests replaced `requestAnimationFrame` with a timer and updated ScrollTrigger every 50 ms. This only affects the test session, not the website.
- 3D frame rate could not be measured for the same reason.
- Earlier I said the Hospitality albums hold 51 photos; the correct count is 49 (107 in total).
