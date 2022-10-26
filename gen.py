from pathlib import Path

me = Path(__file__).resolve().parent

files = 1000

text = """
using System;

namespace Gen {

    public class Gen__i__ {
        public static void Test() {
            Console.WriteLine("hiya");
        }
    }
}
"""

for i in range(files):
    t = text.replace('__i__', str(i))

    file = me / f'Gen/Gen{i}.cs'

    file.write_text(t)