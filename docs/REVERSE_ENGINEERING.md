\# Reverse Engineering Notes



\## Record format



Each record is 48 bytes.



Each record contains 12 little-endian uint32 fields.











\## Common signatures



The most common record type is



(2,15,5,9)



It appears over 1700 times across all maps.



These records are almost certainly tile placement records.









\## Pointer fields



Fields 10 and 11 contain large values.



Example



7217008

8335248



These are not simple file offsets.



Editing Field10 does NOT visibly change rendered graphics.









\## Known facts



✓ Maps render correctly.



✓ Records can be edited.



✓ Edited maps can be rendered.



✓ Pointer edits produce no visible graphical changes.



Unknown:



\- collision

\- transparency

\- hidden routes

\- object lists

\- trigger lists

