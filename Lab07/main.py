from lab07 import Horspool, KMP, EditDistance, LCS, HuffmanCoding


def test_horspool():
    print("=" * 50)
    print("  Horspool's Algorithm Test")
    print("=" * 50)

    h = Horspool()

    T = "ABCBABCABCBAB"
    P = "ABCBAB"
    result = h.match(T, P)
    print(f"\n[Test 1]")
    print(f"  Text    : {T}")
    print(f"  Pattern : {P}")
    print(f"  Result  : {result}")

    T = "ABCABABAAB"
    P = "ABA"
    result = h.match(T, P)
    print(f"\n[Test 2]")
    print(f"  Text    : {T}")
    print(f"  Pattern : {P}")
    print(f"  Result  : {result}")

    T = "ABCDEFGH"
    P = "XYZ"
    result = h.match(T, P)
    print(f"\n[Test 3] (no match expected)")
    print(f"  Text    : {T}")
    print(f"  Pattern : {P}")
    print(f"  Result  : {result}")

    P = "ABCBAB"
    table = h.shift_table(P)
    print(f"\n[Shift Table for '{P}']")
    for char, shift in table.items():
        print(f"  '{char}' → {shift}")

    print()


def test_kmp():
    print("=" * 50)
    print("  KMP Algorithm Test")
    print("=" * 50)

    kmp = KMP()

    P = "AABAAB"
    pi = kmp.lps(P)
    print(f"\n[LPS Table for '{P}']")
    print(f"  Pattern : {list(P)}")
    print(f"  LPS     : {pi}")

    T = "AABAABAAB"
    P = "AABAAB"
    result = kmp.match(T, P)
    print(f"\n[Test 2]")
    print(f"  Text    : {T}")
    print(f"  Pattern : {P}")
    print(f"  Result  : {result}")

    T = "ABCABABAAB"
    P = "ABA"
    result = kmp.match(T, P)
    print(f"\n[Test 3]")
    print(f"  Text    : {T}")
    print(f"  Pattern : {P}")
    print(f"  Result  : {result}")

    T = "ABCDEFGH"
    P = "XYZ"
    result = kmp.match(T, P)
    print(f"\n[Test 4] (no match expected)")
    print(f"  Text    : {T}")
    print(f"  Pattern : {P}")
    print(f"  Result  : {result}")

    print()


def test_edit_distance():
    print("=" * 50)
    print("  Edit Distance (Levenshtein) Test")
    print("=" * 50)
    ed = EditDistance()

    S, T = "TGCATAT", "ATCCGAT"
    dist = ed.compute(S, T)
    print("\n[Test 1] slide example")
    print("  S =", S, "  T =", T)
    print("  Edit Distance =", dist)

    S, T = "HELLO", "HELLO"
    dist = ed.compute(S, T)
    print("\n[Test 2] identical  ->", dist)

    S, T = "ABC", "XYZ"
    dist = ed.compute(S, T)
    print("\n[Test 3] all-different  S=%s T=%s -> %d" % (S, T, dist))

    S, T = "HELLO", ""
    dist = ed.compute(S, T)
    print("\n[Test 4] empty T  S=%s -> %d" % (S, dist))
    print()


def test_lcs():
    print("=" * 50)
    print("  LCS (Longest Common Subsequence) Test")
    print("=" * 50)

    lcs = LCS()

    X, Y = "ABCBDAB", "BDCAB"
    length, seq = lcs.solve(X, Y)
    print("\n[Test 1] classic example")
    print("  X =", X, "  Y =", Y)
    print("  LCS length =", length)
    print("  LCS string =", seq)

    X, Y = "AGGTAB", "GXTXAYB"
    dc_len  = lcs.lcs_dc(X, Y)
    dp_len, dp_seq = lcs.solve(X, Y)
    print("\n[Test 2] DC vs DP")
    print("  X =", X, "  Y =", Y)
    print("  DC  length =", dc_len)
    print("  DP  length =", dp_len)
    print("  LCS string =", dp_seq)

    X, Y = "HELLO", "HELLO"
    length, seq = lcs.solve(X, Y)
    print("\n[Test 3] identical")
    print("  X = Y =", X)
    print("  LCS length =", length, "  LCS =", seq)

    X, Y = "ABC", "XYZ"
    length, seq = lcs.solve(X, Y)
    print("\n[Test 4] no common chars")
    print("  X =", X, "  Y =", Y)
    print("  LCS length =", length, "  LCS =", repr(seq))
    print()


def test_huffman():
    print("=" * 50)
    print("  Huffman Coding Test")
    print("=" * 50)

    hc = HuffmanCoding()

    text = "AABBBCCCCDDDDDEEEEEEE"
    print("\n[Test 1] text =", repr(text))
    encoded, root = hc.encode(text)
    decoded = hc.decode(encoded, root)
    print("  Encoded  :", encoded[:40], "..." if len(encoded) > 40 else "")
    print("  Decoded  :", decoded)
    print("  Match    :", "OK" if decoded == text else "FAIL")

    text2 = "AAAA"
    print("\n[Test 2] text =", repr(text2))
    encoded2, root2 = hc.encode(text2)
    decoded2 = hc.decode(encoded2, root2)
    print("  Encoded  :", encoded2)
    print("  Decoded  :", decoded2)
    print("  Match    :", "OK" if decoded2 == text2 else "FAIL")

    text3 = "hello huffman"
    print("\n[Test 3] text =", repr(text3))
    encoded3, root3 = hc.encode(text3)
    decoded3 = hc.decode(encoded3, root3)
    print("  Decoded  :", decoded3)
    print("  Match    :", "OK" if decoded3 == text3 else "FAIL")
    print()

if __name__ == "__main__":
    test_horspool()
    test_kmp()
    test_edit_distance()
    test_lcs()
    test_huffman()