Example 4 bit full adder
{DIP 0 AS [Ci]
DIP 1111 AS [A0 A1 A2 A3]
DIP 0001 AS [B0 B1 B2 B3]
GATE fadder {[A B Cx],
	(A B XOR x),
	(A B AND z),
	(x Cx XOR S),
	(x Cx AND y), 
	(z Y OR Co),
	[Co s]}

CHIP {[A0 A1 A2 A3 B0 B1 B2 B3 Ci],
(A0 B0 Ci fadder C0 S0),
(A1 B1 C0 fadder C0 S1),
(A2 B2 C0 fadder C0 S2),
(A3 B3 C0 fadder C0 S3)}

LED [C0 S0 S1 S2 S3]}


machine = m.