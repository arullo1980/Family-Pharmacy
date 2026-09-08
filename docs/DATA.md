# Data provenance

## Station list
- **File:** `data/estaciones_poligono_central.xlsx`, sheet "Polígono Central" (20 rows).
- **Origin:** Google Maps search "gasolinera", queried 2026-09-08; the twenty stations closest to the reference centre 18.4690, -69.9295 (Av. Lope de Vega / Av. 27 de Febrero area).
- **Columns:** #, Nombre, Dirección, Teléfono, Latitud, Longitud, Coordenadas, Enlace Google Maps, Horario, Dentro del Polígono, Dist. al centro (km).
- **Polígono Central definition used:** Av. John F. Kennedy (N), Av. 27 de Febrero (S), Av. Winston Churchill (W), Av. Máximo Gómez (E). "Sí" = inside; "Borde / adyacente" = just outside the boundary.
- **Brand** is inferred by `build.py` from the listing name (TotalEnergies, Next, Axxon, Tropigás, Shell, Texaco, Sigma, VP Racing, Óptimo Gas, Trovasa; "La Lira" → Independent).
- **Derived outputs:** `site/data/stations.json` (with polygon and centre), `stations.csv`, `stations.geojson` (points + polygon feature).

## Market figures (as published; see `/market/` sources list)
| Figure | Value | Source |
|---|---|---|
| Fuel stations nationwide | ≈1,025 (ANADEGAS); >780 affiliated | El Nuevo Diario / Diario Libre, Jul 2026 |
| Acquirer commission at stations | 1.95%–2.50% per transaction | Diario Libre, Listín Diario, Jul 2026 |
| Fee per gallon / share of margin | RD$6.59–8.45 / 25%–36% of ≈RD$25 gross margin | Infobae 8 Jul 2026, Diario Libre 6 Jul 2026 |
| Card payments at stations | ≈RD$41,000 MM per year | Diario Libre 8 Jul 2026 |
| Commissions paid by stations | ≈RD$584 MM/month; RD$5,000–6,000 MM/yr | Diario Libre 6 Jul 2026 |
| Card transactions 2025 | 806 million (117 million in 2008) | elDinero (BCRD) |
| Value of card payments 2025 | RD$1,072.5 bn, +12.8% | Invertix (BCRD) |
| Cards' share of value settled | 63.6% | Invertix (BCRD) |
| Debit / credit cards per 1,000 | 757 / 373 (Q1 2026) | Infobae (BCRD bulletin) |
| POS per million inhabitants | 19,038 (Q1 2026) | Infobae (BCRD bulletin) |
| Cash share of payments | ≈75% | Diario Libre, Dec 2025 |
| Fuel prices 2025 | Premium RD$290.10, regular RD$272.50 per gallon | MICM weekly notices |
| New stations/LPG plants approved | 33 (2024–Oct 2025) | EHPLUS+ (MICM) |

The fuel-consumption volume figures that circulated in 2025 press coverage were not used because the
units could not be verified.
