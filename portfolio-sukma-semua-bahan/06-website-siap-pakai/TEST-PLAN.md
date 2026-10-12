# Test Plan — Portfolio I G.N.K. Sukma Kertha Dinata

Target: `06-website-siap-pakai/index.html`, served by `python app.py`.
Environment: built-in Chromium browser, desktop 1600×900 and mobile 375×812.
Method: automated in-page checks (JavaScript) plus visual screenshots.

| ID | Area | Test case | Expected result |
|----|------|-----------|-----------------|
| TC01 | Server & assets | Every image, CV and background referenced by the page loads | All responses are HTTP 200; no broken images |
| TC02 | Loader | Loader shows the name letter by letter; "Enter without sound" closes it | Title split into letters; loader removed; `html.entered` set |
| TC03 | 3D hero | With motion on, the Three.js scene initialises | `html.scene-ready`, canvas sized to the viewport, character loaded |
| TC04 | Dock nav | Home / About / Work / Contact buttons scroll to their section | Section reached; active button gets `aria-current="true"` |
| TC05 | Tabs | Five tabs in order Hospitality, Digital, Marketing, Organizations, Certificates; click and arrow keys switch panels | One panel visible; `aria-selected` and `tabindex` correct |
| TC06 | Works wheel | Each tab builds its card ring and index; selecting an index item unfolds the drum to that card | Card count = log count; active card and counter update |
| TC07 | Photo stage | Each tab shows its Figma background while the wheel is in view, and hides it when scrolled away | Correct `stage_*.jpg` on; off outside the stage |
| TC08 | Lightbox | Opens from proof cards, albums and documents; prev/next; Escape closes and returns focus | Correct image and counter; closes; focus restored |
| TC09 | Albums | 13 albums with 107 photos render and load | Counts match; no broken thumbnails |
| TC10 | Contact | WhatsApp, email, location and CV links | wa.me / mailto / Maps links; CV PDF returns 200 `application/pdf` |
| TC11 | Content & privacy | Name format "I G.N.K. Sukma Kertha Dinata"; no height, weight, religion or full address | Name present; none of the private fields present |
| TC12 | Mobile | 375 px layout | No horizontal scroll; experience log hidden; tabs scroll |
| TC13 | Reduced motion | `?reduced` | No 3D; static card grid shown; content visible |
| TC14 | Sound | Sound toggle starts and stops the soundtrack | `aria-pressed` toggles; AudioContext running then suspended |
| TC15 | Console | Clean load | No JavaScript errors or failed requests |

Results are recorded in `TEST-REPORT.md`.
