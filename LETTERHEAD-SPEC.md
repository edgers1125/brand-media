# Letterhead format (all brands, brand level and government level)

Every letterhead in this repo must comply with this layout. The system fills the letter, so the keep-blank zones must stay empty. Reference diagram: [letterhead-first-page-spec.jpg](letterhead-first-page-spec.jpg)

## First page header, 2480 x 500 px (origin 0,0 top left)

| Area | Coordinates | Rule |
| --- | --- | --- |
| Top bar | full width, y 0 to 120 | Bar only, full width |
| Bottom bar | full width, y 440 to 500 | Bar only, full width |
| Side margins | x 0 to 177 and x 2303 to 2480 | Bars only |
| Logo area | x 177 to 1240, y 120 to 350 | Logo must end above y 350 |
| Zone A | x 177 to 1240, y 360 to 430 | KEEP BLANK, system prints the branch tag |
| Optional tagline | x 1300 to 2160, y 130 to 205 | Right-aligned to x 2160 |
| Zone B | x 1300 to 2160, y 215 to 430 | KEEP BLANK, system prints phone, email and address |
| Optional decoration | x 2160 to 2303, y 130 to 430 | Decoration only |

So no phone, email, address, branch name or any other text goes in the header body. Nothing sits under the logo.

## Other pieces

- Later pages header: 2480 x 250 px slim band.
- Footer, every page: 2480 x 250 px.
- No em dashes anywhere.

## Brand notes

- MedSource uses the MedSource logo for its brand level letterhead and MedSource World for its government level letterhead. Emmanuelle Pharma uses the same logo for both levels.
- Each letterhead's `print.md` and `source.html` carry the zone comments. Check the zones before filing a new or revised letterhead.
