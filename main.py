from problems.Matrix import lc1036_EscapeaLargeMaze

if __name__ == "__main__":
    t = lc1036_EscapeaLargeMaze.Solution()
    print(t.isEscapePossible(
        [[691938, 300406], [710196, 624190], [858790, 609485],
         [268029, 225806], [200010, 188664], [132599, 612099],
         [329444, 633495], [196657, 757958], [628509, 883388]
         ],
        [655988, 180910],
        [267728, 840949]))
