# CURRENT_STATE.md

_Poslední aktualizace: 2026-04-17_

---

## Aktuální fokus
Dokončování homepage (`index.html`) — ladění vizuálu sekcí. Poslední úpravy se týkaly:
- Sekce „O mně" → přepracována na bento grid
- Sekce „S čím pomůžu" → pill cloud (statický, bez interakce)
- Case study karty → pod sebou, full-bleed, glass tagy

---

## Rozdělané věci

### `index.html`
- **Sekce „O mně" (bento grid)** — layout hotový, ale foto (`assets/images/foto-hana.jpg`) potřebuje zkontrolovat ořez a pozici v dlaždici `about__tile--photo`
- **Case study karty** — chybí reálné náhledové obrázky; aktuálně se zobrazují placeholdery (gradient pozadí) protože `carglass-preview.png` a `videolektor-preview.png` jsou v `assets/images/` ale nemusí mít správný obsah

### `carglass.html`
- **Obrázky v detailu** — Hana avizovala, že dodá screenshoty/mockupy z projektu; zatím jsou tam placeholder bloky (`case-image__placeholder`)
- Jinak stránka strukturálně hotová (cover, metadata, obsah case study)

### `videolektor.html`
- **Obsah** — texty jsou v souboru `Videolektor_texty.txt` (root složky), ale nebyly ještě přepsány do HTML
- Struktura stránky je stejná jako carglass.html (zkopírovaná kostra)

---

## Problémy / poznámky

- **Fonty nenačteny přes file://** — složka `assets/fonts/` **neexistuje** (ověřeno `ls`). Fonty AbhayaLibre a Inter jsou v `@font-face` referencovány jako `assets/fonts/*.ttf`, ale fyzicky tam nejsou → padají na system serif/sans. Nutno dodat TTF soubory.
- **Inline CSS ve všech souborech** — každý HTML soubor má vlastní kompletní CSS (záměr, kvůli HTML-to-Figma pluginu). Při změně tokenu nebo nav/footer stylu je třeba změnu zopakovat ve všech třech souborech ručně.
- **Nav a footer** na `carglass.html` a `videolektor.html` jsou synchronizovány s homepage ručně — není sdílená komponenta.
- **Responzivita** — částečně ošetřena (breakpointy existují), ale nebyla testována na mobilních zařízeních.

---

## Next steps

- [ ] **Dodat TTF fonty** do `assets/fonts/` — AbhayaLibre (Regular, Medium, SemiBold, Bold, ExtraBold) + Inter (Regular, Medium)
- [ ] **Vložit obrázky do Carglass** — Hana dodá screenshoty, vložit do `carglass.html` místo placeholderů
- [ ] **Doplnit obsah Videolektor** — přepsat texty z `Videolektor_texty.txt` do `videolektor.html`
- [ ] **Zkontrolovat foto v bento gridu** — ořez a pozici `.about__tile--photo img` po dodání/změně fotky
- [ ] **Favicon** — přidat `<link rel="icon">` do všech tří HTML souborů
- [ ] **OG tagy** — doplnit `og:title`, `og:description`, `og:image` pro sdílení na sítích
- [ ] **Otestovat na mobilu** — projít responzivitu, zejména bento grid O mně a pill cloud
- [ ] **Nasazení** — rozhodnout o hostingu (Netlify / Vercel / vlastní doména) a nasadit
