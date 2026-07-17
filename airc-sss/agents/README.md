# Synthetic student agents (50 instantiated personas)

This folder holds the 50 synthetic-student agents for the Student Journey Gap Analysis (Student Support and Success domain, AI Resource Center). Each file is one persona from the library, fully instantiated as a runnable system prompt: who the student is, what they know and do not know, their device, life constraints, and emotional state, followed by the same hard rules and findings schema every run returns.

These were generated from two sources in the parent folder:

- `synthetic-student-agent.md`, the reusable template (the role, the `{{fields}}`, the hard rules, and the findings schema).
- `_personas-50.html`, the persona library (ID, name, age, profile, home college, language for all 50).

## Status: prompts, not runs

Every file here is an instrument, not a result. Nothing has been run against any live college website. Fieldwork has not started. These are the test participants, ready to be pointed at a task once authorization and the browsing setup are confirmed with OIT.

## How the orchestrator uses these

For a single run, the orchestrator picks three things and combines them:

1. A persona file from this folder (for example `P22_Marisol-Reyes.md`), which supplies the in-character system prompt.
2. A task (for example, “find out what classes to take for nursing” or “find emergency food help”), which replaces the swappable default goal in the file.
3. A target college site to attempt it on (a persona can be run against their home college or, for the crosswalk, another college in the district).

The persona then attempts the task on that college’s public site, in character, thinking aloud, and returns the fixed findings schema. Running the same task across colleges and personas is what produces the comparable set of candidate barriers the study analyzes. A human validates severity and reality before any finding counts.

## The 50 files

| ID | Name | Home college | File |
| --- | --- | --- | --- |
| P01 | Robert Kessler | MCC; swirls to SCC | `P01_Robert-Kessler.md` |
| P02 | Tyler Brooks | PVCC | `P02_Tyler-Brooks.md` |
| P03 | Destiny Carter | SMCC | `P03_Destiny-Carter.md` |
| P04 | Frank DiMarco | PVCC | `P04_Frank-DiMarco.md` |
| P05 | Caleb Smith | EMCC | `P05_Caleb-Smith.md` |
| P06 | Brittany Hale | MCC | `P06_Brittany-Hale.md` |
| P07 | Jordan Lee | PVCC | `P07_Jordan-Lee.md` |
| P08 | Brooke Hanson | CGCC | `P08_Brooke-Hanson.md` |
| P09 | Cody Martin | EMCC | `P09_Cody-Martin.md` |
| P10 | Samantha Wright | SCC | `P10_Samantha-Wright.md` |
| P11 | Leila Hassan | GCC | `P11_Leila-Hassan.md` |
| P12 | Megan O’Brien | GateWay | `P12_Megan-OBrien.md` |
| P13 | Dylan Foster | MCC | `P13_Dylan-Foster.md` |
| P14 | Travis Coleman | SCC | `P14_Travis-Coleman.md` |
| P15 | Hunter Bishop | CGCC; ACE | `P15_Hunter-Bishop.md` |
| P16 | Rachel Dunn | GCC | `P16_Rachel-Dunn.md` |
| P17 | Ashley Bennett | CGCC; swirls to MCC | `P17_Ashley-Bennett.md` |
| P18 | Kaylee Morrison | SMCC | `P18_Kaylee-Morrison.md` |
| P19 | Gregory Pierce | PVCC | `P19_Gregory-Pierce.md` |
| P20 | Amber Sullivan | MCC | `P20_Amber-Sullivan.md` |
| P21 | Nathan Reed | EMCC | `P21_Nathan-Reed.md` |
| P22 | Marisol Reyes | GCC; swirls to EMCC | `P22_Marisol-Reyes.md` |
| P23 | Ana Lucia Torres | Phoenix; Rio for one online class | `P23_Ana-Lucia-Torres.md` |
| P24 | Sofia Ramirez | Phoenix | `P24_Sofia-Ramirez.md` |
| P25 | Gabriel Mendez | Phoenix | `P25_Gabriel-Mendez.md` |
| P26 | Maria Gonzalez | GateWay | `P26_Maria-Gonzalez.md` |
| P27 | Rosa Jimenez | SMCC | `P27_Rosa-Jimenez.md` |
| P28 | Jose Herrera | GCC | `P28_Jose-Herrera.md` |
| P29 | Valeria Castillo | GateWay | `P29_Valeria-Castillo.md` |
| P30 | Diego Morales | SMCC | `P30_Diego-Morales.md` |
| P31 | Lucia Fernandez | Phoenix | `P31_Lucia-Fernandez.md` |
| P32 | Carlos Vega | EMCC | `P32_Carlos-Vega.md` |
| P33 | Isabella Ruiz | CGCC | `P33_Isabella-Ruiz.md` |
| P34 | Miguel Santos | GCC | `P34_Miguel-Santos.md` |
| P35 | Camila Delgado | CGCC; swirls to MCC | `P35_Camila-Delgado.md` |
| P36 | Fernando Rios | Rio + GCC (swirl) | `P36_Fernando-Rios.md` |
| P37 | Alejandra Nunez | GateWay | `P37_Alejandra-Nunez.md` |
| P38 | Emiliano Vargas | Phoenix; ACE | `P38_Emiliano-Vargas.md` |
| P39 | Guadalupe Flores | SMCC | `P39_Guadalupe-Flores.md` |
| P40 | Ricardo Mendoza | MCC | `P40_Ricardo-Mendoza.md` |
| P41 | Jasmine Williams | CGCC | `P41_Jasmine-Williams.md` |
| P42 | Darnell Carter | SCC; swirls to Rio | `P42_Darnell-Carter.md` |
| P43 | Andre Thompson | SMCC | `P43_Andre-Thompson.md` |
| P44 | Nicole Tran | GateWay | `P44_Nicole-Tran.md` |
| P45 | Yuki Tanaka | CGCC | `P45_Yuki-Tanaka.md` |
| P46 | Linda Yazzie | SCC | `P46_Linda-Yazzie.md` |
| P47 | Jaylen Brooks-Ramirez | GCC | `P47_Jaylen-Brooks-Ramirez.md` |
| P48 | Kiana Alofa | MCC | `P48_Kiana-Alofa.md` |
| P49 | Mei Chen | SCC | `P49_Mei-Chen.md` |
| P50 | Hassan Abdi | EMCC | `P50_Hassan-Abdi.md` |
