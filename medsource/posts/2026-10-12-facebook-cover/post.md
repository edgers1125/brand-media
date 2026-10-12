# Facebook Cover: #MedMura is now in the Philippines

| | |
| --- | --- |
| Date | Oct 12, 2026 |
| Type | Facebook cover (1640 × 624) |
| Branch | None (digital sales, 0906 299 3555) |
| Status | Approved |
| Design | Built from the MedSource Design System as HTML, see [`source/cover.html`](source/cover.html) |

Page cover announcing "The certified #MedMura, Medical Source is now in the Philippines". Forest headline band with the green Mura pill, navy contact footer (0906 299 3555, sales.quotations@medsource.com.ph), PhilHealth YAKAP and DSWD AICS GL accreditation badges beside the logo, and a slim diagonal photo column with the hospital bed, equipment and pharmacy shelves.

Not scheduled: a cover is uploaded by hand on the Facebook page, so there is no Metricool post, story or captions.

## Device fit

Facebook shows one cover at 820 × 312 on desktop and 640 × 360 on phones, which trims the sides. The file is 1640 × 624 (2x desktop). Everything essential (logo, badges, headline, contacts, all three photos) sits inside the phone-safe centre, x 290 to 1350, so nothing is clipped on phones. The outer 270 px each side is plain band colour. The bottom-left corner stays clear of the profile photo on desktop. See [`device-preview.png`](device-preview.png).

## Image

<img src="facebook-cover-1640x624.png" width="640">

<img src="device-preview.png" width="430">

## Accreditation badges

- **PhilHealth YAKAP:** the wordmark was cropped from the banner EJ supplied and stacked (PhilHealth over YAKAP) into a compact lockup, with a yellow "Gamot Accredited" pill. The stacked lockup is a rearrangement, not an official PhilHealth layout.
- **DSWD AICS GL:** the AICS emblem supplied by EJ, with "DSWD AICS GL" set beside it and an "Accredited" pill. Third-party logos are used here by EJ's explicit request, as an exception to the usual no-other-organizations'-logos rule.

## Source

`source/cover.html` renders the cover with `source/render.py` (Playwright, 1640 × 624). It reads Poppins and the MedSource logo from `../../../brand`. Photos are EJ's own store photos (bed display, pharmacy shelves, equipment and wheelchairs).
