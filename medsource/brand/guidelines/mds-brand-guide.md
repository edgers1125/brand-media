# MDS Medical Scrubs & Apparel brand guide

MDS is the medical scrubs and apparel line from MedSource. It should feel premium, calm and quietly confident: one soft slate blue-grey, white, generous space, one clean typeface, and the garments themselves as the only other colour.

The feel in three words: **quiet, confident, tailored.** Every publication should look like it belongs to a premium apparel brand that happens to make scrubs, not a hospital supplier.

This file mirrors the [MDS Design System](https://claude.ai/artifact/3GncLT8mqmQqy26hmRNCtP). Tokens are in [`mds-tokens.json`](mds-tokens.json). MDS does not follow the MedSource colours, fonts or layouts in [`brand-guide.md`](brand-guide.md); only the logos folder and the publication workflow are shared.

## Voice

- Speak to clinicians as professionals. Use "you", plain words and short sentences.
- Calm and sure, never loud. No exclamation marks, no emoji, no hype words ("revolutionary", "game-changing", "best ever").
- Headlines are either five words or fewer in uppercase (`display-caps`), or one calm sentence in sentence case (`headline`).
- Product names in title case: "V-Neck Top", "The Core Set". Colour names capitalised: Slate, Ceil Blue, Black.
- Do: "Built for the long shift." · "Made to move with you." · "Pockets where your hands go."
- Don't: "OMG these scrubs are AMAZING!!!" · "The #1 scrubs in the world" · claims you can't back up.
- No em dashes in any copy.

## Logo

Files live in [`../logos/mds`](../logos/mds). Use them as they are, never a redrawn mark.

| Lockup | Use | Files |
| --- | --- | --- |
| Stacked | Covers, packaging, square formats | `mds-stacked-slate`, `mds-stacked-white` |
| Horizontal | Headers, letterheads, wide formats | `mds-horizontal-slate`, `mds-horizontal-white` |
| Icon | Avatars, favicons, social sign-offs | `mds-icon`, `mds-icon-white` |
| Chest mark (icon + MDS, no tagline) | Embroidery and any size below the horizontal minimum | `mds-chest-slate`, `mds-chest-white` |
| Gold foil | Physical foil stamping on deep slate stock only | `mds-stacked-gold-foil` |
| Deep teal | Seasonal or limited line only | `mds-stacked-deep-teal` |

- Slate versions on `surface` (white) and `surface-bone`; white versions on slate, `slate-deep`, dark photos and dark fabric.
- Clear space on every side = one cross arm, about a third of the icon width.
- Minimum sizes: stacked 120 px on screen (25 mm print), horizontal 160 px (35 mm), icon 24 px (6 mm). Below the horizontal minimum use the chest mark.
- Embroider the chest mark 75 to 90 mm wide (80 mm standard) on the wearer's left chest: white thread on slate or navy fabric, slate thread on light fabric, `graphite` tone-on-tone on black.
- Never add gradients, shadows or outlines; never stretch, rotate or recolour; never separate the cross from the V-neck or move the tagline.

## Colour

Monotone, 90/10: almost everything is `ink` (Slate) on `surface` or `surface-bone`. Colour arrives through photography of the scrubs, not through graphic elements.

| Token | Paper theme (default) | Slate theme | Use |
| --- | --- | --- | --- |
| `surface` | #FFFFFF | #3D4A5C | Page, canvas and print ground |
| `surface-bone` | #F3F1ED | #46546A | Warm alternate panel, product backdrops |
| `ink` | #3D4A5C | #FFFFFF | Logo, headlines, body, primary button fill |
| `ink-muted` | #646C78 | #C8CFD9 | Eyebrows, captions, secondary text |
| `on-ink` | #FFFFFF | #3D4A5C | Text on an ink fill |
| `line` | #DCDFE3 | #56647A | 1 px hairline rules |
| `slate-deep` | #2E3947 | | Deep panels, gold foil ground |
| `graphite` | #3A3A3C | | Tone-on-tone thread on black fabric only |
| `gold-foil` | #B8975A | | Physical foil only, never on screen |
| `fabric-slate` / `fabric-ceil` / `fabric-black` | #3D4A5C / #8DB3D5 / #1C1C1E | | Colourway swatch chips only |

- Paper theme is the default. Slate theme (white on slate) is for campaigns, social posts and packaging.
- Section breaks are a 1 px `line` hairline, never boxes, shadows or bordered cards.

## Typography

Fonts in [`../fonts/mds`](../fonts/mds): **Jost** (variable, 100 to 900) for everything and **Cormorant Garamond Italic** for a single accent.

| Style | Size / line | Weight | Tracking | Use |
| --- | --- | --- | --- | --- |
| `display-caps` | 64 / 68 | 600 | 0.12em, uppercase | Campaign headlines, covers; five words or fewer (76 px on a 1080 post) |
| `headline` | 44 / 50 | 500 | -0.005em | Sentence-case headlines longer than five words |
| `title` | 26 / 32 | 500 | | Section titles, product names |
| `body` | 17 / 27 | 400 | | Paragraphs, product descriptions |
| `body-sm` | 14 / 22 | 400 | | Details, captions, legal, hang tags |
| `eyebrow` | 12 / 16 | 500 | 0.2em, uppercase | Labels above headlines, tagline |
| `button` | 14 / 20 | 500 | 0.14em, uppercase | Buttons and CTAs |
| `accent` | 56 / 60 | 400 italic (Cormorant) | | One word or short pull quote beside `display-caps` |

- Build each layout from three sizes at most: `eyebrow` → `display-caps` or `headline` → `body`.
- Uppercase is always tracked; sentence case is never tracked.
- `accent` is one word per layout ("quietly" + "CONFIDENT."). Never body copy, never uppercase.
- Left-align text. Centre only the stacked logo and cover compositions.
- Don't: other typefaces, bold body copy, uppercase paragraphs, or more than one accent.

## Layout

- 8 px base. White space is the premium signal: 64 px outer margins on screens and social (80 px on 1080×1350 posts), 96 px on print and web heroes.
- One focal image per layout, full-bleed or framed with square corners (radius 0). Only swatch chips and size selectors are round.
- Put type in the empty side of the photo; keep the subject off-centre.
- Sign off social posts with the icon at the bottom right; horizontal logo or chest mark top-left on headers.

## Iconography

- No icon set by default; let words and photos do the work.
- If a feature callout truly needs icons: simple 1.5 px line icons with square caps, in `ink` only.
- No emoji and no medical clip-art (heartbeat lines, stethoscopes, pills, crosses other than the logo).

## Photography and art direction

Reference points for feel only: FIGS (pride in healthcare workers), COS and Aesop (restraint, editorial white space), Everlane (honest product close-ups), Apple product pages (one idea per screen).

- Real clinicians, not models in costume. Natural window light. Muted, slightly desaturated grade with soft blacks.
- Motion over posing: walking a corridor, rolling up a sleeve, adjusting the V-neck, end-of-shift on a bench.
- Detail crops: V-neck binding, a pocket, stitching, fabric stretch, the embroidered chest mark.
- Backdrops in brand tones: bone walls, concrete, soft slate-grey. One subject, lots of negative space. The scrubs are the only colour in the frame.
- Avoid: stock smiles to camera, stethoscope-around-the-neck clichés, blue-tinted hospital stock, busy wards, clip-art.

Shot list for a first shoot: corridor walk in morning light (subject left, empty right for type) · hands adjusting the V-neck · flat lay of a folded set on bone paper with hang tag · end-of-shift seated portrait · fabric macro · team line-up in tonal colourways against concrete.

Headline starters: BUILT FOR THE LONG SHIFT · Made to move with you. · *quietly* CONFIDENT. · TWELVE HOURS. ONE SET. · Pockets where your hands go.

## Publication recipes

Templates in the design system: Logos, Social post, Story, Poster, Hang tag, Business card, Web hero, Product card. Start from the closest one and swap the placeholder for real photography.

- **Product post**: `surface-bone` ground, photo in the top two-thirds, `eyebrow` + `display-caps` below, icon sign-off bottom right.
- **Typographic post**: Slate theme, `accent` word over `display-caps`, white horizontal logo on a hairline at the bottom.
- **Story**: one product or one portrait, one sentence, one button.
- **Poster**: photo, `display-caps` headline, one line of `body`, footer on a `line` hairline.
- **Packaging and tags**: slate stock with the white stacked logo, or `slate-deep` stock with `gold-foil`; details on the reverse in `body-sm`.

## Decisions log

- 2026-10-03: brand colour moved from black to Slate #3D4A5C (black read too dark). Monotone, no MedSource colours.
- 2026-10-03: Paper (default) and Slate themes; Jost + Cormorant Garamond Italic accent; square corners.
- 2026-10-17: guide, tokens, fonts and white icon filed in the repo from the design system.
