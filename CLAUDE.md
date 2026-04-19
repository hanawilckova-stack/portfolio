# CLAUDE.md — Portfolio Hana Wilčková

## 1. Přehled projektu
Osobní portfolio UI/UX designérky Hany Wilčkové. Slouží jako prezentace práce, dovedností a kontakt pro potenciální klienty. Obsahuje homepage a dvě case study stránky.

---

## 2. Použité technologie
- **Čisté HTML + CSS + vanilla JS** — žádné frameworky, žádné závislosti
- **Fonty:** Abhaya Libre (serif, nadpisy, wght 400–800) + Inter (sans, body) — načítány lokálně z `assets/fonts/` pomocí `@font-face`
- **CSS custom properties** (design tokeny) — vše v `:root`
- **IntersectionObserver** — scroll fade-in animace
- Soubory jsou určeny pro otevírání přes `file://` protokol i web server

---

## 3. Architektura souborů

```
portfolio/
├── index.html          # Homepage (vše inline: CSS + HTML + JS)
├── carglass.html       # Case study: Redesign webu Carglass
├── videolektor.html    # Case study: Redesign uživatelského profilu Videolektor
├── assets/
│   ├── images/
│   │   ├── foto-hana.jpg
│   │   ├── carglass-cover.png
│   │   ├── carglass-preview.png
│   │   ├── videolektor-cover.png
│   │   └── videolektor-preview.png
│   └── fonts/          # Lokální fonty (TTF) — složka musí existovat
└── CLAUDE.md
```

> **Důležité:** Fonty se načítají relativní cestou `assets/fonts/...` (bez úvodního `/`). Stejně tak obrázky. Absolutní cesty rozbijí `file://` protokol.

---

## 4. Design tokeny (CSS custom properties)

```css
--color-bg:      #F2F1F5   /* světlé pozadí stránky */
--color-accent:  #E8583D   /* oranžová — CTA, zvýraznění */
--color-text:    #1D1D1F   /* téměř černá */
--color-muted:   #6E6E73   /* šedá pro doplňkový text */
--color-border:  #E0DFE5   /* jemný border */
--color-white:   #FFFFFF
--color-footer:  #1D1D1F   /* tmavé pozadí footeru */

--font-serif:    'Abhaya Libre', Georgia, serif
--font-sans:     'Inter', system-ui, sans-serif

--radius-sm: 6px  |  --radius-md: 12px  |  --radius-lg: 20px  |  --radius-full: 9999px
--nav-height: 72px
--max-width:  1160px
```

---

## 5. Coding rules / konvence

- **CSS inline v každém souboru** — kvůli kompatibilitě s HTML-to-Figma pluginem (nesdílíme externí stylesheet)
- **BEM pojmenování** — `.card__title`, `.about__tile--photo` apod.
- **Žádný hover na dekorativních prvcích** — hover stavy pouze na interaktivních prvcích (tlačítka, nav linky, karty)
- **`position: fixed`** na nav (ne `sticky`) + `body { padding-top: var(--nav-height) }`
- **Relativní cesty** pro všechny assety — nikdy `/assets/...`, vždy `assets/...`
- **Rounded corners všude** — konzistentní kulatá grafika (`border-radius`)
- JS v inline `<script>` na konci každého souboru

---

## 6. Sekce na homepage (`index.html`)

| Sekce | ID | Popis |
|---|---|---|
| Nav | — | Fixed, blur při scrollu (`nav--scrolled`) |
| Hero | — | Velký serif H1, centered, gradient pozadí |
| Projekty | `#projekty` | 2 case study karty pod sebou, full-bleed foto, glass tagy |
| S čím pomůžu | `#sluzby` | Pill cloud (statický), font Abhaya Libre |
| O mně | `#o-mne` | Bento grid — foto, citát, stat, zkušenosti, nástroje |
| Kontakt / Footer | `#kontakt` | Tmavé pozadí, telefon, email, LinkedIn |

---

## 7. Co je hotové

- [x] Homepage — kompletní layout všech sekcí
- [x] Nav — fixed, blur on scroll, kotvy (Moje práce / S čím pomůžu / Kontakt)
- [x] Hero — centered H1, serif typografie, gradient pozadí
- [x] Karty case studies — full-bleed obrázek, gradient overlay, glass tagy, serif title 32px
- [x] Sekce „S čím pomůžu" — pill cloud, akcentové tagy tmavé, jemné rotace
- [x] Sekce „O mně" — bento grid (foto + citát + stat + zkušenosti + nástroje)
- [x] Footer — tmavý, kontakty s vlastními SVG ikonami, LinkedIn, copyright
- [x] Scroll fade-in animace (IntersectionObserver)
- [x] Nav blur animace při scrollu
- [x] Stránka Carglass (`carglass.html`) — struktura, cover, obsah case study
- [x] Stránka Videolektor (`videolektor.html`) — struktura, cover, obsah case study
- [x] Lokální fonty (relativní cesty, funguje přes file://)
- [x] Obrázky case studies (cover + preview)

---

## 8. TODO / Co ještě chybí

- [ ] **Obrázky do detailu Carglass** — Hana dodá screenshoty/mockupy, vložit do `carglass.html`
- [ ] **Obsah Videolektor** — doplnit texty a obrázky (soubor `Videolektor_texty.txt` je k dispozici)
- [ ] **Foto Hany** — zkontrolovat zobrazení v bento gridu (ořez, pozice)
- [ ] **Responzivita** — mobile breakpointy jsou rozepsané jen částečně
- [ ] **Favicon** — chybí
- [ ] **OG tagy** — pro sdílení na sociálních sítích
- [ ] **Nasazení** — stránka zatím běží lokálně přes file://
