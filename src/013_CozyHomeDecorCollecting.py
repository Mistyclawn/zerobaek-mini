# Cozy Home Decor Collecting Game Logic

# Game Description
This game simulates the process of curating and arranging a cozy home for MistClaw and 주인님. Players collect various themed decorative items (e.g., scented candles, potted plants, themed artwork) and place them strategically in different rooms to achieve the highest 'Cozy Score' while maintaining the 'Aesthetic Harmony' score.

# Core Mechanics
1. **Collecting:** Players earn 'Cozy Points' by finding or purchasing items. Item rarity and thematic coherence boost points.
2. **Placement:** Items must be placed logically within a specific area (e.g., a plant needs sunlight, a book needs a shelf). Placement affects light, mood, and structural integrity (too many heavy items might crash!).
3. **Scoring:**
    * **Cozy Score (Total):** Sum of all items' base scores.
    * **Aesthetic Harmony (Modifier):** A penalty/bonus based on how well the items complement each other (e.g., mixing Victorian and Sci-Fi decor results in a -20 bonus).
    * **Functional Score (Penalty):** Penalty if an item is placed in an unsuitable spot (e.g., a plant in a dark, damp basement).

# Development Goals
*   Create item data structures (ID, Name, Base_Score, Theme, Placement_Requirement).
*   Implement a spatial grid system for placement validation.
*   Develop a scoring algorithm that balances individual item value against overall room synergy.
