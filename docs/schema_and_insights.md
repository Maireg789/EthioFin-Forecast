# Unified Schema, `impact_links`, Event Timeline, and EDA Insights

## Unified Data Schema
Canonical row fields used across `data/` and notebooks:

- `date`: ISO date (YYYY-MM-DD)
- `country_code`: ISO3 (e.g., ETH)
- `region`: Optional subnational region
- `indicator_code`: Short code (e.g., `USG_TELEBIRR_USERS`, `FI_GLOBALFINDEX_ADULTS`)
- `indicator_name`: Human readable name
- `value`: Numeric
- `unit`: `count`, `percent`, etc.
- `source`: Source name (operator, regulator, dataset)
- `source_url`: Direct URL to source doc (when available)
- `confidence`: `High` / `Medium` / `Low` (qualitative)
- `rationale`: Short explanation for the chosen or adjusted value
- `impact_links`: JSON array linking this row to one or more events

### `impact_links` structure
Each `impact_links` item is an object with:

- `event_id`: stable identifier for the event (string)
- `impact`: numeric fractional contribution used in modeling (e.g., 0.18)
- `rationale`: short justification for the link

Example:

```
[{"event_id":"telebirr_scaleup_2022","impact":0.18,"rationale":"Agent expansion increased active accounts"}]
```

Store `impact_links` as a JSON string in CSVs, or as a nested/struct column in Parquet.

---

## Event Timeline (use to overlay time-series charts)
Use these events as vertical markers in plots. The notebooks use approximate date windows; replace with canonical dates from primary sources where available.

- `telebirr_launch` — 2021–2022: Telebirr introduction and national rollout (wallet + agent network)
- `fayda_id_pilots` — 2022–2024: Fayda / national digital ID pilots and scaling
- `mpesa_entry` — 2023: Safaricom Ethiopia / M-Pesa market entry
- `regulatory_interop` — 2022–2024: Interoperability and regulatory clarity measures
- `distribution_partnerships` — 2022–2024: major agent and airtime distribution deals

How to overlay in plots:
- Add vertical lines at event date(s). Use `impact_links` weights to annotate expected contribution.
- Compare observed deviation from baseline forecast within ±6 months of event.

---

## EDA — Key Insights (concise)
1. **Usage Crossover:** Digital P2P transfers now exceed ATM withdrawal transaction counts, showing a structural shift in payment behavior.
2. **Platform-Led Growth:** Telebirr accounts explain the largest absolute increase in active accounts during 2021–2024; distribution networks and agent liquidity were key drivers.
3. **Identity Bottleneck:** Areas with low digital ID coverage show weak conversion from SIM ownership to active mobile-money usage.
4. **Event Signals:** Telebirr scale-ups and M-Pesa market entry produce observable short-term upticks in account creation and transaction frequency, concentrated in urban centers.
5. **Heterogeneous Adoption:** Significant regional heterogeneity — some regions plateau while others sustain steep adoption curves.
6. **Forecast Sensitivity:** Forecast scenarios are highly sensitive to `impact_links` weightings for Digital ID and platform interoperability; small changes in assumed impact materially shift 2027 inclusion estimates.

---

## Provenance & Next Steps
- The `data_enrichment_log.md` has been updated to include `source_url`, `confidence`, and `rationale` columns for each enrichment entry.
- Next: replace placeholder source URLs in `data_enrichment_log.md` with canonical links from original source documents, and fix the README formatting to reference this doc.
