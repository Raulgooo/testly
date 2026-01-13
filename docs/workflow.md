# AI WorkFlow

**As of right now, the workflow used to analyze pdf textbooks and generate the calendar + content is the following:**

---
config:
  layout: fixed
---
flowchart TB
    A["START"] --> B["Fetch Book Identifier 
    (get_book_node)"]
    B --> C["About The Book Parse (about_node)"]
    C --> D["Generate Book Outline (book_structure_node)"]
    D --> E["Map Chapters 
    (map_outline_node)"]
    E -- CHAPTER 1 --> F["Generate Chapter Analysis (chapter_analysis)"]
    E -- CHAPTER 2 --> G["Generate Chapter Analysis (chapter_analysis)"]
    E -- CHAPTER N --> H["Generate Chapter Analysis (chapter_analysis)"]
    G --> I["Reducer"]
    F --> I
    H --> I
    n1["N chapters are parsed from outline so chapter_analysis runs n times in parallel."]